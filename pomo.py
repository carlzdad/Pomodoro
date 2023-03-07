import streamlit as st
import time

# Adapted from https://github.com/dataprofessor/pomodoro-app

# --- Greeting ---
st.title("""
Welcome to Pomodoro!
"""
)

# --- Converter ---
def convert(t):
    # Convert minutes to seconds
    return int(t) * 60


# --- App ---
settings = st.form(key='settings')
settings.subheader("""
Timer Settings (mins)
To edit the timer, update the setting value and click start. 
"""
)
# st.caption("""
# To reset the Pomo Sessions counter, please refresh the page. 
# """
# )
focus = int(settings.text_input("Focus: ", value = 25))
focus = convert(focus)
short = settings.text_input("Short Break: ", value = 5)
short = convert(short)
long = int(settings.text_input("Long Break: ", value = 30))
long = convert(long)

start = settings.form_submit_button("Start")

focus_count = 0
short_count = 0

if start:
    
    focus_count += 1
    short_count += 1 

    # col1, col2 = st.columns(2)
    # with col1:
    #     st.metric(label = "Focus Sessions",value = focus_count)
    # with col2: st.metric(label = "Short Breaks", value = short_count)
    
    with st.empty():
        if focus_count >= 4 and focus_count % 4 == 0:
            while long:
                st.success("🎉 Time for a long break!")
                mins, secs = divmod(long, 60)
                timer = '{:02d}:{:02d}'.format(mins, secs)
                st.header(f"""
                Get up, take a break, see you in 30.
                {timer}
                """)
                time.sleep(1)
                long -= 1
                
        else: 
            while focus:
                mins, secs = divmod(focus, 60)
                timer = '{:02d}:{:02d}'.format(mins, secs)
                st.header(f"""
                ⏱️ {timer} Werk it. 
                """)
                time.sleep(1)
                focus -= 1
                st.success("🎉 Time for a break!")
            while short:
                mins, secs = divmod(short, 60)
                timer = '{:02d}:{:02d}'.format(mins, secs)
                st.header(f"""
                {timer} Take a break!
                """)
                time.sleep(1)
                short -= 1
                st.success("Back to it!")
                
    # reset = st.button("Reset")
    # if reset:
    #     st.stop()