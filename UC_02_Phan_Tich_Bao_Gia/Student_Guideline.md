# Hướng dẫn học tập (Student Guideline): Phân tích & So sánh Báo giá VẠN NĂNG (Universal)

Chào mừng bạn đến với học phần thực hành giúp giải quyết bài toán "Cân não" nhất của bộ phận thu mua bằng sức mạnh của AI Agent. Hệ thống "Vạn năng" này giúp bạn xử lý mọi loại báo giá phát sinh trong dự nghiệp kinh doanh của mình.

## 1. Chuẩn bị dữ liệu đầu vào
- **Dữ liệu thô:** Đảm bảo bạn đã có thư mục **`Raw_Quotations/Su_Kien`** (hoặc bất kỳ thư mục báo giá nào khác như VPP, Thiết bị IT...).
- **Lưu ý quan trọng:** Hãy ĐÓNG tất cả các file Excel hoặc CSV liên quan (`Tong_Hop_Bao_Gia_Granular.csv`) nếu bạn đang mở chúng trên máy tính trước khi cho AI thực thi.

## 2. Quy trình "Vạn năng" (Universal Workflow)

Hệ thống này được thiết kế theo cấu trúc **Dữ liệu hàng dọc (Granular Data)** để bạn có thể đối soát từng hạng mục nhỏ của nhà thầu.

### Bước 1: Số hóa & Trích xuất (Dành cho mọi loại báo giá)
AI sẽ tự động nhận diện bối cảnh và phân rã báo giá thành từng dòng chi tiết (Line Items). Điều này giúp bạn so sánh "táo với táo, cam với cam" giữa các đơn vị.
1. Truy cập file lệnh: 👉 **[01_Prompt_Chiet_Xuat_Bao_Gia.md](./01_Prompt_Chiet_Xuat_Bao_Gia.md)**
2. Sao chép và dán vào khung chat với AI Agent (Antigravity).
3. Kết quả: Một tệp **`Tong_Hop_Bao_Gia_Granular.csv`** chứa dữ liệu tách bạch giữa **Giá** và **Đặc tính kỹ thuật** cho từng hạng mục.

### Bước 2: Báo cáo Phân tích thầu Chiến lược (3 Phần)
AI sẽ nhóm các hạng mục giống nhau để so sánh đối đầu và đưa ra phán quyết cuối cùng.
1. Truy cập file lệnh: 👉 **[02_Prompt_Dashboard_Bao_Gia.md](./02_Prompt_Dashboard_Bao_Gia.md)**
2. Sao chép và dán vào khung chat với AI Agent.
3. **Kết quả trình duyệt thầu chuyên nghiệp:**
   - Một **Báo cáo Phân tích thầu Chiến lược 3 Phần** (`Strategic_Comparison_Report.html`).
   - Phân tích biện luận so sánh đối đầu từng hạng mục và đánh giá tổng hợp năng lực cho mỗi nhà thầu.
   - Kết luận "Thắng thầu" kèm các "Lưu ý đàm phán" (Negotiation tips).

## 3. Các lưu ý quan trọng (Trên lớp)
- **Dữ liệu Hàng dọc:** Vì mỗi nhà thầu có nhiều hàng dữ liệu, đây là bí quyết để bạn tạo ra các ma trận so sánh chi li nhất (Audit thầu chuyên sâu).
- **Tính linh hoạt:** Bộ lệnh này có thể dùng cho mọi nhu cầu thu mua: Từ dự án triệu đô đến việc mua trà sữa cho văn phòng.

---

## 4. BÀI TẬP VỀ NHÀ: Ứng dụng & Kiểm chứng thực tế

### 📈 Thử thách 1: Ứng dụng tại doanh nghiệp
Hãy sử dụng chính các báo giá thực tế mà bạn đang xử lý tại công ty để thực hành:
1. Cho AI trích xuất dữ liệu gốc hàng dọc bằng Prompt Bước 1.
2. Thiết kế báo cáo thầu (Báo cáo Phân tích Chiến lược) bằng Prompt Bước 2.

### 🔍 Thử thách 2: Kiểm chứng & Đối soát dữ liệu (QA/QC)
Tự xây dựng một Prompt để yêu cầu AI so sánh file HTML vừa tạo với dữ liệu trong thư mục báo giá gốc. Nếu thấy sai số hoặc nhầm lẫn, hãy yêu cầu AI giải trình và điều chỉnh lại báo cáo.

---

*Chúc bạn làm chủ sức mạnh AI và trở thành chuyên gia thu mua dữ liệu sành sỏi!*
