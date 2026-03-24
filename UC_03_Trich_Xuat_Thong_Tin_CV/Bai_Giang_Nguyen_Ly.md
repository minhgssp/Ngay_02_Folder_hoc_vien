# BÀI GIẢNG: NGUYÊN LÝ ÁNH XẠ TỪ TƯ DUY DATA ENTRY SANG AI CV HÀNG LOẠT
*(Giáo trình Hạt nhân: Làm chủ Antigravity bằng cách mổ xẻ hành vi của chính mình)*

---

Làm sao AI có thể tự bóc tách trăm bản CV không theo quy chuẩn nào rồi thả đúng chóc vào một cái rổ (bảng Master Data)? Giống ở Use Case trước, hãy phân tích cách một Nhân sự HR đi gom nhặt thông tin CV.

## 1. Phân rã hành động làm việc "chân tay" (Data Entry) của con người 
Công việc thường ngày của HR vào buổi sáng: Cả trăm cái Email tải về. Bạn phải thao tác mở từng file PDF/Word ra. 

1. **Bước 1 (Đảo mắt tìm kiếm mục tiêu):** Bạn có nhiệm vụ nhặt 4 thông tin: Tên, Email, SĐT, Năm sinh. Bạn đọc lướt nhanh từ trên xuống dưới tờ giấy. Dù số điện thoại giấu ở góc trái, trên đỉnh hay dưới đáy, bạn vẫn tìm ra vì bạn biết cấu trúc của "nhóm 10 con số" hoặc chữ "Mobile/Phone".
2. **Bước 2 (Gắp Nhặt, vứt bỏ rườm rà):** Bạn copy 09xxx. Bạn thấy thừa cụm chữ "Số ĐT: ", bạn xóa nó đi trong quá trình sao chép. 
3. **Bước 3 (Thả vào đúng Rổ):** Mở ứng dụng Excel, dán số đó vào cái Cột tên là "Số Điện Thoại". Xong 1 người. Đóng cái Tab file CV đó lại. 
4. **Bước 4 (Vòng Lặp Vô Hành):** Làm lại 3 bước trên 100 lần đến khi hết thư mục.

## 2. Ánh xạ sang Năng lực Cốt lõi của AI Agent (Antigravity)
Khi được kích hoạt chạy tự động hàng loạt CV, AI không hề có "mắt" để quét như bạn, nhưng nó sở hữu 2 động cơ lõi cực khủng:

* **Năng lực Phân tích bối cảnh Văn bản (Contextual Extraction):** Không dùng các câu lệnh lập trình ngớ ngẩn (kiểu như: Cứ thấy chữ SĐT thì copy đoạn kế tiếp), AI có khả năng suy luận mạnh mẽ. Mọi dạng chuỗi (dù ghi là P/h - Điện thoại di động - Zalo...) đều được AI đánh giá "Ý nghĩa là gì?" từ đó rút ra chính xác kết quả lõi. Đây là năng lực biến tài liệu thô vô nghĩa (Unstructured Data) thành dữ liệu có cấu trúc ý nghĩa (Structured Data - CSV).
* **Năng lực Xử lý Tuần hoàn Đa luồng (Batch Processing Machine):** AI của Antigravity có trong mình một chiếc quạt gió làm nguội và hệ thống vòng lặp tự động (Script Python đứng đằng sau AI Agent). Nó vận hành như một phân xưởng Robot, bật lên 1 tệp, bóc 5 giây, gói vào, rồi đẩy tệp tiếp theo, làm miết cho đến khi sạch kho. Không biết mệt mỏi!

## 3. BÀI HỌC KHÁI QUÁT HÓA DÀNH CHO BẠN
"Nhập liệu bằng tay - Data Entry" bằng thao tác Sao chép-Dán đã lỗi thời ở thế giới AI này!
**Quy tắc chung:** Bạn đừng để phòng HR/Hành chính phải làm công việc bốc vác kỹ thuật số "Bưng bê chữ từ cửa này sang cửa khác". Chỉ cần bạn dạy AI cách hiểu (Prompt nhận diện cấu trúc Dữ liệu), nó sẽ gánh vác vòng lặp 1000 file mà không than thở một lời!
