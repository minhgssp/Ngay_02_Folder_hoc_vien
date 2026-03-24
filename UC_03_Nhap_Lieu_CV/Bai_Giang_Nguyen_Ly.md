# BÀI GIẢNG: NGUYÊN LÝ HOẠT ĐỘNG CỦA AI TRONG NHẬP LIỆU CV HÀNG LOẠT
*(Dành cho học viên không có nền tảng kỹ thuật/lập trình)*

---

## 1. Vấn đề thực tế của Tuyển dụng (HR)
Hàng ngày, bộ phận tuyển dụng thường nhận hàng trăm CV gửi về qua email, đa phần là file PDF, file Word.
Để quản lý nguồn ứng viên và tránh sót việc, HR phải:
- Tải từng file về máy, lưu giữ ở một nơi.
- Mở từng CV để đọc lướt các thông tin cơ bản.
- Sao chép Số điện thoại, Tên, Năm sinh, Email, Trường học... rồi gõ thủ công vào 1 bảng Excel Master của công ty.
👉 **Kết quả:** Thời gian chìm ngập trong việc mở, copy và đóng cửa sổ máy tính. Sự nghiệp kết nối con người (Tuyển dụng) bị biến thành... chiếc máy đánh máy lỗi thời, lặp đi lặp lại.

## 2. Trợ lý AI giải quyết bài toán này như thế nào?

Hình dung AI trong Use Case này hoạt động như **"10 người thực tập sinh cùng làm việc không ngừng nghỉ 24/7"**.

### Cơ chế hoạt động:
Khi khởi chạy hệ thống trên cả một thư mục chứa đầy CV, AI sẽ thực hiện các bước sau hoàn toàn tự động mà không cần sự can thiệp của bạn:

1. **Rút Lõi Hồ Sơ:** AI mở hàng chục file CV đó lên với "tốc độ của máy tính". Nó sẽ dùng khả năng phân tích ngôn ngữ để lục tìm đâu là Dòng Họ Tên, đâu là Dòng Số Điện Thoại. Đặc biệt, nó loại bỏ các từ dư thừa như "Mobile:", "Phone number"... chỉ để lại dòng số nguyên chất đưa vào ô Excel.
2. **Kỷ Luật Bảng Biểu (Lên CSV/Excel):** Một khi đã rút lõi xong thông tin của 100 người, AI nhét gọn dữ liệu vào 1 file Excel tổng cục (gọi là Master Data). Tên 1 cột, SĐT 1 cột, Email 1 cột thẳng tắp, sạch sẽ.
3. **Vén Tấm Màn Tổng Thể (Vẽ Biểu Đồ):** Dữ liệu dạng danh sách rất chán để nhìn. Khóa học trao cho bạn câu lệnh gọi AI "vẽ biểu đồ". AI đọc danh sách đó và chia tỷ lệ: Bao nhiêu % nữ, bao nhiêu % nam, Nguồn ứng viên về từ Website nào nhiều nhất... và trình chiếu chúng dưới dạng một Trang Quản trị màu sắc (Dashboard) rất sống động trên trình duyệt.

## 3. Lợi ích mang lại cho Bạn (HR)
- **Tập trung vào yếu tố "Con người" (Human-Touch):** Bạn không còn là máy đánh chữ. Thay vì lãng phí 2 tiếng mỗi sáng rà file CV, bạn để AI làm điều đó trong 10 giây và dành 2 tiếng còn lại để bốc điện thoại phỏng vấn, thu hút ứng viên tài năng.
- **Tiện lợi toàn diện:** Trong file Excel được lập tự động, AI luôn đính kèm **Đường dẫn đến file gốc**. Bạn chỉ việc rà sơ bảng tổng kết, nếu thấy ứng viên nào ưng ý, Click thẳng vào đường dẫn là máy tính tải bản CV gốc lên ngay lập tức.
- **Dễ dàng biến tấu:** AI của bạn rất ngoan. Giao diện biểu đồ Dashboard được dựng nên hoàn toàn từ 1 câu yêu cầu. Hôm nay bạn thích xem biểu đồ tròn, ngày mai bạn thích màu đỏ, ban giám đốc muốn xem báo cáo ngôn ngữ... bạn chỉ việc ra lệnh bằng tiếng Việt, AI sẽ sắp xếp lại toàn bộ báo cáo trong tích tắc.
