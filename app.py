# import necessary libraries
import streamlit as st
import random

def random_case(text):
    # Convert string to list to use list methods
    text = list(text)
    for i in range(len(text)):
        # Randomly decide if the character should be uppercase or lowercase
        if random.choice([True, False]):
            text[i] = text[i].upper()
        else:
            text[i] = text[i].lower()
    return "".join(text)

st.title(random_case("RaNdOmCaSEr"))

# Text input box
user_input = st.text_input("Enter your text here:")

if user_input:
    # Apply random casing to the input string
    result = random_case(user_input)

    # Display the result
    # st.text("Your text with random casing:")
    st.write(result)
