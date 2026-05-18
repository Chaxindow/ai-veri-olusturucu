import os
from dotenv import load_dotenv

# .env dosyasındaki değişkenleri sisteme yükler
load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")

