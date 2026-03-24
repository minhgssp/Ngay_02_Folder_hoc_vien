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

1. Tại thanh Sidebar trái của VS Code, chuột phải vào thư mục `UC_03_Nhap_Lieu_CV`.
2. Chọn **Reveal in File Explorer** (Mở trong thư mục máy tính).
3. Tìm và mở file **`ds_ung_vien.csv`** bằng Excel.
4. Kiểm tra sự chính xác của dữ liệu: Tên, Email, SĐT đã được phân chia cột ngăn nắp.

### Bước 4: Thiết kế Dashboard Quản lý (Tại lớp)

Để có một báo cáo biểu đồ trực quan và tự động kết nối với dữ liệu CSV, hãy thực hiện theo bộ Prompt tối ưu sau:

1. Truy cập file lệnh: 👉 **[05_Prompt_Dashboard_V2.md](./05_Prompt_Dashboard_V2.md)**
2. Sao chép (Ctrl+C) toàn bộ nội dung trong khung **[SYSTEM / ROLE]**.
3. Dán (Ctrl+V) vào khung chat với AI Agent (Antigravity).
4. **AI Agent sẽ tự động:**
   - Thiết kế Dashboard chuyên nghiệp (`Recruitment_Dashboard.html`).
   - Đấu nối dữ liệu thực tế từ file CSV bạn vừa tạo ở Bước 3.
   - Kiểm tra và tự động khởi chạy Local Server qua Python.
5. **Xem kết quả:** Trình duyệt sẽ tự động mở địa chỉ: `http://localhost:8000/Recruitment_Dashboard.html`.

## 3. Các lưu ý quan trọng (Trên lớp)
- **Real-time Sync:** Nhờ có Local Server, Dashboard sẽ tự động cập nhật dữ liệu mới nếu bạn thực hiện thay đổi trong file CSV.
- **Truy xuất hồ sơ:** Nhờ có cột **Đường dẫn file gốc**, bạn có thể nhấp trực tiếp vào ô để mở lại CV gốc của ứng viên trong tích tắc.
- **WOW Moment:** Hãy cùng cả lớp quan sát biểu đồ báo cáo nhân sự xuất hiện chỉ sau vài giây thực thi lệnh AI.

---

## 4. BÀI TẬP VỀ NHÀ: Cá nhân hóa Báo cáo thực tế doanh nghiệp

Để biến những gì đã học thành công cụ hữu ích cho công việc hàng ngày, hãy thực hành cá nhân hóa hệ thống báo cáo:

### 📊 Thử thách 1: Tùy chỉnh cấu trúc Dữ liệu (Master Data)
Mỗi công ty có một quy trình quản lý hồ sơ và nhu cầu thông tin khác nhau. Hãy yêu cầu AI Agent cập nhật file **[04_Prompt_Chiet_Xuat_CV_V2.md](./04_Prompt_Chiet_Xuat_CV_V2.md)** để trích xuất thêm các thông tin đặc thù của công ty bạn:
- **Ví dụ:** Thêm cột "Mức lương mong muốn", "Chứng chỉ tiếng Anh (IELTS/TOEIC)", "Bộ phận ứng tuyển", hoặc "Hiring Manager" phụ trách.
- **Thực hành trên dữ liệu thật:** Nếu có thể, hãy sử dụng bộ CV thực tế của chính doanh nghiệp bạn để thử nghiệm khả năng trích xuất của AI.

### 📈 Thử thách 2: Cá nhân hóa Dashboard theo KPI & Brand
Sử dụng dữ liệu đặc thù đã trích xuất được ở Thử thách 1 để yêu cầu AI Agent thiết kế lại Dashboard:
- **Branding:** Áp dụng mã màu thương hiệu (Hex) và chèn Logo công ty bạn vào Dashboard.
- **KPI Reports:** Thay đổi các loại biểu đồ để phản ánh đúng thực tế tuyển dụng (VD: Tỷ lệ ứng viên theo phòng ban, Thống kê trình độ ngoại ngữ, Phân bổ nguồn tuyển dụng hiệu quả nhất...).

---

## 5. Xuất bản và chia sẻ

Để xuất bản Landing Page hoặc Dashboard thành file PDF hoặc Ảnh để gửi báo cáo tuần cho Sếp:
- **Chrome:** Cài đặt Extension **GoFullPage**.
- **Safari (Mac):** Chọn **File > Export as PDF**.

---

*Chúc bạn hoàn thành bài thực hành và sở hữu hệ thống dữ liệu nhân sự thông minh cho riêng mình!*
