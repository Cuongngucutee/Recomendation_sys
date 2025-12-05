import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import numpy as np

class CustomerSegmentationModule:
    def __init__(self, master_df):
        self.df = master_df
        self.rfm_df = None

    def run(self, n_clusters=4):
        print("   -> [Module 2] Đang chạy Customer Segmentation (RFM + K-Means)...")
        
        # 1. Tính toán chỉ số RFM
        # Lấy ngày cuối cùng trong data + 1 ngày làm mốc hiện tại
        now_date = self.df['order_purchase_timestamp'].max() + pd.Timedelta(days=1)
        
        rfm = self.df.groupby('customer_unique_id').agg({
            'order_purchase_timestamp': lambda x: (now_date - x.max()).days, # Recency
            'order_id': 'nunique',                                           # Frequency
            'price': 'sum'                                                   # Monetary
        }).reset_index()
        
        rfm.columns = ['customer_id', 'Recency', 'Frequency', 'Monetary']
        
        # 2. Chuẩn hóa dữ liệu (Scaling) để chạy K-Means tốt hơn
        scaler = StandardScaler()
        rfm_scaled = scaler.fit_transform(rfm[['Recency', 'Frequency', 'Monetary']])
        
        # 3. Chạy K-Means Clustering
        kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
        rfm['Cluster'] = kmeans.fit_predict(rfm_scaled)
        
        # 4. Gán nhãn thủ công (Heuristic) dựa trên Monetary trung bình của cụm
        # Sắp xếp cụm theo số tiền chi tiêu tăng dần
        cluster_avg_spend = rfm.groupby('Cluster')['Monetary'].mean().sort_values()
        
        # Map lại: 0 -> Thấp nhất, 3 -> Cao nhất (VIP)
        cluster_mapping = {old_label: new_label for new_label, old_label in enumerate(cluster_avg_spend.index)}
        rfm['Segment_Level'] = rfm['Cluster'].map(cluster_mapping)
        
        # Đặt tên thân thiện
        segment_names = {
            0: 'Khách vãng lai (Low Value)',
            1: 'Khách tiềm năng (Potential)',
            2: 'Khách trung thành (Loyal)',
            3: 'Khách VIP (High Value)'
        }
        if n_clusters == 4:
            rfm['Segment_Name'] = rfm['Segment_Level'].map(segment_names)
        
        self.rfm_df = rfm
        print(f"      ✔ Đã phân chia {len(rfm)} khách hàng thành {n_clusters} cụm.")
        return self.rfm_df

    def save(self, path):
        if self.rfm_df is not None:
            self.rfm_df.to_csv(path, index=False)
            print(f"      💾 Đã lưu phân cụm khách hàng tại: {path}")