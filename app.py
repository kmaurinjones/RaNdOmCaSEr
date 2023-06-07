import streamlit as st
import random
import SessionState

def randomize_casing(text):
    result = ''
    for char in text:
        if random.randint(0, 1):
            result += char.upper()
        else:
            result += char.lower()
    return result

st.title(randomize_casing("RaNdOmCaSEr"))

# Informative text that doesn't change upon refresh
st.write(randomize_casing("Enter any text below to have its casing randomized:"))

# Consistent prompt text for text area
user_input = st.text_area("Enter text:", height = 200)

# Store user_input in a session state so it can be accessed even after reruns
state = SessionState.get(user_input=user_input)

if user_input:
    # Update the stored user_input whenever new input is entered
    state.user_input = user_input

button_text = randomize_casing("rAndOMiZe cAsiNg")
if st.button(button_text):
    randomized_text = randomize_casing(state.user_input)
    st.text_area("Randomized Text:", randomized_text, height = 200)