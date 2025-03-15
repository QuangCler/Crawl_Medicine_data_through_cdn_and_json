import json
import requests
import os

# Đọc dữ liệu từ file JSON
file_path = r"Crawl\data.json"
with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)

pdf_folder = r"C:\Users\QuangCler\Desktop\Coding\downloaded_pdfs"
os.makedirs(pdf_folder, exist_ok=True)

failed_pdfs = []

for item in data:
    ten_thuoc = item.get("tenThuoc", "Unknown").replace(" ", "_")
    pdf_file_name = item.get("meta", {}).get("fileName")

    if pdf_file_name:
        pdf_url = f"https://cdn.drugbank.vn/{pdf_file_name}"
        pdf_path = os.path.join(pdf_folder, pdf_file_name)

        # Tải PDF
        try:
            response = requests.get(pdf_url, stream=True, timeout=10)
            if response.status_code == 200:
                with open(pdf_path, "wb") as pdf_file:
                    for chunk in response.iter_content(1024):
                        pdf_file.write(chunk)
                print(f"Tải thành công: {pdf_path}")
            else:
                print(f"Lỗi khi tải PDF {pdf_url}: {response.status_code}")
                failed_pdfs.append(pdf_url)
        except Exception as e:
            print(f"Lỗi khi tải PDF {pdf_url}: {str(e)}")
            failed_pdfs.append(pdf_url)

if failed_pdfs:
    print("\nCác PDF không tải được:")
    for url in failed_pdfs:
        print(url)

print("\nHoàn tất quá trình tải PDF!")
