# 🏃‍♂️직원 퇴사 예측 모델🏃‍♂️
> 프로젝트 기간 : 2024-11-13 ~ 2024-11-14 (총 2일)

![배사](https://github.com/user-attachments/assets/e2f83b79-320e-49c3-8551-511a56be997d)
## 팀명
SKN06-2nd-2Team : 퇴사자들

## 팀원 소개
| 성은진 | 노원재 | 전하연 | 조해원 | 
|--|--|--|--|
|  |![원재님](https://github.com/user-attachments/assets/76753c14-6447-489e-8b4a-049ceeb88af5)|![하연님](https://github.com/user-attachments/assets/f4757293-c9bb-4487-a5b0-60ba193f1537)|![해원님](https://github.com/user-attachments/assets/f24c3139-aebd-467b-bfc9-020e86b1ded5)


## 프로젝트 개요
> 직원들이 퇴사하는 이유에는 다양한 요인이 있을 것입니다. 그중 8가지 특징을 기반으로 직원의 퇴사 가능성을 예측하는 모델을 개발하여, 퇴사율을 줄이고 직원이 유지 및 만족도를 높일 수 있는 전략을 수립하고자 합니다.

## 전처리

### 결측치
| 변수명 | 처리 방법 |
| --- | --- |
| avg_monthly_hrs | 결측치 없음
| department | 열 삭제/(결측치가 많고 결과에 큰 영향을 미칠 것같지 않아 삭제함)
| filed_complaint | 결측값을 0으로 채우기
| last_evaluation | 결측치를 평균값으로 대체     
| n_projects | 결측치 없음             
| recently_promoted | 결측값을 0으로 채우기  
| salary | 결측치 없음                  
| satisfaction | 결측치를 평균값으로 대체        
| status | 결측치 없음                 
| tenure | 결측값을 1으로 채우기    

### 이상치
![이상치](https://github.com/user-attachments/assets/85cc0ab3-58a4-4e2c-a738-6f8b002293c5)

## 📊EDA

![분포](https://github.com/user-attachments/assets/824faec9-74b1-4c06-b10c-f13975d4a8c0)

### 상관관계
![히트맵](https://github.com/user-attachments/assets/9cba910a-90a4-46a0-8a5a-578e664718d0)

### 카테고리 변수 퇴사율 시각화
![카테고리별](https://github.com/user-attachments/assets/d22b67f7-84ec-49f1-a7b0-4a8c66e4bc46)

### 수치형 변수 퇴사율 시각화
![수치](https://github.com/user-attachments/assets/1f099914-fbae-4507-a837-cba2e271f684)


# ⚙️Machine Learning

### 사용된 ML모델
1. Decision Tree
2. Random Forest
3. XGBoost
4. KNN

### 모델 별 평가 지표
| 모델 | Accuracy | Precision | Recall | F1 Score | ROC AUC |
| --- | --- | --- | --- | --- | --- |
| **Decision Tree** | 0.9733 | 0.9563 | 0.9727 | 0.9416 | 0.96 |
| **Random Forest** | 0.9810 | 0.9809 | 0.9364 | 0.9582 | 0.99 |
| **XGBoost** | 0.9824 | 0.9795 | 0.9440 | 0.9614 | 0.99 |
| **KNN** | 0.9708 | 0.9152 | 0.9636 | 0.9388 | 0.99 |

- 모델 평가결과에 따라 Random Forest와 XGBoost가 가장 좋은 성능을 보이고 있음

### 모델 별 요약
1. Decision Tree  <br>
![트리](https://github.com/user-attachments/assets/96dc6fb4-c65d-4149-8a26-2103f6b5255a)

2. Random Forest <br>
![랜덤포레스트](https://github.com/user-attachments/assets/3b76dc9c-4d56-4bee-8e62-616c4920134e)

3. XGBoost  <br>
![부스트](https://github.com/user-attachments/assets/50454c73-9a2b-495a-ae6a-30f781844c89)

### 최종 모델 선정 : XGBoost
- 데이터셋에 클래스 불균형이 있는 경우, F1 점수나 ROC-AUC가 더 적합할 수 있음
- 특히 정확성이 가장 탁월하여 XGBoost (최적화)모델을 선택함

# 🧠Deep Learing 

## 과적합 여부
<table>
  <tr>
    <th style="text-align:center;">Decision Tree</th>
    <th style="text-align:center;">Random Forest</th>
  </tr>
  <tr>
    <td style="text-align:center;"><img src="https://github.com/user-attachments/assets/030dd222-5c16-4ff9-bd87-9e6ce107d59d" alt="과적합dt"></td>
    <td style="text-align:center;"><img src="https://github.com/user-attachments/assets/08cc050f-4d33-416e-8aeb-4a32371daad4" alt="과적합rf"></td>
  </tr>
  <tr>
    <th style="text-align:center;">XGBoost</th>
    <th style="text-align:center;">KNN</th>
  </tr>
  <tr>
    <td style="text-align:center;"><img src="https://github.com/user-attachments/assets/6c1e309c-9ad2-42cd-8132-27365750c1b2" alt="과적합xgb"></td>
    <td style="text-align:center;"><img src="https://github.com/user-attachments/assets/e5b9d34f-f501-42cb-b13e-9f56041f42e9" alt="과적합knn"></td>
  </tr>
</table>
- KNN에서 작은 K 값에서는 분산(variance)이 높고, 큰 K 값에서는 편향(bias)이 높아지는 경향이 있음
- 
- 


# Streamlit 구현
(사진)

## 프로젝트 회고
성은진 :
노원재 : 
전하연 :
조해원 : 
