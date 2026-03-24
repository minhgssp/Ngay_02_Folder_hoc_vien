import http.server
import socketserver
import webbrowser
import os

# --- Cấu trúc thư mục ---
PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def start_server():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"--- [RECRUITMENT DASHBOARD SERVER STARTED] ---")
        print(f"Server dang chay tai: http://localhost:{PORT}/Recruitment_Dashboard.html")
        print(f"Nhan Ctrl + C de dung Server.")
        
        # Tu dong mo trinh duyet
        url = f"http://localhost:{PORT}/Recruitment_Dashboard.html"
        webbrowser.open(url)
        
        httpd.serve_forever()

if __name__ == "__main__":
    start_server()
