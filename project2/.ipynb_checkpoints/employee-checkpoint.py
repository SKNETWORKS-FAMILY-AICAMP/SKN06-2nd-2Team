import streamlit as st
import pandas as pd
import joblib

# 모델 로드
model = joblib.load("employee_churn_model.pkl")

# Streamlit 앱 설정
st.title("Employee Churn Prediction App")
st.write("This application predicts the likelihood of an employee leaving the company based on various features.")

# 입력 필드 생성 (학습 데이터와 동일한 특성 이름 사용)
def get_user_input():
    satisfaction = st.slider('Satisfaction Level', 0.0, 1.0, 0.5)
    last_evaluation = st.slider('Last Evaluation', 0.0, 1.0, 0.5)
    n_projects = st.number_input('Number of Projects', min_value=1, max_value=10, value=3)
    avg_monthly_hrs = st.number_input('Average Monthly Hours', min_value=50, max_value=350, value=160)
    tenure = st.number_input('Years at Company (Tenure)', min_value=1, max_value=20, value=3)  # 'time_spent_company'를 'tenure'로 변경
    filed_complaint = st.selectbox('Filed Complaint', [0, 1])
    recently_promoted = st.selectbox('Recently Promoted', [0, 1])
    salary = st.selectbox('Salary Level', ['low', 'medium', 'high'])
    
    # salary를 숫자로 인코딩
    salary_encoding = {'low': 0, 'medium': 1, 'high': 2}
    
    # 사용자 입력을 데이터프레임으로 변환
    user_data = {
        'avg_monthly_hrs': avg_monthly_hrs,
        'filed_complaint': filed_complaint,
        'last_evaluation': last_evaluation,
        'n_projects': n_projects,
        'recently_promoted': recently_promoted,
        'salary': salary_encoding[salary],
        'satisfaction': satisfaction,
        'tenure': tenure,
    }
    return pd.DataFrame(user_data, index=[0])

# 사용자 입력 데이터
input_df = get_user_input()

# 예측 버튼
if st.button("Predict"):
    # 예측 수행
    prediction = model.predict(input_df)
    prediction_proba = model.predict_proba(input_df)
    
    # 결과 표시
    if prediction[0] == 1:
        st.error("Prediction: The employee is likely to leave.")
    else:
        st.success("Prediction: The employee is likely to stay.")
    
    st.write(f"Probability of Leaving: {prediction_proba[0][1]*100:.2f}%")
    st.write(f"Probability of Staying: {prediction_proba[0][0]*100:.2f}%")