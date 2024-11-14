import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go

# 모델 로드
model = joblib.load("employee_churn_model.pkl")

# Streamlit 앱 설정
st.title("직원 이탈 예측 애플리케이션")
st.write("""
이 애플리케이션은 다양한 특징을 기반으로 직원의 이탈 가능성을 예측합니다.\n
아래의 값을 조정하여 직원의 데이터를 입력하세요.
""")

# 입력 필드 생성 (학습 데이터와 동일한 특성 이름 사용)
def get_user_input():
    st.subheader("직원 정보 입력")
    
    satisfaction = st.slider('만족도', 0.0, 1.0, 0.5, help="직원의 만족도를 입력하세요 (0: 낮음, 1: 높음)")
    last_evaluation = st.slider('업무 평가 점수', 0.0, 1.0, 0.5, help="직원의 최근 업무 평가 점수를 입력하세요 (0: 낮음, 1: 높음)")
    n_projects = st.number_input('진행 프로젝트 수', min_value=1, max_value=10, value=3, help="직원이 참여하고 있는 프로젝트 수를 입력하세요")
    avg_monthly_hrs = st.number_input('월 평균 근무 시간', min_value=50, max_value=350, value=160, help="직원의 월 평균 근무 시간을 입력하세요")
    tenure = st.number_input('근속 연수', min_value=1, max_value=20, value=3, help="직원의 근속 연수를 입력하세요")
    filed_complaint = st.selectbox('불만 제기 여부', [0, 1], format_func=lambda x: "예" if x == 1 else "아니오", help="직원이 불만을 제기했는지 여부를 선택하세요")
    recently_promoted = st.selectbox('최근 승진 여부', [0, 1], format_func=lambda x: "예" if x == 1 else "아니오", help="직원이 최근에 승진했는지 여부를 선택하세요")
    salary = st.selectbox('급여 수준', ['낮음', '중간', '높음'], help="직원의 급여 수준을 선택하세요")
    
    # salary를 숫자로 인코딩
    salary_encoding = {'낮음': 0, '중간': 1, '높음': 2}
    
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
if st.button("예측하기"):
    # 예측 수행
    prediction = model.predict(input_df)
    prediction_proba = model.predict_proba(input_df)
    
    # 결과 표시
    st.subheader("예측 결과")
    
    if prediction[0] == 1:
        st.error("예측 결과: 이 직원은 이탈할 가능성이 높습니다.")
    else:
        st.success("예측 결과: 이 직원은 이탈할 가능성이 낮습니다.")
    
    # 결과 확률 표시
    st.write(f"**이탈할 확률:** {prediction_proba[0][1]*100:.2f}%")
    st.write(f"**잔류할 확률:** {prediction_proba[0][0]*100:.2f}%")
    
    # 게이지 그래프 시각화 (이탈 확률)
    st.subheader("이탈 확률 게이지")
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=prediction_proba[0][1] * 100,
        title={'text': "이탈 확률 (%)"},
        gauge={'axis': {'range': [0, 100]},
               'bar': {'color': "red"},
               'steps': [
                   {'range': [0, 50], 'color': "lightgreen"},
                   {'range': [50, 75], 'color': "yellow"},
                   {'range': [75, 100], 'color': "red"}],
               'threshold': {'line': {'color': "black", 'width': 4}, 'thickness': 0.75, 'value': prediction_proba[0][1] * 100}}))
    st.plotly_chart(fig)
    
    # 결과 해석
    st.subheader("결과 해석")
    if prediction_proba[0][1] > 0.7:
        st.warning("이탈 가능성이 높습니다. 직원과의 면담이나 직무 만족도 향상 방안을 고려해보세요.")
    elif prediction_proba[0][1] > 0.5:
        st.info("이탈 가능성이 중간 수준입니다. 해당 직원의 직무 몰입도와 만족도를 주기적으로 확인하세요.")
    else:
        st.success("이탈 가능성이 낮습니다. 이 직원은 현재 회사에 만족하고 있습니다.")

# import streamlit as st
# import pandas as pd
# import joblib

# # 모델 로드
# model = joblib.load("employee_churn_model.pkl")

# # Streamlit 앱 설정
# st.title("Employee Churn Prediction App")
# st.write("""
# This application predicts the likelihood of an employee leaving the company based on various features.
# Please adjust the values below to match the employee's data.
# """)

# # 입력 필드 생성 (학습 데이터와 동일한 특성 이름 사용)
# def get_user_input():
#     st.subheader("Employee Information")
    
#     satisfaction = st.slider('Satisfaction Level', 0.0, 1.0, 0.5, help="Employee's satisfaction level (0: low, 1: high)")
#     last_evaluation = st.slider('Last Evaluation', 0.0, 1.0, 0.5, help="Score from the employee's most recent evaluation (0: low, 1: high)")
#     n_projects = st.number_input('Number of Projects', min_value=1, max_value=10, value=3, help="Number of projects the employee is involved in")
#     avg_monthly_hrs = st.number_input('Average Monthly Hours', min_value=50, max_value=350, value=160, help="Average number of hours worked per month")
#     tenure = st.number_input('Years at Company (Tenure)', min_value=1, max_value=20, value=3, help="Number of years the employee has been with the company")
#     filed_complaint = st.selectbox('Filed Complaint', [0, 1], help="1 if the employee has filed a complaint, 0 otherwise")
#     recently_promoted = st.selectbox('Recently Promoted', [0, 1], help="1 if the employee was promoted recently, 0 otherwise")
#     salary = st.selectbox('Salary Level', ['low', 'medium', 'high'], help="Employee's salary level")
    
#     # salary를 숫자로 인코딩
#     salary_encoding = {'low': 0, 'medium': 1, 'high': 2}
    
#     # 사용자 입력을 데이터프레임으로 변환
#     user_data = {
#         'avg_monthly_hrs': avg_monthly_hrs,
#         'filed_complaint': filed_complaint,
#         'last_evaluation': last_evaluation,
#         'n_projects': n_projects,
#         'recently_promoted': recently_promoted,
#         'salary': salary_encoding[salary],
#         'satisfaction': satisfaction,
#         'tenure': tenure,
#     }
#     return pd.DataFrame(user_data, index=[0])

# # 사용자 입력 데이터
# input_df = get_user_input()

# # 예측 버튼
# if st.button("Predict"):
#     # 예측 수행
#     prediction = model.predict(input_df)
#     prediction_proba = model.predict_proba(input_df)
    
#     # 결과 표시
#     st.subheader("Prediction Results")
    
#     if prediction[0] == 1:
#         st.error("Prediction: The employee is likely to leave.")
#     else:
#         st.success("Prediction: The employee is likely to stay.")
    
#     # 결과 확률 표시
#     st.write(f"**Probability of Leaving:** {prediction_proba[0][1]*100:.2f}%")
#     st.write(f"**Probability of Staying:** {prediction_proba[0][0]*100:.2f}%")
    
#     # 결과 해석
#     st.subheader("Interpretation")
#     if prediction_proba[0][1] > 0.7:
#         st.warning("High likelihood of leaving. Consider discussing concerns with the employee or reviewing their recent workload and satisfaction levels.")
#     elif prediction_proba[0][1] > 0.5:
#         st.info("Moderate likelihood of leaving. Keep an eye on this employee's engagement and satisfaction.")
#     else:
#         st.success("Low likelihood of leaving. The employee seems to be well-adjusted to the company environment.")