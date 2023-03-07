import streamlit as st
import time

# --- CSS --- 
# def local_css(file_name):
#     with open(file_name) as f:
#         st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
# local_css("style.css")


# --- Greeting ---
st.title("""
⏱️ Welcome to Pomodoro!

Let's get focused.
"""
)

# --- converter ---
def convert(t):
    return int(t) * 60

# --- App ---
settings = st.form(key='settings')
settings.subheader("""
Timer Settings (mins)
"""
)
focus = int(settings.text_input("Focus: ", value = 25))
focus = convert(focus)
short = settings.text_input("Short Break: ", value = 5)
short = convert(short)
long = settings.text_input("Long Break: ", value = 15)
submit = settings.form_submit_button("Start")

if submit:
    with st.empty():
        while focus:
            mins, secs = divmod(focus, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            st.header(f"⏱️ {timer}")
            time.sleep(1)
            focus -= 1
            st.success("🎉 25 minutes done, time for a break!")
        while short:
            s = convert(short)
            mins, secs = divmod(s, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            st.header(f"⏱️ {timer}")
            time.sleep(1)
            s -= 1
            st.success("Back to it!")







