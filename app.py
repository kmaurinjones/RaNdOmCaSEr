
import streamlit as st
import random

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

button_text = randomize_casing("rAndOMiZe cAsiNg")
if st.button(button_text):
    randomized_text = randomize_casing(user_input)
    # st.write(f"Randomized Text: {randomized_text}")
    st.text_area(randomized_text, height = 200)