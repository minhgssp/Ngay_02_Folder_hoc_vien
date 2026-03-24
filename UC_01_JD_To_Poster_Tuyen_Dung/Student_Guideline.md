# Hướng dẫn học tập (Student Guideline): Chuyển đổi JD thành Poster Tuyển dụng

Chào mừng bạn đến với học phần thực hành chuyển đổi Bản mô tả công việc (JD) thành một trang Poster Tuyển dụng tuyển dụng chuyên nghiệp. Hướng dẫn này giúp bạn tự học cách vận hành AI Agent để tạo ra sản phẩm hoàn chỉnh.

## 1. Chuẩn bị dữ liệu đầu vào

- Đảm bảo bạn đã có file JD (định dạng `.txt` hoặc .md hoặc .doc).
- (Tùy chọn) Nếu bạn đã có ảnh Banner thiết kế sẵn, hãy đổi tên thành `banner.png` và để cùng thư mục.

## 2. Quy trình thực hành (Tại lớp)

Thay vì phải nhớ từng bước kỹ thuật phức tạp, chúng ta sẽ sử dụng bộ Prompt tối ưu đã được đóng gói sẵn.

### Bước 1: Gọi Prompt thiết kế

Hãy truy cập file sau để lấy lệnh:
👉 **[03_Prompt_Poster_Tuyen_Dung_V2.md](./03_Prompt_Poster_Tuyen_Dung_V2.md)**

### Bước 2: AI Agent thực thi

1. Mở file Prompt trên, sao chép (Ctrl+C) toàn bộ nội dung trong khung **[SYSTEM / ROLE]**.
2. Dán (Ctrl+V) vào khung chat với AI Agent.
3. Cung cấp file JD hoặc dán nội dung JD của bạn vào.

### Bước 3: Kiểm tra kết quả

Sau khi AI Agent báo đã hoàn thành, hãy thực hiện các thao tác sau để xem sản phẩm:

1. Tại thanh Sidebar bên trái của VS Code (hoặc trình soạn thảo), chuột phải vào thư mục `UC_01_JD_To_Landing_Page`.
2. Chọn **Reveal in File Explorer** (Mở trong thư mục máy tính).
3. Tìm file **`poster_tuyen_dung.html`** mới được sinh ra.
4. Chuột phải vào file, chọn **Open with** và chọn trình duyệt của bạn (Chrome/Edge) để xem kết quả.

## 3. Các lưu ý quan trọng (Trên lớp)

- **Banner:** AI Agent sẽ tự động tìm kiếm file banner có sẵn trong thư mục. Nếu không thấy, nó sẽ hỏi ý kiến bạn trước khi thiết kế mới.
- **Vị trí lưu trữ:** File Poster Tuyển dụng sinh ra luôn nằm cùng thư mục với file JD đỏ của bạn.

## 4. Xuất bản và chia sẻ

Để xuất bản Poster Tuyển dụng thành file PDF hoặc Ảnh để gửi báo cáo, bạn có 3 cách thực hiện (Khuyến khích dùng Cách 1):

- **Cách 1: Sử dụng AI Agent xuất PDF tự động (Pageless PDF)**
  Hãy nhắn vào khung chat yêu cầu sau để AI Agent tự động chạy mã lệnh:

  > *"Hãy chạy script `04_export_pageless_pdf.py` để xuất file `poster_tuyen_dung.html` thành PDF nhé."*
  >
- **Cách 2: Sử dụng Chrome Extension (Thủ công)**
  Cài đặt Extension **GoFullPage** và bấm chụp tàn màn hình để tải ảnh/PDF.
- **Cách 3: Sử dụng Safari trên máy Mac (Thủ công)**
  Chọn **File > Export as PDF** trực tiếp trên trình duyệt.

---

## BÀI TẬP VỀ NHÀ: Cá nhân hóa thương hiệu

Để trang Poster Tuyển dụng trông chuyên nghiệp và đúng với hình ảnh công ty bạn, hãy thực hiện các tùy chỉnh sau tại nhà:

### 🎨 Tùy chỉnh màu sắc

Trong file **[03_Prompt_Poster_Tuyen_Dung_V2.md](./03_Prompt_Poster_Tuyen_Dung_V2.md)**, hãy tìm đến phần **Brand Guidelines** và thay đổi mã màu (Hex Code) theo ý muốn:

- **Primary Color:** Thay đổi mã màu chủ đạo của công ty bạn.
- **Accent Color:** Thay đổi mã màu điểm nhấn (cho nút bấm).
- **Mẹo:** Bạn có thể dùng trang [coolors.co](https://coolors.co) để tìm bộ phối màu đẹp.

### 🖼️ Bổ sung Logo công ty

1. Chuẩn bị tệp ảnh logo của bạn và đổi tên thành `logo.png`.
2. Gửi thêm yêu cầu cho AI: *"Hãy chèn tệp logo.png vào vị trí trang trọng trong phần Header."*

---

---

*Chúc bạn có trải nghiệm và sản phẩm hoàn hảo!*
