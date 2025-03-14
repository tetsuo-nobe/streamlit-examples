import streamlit as st    

# st.columns([3,1])は、2列で3:1の比率という意味
left, right = st.columns([3,1])
left.header('左側のヘッダー:3')
right.header('左側のヘッダー:1')

button_disabled = True

name = left.text_input('名前', key="name")

start = left.button('開始')

if start is True:
    right.markdown(name)
    right.markdown(len(str(name)))
