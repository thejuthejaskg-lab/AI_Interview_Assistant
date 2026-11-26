import streamlit as st
from groq import Groq

st.set_page_config(page_title='AI Interview Assistantr',layout='centered')
st.title('AI Interview Assistant')
st.caption('practice interviews with AI - generated questions and constructive feedback.')
st.caption('created by THEJAS KG ')
st.write('Department of AI&DS')
try:
    client = Groq(api_key=st.secrets['GROQ_API_KEY'])
    st.write('API connection successful')     
except(KeyError, FileNotFoundError):
    st.error('GROQ_API_KEY is missing .add it to streamlit cloud -> app setting')
    st.stop()
role = st.selectbox("Select job role",[
    "python Developer",
    "Java Developer",
    "Data Analyst",
    "Machine Learning Engineer",
    "Software Engineer",
    "HR Executive"
])
if st.button('Generate Interview question'):

    prompt = "Generate Interview question for the role of" + role

    response = clientr.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {"role":"system","content": "you are an experienced technical interview."},
        { "role" : "user","content" :"prompt"}
    ]
)

output = response.choices[0].message.content
st.write(output)
            
    

  
                    
