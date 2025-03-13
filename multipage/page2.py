from PIL import Image, ImageOps
import streamlit as st


st.header(':rainbow[ページ 2]')

if 'image_upload' in st.session_state:
    img = st.session_state.image_upload
    st.markdown(f'ファイル: {img.filename}')
    
