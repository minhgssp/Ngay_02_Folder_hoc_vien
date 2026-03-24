from playwright.sync_api import sync_playwright
import os
import sys

def convert_html_to_pageless_pdf(html_path, pdf_path=None):
    """
    Chuyển đổi file HTML sang PDF không chia trang (Pageless/Continuous).
    Sử dụng Playwright để tự động tính toán chiều cao nội dung.
    """
    html_path = os.path.abspath(html_path)
    if pdf_path is None:
        pdf_path = html_path.replace(".html", ".pdf")
    else:
        pdf_path = os.path.abspath(pdf_path)

    print(f"🚀 Bắt đầu chuyển đổi: {os.path.basename(html_path)}")

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # 1. Ép trình duyệt hiển thị kiểu Screen để bỏ qua ngắt trang CSS Print
        page.emulate_media(media="screen")

        # 2. Thiết lập độ rộng chuẩn (Desktop-like) để tính toán layout đúng
        page.set_viewport_size({"width": 1280, "height": 800})

        # 3. Load file HTML
        file_url = f"file:///{html_path.replace(os.path.sep, '/')}"
        page.goto(file_url)
        page.wait_for_load_state("networkidle")

        # 4. Tính toán chiều cao toàn bộ nội dung sau khi đã render
        content_height = page.evaluate("document.documentElement.scrollHeight")
        
        # 5. Cập nhật viewport bằng đúng chiều cao nội dung (giúp rendering chính xác hơn)
        page.set_viewport_size({"width": 1280, "height": content_height})

        print(f"📐 Kích thước nội dung: 1280px x {content_height}px")

        # 6. Xuất PDF bản SINGLE PAGE
        # Bí quyết: page.pdf với width/height vượt qua khổ A4 chuẩn sẽ tạo ra 1 trang liên tục
        page.pdf(
            path=pdf_path,
            width="1280px", 
            height=f"{content_height + 2}px", # Thêm 2px buffer
            margin={"top": "0px", "right": "0px", "bottom": "0px", "left": "0px"},
            print_background=True,
            scale=1.0,
            prefer_css_page_size=False # Quan trọng để không dùng CSS @page (nếu có)
        )

        browser.close()

    print(f"✅ Đã cập nhật file PDF: {pdf_path}")

if __name__ == "__main__":
    target_html = r"c:\commandcenter\08_Ylake\02_Production\C01_Masterclass_HR_AI\Session_02_Thuchanh\khoa-hoc-ai-hr\Bai_1_Tuyen_Dung\UC_01_JD_To_Landing_Page\poster_tuyen_dung.html"
    if len(sys.argv) > 1: target_html = sys.argv[1]
    
    if os.path.exists(target_html):
        convert_html_to_pageless_pdf(target_html)
