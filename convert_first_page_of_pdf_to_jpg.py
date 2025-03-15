import os
from pdf2image import convert_from_path

pdf_folder = r"C:\Users\QuangCler\Desktop\Coding\downloaded_pdfs"
output_folder = r"C:\Users\QuangCler\Desktop\Coding\Crawl\First_img"
poppler_path = r"C:\Program Files\poppler-windows-24.08.0-0\bin"

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(pdf_folder):
    if filename.lower().endswith(".pdf"):
        pdf_path = os.path.join(pdf_folder, filename)
        try:
            images = convert_from_path(pdf_path, first_page=1, last_page=1, poppler_path=poppler_path)
            if images:
                image_filename = os.path.splitext(filename)[0] + ".jpg"
                image_path = os.path.join(output_folder, image_filename)
                images[0].save(image_path, "JPEG")
                print(f"Đã lưu ảnh: {image_path}")
            else:
                print(f"Không tìm thấy trang nào trong PDF: {filename}")
        except Exception as e:
            print(f"Lỗi khi xử lý {filename}: {e}")

print("Hoàn thành chuyển đổi!") 
