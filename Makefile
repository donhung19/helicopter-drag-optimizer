# Biến số để dễ quản lý
PYTHON = python
MAIN = main.py
INPUT = data/fleet_data.csv

# Lệnh cài đặt thư viện
install:
	pip install -r requirements.txt

# Lệnh chạy mặc định
run:
	$(PYTHON) -m main --input $(INPUT)

# Lệnh chạy với file dữ liệu mới
run-new:
	$(PYTHON) -m main --input data/my_new_fleet.csv

# Lệnh dọn dẹp các file ảnh cũ trong exports
clean:
	rm -f exports/*.csv
	rm -f exports/*.png


# Lệnh hướng dẫn
help:
	@echo "Các lệnh khả dụng:"
	@echo "  make install  : Cài đặt thư viện cần thiết"
	@echo "  make run      : Chạy phân tích với dữ liệu mặc định"
	@echo "  make run-new  : Chạy với file my_new_fleet.csv"
	@echo "  make clean    : Xóa file rác và bộ nhớ đệm"