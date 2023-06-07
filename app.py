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

# Streamlit code
st.title(random_case('randomcaser'))

instruction_text = random_case("Enter your text here:")

# Text input box
user_input = st.text_input(instruction_text)

if user_input:
    # Apply random casing to the input string
    result = random_case(user_input)

    # Display the result
    # st.text(random_case("Your text with random casing:"))
    st.write(result)

    st.write("\n")
    st.write(random_case("If you like this app, consider leaving a ⭐ on the GitHub repo. If you have any feedback or would like any additions to be made to the app, feel free to email me at kmaurinjones@gmail.com."))