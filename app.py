import streamlit as st
import ui.layout as ui
from core.engine import generate_dataset

# Arayüzü oluştur
ui.setup_page()
ui.render_header()


# Ayarlar alınacak
user_api_key, selected_model = ui.render_sidebar()
topic, row_count, tone = ui.render_input_section()

st.divider()
if st.button("Veri Setini Üret", type="primary", use_container_width=True):
# API Anahtarı boş mu diye kontrol ediyoruz
    if not user_api_key:
        st.error("Lütfen sol menüden OpenAI API Anahtarınızı girin. İşlem yapılamıyor.")
    else:
        with st.spinner(f"{selected_model} verileri hazırlıyor, lütfen bekleyin..."):
            try:
                # Motoru çağırırken user_api_key'i de gönderiyoruz
                df = generate_dataset(
                    api_key=user_api_key, 
                    model=selected_model, 
                    topic=topic, 
                    tone=tone, 
                    row_count=row_count
                )
                
                st.success("Veri seti başarıyla oluşturuldu!")
                st.dataframe(df, use_container_width=True)
                
                csv_data = df.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="📥 CSV Olarak İndir",
                    data=csv_data,
                    file_name="ozel_veri_seti.csv",
                    mime="text/csv"
                )
                
            except Exception as e:
                st.error(f"Sistem Hatası: {e}")