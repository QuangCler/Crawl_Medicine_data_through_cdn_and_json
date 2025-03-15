# 🏥 Crawl Medicine Data Through CDN and JSON

## 📖 Introduction
**Crawl_Medicine_data_through_cdn_and_json** is a Python-based project that collects medicine data from **CDN-based APIs** and parses **JSON responses**. The extracted data can be stored for further analysis.

## 🚀 Features
- ✅ Fetch **medicine data from public APIs using CDN**.
- ✅ **Convert PDF documents to images** (if applicable).
- ✅ **Parse JSON responses** and store them in structured formats.
- ✅ **Handle API requests, rate limits, and retries**.

## 🛠️ Tech Stack
- **Programming Language**: Python  
- **Libraries Used**:
  - `requests` (for API calls)
  - `pdf2image` (for converting PDF to images)
  - `os` (for file handling)
  - `json` (for parsing JSON responses)

## 📂 Project Structure
Crawl_Medicine_data/
│── .gitattributes                     # Git settings
│── convert_first_page_of_pdf_to_jpg.py # Script to convert the first page of PDF to JPG
│── crawl_image_medicine.py            # Script to crawl medicine-related images
│── crawl_pdf_medicine.py              # Script to crawl medicine data from PDFs
│── data.json                           # JSON file to store crawled data
│── README.md                           # Project documentation
│── requirements.txt                     # Dependencies file

## 🔧 Installation
1️⃣ **Clone the repository**  
git clone https://github.com/your-QuangCler/Crawl_Medicine_data_through_cdn_and_json.git
cd Crawl_Medicine_data_through_cdn_and_json
2️⃣ **Create a virtual environment (optional but recommended)**
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3️⃣ **Install dependencies**
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
 