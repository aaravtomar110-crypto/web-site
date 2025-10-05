import streamlit as st

st.title ("Welcome to Mypython Gyan")
st.header ("Complete couses")
st.subheader ("Basic condept")
st.subheader ("all string")
st.markdown ("I love python")
st.code ("""for i in  range (1,6,9):
                print ("Hi satyam this side and i will provided the complite python knowlegde")
                
            """)

Name = st.text_input("Enter your Name")
fname = st.text_input("Enter your Father name")
adr = st.text_area(" Enter your Text")
classdata = st.selectbox("Enter your class :", (1,2,3,4,5,6))

button = st.button ("Apply")
if button :
            st.markdown(f"""
                           Name : {Name}
                                Father Name : {fname}
                                    Address : {adr}
                                       class : {classdata}""")