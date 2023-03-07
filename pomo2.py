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
st.caption("""
To reset the timer, press stop at the top right corner. 
Then updated the value and hit start. 
""")
focus = int(settings.text_input("Focus: ", value = 25))
focus = convert(focus)
short = settings.text_input("Short Break: ", value = 5)
short = convert(short)
long = int(settings.text_input("Long Break: ", value = 30))
long = convert(long)
submit = settings.form_submit_button("Start")

pomo_count = []


if submit:
    with st.empty():
        while focus:
            mins, secs = divmod(focus, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            st.header(f"""
            ⏱️ {timer}
            Let's get focused.
            """)
            time.sleep(1)
            focus -= 1
            st.success("🎉 Time for a break!")
            pomo_count.append('1')
            # if len(pomo_count) == 4:
            #     while long:
            #         st.success("🎉 Time for a long break!")
            #         mins, secs = divmod(long, 60)
            #         timer = '{:02d}:{:02d}'.format(mins, secs)
            #         st.header(f"""
            #         ⏱️ {timer}
            #         Get up, take a break, see you in 30.
            #         """)
            #         time.sleep(1)
            #         long -= 1

        while short:
            mins, secs = divmod(short, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            st.header(f"""
            ⏱️ {timer}
            Take a break!
            """)
            time.sleep(1)
            short -= 1
            st.success("Back to it!")







