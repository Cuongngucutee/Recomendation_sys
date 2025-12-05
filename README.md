Olist 360 - Hệ Thống Phân Tích & Gợi Ý Mua Sắm 🛒

Dự án Khai phá dữ liệu (Data Mining) phân tích hành vi mua sắm trên sàn TMĐT Olist (Brazil), tích hợp hệ thống gợi ý sản phẩm (Recommendation System) và phân khúc khách hàng (Segmentation).

📋 Yêu cầu tiên quyết (Prerequisites)

Các thành viên chỉ cần cài đặt Docker và Docker Compose:

Tải Docker Desktop (Windows/Mac/Linux)

Không cần cài Python hay các thư viện pandas, sklearn trên máy cá nhân.

📂 Cấu trúc dự án

Olist_Project_Full/
├── data/
│   ├── raw/                <-- CHÉP 9 FILE CSV CỦA KAGGLE VÀO ĐÂY
│   └── processed/          <-- Dữ liệu sau xử lý (Docker tự sinh ra)
├── src/                    <-- Mã nguồn Python (Backend)
├── web_app/                <-- Giao diện Web (Frontend)
├── outputs/                <-- Kết quả mô hình (Rules, Charts)
├── docker-compose.yml      <-- File chạy Docker
└── README.md               <-- Hướng dẫn sử dụng


🚀 Hướng dẫn chạy (Quick Start)

Bước 1: Chuẩn bị dữ liệu

Do dữ liệu Olist khá lớn, không được commit lên Git. Các bạn cần tải thủ công và đưa vào thư mục data/raw/.

Tải Dataset tại: Kaggle Olist Dataset

Giải nén và copy toàn bộ các file .csv vào thư mục data/raw/ của dự án.

Đảm bảo cấu trúc file đúng như sau:

data/raw/olist_orders_dataset.csv

data/raw/olist_order_items_dataset.csv

... (và các file khác)

Bước 2: Chạy dự án bằng Docker

Mở Terminal (hoặc CMD/PowerShell) tại thư mục gốc của dự án và chạy lệnh:

docker-compose up --build




Bước 3: Trải nghiệm Demo

Sau khi thấy terminal báo Serving HTTP on 0.0.0.0 port 8000, hãy mở trình duyệt và truy cập:

👉 http://localhost:8000



Nhóm Phát Triển: [Tên các thành viên]
Môn học: Khai phá dữ liệu