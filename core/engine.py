from openai import OpenAI
import pandas as pd
import json


def generate_dataset(api_key: str,model:str, topic:str, tone:str, row_count:int) -> pd.DataFrame:
    """OpenAI API kullanarak dinamik veri seti oluşturur."""

    client = OpenAI(api_key=api_key)

    system_prompt = (
        "Sen profesyonel bir veri bilimcisin. İstenen veriyi SADECE JSON formatında ver. "
        "Format şu şekilde olmalı: {'data': [{'Kolon1': 'Deger1', 'Kolon2': 'Deger2'}]} "
        "Başka hiçbir açıklama yazma. Satır sayısı belirtildiyse o sayıda üretmeye çalış."
    )

    user_prompt = f"Senaryo ve Detaylar: {topic}. Ton: {tone}. İstenen Satır Sayısı: {row_count}. Lütfen bu özelliklere uygun, ilgili departmanları ve içerikleri belirten kolonlara sahip bir veri seti üret."

    response = client.chat.completions.create(
        model=model,
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.7,
    )

    result = response.choices[0].message.content
    result_dict = json.loads(result)
    return pd.DataFrame(result_dict['data'])
