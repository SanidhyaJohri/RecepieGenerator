import streamlit as st
import Intro
import diffusionModel

PAGES={
    "Introduction": Intro,
    "Generator": diffusionModel
    
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()