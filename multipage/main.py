# mulltipage で session state を共有する

import streamlit as st

if 'image_upload' in st.session_state:
    st.sidebar.markdown(f'ファイル: {st.session_state.image_upload.filename}')

pg = st.navigation({
    'マイサービス': [
        st.Page('page1.py', title='メニュー 1', icon='1️⃣'),
        st.Page('page2.py', title='メニュー 2', icon='2️⃣')
    ]})
pg.run()
