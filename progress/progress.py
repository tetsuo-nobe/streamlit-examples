#!/usr/bin/env -S python -m streamlit run

import streamlit as st
import pandas as pd
import numpy as np
from vega_datasets import data
import time

@st.cache_data
def say_helo(name):
    print(f'input_text1: `{name}.`')
    msg = 'Hello!' + name
    return msg


#tab1, tab2= st.tabs(['タブ1', 'タブ2'])

#with tab1:
input_text1 = st.text_input('**名前を入力して Enter を押してください。**', key="tab1", value=None)
st.markdown('10 秒後にメッセージを表示します。')
graph = st.empty()
with graph:
        bar = st.progress(value=0.0, text='計算中')

if input_text1 is not None:
  msg = say_helo(input_text1)
  for i in range(1,11):
    time.sleep(1)
    bar.progress(value=i/10, text='計算中')
  st.markdown(msg)

  
