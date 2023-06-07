# import streamlit as st
# import random

# def randomize_casing(text):
#     result = ''
#     for char in text:
#         if random.randint(0, 1):
#             result += char.upper()
#         else:
#             result += char.lower()
#     return result

# st.title(randomize_casing("RaNdOmCaSEr"))
# st.write(randomize_casing("Enter any text to have its casing randomized"))

# # user_input = st.text_input("Enter text")
# text_area_text = randomize_casing('Enter text')
# user_input = st.text_area(f'{text_area_text}', height = 200)

# button_text = randomize_casing("rAndOMiZe cAsiNg")
# if st.button(f'{button_text}'):
#     randomized_text = randomize_casing(user_input)
#     st.write(f"Randomized Text: {randomized_text}")

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