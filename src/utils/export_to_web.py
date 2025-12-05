import pandas as pd
import json
import os

def export_results_to_js(output_dir='outputs', web_dir='web_app'):
    """
    Chuyển đổi kết quả phân tích (CSV) thành file JavaScript để Web hiển thị
    """
    print("   -> [Web Export] Đang xuất dữ liệu sang Dashboard...")
    
    os.makedirs(web_dir, exist_ok=True)
    js_content = "window.dashboardData = {};\n"

    # 1. XUẤT DỮ LIỆU BIỂU ĐỒ DOANH THU (SEASONALITY)
    try:
        monthly_df = pd.read_csv(os.path.join(output_dir, 'monthly_revenue.csv'))
        # Chuyển thành list để JS đọc được
        chart_data = {
            'labels': monthly_df['Month'].tolist(),
            'values': monthly_df['Total_Revenue'].tolist()
        }
        js_content += f"window.dashboardData.revenueChart = {json.dumps(chart_data)};\n"
    except Exception:
        print("      ⚠️ Không tìm thấy monthly_revenue.csv (Sẽ dùng dữ liệu mẫu)")

    # 2. XUẤT DỮ LIỆU PHÂN KHÚC KHÁCH HÀNG (SEGMENTATION)
    try:
        seg_df = pd.read_csv(os.path.join(output_dir, 'customer_segments.csv'))
        # Đếm số lượng khách mỗi nhóm
        seg_counts = seg_df['Segment_Name'].value_counts()
        seg_data = {
            'labels': seg_counts.index.tolist(),
            'values': seg_counts.values.tolist()
        }
        js_content += f"window.dashboardData.segmentChart = {json.dumps(seg_data)};\n"
    except Exception:
        print("      ⚠️ Không tìm thấy customer_segments.csv")

    # 3. XUẤT LUẬT KẾT HỢP (ASSOCIATION RULES)
    try:
        rules_df = pd.read_csv(os.path.join(output_dir, 'rules.csv'))
        # Chỉ lấy top 100 luật mạnh nhất để web nhẹ
        top_rules = rules_df.head(100)
        
        # Chuyển đổi thành Dictionary: {'item_A': ['item_B', 'item_C']}
        rules_dict = {}
        for _, row in top_rules.iterrows():
            ant = row['antecedents']
            cons = row['consequents']
            if ant not in rules_dict:
                rules_dict[ant] = []
            if cons not in rules_dict[ant]:
                rules_dict[ant].append(cons)
        
        js_content += f"window.dashboardData.rules = {json.dumps(rules_dict)};\n"
    except Exception:
        print("      ⚠️ Không tìm thấy rules.csv")

    # Ghi ra file data.js
    with open(os.path.join(web_dir, 'data.js'), 'w', encoding='utf-8') as f:
        f.write(js_content)
    
    print(f"      ✔ Đã tạo file dữ liệu Web tại: {os.path.join(web_dir, 'data.js')}")

if __name__ == "__main__":
    export_results_to_js()