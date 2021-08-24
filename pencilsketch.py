import streamlit as st
import numpy as np
from PIL import Image
import cv2

def dodgeV2(x,y):
  return cv2.divide(x,255-y, scale=256)

# function to convert image to pencil sketch

def pencilsketch(input_image):

    # converting an image into gray scale image
    grayImage = cv2.cvtColor(input_image,cv2.COLOR_BGR2GRAY)

    # Inverting an image
    invertImage = cv2.bitwise_not(grayImage)

    # Smoothing the image
    image_smoothing = cv2.GaussianBlur(invertImage, (21,21),sigmaX=0, sigmaY=0)

    # final image
    final_image = dodgeV2(grayImage,image_smoothing)

    return final_image

st.title("PencilSketcher App")
description = '<p style=" color:Blue; font-size: 18px;">This web app will help to convert your photos to realistic Pencil Sketches. Try it now!</p>'
st.markdown(description, unsafe_allow_html=True)

file_image = st.sidebar.file_uploader("Choose your photo!", type=['jpg','png','jpeg'])

if file_image is None:
    st.write("No images uploaded! (Upload image from left side panel)")
else:
    inp_image = Image.open(file_image)
    final_sketch = pencilsketch(np.array(inp_image))
    st.write("Input Photo ----->")
    st.image(file_image, use_column_width=True, )
    st.write("Output Photo ----->")
    st.image(final_sketch , use_column_width=True)

footer = "<a href='https://github.com/khushi-purwar/Pencil-Sketcher-App-using-ML/blob/master/pencilsketch.py'>Click Here</a> to view the source code"
st.markdown(footer, unsafe_allow_html=True)