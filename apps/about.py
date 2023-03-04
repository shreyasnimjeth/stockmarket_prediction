import streamlit as st
from PIL import Image
def app():
    st.title("ABOUT")
    col1, col2 = st.columns(2)
    with col1:
  
            st.header("`# About`")
            st.header("HELLO !! ")
            st.header("`THIS IS WEB APP FOR STOCK MARKET PREDICTION`")
            st.write("<h1 style='font-size:20px;'>Stock Market Prediction App is an part of Major Project of college (ST. VENCENT PALLOTTI COLLEGE OF ENGINEERING AND TECHNOLOGY NAGPUR), Which is allifated to RTMNU (NAGPUR UNIVERSITY)</h1>", unsafe_allow_html=True)
           
            st.header("`OUR TEAM MEMBERS`")
            st.write(" ")
            st.write("<h1 style='font-size:20px;'>1.SHREYAS NIMJE</h1>", unsafe_allow_html=True)
            st.write("<h1 style='font-size:20px;'>2.WARAD DALAL</h1>", unsafe_allow_html=True)
            st.write("<h1 style='font-size:20px;'>3.Vedant Bopanawar</h1>", unsafe_allow_html=True)
            
            st.write("  ")
            st.header("`OUR PROJECT GUIDE`")
            st.write("<h1 style='font-size:20px;'>Dr. SAMIR AJANI</h1>", unsafe_allow_html=True)
            
       
    with col2:
        image = Image.open("image.jpg")
        st.image(image, caption="My Image", use_column_width=True, clamp=False)
