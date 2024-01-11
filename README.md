# Speed Layer

## Luồng hoạt động

1. Crawl dữ liệu từ VnStock

- Crawl danh sách các mã cổ phiếu trên vnstock. Từ danh sách mã cổ phiếu thực hiện lấy giá cổ phiếu trong ngày

2. Cấu hình Kafka

- Kafka được cấu hình với 3 brokers ở 3 cổng 9092, 9093, 9094
- Tạo topic lưu trữ dữ liệu bin/kafka-topics.sh --create --bootstrap-server localhost:9092 ,localhost:9093, localhost:9094 --replication-factor 3 --partitions 3 --topic <name_topic>

3. Đẩy dữ liệu lên Kafka

- Chạy file kafka_producer.py
- Dữ liệu trong ngày của các mã cổ phiếu được đẩy lên Kafka thông qua topic và các brokers đã cấu hình

4. Đọc dữ liệu mới từ Kafka và đưa vào Elasticsearch

- Chạy file kafka_comsummer.py
- Comsummer tiến hành đọc dữ liệu mới nhất (cấu hình auto_offset_reset='latest') được producer gửi lên Kafka. Sau đó dữ liệu được lưu trữ trên Elasticsearch với index là 'test_index'

5. Trục quan hóa dữ liệu

- Lọc dữ liệu dựa theo mã cổ phiếu (ticker), chọn trục ngang là time, trục dọc là volume để biểu diễn khối lượng giao dịch của cổ phiếu theo thời gian
