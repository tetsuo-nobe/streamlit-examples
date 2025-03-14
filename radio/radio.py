import streamlit as st

OPTIONS = {
    '個人': {
        'first': '個人の情報',
        'second': '世帯情報',
        'text': '姓名を入力してください。',
        'icon': ':material/person:',
        'image': False,
        'input': lambda: st.text_input('ダミー', label_visibility='hidden',
                    value=None, placeholder='姓名を入力してください。'),
    },
    '法人': {
        'first': '法人の情報',
        'second': '関連企業情報',
        'text': '法人名を入力してください。',
        'icon': ':material/corporate_fare:',
        'image': True,
        'input': lambda: st.text_input('ダミー', label_visibility='hidden',
                    value=None, placeholder='法人名を入力してください。'),
    }
}

# ページタイトル
st.header('顧客情報の検索')

# ラジオボタンの表示
im = st.radio(label='ダミー', label_visibility='hidden',
        options=OPTIONS.keys(), horizontal=True)

# ラジオボタンで選択されたキーの情報を辞書を取得
options = OPTIONS[im]

# タブの表示
tab1, tab2 = st.tabs([options['first'], options['second']])

with tab1:
     if im == '個人':
       input_text1 = st.text_input('**名前を入力して Enter を押してください。**', key="tab1", value=None)
     elif im == '法人':
       input_text1 = st.text_input('**名称を入力して Enter を押してください。**', key="tab1", value=None)
