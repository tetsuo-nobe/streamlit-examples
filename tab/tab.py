import streamlit as st

@st.cache_data
def say_helo(name):
    print(f'input_text1: {name}')
    msg = 'Hello!' + name
    return msg

@st.cache_data
def is_even(num):
    msg = ""
    print(f'input_text2: {num}')
    if num.isdigit():
        if int(num) % 2 == 0:
            msg = "入力された値は偶数です。"
        else:
            msg = "入力された値は奇数です。"
    else:
        msg = "入力された値は数値ではありません。"
    return msg

# st.tabs ではタブは 2 つ以上必要
tab1, tab2= st.tabs(['タブ1', 'タブ2'])

with tab1:
    input_text1 = st.text_input('**名前を入力してください。**', key="tab1", value=None)

with tab2:
    input_text2 = st.text_input('**何か数字を入力してください。**', key="tab2",value=None)


if input_text1 is not None:
    try:
        text = say_helo(input_text1)
    except Exception as e:
        st.error(
            f'`{input_text1}`の入力後にエラーが発生しました。',
            icon=':material/network_locked:')
        st.exception(e)
        st.stop()

    with tab1:
        st.markdown(text)

    with tab2:
        st.markdown(f'タブ1 で入力された値は `{input_text1}` です。')

if input_text2 is not None:
    try:
        text = is_even(input_text2)
    except Exception as e:
        st.error(
            f'`{input_text2}`の入力後にエラーが発生しました。',
            icon=':material/network_locked:')
        st.exception(e)
        st.stop()

    with tab1:
        st.markdown(f'タブ2 で入力された値は `{input_text2}` です。')
    with tab2:
        st.markdown(text)
        


