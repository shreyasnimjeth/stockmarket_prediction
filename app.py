import streamlit as st
from multiapp import MultiApp
from apps import prediction,new, about# import your app modules here

app = MultiApp()

st.markdown("""
# prediction-Page App
""")


# Add all your application here

app.add_app("HOME", new.app)
app.add_app("PREDITION", prediction.app)

app.add_app("ABOUT", about.app)



# The main app
app.run()