import streamlit as st
import function as fun
import base64

time = fun.time_now()

# Функція для перетворення зображення у base64
def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# Отримання base64 зображення
img_base64 = get_base64("image.png")

# Вставка стилю з правильним CSS
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{img_base64}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        color: white;
        
    }}
    
    label {{
        color: white !important;
    }}
    
    </style>
    """,
    unsafe_allow_html=True
)


st.title(time)
text_placeholder = st.empty()
res = st.time_input("Оберіть час о котрій прокидатися: ", key="wakeup")

if res:
    result = [res.hour, res.minute, res.second]
    wakeup = fun.alarm_clock(*result)
    text_placeholder.markdown(
        f"<p style='color:white;'><h3>Час для підйому: {wakeup}</h3></p>",
        unsafe_allow_html=True
    )

