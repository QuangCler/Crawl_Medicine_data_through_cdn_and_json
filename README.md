# 🏥 Crawl Medicine Data Through CDN and JSON

## 📖 Introduction
**Crawl_Medicine_data_through_cdn_and_json** is a Python-based project that collects medicine-related data from **CDN APIs, PDFs, and images**. The extracted data is structured and stored for further analysis.

## 🚀 Features
- ✅ Crawl **medicine images** and process them.
- ✅ **Extract data from PDFs**, including converting the first page to an image.
- ✅ **Parse JSON responses** from medical APIs.
- ✅ Store and manage extracted data in `data.json`.

---

## 📂 Project Structure
Crawl_Medicine_data/ │── .gitattributes # Git settings │── convert_first_page_of_pdf_to_jpg.py # Convert first page of PDF to JPG │── crawl_image_medicine.py # Crawl medicine-related images │── crawl_pdf_medicine.py # Crawl medicine data from PDFs │── data.json # JSON file to store crawled data │── README.md # Project documentation │── requirements.txt # Dependencies file

yaml
Sao chép
Chỉnh sửa

---

## 🔧 Installation

### 1️⃣ Clone the repository  
```bash
git clone https://github.com/QuangCler/Crawl_Medicine_data_through_cdn_and_json.git
cd Crawl_Medicine_data_through_cdn_and_json
2️⃣ Create a virtual environment (optional but recommended)
bash
Sao chép
Chỉnh sửa
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3️⃣ Install dependencies
bash
Sao chép
Chỉnh sửa
pip install -r requirements.txt
🏃‍♂️ Usage
Convert First Page of PDF to JPG
bash
Sao chép
Chỉnh sửa
python convert_first_page_of_pdf_to_jpg.py
Crawl Medicine Image Data
bash
Sao chép
Chỉnh sửa
python crawl_image_medicine.py
Crawl PDF Medicine Data
bash
Sao chép
Chỉnh sửa
python crawl_pdf_medicine.py
🏗️ Future Improvements
🔄 Support for additional APIs and document formats.
📊 Data visualization and analysis tools.
🔍 Improved error handling and logging.
🤝 Contribution
Feel free to submit issues, pull requests, or suggestions to improve the project.

📜 License
This project is licensed under the MIT License.

