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

# Streamlit code for randomcaser
st.title(random_case('RandomCaser'))

# Text input box for randomcaser
user_input = st.text_input("Enter your text here:")

if user_input:
    # Initial random casing of the input string
    result = random_case(user_input)
    
    # Button to re-randomize the text
    if st.button("Re-randomize"):
        result = random_case(user_input)
    
    st.markdown(random_case("Copy to clipboard using the button in the field below."))
    # Display the result as code, so it gets a "copy" button
    st.code(result, language="text")
