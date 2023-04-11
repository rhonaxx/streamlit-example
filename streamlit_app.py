import streamlit as st
import openai
import requests
import os
from PIL import Image
from io import BytesIO

OPENAI_API_KEY=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

#set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

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

#define list of interesting prompts
prompts = [
    "A flying car powered by solar energy",
    "A tree made of candy",
    "A city on the moon",
    "A robot serving coffee to people in a park",
    "A giant sea monster attacking a ship"
]

#display list of prompts to user
st.sidebar.title("Select a prompt")
selected_prompt = st.sidebar.selectbox("", prompts)

#generate image for selected prompt and display
st.title(selected_prompt)
image = generate_image(selected_prompt)
st.image(image, caption=selected_prompt)

#prompt user for new input
new_prompt = st.text_input("Enter a prompt:")

#generate image for new prompt and display
if new_prompt:
    st.title(new_prompt)
    image = generate_image(new_prompt)
    st.image(image, caption=new_prompt)
