# Hướng dẫn học tập (Student Guideline): Tạo Báo Cáo Tuyển Dụng Tự Động

Chào mừng bạn đến với học phần thực hành giúp thiết kế một bảng điều khiển số liệu (Dashboard) chuyên nghiệp từ nguồn dữ liệu CSV đã được chuẩn bị sẵn, hoàn toàn không cần kỹ năng lập trình.

## 1. Chuẩn bị dữ liệu đầu vào

- Đảm bảo bạn đã có file **`Mockup_Master_Data_UngVien.csv`** (hoặc file CSV bạn đã xuất từ các bài thực hành trước) nằm cùng thư mục này.
- **Lưu ý quan trọng:** Hãy ĐÓNG tất cả các file Excel hoặc CSV liên quan để tránh báo lỗi "File is busy".

## 2. Quy trình thực hành (Tại lớp)

Để có một báo cáo biểu đồ trực quan và tự động kết nối với dữ liệu CSV, hãy thực hiện theo bộ Prompt thiết kế sau:

### Bước 1: Gọi Prompt Thiết kế Dashboard
1. Truy cập file lệnh: 👉 **[05_Prompt_Dashboard_V2.md](./05_Prompt_Dashboard_V2.md)**
2. Sao chép (Ctrl+C) toàn bộ nội dung trong khung **[SYSTEM / ROLE]**.

### Bước 2: AI Agent thực thi
1. Dán (Ctrl+V) vào khung chat với AI Agent (Antigravity).
2. **AI Agent sẽ tự động:**
   - Đọc dữ liệu từ file CSV.
   - Thiết kế Dashboard chuyên nghiệp (`Recruitment_Dashboard.html`).
   - Đấu nối dữ liệu thực tế và tự động khởi chạy Local Server qua Python.

### Bước 3: Kiểm tra kết quả
1. Trình duyệt sẽ tự động mở địa chỉ: `http://localhost:8000/Recruitment_Dashboard.html`.
2. Nếu không tự động mở, bạn có thể nhấp vào link do AI cung cấp.

## 3. Các lưu ý quan trọng (Trên lớp)
- **Real-time Sync:** Nhờ có Local Server, Dashboard sẽ tự động cập nhật dữ liệu nếu bạn thực hiện thay đổi trong file CSV tương ứng.
- **WOW Moment:** Hãy cùng quan sát biểu đồ báo cáo nhân sự xuất hiện chỉ sau vài giây thực thi lệnh AI.

---

## 4. BÀI TẬP VỀ NHÀ: Cá nhân hóa Báo cáo thực tế doanh nghiệp

Để biến những gì đã học thành công cụ hữu ích cho công việc hàng ngày, hãy thực hành cá nhân hóa hệ thống báo cáo:

### Thử thách: Cá nhân hóa Dashboard theo KPI & Brand
Sử dụng dữ liệu đặc thù đã trích xuất được ở bài học trước để yêu cầu AI Agent thiết kế lại Dashboard:
- **Branding:** Áp dụng mã màu thương hiệu (Hex) và chèn Logo công ty bạn vào Dashboard.
- **KPI Reports:** Thay đổi các loại biểu đồ để phản ánh đúng thực tế tuyển dụng (VD: Tỷ lệ ứng viên theo phòng ban, Thống kê trình độ ngoại ngữ, Phân bổ nguồn tuyển dụng hiệu quả nhất...).

---

## 5. Xuất bản và chia sẻ

Để xuất bản Poster Tuyển dụng hoặc Dashboard thành file PDF hoặc Ảnh để gửi báo cáo tuần cho Sếp:
- **Chrome:** Cài đặt Extension **GoFullPage**.
- **Safari (Mac):** Chọn **File > Export as PDF**.

---

*Chúc bạn hoàn thành bài thực hành và sở hữu hệ thống dữ liệu nhân sự thông minh cho riêng mình!*
