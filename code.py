import streamlit as st 
import pandas as pd
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI
import matplotlib


matplotlib.use('TkAgg')

st.cache()

API_KEY = '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'
llm = OpenAI(api_token = API_KEY, engine = "gpt-3.5-turbo")
pandas_ai= PandasAI(llm, middlewares=[StreamlitMiddleware()], verbose=False)


st.title('CSV chatbot')
uploaded_file = st.file_uploader('Upload CSV file for analysis', type = ['csv'])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df.head())
    
    prompt = st.text_area('Enter your question here:')
    
    if st.button('Generate'):
        if prompt:
            with st.spinner('Generating an answer, please wait....'):
               st.write(pandas_ai.run(df, prompt=prompt))
        else:
            st.warning('Prompt cannot be empty. Please ask a question')
            
