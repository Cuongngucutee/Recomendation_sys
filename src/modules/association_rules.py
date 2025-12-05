import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import fpgrowth, association_rules

class AssociationRulesModule:
    def __init__(self, master_df):
        self.df = master_df
        self.rules = None

    def run(self, min_support=0.0005, min_threshold=1.0):
        print("   -> [Module 1] Đang chạy Association Rules (Cross-selling)...")
        
        # --- FIX LỖI TYPE ERROR (STR vs FLOAT) ---
        # 1. Tạo bản sao để không ảnh hưởng data gốc
        df_clean = self.df.copy()

        # 2. Loại bỏ các dòng mà product_category bị NaN (Rỗng)
        # Vì NaN (Float) không thể so sánh với Tên sản phẩm (String)
        df_clean = df_clean.dropna(subset=['product_category'])

        # 3. Ép kiểu toàn bộ về String cho chắc chắn
        df_clean['product_category'] = df_clean['product_category'].astype(str)
        # ------------------------------------------

        # 4. Gom nhóm Order ID -> List sản phẩm
        # Chỉ lấy các đơn có >= 2 sản phẩm
        basket = df_clean.groupby('order_id')['product_category'].apply(list)
        basket = basket[basket.apply(len) >= 2].tolist()
        
        print(f"      - Số lượng giao dịch hợp lệ (>=2 items): {len(basket)}")
        if len(basket) == 0:
            print("      ⚠️ Không đủ dữ liệu để chạy luật kết hợp.")
            return None

        # 5. One-hot Encoding
        te = TransactionEncoder()
        try:
            te_ary = te.fit(basket).transform(basket)
        except TypeError as e:
            print(f"      ❌ Vẫn còn lỗi dữ liệu: {e}")
            return None
            
        df_onehot = pd.DataFrame(te_ary, columns=te.columns_)

        # 6. FP-Growth
        # min_support thấp để bắt các luật ngách (Long-tail)
        frequent_itemsets = fpgrowth(df_onehot, min_support=min_support, use_colnames=True)

        if frequent_itemsets.empty:
            print("      ⚠️ Không tìm thấy tập phổ biến.")
            return None

        # 7. Sinh luật
        rules = association_rules(frequent_itemsets, metric="lift", min_threshold=min_threshold)
        
        if rules.empty:
            print("      ⚠️ Không tìm thấy luật nào thỏa mãn ngưỡng Lift.")
            return None

        # 8. Làm sạch kết quả (Convert frozenset sang string)
        rules['antecedents'] = rules['antecedents'].apply(lambda x: list(x)[0])
        rules['consequents'] = rules['consequents'].apply(lambda x: list(x)[0])
        
        # Sắp xếp luật mạnh nhất lên đầu
        rules = rules.sort_values('lift', ascending=False)
        
        self.rules = rules
        print(f"      ✔ Tìm thấy {len(rules)} luật kết hợp (Lift > {min_threshold})")
        return self.rules

    def save(self, path):
        if self.rules is not None:
            self.rules.to_csv(path, index=False)
            print(f"      💾 Đã lưu rules tại: {path}")
        else:
            print("      ⚠️ Không có rules nào để lưu.")