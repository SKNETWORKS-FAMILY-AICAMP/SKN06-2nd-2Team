import streamlit as st
import pandas as pd
import joblib
import plotly.graph_objects as go

# 모델 로드
model = joblib.load("employee_churn_model.pkl")

# 세션 상태 설정: 'app_started'가 없으면 False로 초기화
if "app_started" not in st.session_state:
    st.session_state.app_started = False

# 대문 화면 (app_started가 False일 때만)
if not st.session_state.app_started:
    # 대문 이미지 표시
    st.image("C:\\Users\\Playdata\\Desktop\\project2\\image\\대문사진.jpg", use_column_width=True)
    st.title("직원 이탈 예측 어플리케이션")
    st.write("어플리케이션을 시작하려면 아래 버튼을 클릭하세요.")
    
    # 애플리케이션 시작 버튼 클릭 시 app_started를 True로 설정
    start_app = st.button("어플리케이션 시작")
    if start_app:
        st.session_state.app_started = True  # 세션 상태를 업데이트하여 대문 화면을 종료

# 직원 정보 입력 화면 (app_started가 True일 때만)
if st.session_state.app_started:
    st.title("직원 이탈 예측 어플리케이션")
    st.write("아래의 값을 조정하여 직원의 데이터를 입력하세요.")

    # 입력 필드 생성 함수
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

    # 사용자 입력 데이터 가져오기
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
        
        # 결과 해석 및 이미지 표시
        st.subheader("결과 해석")
        if prediction_proba[0][1] > 0.7:
            st.image(r"image\퇴사할거임.png", use_column_width=True)
            st.warning("이탈 가능성이 높습니다. 직원과의 면담이나 직무 만족도 향상 방안을 고려해보세요.")
        elif prediction_proba[0][1] > 0.5:
            st.image(r"image\퇴사고민중.png", use_column_width=True)
            st.info("이탈 가능성이 중간 수준입니다. 해당 직원의 직무 몰입도와 만족도를 주기적으로 확인하세요.")
        else:
            st.image(r"image\퇴사안함.png", use_column_width=True)
            st.success("이탈 가능성이 낮습니다. 이 직원은 현재 회사에 만족하고 있습니다.")