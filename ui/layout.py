import streamlit as st
from core.config import API_KEY

def setup_page() -> None:
    st.set_page_config(page_title="Profesyonel Veri Üretici", page_icon="📈", layout="wide")

def render_header() -> None:
    st.title("Profesyonel Yapay Zeka Veri Seti Üretici")
    st.markdown("Kendi API anahtarınızı girin ve detaylı senaryolarla veri setleri oluşturun.")
    st.divider()

def render_sidebar() -> tuple[str, str]:
    with st.sidebar:
        st.header("Ayarlar")
        
        default_key = API_KEY if API_KEY else ""

        user_api_key = st.text_input(
            "OpenAI API Anahtarı", 
            value=default_key, 
            type="password", 
            help="Kendi OpenAI API anahtarınızı buraya yapıştırın. Bu anahtar kaydedilmez."
        )

        model_choice = st.selectbox("Yapay Zeka Modeli", ["gpt-5.4-mini", "gpt-5.4"])
        return user_api_key, model_choice


def render_input_section() -> tuple[str, int, str]:
    col1, col2 = st.columns(2)
    with col1:
       st.subheader("📋 Parametreler")
       default_scenario = "Bir şirkette İnsan Kaynakları, Satın Alma ve Destek departmanlarına gelen örnek e-postalar. Kolonlar: 'E-posta Metni', 'Departman', 'Öncelik Durumu' şeklinde olsun."
       topic = st.text_area("Senaryo ve Veri Detayları", value=default_scenario, height=120)
       row_count = st.number_input("Satır Sayısı", min_value=1, max_value=1000, value=200, step=10)
    with col2:
        st.subheader("🎨 Ton Seçimi")
        tone = st.selectbox("Ton/Tarz", ["Resmi", "Günlük", "Agresif", "Pozitif"])

    return topic, row_count, tone