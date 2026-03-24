# TỔNG QUAN KHÓA HỌC: MASTERCLASS AI FOR BACKOFFICE (HR & PROCUREMENT)
**Phiên bản:** 1.0
**Đối tượng:** Nhân sự thuộc khối Backoffice (Tuyển dụng, Kế toán - Mua sắm, Hành chính)
**Mục tiêu:** Ứng dụng AI Agent (Antigravity) nhằm tự động hóa các quy trình cốt lõi, giảm thiểu thao tác thủ công và nâng cao hiệu suất ra quyết định bằng dữ liệu (Data-driven).

---

## 🌟 1. GIỚI THIỆU HỆ SINH THÁI THỰC HÀNH
Khóa học này được thiết kế theo cấu trúc "Learning by doing" (Học qua hành). Bạn sẽ thao tác trực tiếp trên 3 bài toán (Use Case) phổ biến nhất của khối Backoffice, thông qua sức mạnh của nền tảng AI Agent "Antigravity". 

Hệ thống cung cấp một môi trường tương tác trơn tru bằng các câu lệnh (Prompt) đã được đóng gói tối ưu hóa, đảm bảo độ chính xác tuyệt đối mà không cần người học phải biết lập trình.

## 🚀 2. LỘ TRÌNH 3 USE CASE CỐT LÕI

### 💼 Use Case 01: Thiết kế Poster Tuyển Dụng Nhanh (Từ JD)
- **Vấn đề giải quyết:** Thay vì phụ thuộc vào Designer hoặc IT để cập nhật trang tuyển dụng, HR có thể tự thiết kế trang đích (Poster Tuyển dụng) ngay lập tức.
- **Dữ liệu đầu vào:** File văn bản thô chức nội dung mô tả công việc (JD).
- **Quy trình hoạt động:**
  1. Đưa JD vào để AI Agent tự động đọc hiểu và phân tích.
  2. Sử dụng câu lệnh đã tối ưu (Prompt Poster Tuyen Dung V2) gọi AI sinh ra giao diện HTML chuyên nghiệp, tự động kết nối với Logo/Banner của doanh nghiệp.
  3. Xuất bản và chia sẻ: Sử dụng công cụ "Pageless PDF" (xuất PDF không trang) giúp Poster Tuyển dụng trở thành 1 hình ảnh dài mượt mà để gửi báo cáo.
- **[👉 Xem chi tiết Hướng dẫn Use Case 01](./UC_01_JD_To_Poster_Tuyen_Dung/Student_Guideline.md)**

### 📊 Use Case 02: Phân Tích & So Sánh Báo Giá "Vạn Năng" (Procurement)
- **Vấn đề giải quyết:** Bài toán cân não của phòng thu mua (Procurement/Purchasing) khi phải đối chiếu hàng trăm hạng mục từ các nhà cung cấp khác nhau để tìm ra đơn vị tối ưu nhất.
- **Dữ liệu đầu vào:** Các file báo giá hỗn hợp từ nhà thầu (Sự kiện, Văn phòng phẩm, Thiết bị...).
- **Quy trình hoạt động:**
  1. **Số hóa dạng dọc:** AI tự động phân rã báo giá thô, tách bạch "Giá" và "Đặc tính kỹ thuật" dưới định dạng hàng dọc (Granular Data) vào file `.csv`. Điều này đảm bảo tính khách quan "So sánh táo với táo, cam với cam".
  2. **Báo cáo Chiến lược:** AI tiếp tục xử lý cục dữ liệu CSV sinh ra báo cáo "Đối đầu ba phần" (Strategic Comparison Report) bằng giao diện HTML hiển thị trên trình duyệt. Đánh giá tính chiến thắng của nhà thầu và đưa ra lưu ý đàm phán.
- **[👉 Xem chi tiết Hướng dẫn Use Case 02](./UC_02_Phan_Tich_Bao_Gia/Student_Guideline.md)**

### 🗂️ Use Case 03: Số Hóa & Trích Xuất Hồ Sơ Ứng Viên Hàng Loạt (HR)
- **Vấn đề giải quyết:** Nỗi đau lớn nhất của quy trình tiếp nhận nhân sự: Gõ lại từng thông tin ứng viên từ hàng trăm file PDF/Word khác nhau vào Excel.
- **Dữ liệu đầu vào:** Thư mục chứa các file hồ sơ ứng viên (Dummy CVs).
- **Quy trình hoạt động:**
  1. Trích xuất đa chiều: AI tự động duyệt toàn bộ thư mục, đọc hiểu từng file thư xin việc (cả PDF hoặc Word) và bóc tách những trường thông tin mong muốn (Tên, SĐT, Email...) thả vào 1 tệp Excel `ds_ung_vien.csv`.
- **[👉 Xem chi tiết Hướng dẫn Use Case 03](./UC_03_Trich_Xuat_Thong_Tin_CV/Student_Guideline.md)**

### 📈 Use Case 04: Tạo Dashboard Báo Cáo Nhân Sự (Từ Dữ Liệu CV)
- **Vấn đề giải quyết:** Từ đống dữ liệu đã trích xuất, HR cần tự mình xây dựng bảng biểu đồ tổng quan mà không tốn cả buổi thiết kế báo cáo.
- **Dữ liệu đầu vào:** File báo cáo nhân sự tổng `Mockup_Master_Data_UngVien.csv`.
- **Quy trình hoạt động:**
  1. Tạo Dashboard quản trị nhân sự tổng: Dùng câu lệnh tối ưu để AI thiết kế 1 Dashboard bằng HTML.
  2. Trực quan hóa dữ liệu tự động với Chart.js và truy xuất tức thì giao diện Local Server.
- **[👉 Xem chi tiết Hướng dẫn Use Case 04](./UC_04_Tao_Bao_Cao/Student_Guideline.md)**

---

## 🎯 3. BẢN LỀ HOẠT ĐỘNG & NGUYÊN TẮC VẬN HÀNH

- **Nguyên tắc "Đóng cửa sổ":** Luôn luôn đóng tất cả các file dữ liệu `.csv`, `.xlsx` trên bộ gõ của bạn **trước khi** yêu cầu AI đọc và viết vào file để tránh lỗi xung đột hệ thống (File is busy).
- **QA / QC dữ liệu sinh ra:** AI Agent thông minh nhưng luôn cần sự thẩm định của con người ở đầu ra. Yêu cầu QA/QC nghiêm ngặt giữa tài liệu thô gốc và tài liệu AI đã trích xuất.
- **Tùy biến cao:** Khóa học được thiết kế để bạn mang các tài liệu (Báo giá, JD, CV) thực tế của công ty **mình** để AI phân tích. Cấu trúc Prompt mà lớp học cung cấp hoàn toàn thích ứng với mọi ngữ cảnh.

---
*Chúc các Anh / Chị học viên của Masterclass khám phá thành công và làm chủ năng lượng tự động hóa cho chuỗi hoạt động Backoffice của mình!*
