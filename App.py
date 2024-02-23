import streamlit as st
import textwrap
import os
import PIL.Image
import google.generativeai as genai

# Used to securely store your API key
os.environ['GOOGLE_API_KEY'] = 'AIzaSyAc7Ii4wHf_whau2q--rgjfdht8-I5xhSY'
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

genai.configure(api_key=GOOGLE_API_KEY)
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        generative_model_name = m.name
        break

def generate_questions_from_image(image):
    # Display the uploaded image
    st.image(image, caption='Uploaded Image', use_column_width=True)
    
    # Initialize generative model
    model = genai.GenerativeModel('gemini-pro-vision')
    
    # Generate questions based on the image
    response = model.generate_content(["Prepare 3 questions for the given image", image], stream=True)
    response.resolve()
    
    # Display the generated questions
    st.write(response.text)
    print(response.text)

def about_project():
    st.title("About Project")
    st.write(
        """
        ## Project Overview
        The Image to Questions Generator is a web application designed to generate questions based on an uploaded image. Leveraging state-of-the-art generative AI models, the application processes the content of the image and formulates questions to prompt further understanding or analysis.

        ## Motivation
        Visual content is abundant on the internet, and extracting meaningful information from images is crucial for various applications such as educational content creation, image analysis, and content moderation. However, manually generating questions from images can be time-consuming and resource-intensive. Hence, the aim of this project is to automate this process using machine learning techniques.

        ## Features
        - **Image Upload**: Users can upload an image in common formats like JPG, JPEG, or PNG.
        - **Question Generation**: Upon image upload, the application processes the image content using a generative AI model to formulate relevant questions.
        - **Streamlit Interface**: The application is built using Streamlit, a user-friendly framework for creating data-focused web applications in Python.
        - **Markdown Display**: The generated questions are displayed using Markdown formatting for clarity and readability.

        ## Technologies Used
        - **Streamlit**: Used to build the web interface of the application.
        - **PIL (Python Imaging Library)**: Utilized to handle image uploads and processing.
        - **GenerativeAI by Google**: Integrated to access state-of-the-art generative AI models for question generation.
        """
    )

    st.markdown("<h1 style='text-align: left; color: white; font-size: 20px;'>Architecture of the project:</h1>", unsafe_allow_html=True)
    st.image('Architecture.jpeg', use_column_width=True)

    st.write(
        """
        ## How It Works
        1. **Image Upload**: Users upload an image using the provided file uploader.
        2. **Question Generation**: The uploaded image is processed by a pre-trained generative AI model capable of understanding visual content.
        3. **Output Display**: The generated questions are displayed on the web interface, providing users with prompts based on the content of the uploaded image.

        ## Future Enhancements
        - **Improved Question Quality**: Refinement of the generative model or integration of feedback mechanisms to enhance the quality of generated questions.
        - **Support for Different Languages**: Extension of the application to support question generation in multiple languages.
        - **Customization Options**: Addition of features allowing users to customize the types or number of questions generated.

        ## Conclusion
        The Image to Questions Generator is a practical application of machine learning technology, offering a convenient solution for generating questions from visual content. Whether used for educational purposes, content analysis, or creative exploration, the application demonstrates the potential of AI-driven tools to simplify complex tasks.
        """
    )

def image_to_questions():
    st.title("Image to Questions Generator")
    st.write("Upload an image and get questions generated based on it.")

    uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        img = PIL.Image.open(uploaded_image)
        generate_questions_from_image(img)

def main():
    page = st.sidebar.radio("Go to", ["About Project", "Image to Questions"])

    if page == "About Project":
        about_project()
    elif page == "Image to Questions":
        image_to_questions()

if __name__ == "__main__":
    main()
