import os
import pandas as pd
from src.data_loader import OlistDataLoader
from src.preprocessing import DataPreprocessor

# Import các modules phân tích mới
from src.modules.association_rules import AssociationRulesModule
from src.modules.customer_segment import CustomerSegmentationModule
from src.modules.seasonal_analysis import SeasonalAnalysisModule

# Cấu hình đường dẫn
RAW_DATA_PATH = 'data/raw'
PROCESSED_DATA_PATH = 'data/processed'
OUTPUT_PATH = 'outputs'
MASTER_FILE_NAME = 'olist_master_data.pkl'

def run_phase_1_data_pipeline():
    print("\n=======================================================")
    print("   GIAI ĐOẠN 1: XÂY DỰNG DATA PIPELINE (OLIST 360)")
    print("=======================================================\n")

    os.makedirs(PROCESSED_DATA_PATH, exist_ok=True)

    # Kiểm tra xem file Master đã tồn tại chưa để tránh chạy lại (cache)
    master_path = os.path.join(PROCESSED_DATA_PATH, MASTER_FILE_NAME)
    if os.path.exists(master_path):
        print(f"✔ Tìm thấy Master Data tại: {master_path}")
        print("✔ Bỏ qua bước xử lý thô. Đang load dữ liệu...")
        return pd.read_pickle(master_path)

    # Nếu chưa có thì chạy quy trình load
    loader = OlistDataLoader(RAW_DATA_PATH)
    data_dict = loader.load_all()
    
    if data_dict is None:
        print("❌ Dừng chương trình do lỗi load dữ liệu.")
        return None

    processor = DataPreprocessor(data_dict)
    master_df = processor.process_master_data()
    processor.save_master(master_path)
    
    return master_df

def run_phase_2_modeling(master_df):
    print("\n=======================================================")
    print("   GIAI ĐOẠN 2: CHẠY CÁC MÔ HÌNH PHÂN TÍCH")
    print("=======================================================\n")
    
    os.makedirs(OUTPUT_PATH, exist_ok=True)

    # --- MÔ HÌNH 1: ASSOCIATION RULES (GỢI Ý MUA KÈM) ---
    assoc_model = AssociationRulesModule(master_df)
    # Support thấp (0.0001) để bắt nhiều luật, confidence thấp để lấy diện rộng
    assoc_model.run(min_support=0.0002, min_threshold=1.0)
    assoc_model.save(os.path.join(OUTPUT_PATH, 'rules.csv'))

    print("-" * 30)

    # --- MÔ HÌNH 2: CUSTOMER SEGMENTATION (PHÂN KHÚC) ---
    seg_model = CustomerSegmentationModule(master_df)
    seg_model.run(n_clusters=4) # Chia làm 4 nhóm khách hàng
    seg_model.save(os.path.join(OUTPUT_PATH, 'customer_segments.csv'))

    print("-" * 30)

    # --- MÔ HÌNH 3: SEASONAL ANALYSIS (MÙA VỤ) ---
    season_model = SeasonalAnalysisModule(master_df)
    season_model.run()
    season_model.save(OUTPUT_PATH)
    
    print("\n🎉 GIAI ĐOẠN 2 HOÀN TẤT! HÃY KIỂM TRA THƯ MỤC 'OUTPUTS'")

if __name__ == "__main__":
    # Chạy nối tiếp Phase 1 -> Phase 2
    master_df = run_phase_1_data_pipeline()
    
    if master_df is not None:
        run_phase_2_modeling(master_df)
        from src.utils.export_to_web import export_results_to_js
        export_results_to_js()