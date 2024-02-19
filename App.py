import streamlit as st
import tempfile
import google.generativeai as genai
import os
import PIL.Image

# Configure the API key
os.environ['GOOGLE_API_KEY'] = 'AIzaSyAc7Ii4wHf_whau2q--rgjfdht8-I5xhSY'

# Define the function to generate questions
def generate_questions(image):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content(["Prepare 5 questions for the given image", image], stream=True)
    response.resolve()
    return response.text

# Define the main Streamlit app
def main():
    st.title("Image Question Generation")

    # File uploader widget
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display the uploaded image
        image = PIL.Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        # Generate questions on button click
        if st.button('Generate Questions'):
            with st.spinner('Generating questions...'):
                questions = generate_questions(image)
                st.markdown(questions)

if __name__ == "__main__":
    main()
