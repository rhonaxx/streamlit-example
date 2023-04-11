import streamlit as st
import openai
import requests
import os
from PIL import Image
from io import BytesIO


#set OpenAI API key
openai.api_key = st.secrets["api_key"]

#define function to generate image from prompt
def generate_image(prompt):
    #generate image using DALL-E API
    response = openai.Image.create(
      prompt=prompt,
      n=1,
      size="512x512"
    )

    #get image URL from response
    image_url = response['data'][0]['url']

    #fetch image from URL and return as PIL Image object
    image_response = requests.get(image_url)
    image = Image.open(BytesIO(image_response.content))
    return image

st.title "Welcome to Image Visualizer."
         "Describe the image. Example: A flying car powered by solar energy."

#prompt user for new input
new_prompt = st.text_input("Enter a prompt:")

#generate image for new prompt and display
if new_prompt:
    st.title(new_prompt)
    image = generate_image(new_prompt)
    st.image(image, caption=new_prompt)
