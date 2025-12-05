import pandas as pd

class SeasonalAnalysisModule:
    def __init__(self, master_df):
        self.df = master_df
        self.hourly_stats = None
        self.monthly_stats = None

    def run(self):
        print("   -> [Module 3] Đang chạy Seasonal Analysis (Time Series)...")
        
        # 1. Phân tích Giờ vàng (Hourly Trend)
        self.hourly_stats = self.df.groupby('purchase_hour')['order_id'].nunique().reset_index()
        self.hourly_stats.columns = ['Hour', 'Total_Orders']
        self.hourly_stats = self.hourly_stats.sort_values('Total_Orders', ascending=False)
        
        # 2. Phân tích Tháng (Monthly Trend - Tìm Black Friday)
        # Chuyển đổi purchase_month về dạng string để dễ lưu
        self.df['month_str'] = self.df['order_purchase_timestamp'].dt.strftime('%Y-%m')
        self.monthly_stats = self.df.groupby('month_str')['price'].sum().reset_index()
        self.monthly_stats.columns = ['Month', 'Total_Revenue']
        
        # Đánh dấu tháng doanh thu cao nhất
        max_rev = self.monthly_stats['Total_Revenue'].max()
        peak_month = self.monthly_stats[self.monthly_stats['Total_Revenue'] == max_rev]['Month'].values[0]
        
        print(f"      ✔ Giờ đặt hàng nhiều nhất: {self.hourly_stats.iloc[0]['Hour']}h")
        print(f"      ✔ Tháng doanh thu cao nhất: {peak_month} (Kiểm tra xem có phải Black Friday không)")
        
        return self.hourly_stats, self.monthly_stats

    def save(self, output_dir):
        import os
        if self.hourly_stats is not None:
            self.hourly_stats.to_csv(os.path.join(output_dir, 'hourly_stats.csv'), index=False)
            self.monthly_stats.to_csv(os.path.join(output_dir, 'monthly_revenue.csv'), index=False)
            print(f"      💾 Đã lưu thống kê thời gian tại: {output_dir}")