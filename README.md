# 🏥 Crawl Medicine Data Through CDN and JSON

## 📖 Introduction
**Crawl_Medicine_data_through_cdn_and_json** is a Python-based project that collects medicine-related data from **CDN APIs, PDFs, and images**. The extracted data is structured and stored for further analysis.

## 🚀 Features
- ✅ Crawl **medicine images** and process them.
- ✅ **Extract data from PDFs**, including converting the first page to an image.
- ✅ **Parse JSON responses** from medical APIs.
- ✅ Store and manage extracted data in `data.json`.

## 📊 Result Summary

I successfully extracted and processed **2000+ PDFs and images** from website data.

### 📄 Extracted PDFs  
✅ **2000+ medical PDFs** collected from various sources.

![PDF Demo](https://github.com/QuangCler/Crawl_Medicine_data_through_cdn_and_json/blob/main/Demo_images/crawl_pdf_medicine.png)

---

### 🖼️ Extracted Images  
✅ **2000+ images of medicines** extracted and processed.

![Image Demo](https://github.com/QuangCler/Crawl_Medicine_data_through_cdn_and_json/blob/main/Demo_images/crawl_image_medicine.png)

---

### 📂 Summary Table

| Data Type  | Quantity | Storage Format |
|------------|---------|----------------|
| 📄 PDFs    | 2000+   | `.pdf` files in `/data/pdfs/` |
| 🖼️ Images  | 2000+   | `.jpg` / `.png` in `/data/images/` |
| 📊 JSON    | Structured | Stored in `data.json` |

✅ **All data successfully crawled and saved!**

---

## 📂 Project Structure
```
Crawl_Medicine_data/
│── .gitattributes                     # Git settings
│── convert_first_page_of_pdf_to_jpg.py # Convert first page of PDF to JPG
│── crawl_image_medicine.py            # Crawl medicine-related images
│── crawl_pdf_medicine.py              # Crawl medicine data from PDFs
│── data.json                           # JSON file to store crawled data
│── README.md                           # Project documentation
│── requirements.txt                    # Dependencies file
```

---

## 🔧 Installation

### 1️⃣ Clone the repository  
```bash
git clone https://github.com/QuangCler/Crawl_Medicine_data_through_cdn_and_json.git
cd Crawl_Medicine_data_through_cdn_and_json
```

### 2️⃣ Create a virtual environment (optional but recommended)  
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3️⃣ Install dependencies  
```bash
pip install -r requirements.txt
```

---

## 🏃‍♂️ Usage

### Convert First Page of PDF to JPG  
```bash
python convert_first_page_of_pdf_to_jpg.py
```

### Crawl Medicine Image Data  
```bash
python crawl_image_medicine.py
```

### Crawl PDF Medicine Data  
```bash
python crawl_pdf_medicine.py
```

---

## 🏗️ Future Improvements  
- 🔄 **Support for additional APIs and document formats**.  
- 📊 **Data visualization and analysis tools**.  
- 🔍 **Improved error handling and logging**.  

---

## 🤝 Contribution  
Feel free to submit **issues, pull requests, or suggestions** to improve the project.

---

## 📜 License  
This project is licensed under the **MIT License**.

---

📌 **Developed by [Your Name]** | 🚀 Happy Crawling!
