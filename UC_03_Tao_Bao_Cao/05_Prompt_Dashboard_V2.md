# BỘ PROMPT TỐI ƯU CẤP ĐỘ 3: TỰ ĐỘNG HÓA DASHBOARD & LOCAL SERVER

**Bạn Copy (Ctrl+C) nguyên văn khung chữ phía dưới và cung cấp cho AI Assistant (Agent) để thực thi chu trình báo cáo cuối cùng:**

---

**[SYSTEM / ROLE]**
Hãy đóng vai một HR Tech Consultant & Dashboard Designer. Nhiệm vụ của bạn là biến tệp dữ liệu phẳng (.csv) thành một Dashboard báo cáo tuyển dụng trực quan, hiện đại và tự động kết nối dữ liệu.

**[Nhiệm vụ 1: THIẾT KẾ DASHBOARD TRỰC QUAN]**
Tạo file `Recruitment_Dashboard.html` tại cùng thư mục với các tiêu chuẩn sau:
1. **Dữ liệu nguồn:** Đấu nối trực tiếp với file `Master_Data_Report.csv`.
2. **Kỹ thuật:** 
   - Sử dụng `Chart.js` để vẽ biểu đồ (Nguồn CV, Trạng thái phỏng vấn, Phân bổ kỹ năng).
   - Sử dụng `PapaParse` (CDN) để đọc và phân tích file CSV ngay trong trình duyệt.
   - Viết mã Javascript để tự động tính toán các chỉ số (Tổng CV, Tỷ lệ Pass, Nguồn hiệu quả nhất) từ tệp CSV.
3. **Thẩm mỹ (Lalago Brand):**
   - Màu chủ đạo: Deep Navy (`#00375A`), Màu nhấn: Warm Amber (`#FCBB13`).
   - Phong cách: Glassmorphism, bo góc mềm mại, hiệu ứng hover chuyên nghiệp.

**[Nhiệm vụ 2: TỰ ĐỘNG HÓA HỆ THỐNG]**
1. **Kiểm tra Server:** Kiểm tra xem file `run_dashboard_server.py` đã tồn tại chưa. Nếu chưa, hãy tạo mới file này với nội dung khởi chạy máy chủ HTTP tại cổng 8000.
2. **Thực thi lệnh:** Ngay sau khi đã chuẩn bị xong file Dashboard và Server, hãy **SỬ DỤNG TOOL run_command** để thực thi lệnh: `python run_dashboard_server.py`.
3. **Xác nhận:** Thông báo cho người dùng biết Dashboard đã sẵn sàng tại địa chỉ `http://localhost:8000/Recruitment_Dashboard.html`.

**[QA/QC]**
- Đảm bảo logic đọc file CSV không bị lỗi "CORS" (đây là lý do cần chạy qua Server).
- Đảm bảo các biểu đồ hiển thị đúng số liệu thực tế từ file tổng hợp.

---

💡 **Lưu ý cho Sinh viên:** 
- Đây là bước "WOW" nhất của quy trình: Biến dữ liệu thô thành thông tin chiến lược chỉ bằng 1 cú Click.
- AI sẽ tự động mở Server cho bạn. Nếu muốn dừng lại, hãy quay lại Terminal và nhấn `Ctrl + C`.
