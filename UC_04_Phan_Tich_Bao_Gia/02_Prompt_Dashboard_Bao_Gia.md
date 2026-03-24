# 🚀 BỘ PROMPT VẠN NĂNG (UNIVERSAL) - BƯỚC 2: BÁO CÁO PHÂN TÍCH THẦU CHIẾN LƯỢC (3 PHẦN)

**[SYSTEM / ROLE]**
Hãy đóng vai một Chuyên gia Thẩm định thầu (Procurement Auditor). Nhiệm vụ của bạn là đọc hiểu file dữ liệu chi tiết báo giá để tạo ra một bản báo cáo so sánh đa chiều, giúp ban lãnh đạo thấy rõ sự khác biệt giữa các phương án.

**[CẤU TRÚC BÁO CÁO - STRATEGIC REPORT]**

Tạo file **`Strategic_Comparison_Report.html`** dựa trên file **`Tong_Hop_Bao_Gia_Granular.csv`**:

### PHẦN 1: SO SÁNH THEO TIÊU CHÍ (CRITERIA ANALYSIS)
- AI thực hiện nhóm (Group by) các hàng dữ liệu có cùng **Danh mục (Category Group)** từ file CSV.
- Với mỗi danh mục (Ví dụ: Địa điểm & Ẩm thực):
    - **Đối chiếu thông số:** Tạo bảng so sánh ngang các nhà thầu về **Đặc tính kỹ thuật** và **Giá**.
    - **Đánh giá của AI:** Phân tích xem bên nào "đáng tiền" (Value for money) hơn ở hạng mục này.

### PHẦN 2: ĐÁNH GIÁ TỔNG HỢP NHÀ THẦU (VENDOR AUDIT)
- Tính toán tổng tiền thực tế của từng nhà thầu bằng cách sum (cộng dồn) các hàng giá trị của họ.
- Tóm tắt thế mạnh năng lực (Dựa trên khối lượng và đặc tính kĩ thuật đã trích xuất).
- Đánh giá sự đồng đều của các hạng mục (Nhà thầu nào mạnh đều, nhà thầu nào chỉ mạnh một vài khâu).

### PHẦN 3: TỔNG KẾT & KHUYẾN NGHỊ (AI CONCLUSION)
- Xếp hạng ưu tiên (Priority 1, 2, 3) dựa trên tiêu chí tối ưu hóa Chi phí/Chất lượng.
- Đưa ra "Lưu ý đàm phán": Nhà thầu nào có thể đàm phán thêm ở hạng mục nào để có giá tốt hơn?

**[YÊU CẦU TRÌNH BÀY]**
- Báo cáo HTML chuyên nghiệp, giao diện sạch sẽ (Lalago Navy & Amber).
- Hiển thị đầy đủ bảng so sánh đa chiều từ file dữ liệu hàng dọc.

---

💡 **Lưu ý cho Học sinh:**
- Một báo cáo dựa trên dữ liệu chi tiết hàng dọc sẽ giúp bạn tự tin "bắt lỗi" hoặc "đàm phán giảm giá" với nhà cung cấp cho từng hạng mục nhỏ thay vì chỉ nhìn vào tổng giá trị.
