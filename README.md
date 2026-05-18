# Yapay Zeka Veri Seti Oluşturucu 

Bu proje, OpenAI API ve Streamlit kullanarak dinamik, özelleştirilebilir ve anında indirilebilir veri setleri oluşturmanızı sağlayan modüler bir web uygulamasıdır.

## Özellikler
* **Dinamik Prompting:** Kendi senaryonuzu, satır sayısını ve veri tonunu belirleyin.
* **Modüler Yapı:** Temiz kod (clean code) prensiplerine uygun, yönetilebilir klasör mimarisi.
* **Güvenli API Yönetimi:** `.env` dosyası veya doğrudan kullanıcı arayüzü üzerinden API anahtarı girişi.
* **Hızlı Çıktı:** Üretilen veriyi anında tablo olarak görüntüleme ve tek tıkla CSV olarak indirme.

## Kurulum Adımları

1. **Projeyi indirin:**
```bash
git clone [https://github.com/Chaxindow/ai-veri-olusturucu.git](https://github.com/Chaxindow/ai-veri-olusturucu.git)
cd ai-veri-olusturucu
```

2. **Gerekli kütüphaneleri yükleyin:**
Python yüklü olduğundan emin olun ve terminalde şu komutu çalıştırın:
```bash
pip install -r requirements.txt
```

3. **API Anahtarınızı ayarlayın (İsteğe bağlı):**
Ana dizinde bir `.env` dosyası oluşturun ve OpenAI API anahtarınızı ekleyin:
```env
OPENAI_API_KEY=sizin-api-anahtariniz-buraya
```
*(Not: `.env` dosyası oluşturmazsanız, API anahtarınızı uygulamayı açtığınızda ekrandaki kutucuğa da girebilirsiniz.)*

## Nasıl Çalıştırılır?

Terminalinizde aşağıdaki komutu çalıştırarak uygulamayı başlatın:
```bash
streamlit run app.py
```
Tarayıcınızda açılan sekmeden veri setlerinizi üretmeye başlayabilirsiniz!

---

# AI Dataset Generator 📈

This project is a modular web application that allows you to create dynamic, customizable, and instantly downloadable datasets using the OpenAI API and Streamlit.

## Features
* **Dynamic Prompting:** Set your own scenario, row count, and data tone.
* **Modular Structure:** Built with clean code principles and manageable folder architecture.
* **Secure API Management:** Enter your API key via a `.env` file or directly through the user interface.
* **Fast Export:** View the generated data instantly as a table and download it as a CSV with one click.

## Installation Steps

1. **Clone the repository:**
```bash
git clone [https://github.com/Chaxindow/ai-veri-olusturucu.git](https://github.com/Chaxindow/ai-veri-olusturucu.git)
cd ai-veri-olusturucu
```

2. **Install required libraries:**
Make sure you have Python installed, then run:
```bash
pip install -r requirements.txt
```

3. **Set up your API Key (Optional):**
Create a `.env` file in the root directory and add your OpenAI API key:
```env
OPENAI_API_KEY=your-api-key-here
```
*(Note: If you skip this step, you can simply paste your API key into the input box on the app's user interface.)*

## How to Run

Start the application by running the following command in your terminal:
```bash
streamlit run app.py
```
A new tab will open in your browser where you can start generating datasets!
