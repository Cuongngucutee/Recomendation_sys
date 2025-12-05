# Sử dụng Python 3.9 phiên bản gọn nhẹ (slim)
FROM python:3.9-slim

# Thiết lập thư mục làm việc trong container
WORKDIR /app

# Copy file cài đặt thư viện vào trước để tận dụng Docker cache
COPY requirements.txt .

# Cài đặt các thư viện cần thiết
# Thêm --no-cache-dir để giảm dung lượng image
RUN pip install --no-cache-dir -r requirements.txt

# Copy toàn bộ mã nguồn dự án vào container
COPY . .

# Mặc định container sẽ không chạy lệnh gì cụ thể (sẽ được điều khiển bởi docker-compose)
CMD ["bash"]