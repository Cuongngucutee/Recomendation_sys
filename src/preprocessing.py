import pandas as pd

class DataPreprocessor:
    def __init__(self, data_dict):
        """
        :param data_dict: Dictionary chứa các DataFrame đã load (orders, items, products...)
        """
        self.data = data_dict
        self.master_df = None

    def process_master_data(self):
        """
        Quy trình tạo bảng Master: 
        Orders + Items + Products + Translation + Customers + Payments
        """
        print("--- BẮT ĐẦU XỬ LÝ & MERGE DỮ LIỆU (MASTER PIPELINE) ---")
        
        # 1. Trích xuất các bảng từ dictionary
        df_orders = self.data['orders']
        df_items = self.data['items']
        df_products = self.data['products']
        df_trans = self.data['translation']
        df_customers = self.data['customers']
        # df_payments = self.data['payments'] 
        # Lưu ý: Tạm thời chưa merge Payments vào Master để tránh duplicate dòng (vì 1 đơn có thể trả góp nhiều lần)
        # Payments sẽ được dùng riêng trong Module Phân khúc khách hàng sau này.

        # 2. Bước Merge (Nối bảng)
        # Merge 1: Đơn hàng + Chi tiết sản phẩm (Left Join để giữ thông tin đơn hàng)
        # Chúng ta chỉ quan tâm đơn hàng đã có items (để phân tích sản phẩm), nên dùng Inner hoặc Left từ Items
        print("   -> Merging: Orders + Items...")
        master = df_orders.merge(df_items, on='order_id', how='inner')

        # Merge 2: + Thông tin Sản phẩm
        print("   -> Merging: + Products...")
        master = master.merge(df_products, on='product_id', how='left')

        # Merge 3: + Dịch tên sản phẩm (Tiếng Anh)
        print("   -> Merging: + Translations...")
        master = master.merge(df_trans, on='product_category_name', how='left')

        # Merge 4: + Thông tin Khách hàng (Quan trọng: Để lấy customer_unique_id)
        print("   -> Merging: + Customers...")
        master = master.merge(df_customers, on='customer_id', how='left')

        # 3. Bước Cleaning (Làm sạch)
        print("   -> Cleaning: Xử lý ngày tháng và tên sản phẩm...")
        
        # Chuyển đổi cột thời gian sang datetime object
        time_cols = ['order_purchase_timestamp', 'order_approved_at', 'order_delivered_customer_date']
        for col in time_cols:
            if col in master.columns:
                master[col] = pd.to_datetime(master[col])

        # Xử lý tên sản phẩm: Nếu không có tiếng Anh, dùng tạm tiếng Bồ Đào Nha
        master['product_category'] = master['product_category_name_english'].fillna(master['product_category_name'])
        
        # Lọc bỏ các dòng không xác định được sản phẩm (nếu cần thiết cho bài toán gợi ý)
        # master = master.dropna(subset=['product_category']) 

        # Chỉ giữ lại các đơn hàng đã hoàn thành (delivered) để phân tích chính xác
        master = master[master['order_status'] == 'delivered']

        # Chọn lọc các cột quan trọng để giữ lại cho Master Table
        selected_columns = [
            'order_id', 
            'customer_unique_id', # ID duy nhất của khách (dùng cho Segmentation)
            'customer_city', 
            'customer_state',
            'order_purchase_timestamp', # Dùng cho Seasonality
            'product_id', 
            'product_category', # Dùng cho Association Rules
            'price', 
            'freight_value'
        ]
        
        self.master_df = master[selected_columns].copy()
        
        # Thêm cột Tháng-Năm và Giờ để tiện phân tích sau này
        self.master_df['purchase_month'] = self.master_df['order_purchase_timestamp'].dt.to_period('M')
        self.master_df['purchase_hour'] = self.master_df['order_purchase_timestamp'].dt.hour
        self.master_df['total_item_value'] = self.master_df['price'] + self.master_df['freight_value']

        print(f"✔ Xử lý hoàn tất! Kích thước bảng Master: {self.master_df.shape}")
        return self.master_df

    def save_master(self, output_path):
        """Lưu kết quả ra file"""
        if self.master_df is not None:
            print(f"   -> Đang lưu Master Data xuống: {output_path}")
            # Lưu dạng Pickle để giữ nguyên định dạng datetime và đọc nhanh
            self.master_df.to_pickle(output_path)
            
            # Lưu thêm 1 bản CSV nhỏ để xem thử (preview)
            csv_path = output_path.replace('.pkl', '.csv')
            self.master_df.head(100).to_csv(csv_path, index=False)
            print(f"   -> Đã lưu file preview CSV tại: {csv_path}")
        else:
            print("❌ Chưa có dữ liệu để lưu.")