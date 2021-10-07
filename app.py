import streamlit as st
from multiapp import MultiApp
from apps import Preparation,Selection,Upload,Visualisation, Description # import your app modules here
import helper as h
app = MultiApp()

#Sogeti logo
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Sogeti-logo-2018.svg/1280px-Sogeti-logo-2018.svg.png", 
                         use_column_width=True)

#background
h.set_bg()

#sidebar header
h.header("Image Quality Wrapper",is_sidebar=True)

app.add_app("Upload", Upload.app)
app.add_app("Preparation", Preparation.app)
app.add_app("Description", Description.app)
app.add_app("Visualisation", Visualisation.app)
app.add_app("Selection", Selection.app)
# The main app
app.run()