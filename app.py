# import streamlit as st
# import random

# def random_case(text):
#     # Convert string to list to use list methods
#     text = list(text)
#     for i in range(len(text)):
#         # Randomly decide if the character should be uppercase or lowercase
#         if random.choice([True, False]):
#             text[i] = text[i].upper()
#         else:
#             text[i] = text[i].lower()
#     return "".join(text)

# # Streamlit code
# st.title(random_case('randomcaser'))

# # Text input box
# # user_input = st.text_input(random_case("Enter your text here:"))
# user_input = st.text_input("Enter your text here:")

# if user_input:
#     # Apply random casing to the input string
#     result = random_case(user_input)

#     # Display the result
#     # st.text("Your text with random casing:")
#     st.write(result)


# #### INTEGRATE THIS INTO THE ABOVE

# def main():
#     st.title("Copy Paste in streamlit")
#     pathinput = st.text_input("Enter your Path:")
#     #you can place your path instead
#     Path = f'''{pathinput}'''
#     st.code(Path, language="python")
#     st.markdown("Now you get option to copy")
# if __name__ == "__main__":main()

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
    # Apply random casing to the input string
    result = random_case(user_input)
    st.markdown("Copy to clipboard using the button in the field below.")
    # Display the result as code, so it gets a "copy" button
    st.code(result, language = "text")