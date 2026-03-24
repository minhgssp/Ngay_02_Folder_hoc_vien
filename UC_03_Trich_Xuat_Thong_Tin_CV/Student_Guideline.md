# Hướng dẫn học tập (Student Guideline): Số hóa & Nhập liệu CV hàng loạt

Chào mừng bạn đến với học phần thực hành giúp giải quyết nỗi đau điển hình của người làm tuyển dụng: Phải gõ lại thông tin ứng viên thủ công từ hàng trăm file CV khác nhau.

## 1. Chuẩn bị dữ liệu đầu vào

- Đảm bảo bạn đã có thư mục **`Dummy_CVs`** chứa các file CV (PDF, Word, Text) đa dạng định dạng.
- **Lưu ý quan trọng:** Hãy ĐÓNG tất cả các file Excel hoặc CSV liên quan (`ds_ung_vien.csv`, `Master_Data_Report.csv`) nếu bạn đang mở chúng trên máy tính để tránh AI báo lỗi "File is busy".

## 2. Quy trình thực hành (Tại lớp)

Chúng ta sẽ sử dụng bộ Prompt trích xuất dữ liệu chuyên sâu để thực hiện nhiệm vụ này một cách tự động.

### Bước 1: Gọi Prompt Trích xuất

Hãy truy cập file sau để lấy câu lệnh:
👉 **[04_Prompt_Chiet_Xuat_CV_V2.md](./04_Prompt_Chiet_Xuat_CV_V2.md)**

### Bước 2: AI Agent thực thi

1. Mở file Prompt trên, sao chép (Ctrl+C) toàn bộ nội dung trong khung **[SYSTEM / ROLE]**.
2. Dán (Ctrl+V) vào khung chat với AI Agent (Antigravity).
3. AI sẽ tự động duyệt qua từng file trong `Dummy_CVs` để đọc hiểu và tổng hợp dữ liệu.

### Bước 3: Kiểm tra kết quả

Sau khi AI hoàn thành, hãy thực hiện thác tác sau để kiểm chứng:

1. Tại thanh Sidebar trái của VS Code, chuột phải vào thư mục `UC_03_Trich_Xuat_Thong_Tin_CV`.
2. Chọn **Reveal in File Explorer** (Mở trong thư mục máy tính).
3. Tìm và mở file **`ds_ung_vien.csv`** bằng Excel (hoặc kiểm tra bằng phần mở rộng CSV của VS Code).
4. Kiểm tra sự chính xác của dữ liệu: Tên, Email, SĐT đã được phân chia cột ngăn nắp.

## 3. Các lưu ý quan trọng (Trên lớp)
- **Kiểm tra File Log:** Việc trích xuất file hàng loạt đôi lúc AI có xu hướng cắt bớt bước (lazy). Nếu thấy thiếu CV, hãy yêu cầu AI "Đọc lại lần nữa file X hoặc Y".
- **Thông tin rỗng:** Các file CV thiếu thông tin tiêu chuẩn (VD: không có Ngày sinh) sẽ tự động được ghi nhận là "Không tìm thấy".

## 4. BÀI TẬP VỀ NHÀ: Cá nhân hóa việc Trích xuất CV thực tế

Để biến những gì đã học thành công cụ hữu ích cho công việc hàng ngày, hãy thực hành cá nhân hóa hệ thống:

### Thử thách: Tùy chỉnh cấu trúc Dữ liệu (Master Data)
Mỗi công ty có một quy trình quản lý hồ sơ và nhu cầu thông tin khác nhau. Hãy yêu cầu AI Agent cập nhật file **[04_Prompt_Chiet_Xuat_CV_V2.md](./04_Prompt_Chiet_Xuat_CV_V2.md)** để trích xuất thêm các thông tin đặc thù của công ty bạn:
- **Ví dụ:** Thêm cột "Mức lương mong muốn", "Chứng chỉ tiếng Anh (IELTS/TOEIC)", "Bộ phận ứng tuyển", hoặc "Hiring Manager" phụ trách.
- **Thực hành trên dữ liệu thật:** Nếu có thể, hãy sử dụng bộ CV thực tế của chính doanh nghiệp bạn để thử nghiệm khả năng trích xuất của AI. Chú ý che các thông tin cá nhân.

---

*Chúc bạn hoàn thành bài thực hành và sở hữu hệ thống dữ liệu nhân sự tự động cho riêng mình!*
