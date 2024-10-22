import streamlit as st
import os
from PIL import Image
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

model = genai.GenerativeModel(model_name="gemini-1.5-pro")

st.set_page_config("Image Description")
st.title('Image Desciption using Gemini AI')
input = st.text_input("Input: ",key="input")

uploaded_image = st.file_uploader("Upload an image file", type=["png", "jpg", "jpeg","gif"])
image = ""
if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image", use_column_width=True)

def generate_gemini_response(input, image):
    if input != '':
        response = model.generate_content([image, input])
    else:
        response = model.generate_content(image)
    
    return response.text

submit = st.button("Get a Response")

if submit:
    if image is None or image=="":
        st.warning("Please upload an image.")
    else:
        response = generate_gemini_response(input, image)
        st.subheader("The Response is:")
        st.write(response)