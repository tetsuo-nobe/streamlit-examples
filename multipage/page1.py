from PIL import Image
import streamlit as st


st.header(':rainbow[ページ 1]')

# アップロードされた後に Image オブジェクトを作成しファイル名もセットして st.session_state に格納
def onchange():
    img = Image.open(st.session_state._image_upload)
    img.filename = st.session_state._image_upload.name
    st.session_state.image_upload = img

# アップロードされた画像は io.ByteIO の子オブジェクトとして key で指定されたキーで st.session_state に格納される
st.file_uploader('画像ファイルをアップロードしてください',
                 key='_image_upload', on_change=onchange)

# st.session_state に Image オブジェクトがあれば表示する
if 'image_upload' in st.session_state:
    img = st.session_state.image_upload
    st.image(img)

