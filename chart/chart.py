import streamlit as st
import pandas as pd
import numpy as np
from vega_datasets import data

tab1,tab2,tab3,tab4 = st.tabs(['stack vertical','stack horizontal','stack=False','Custom DataFrame'])

with tab1:
    if st.button("チャートを表示"):

        with tab1:
            # Example: stack vertical
            st.markdown('stack vertical')
            chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a","b","c"])
            print(chart_data)
            st.bar_chart(chart_data)

        with tab2:
            # Example: stack horizontal
            st.markdown('stack horizontal')
            source = data.barley()
            st.bar_chart(source, x="variety", y="yield", color="site", horizontal=True)

        with tab3:
            # Example: stack=False
            st.markdown('stack=False')
            st.bar_chart(source, x="year", y="yield", color="site", stack=False)

        with tab4:
            # Example: Custom DataFrame
            st.markdown('Custom DataFrame')
            list1=[[1,2,3], [21,22,23], [31,32,33]]
            index1 = ["Row1", "Row2", "Row3"]
            columns1 =["Col1", "Col2", "Col3"]
            chart_data = pd.DataFrame(data=list1, index=index1, columns=columns1)
            st.bar_chart(chart_data, stack=False)
