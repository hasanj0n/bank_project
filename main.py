import streamlit as st
from page1 import loan_prediction
from page2 import chatBot

def main():
    st.sidebar.title("Navigation")
    pages = ["Bank Loan Prediction","Chatbot"]
    selection = st.sidebar.radio("Go to", pages)
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

    if selection == "Bank Loan Prediction":
        loan_prediction()
    else: 
        chatBot()

if __name__ == "__main__":
    main()