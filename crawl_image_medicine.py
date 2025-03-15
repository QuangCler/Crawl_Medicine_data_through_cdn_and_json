import json
import requests
import os

file_path = "Crawl\data.json"
with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)

image_folder = "downloaded_images"
os.makedirs(image_folder, exist_ok=True)

for item in data:
    ten_thuoc = item.get("tenThuoc", "Unknown").replace(" ", "_")
    image_urls = item.get("images", [])

    for idx, url in enumerate(image_urls):
        if url: 
            image_ext = url.split(".")[-1]  
            image_path = os.path.join(image_folder, f"{ten_thuoc}_{idx}.{image_ext}")

            try:
                response = requests.get(url, stream=True)
                if response.status_code == 200:
                    with open(image_path, "wb") as img_file:
                        for chunk in response.iter_content(1024):
                            img_file.write(chunk)
                    print(f"Tải thành công: {image_path}")
                else:
                    print(f"Lỗi khi tải ảnh {url}: {response.status_code}")
            except Exception as e:
                print(f"Lỗi khi tải ảnh {url}: {str(e)}")

print("Hoàn tất quá trình tải ảnh!")
thuoc_co_anh = [item for item in data if item.get("images") and any(item["images"])]

for thuoc in thuoc_co_anh:
    print(f"Tên thuốc: {thuoc['tenThuoc']}")
    print(f"Ảnh: {thuoc['images']}")
    print("-" * 50)
