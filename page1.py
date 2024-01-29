import streamlit as st
from PIL import Image
import joblib
import pandas as pd

model = joblib.load("model.jbl")

def loan_prediction():
    img1 = Image.open('approved.png')
    img1 = img1.resize((700, 400))
    st.image(img1, use_column_width=False)
    st.title("Bank Loan Prediction using Machine Learning")

    # full name
    fn = st.text_input('Full Name')

    # Number of dependents
    no_of_dependents = st.number_input("Applicant's number of dependents", value=0)

    # education feature
    edu_display = ('Not Graduate', 'Graduate')
    edu_options = list(range(len(edu_display)))
    education = st.radio('Education Status', edu_options, format_func=lambda x: edu_display[x])

    # employment feature
    emp_display = ('No', 'Yes')
    emp_options = list(range(len(emp_display)))
    self_employed = st.radio('Employment Status', emp_options, format_func=lambda x: emp_display[x])

    # applicant income
    income_annum = st.number_input("Applicant's Annual Income(₹)", value=0)

    # Amount of loan
    loan_amount = st.number_input("Loan Amount(₹)", value=0)

    # Term of loan
    loan_term = st.number_input("Loan Term(months)", value=0)

    # Cibil score
    cibil_score = st.number_input('Cibil score', value=0)

    # Residential assets value
    residential_assets_value = st.number_input('Residential assets value(₹)', value=0)

    # Commercial assets value
    commercial_assets_value = st.number_input('Commercial assets value(₹)', value=0)

    # Luxury assets value
    luxury_assets_value = st.number_input('Luxury assets value(₹)', value=0)

    # Bank assets value
    bank_asset_value = st.number_input('Bank assets value(₹)', value=0)

    if st.button("Submit"):
        # features
        data = {
            'no_of_dependents': no_of_dependents,
            'education': education,
            'self_employed': self_employed,
            'income_annum': income_annum,
            'loan_amount': loan_amount,
            'loan_term': loan_term,
            'cibil_score': cibil_score,
            'residential_assets_value': residential_assets_value,
            'commercial_assets_value': commercial_assets_value,
            'luxury_assets_value': luxury_assets_value,
            'bank_asset_value': bank_asset_value
        }

        index = [1]
        features = pd.DataFrame(data, index=index)
        ans = model.predict(features)[0]

        if ans == 0:
            st.error(f"Sorry {fn}, your request is rejected!")
        else:
            st.success(f"Congratulations {fn}, your request is approved!")




