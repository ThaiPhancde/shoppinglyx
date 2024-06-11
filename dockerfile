# Sử dụng một image chính thức của Python làm image nền
FROM python:3.9-slim

# Đặt thư mục làm việc trong container
WORKDIR /app

# Copy tệp requirements.txt vào thư mục làm việc
COPY req.txt .

# Cài đặt các thư viện Python được liệt kê trong requirements.txt
RUN pip install -r req.txt

# Copy toàn bộ mã nguồn của ứng dụng Django vào thư mục làm việc
COPY . .

# Thiết lập biến môi trường
ENV PYTHONUNBUFFERED=1

# Mở port mà ứng dụng sẽ chạy
EXPOSE 8000

# Chạy lệnh để khởi động ứng dụng Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]