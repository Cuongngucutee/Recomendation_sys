import pandas as pd
import os

class OlistDataLoader:
    def __init__(self, raw_data_path):
        self.path = raw_data_path
        # Định nghĩa map: Tên biến mong muốn -> Tên file CSV thực tế
        self.file_map = {
            'orders': 'olist_orders_dataset.csv',
            'items': 'olist_order_items_dataset.csv',
            'products': 'olist_products_dataset.csv',
            'customers': 'olist_customers_dataset.csv',
            'payments': 'olist_order_payments_dataset.csv',
            'translation': 'product_category_name_translation.csv'
        }

    def load_dataset(self, dataset_name):
        """Đọc một file CSV cụ thể"""
        if dataset_name not in self.file_map:
            raise ValueError(f"Dataset '{dataset_name}' không tồn tại trong cấu hình.")
        
        file_name = self.file_map[dataset_name]
        file_path = os.path.join(self.path, file_name)
        
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"❌ Không tìm thấy file: {file_path}")
            
        print(f"   -> Đang đọc {file_name}...")
        return pd.read_csv(file_path)

    def load_all(self):
        """Đọc toàn bộ các file cần thiết"""
        print(f"--- BẮT ĐẦU LOAD DỮ LIỆU TỪ: {self.path} ---")
        data = {}
        try:
            for key in self.file_map:
                data[key] = self.load_dataset(key)
            print("✔ Tải toàn bộ dữ liệu thành công!")
            return data
        except Exception as e:
            print(f"❌ Lỗi khi tải dữ liệu: {e}")
            return None