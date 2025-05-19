import streamlit as st
import function as fun
import base64

time = fun.time_now()


def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()


img_base64 = get_base64("image.png")


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

    <script>
    const interval = setInterval(() => {{
        const inputs = document.querySelectorAll('input[type="time"]');
        if (inputs.length) {{
            inputs.forEach(input => input.setAttribute('readonly', true));
            clearInterval(interval);
        }}
    }}, 500);
    </script>
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
        f"<h3 style='color:white;'>Час для підйому: {wakeup}</h3>",
        unsafe_allow_html=True
    )
