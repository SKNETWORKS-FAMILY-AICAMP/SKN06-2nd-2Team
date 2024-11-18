# 🏃‍♂️직원 퇴사 예측 모델🏃‍♂️
> 프로젝트 기간 : 2024-11-13 ~ 2024-11-14 (총 2일)

![배사](https://github.com/user-attachments/assets/e2f83b79-320e-49c3-8551-511a56be997d)
## 팀명
SKN06-2nd-2Team : 퇴사자들✨

## 팀원 소개
| 성은진 | 노원재 | 전하연 | 조해원 | 
|--|--|--|--|
| <img src="https://github.com/user-attachments/assets/f44655ee-a119-4a82-a43f-c23eabbb9c9f" width="220"/> | <img src="https://github.com/user-attachments/assets/76753c14-6447-489e-8b4a-049ceeb88af5" width="220"/> | <img src="https://github.com/user-attachments/assets/f4757293-c9bb-4487-a5b0-60ba193f1537" width="220"/> | <img src="https://github.com/user-attachments/assets/f24c3139-aebd-467b-bfc9-020e86b1ded5" width="220"/> |

## 프로젝트 개요
> 직원들이 퇴사하는 이유에는 다양한 요인이 있을 것입니다. 그중 8가지 특징을 기반으로 직원의 퇴사 가능성을 예측하는 모델을 개발하여, 퇴사율을 줄이고 직원이 유지 및 만족도를 높일 수 있는 전략을 수립하고자 합니다.

## 전처리

### 결측치
| 변수명 | 처리 방법 |
| --- | --- |
| avg_monthly_hrs(평균 월 근무 시간) | 결측치 없음
| department(부서) | 열 삭제
| filed_complaint(부서 만족) | 결측값을 0으로 채우기
| last_evaluation(최근 평가) | 결측치를 평균값으로 대체     
| n_projects(프로젝트 수) | 결측치 없음             
| recently_promoted(최근 승진 여부) | 결측값을 0으로 채우기  
| salary(급여) | 결측치 없음                  
| satisfaction(만족도) | 결측치를 평균값으로 대체        
| status(퇴사 여부) | 결측치 없음                 
| tenure(근속 기간) | 결측값을 1으로 채우기    

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

### 모델 별 요약
1. Decision Tree  <br>
![트리](https://github.com/user-attachments/assets/96dc6fb4-c65d-4149-8a26-2103f6b5255a)

2. Random Forest <br>
![랜덤포레스트](https://github.com/user-attachments/assets/3b76dc9c-4d56-4bee-8e62-616c4920134e)

3. XGBoost  <br>
![부스트](https://github.com/user-attachments/assets/50454c73-9a2b-495a-ae6a-30f781844c89)

### 모델 별 평가 지표
| 모델 | Accuracy | Precision | Recall | F1 Score | ROC AUC |
| --- | --- | --- | --- | --- | --- |
| **Decision Tree** | 0.9733 | 0.9563 | 0.9727 | 0.9416 | 0.96 |
| **Random Forest** | 0.9810 | 0.9809 | 0.9364 | 0.9582 | 0.99 |
| **XGBoost** | 0.9824 | 0.9795 | 0.9440 | 0.9614 | 0.99 |
| **KNN** | 0.9708 | 0.9152 | 0.9636 | 0.9388 | 0.99 |

- 모델 평가결과에 따라 Random Forest와 XGBoost가 가장 좋은 성능을 보이고 있음

![Before](https://github.com/user-attachments/assets/37707bbb-0410-4192-9525-b779ba037297) ![After](https://github.com/user-attachments/assets/af2c3cec-3153-4df0-b23a-b8b9b22e90f0)

### -> 최종 모델 선정 : XGBoost
- 데이터셋에 클래스 불균형이 있는 경우, F1 점수나 ROC-AUC가 더 적합할 수 있음, 특히 정확성이 가장 탁월하여 XGBoost (최적화)모델을 선택함
- 하이퍼파라미터 선정
  1. 초기 모델 학습 및 평가
  기본 XGBoost 모델로 데이터를 학습하고 테스트 데이터를 통해 성능을 평가함. 초기 모델의 성능을 바탕으로 하이퍼파라미터 최적화를 진행할 필요성을 확인함

  2. 하이퍼파라미터 튜닝
  탐색 대상 하이퍼파라미터: learning_rate, max_depth, min_child_weight, gamma, colsample_bytree의 다양한 조합을 무작위로 탐색하여 최적의 값을 찾음
  탐색 과정: RandomizedSearchCV로 50개의 하이퍼파라미터 조합을 3-폴드 교차 검증을 통해 평가함.
  최적의 하이퍼파라미터: 각 매개변수를 조정하여 최적의 학습 속도, 트리 깊이, 분할 조건을 선정함.

  3. 최적화된 모델 평가
  최적화된 XGBoost 모델로 최종 평가를 진행한 결과, 예측 정확도가 향상되었으며, 과적합을 방지하면서도 일반화 성능이 개선되었습니다.

  4. 결론
  하이퍼파라미터 최적화를 통해 XGBoost 모델의 예측 성능을 개선하고 이탈 예측의 정확성을 높였습니다.


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
1. 훈련 정확도와 검증 정확도의 유사성 : 훈련 정확도와 검증 정확도 사이의 차이가 크게 벌어지지 않고 유사한 수준에서 유지됨을 볼 수 있음. <br>
2. 트리 개수 증가에 따른 안정적인 성능: 트리 개수를 늘려도 훈련 정확도와 검증 정확도 모두 큰 변화 없이 안정적인 수치를 유지하고 있음. <br>
3. 검증 정확도의 안정적 수렴: 검증 정확도가 특정 값(약 0.982) 근처에서 안정화되었으며, 훈련 정확도 역시 0.985 부근에서 일정하게 유지되고 있습니다. 위 이유들로 판단했을 때 이 모델은 과적합되지 않았으며, 데이터에 대해 적절한 일반화 성능을 갖추고 있다고 할 수 있음.

# 🧠Deep Learning

## 검증
![딥러닝](https://github.com/user-attachments/assets/5d8c15ce-6ddd-4baf-82d4-577450bcc12f)

# 💡Streamlit 구현
<table style="width: 100%; text-align: center;">
  <tr>
    <td><img src="https://github.com/user-attachments/assets/559a72b0-1ae9-4508-9e39-ed31f81d4478" width="500"/></td>
    <td><img src="https://github.com/user-attachments/assets/9f6b49c8-7c8a-43c1-8faa-0b36474b609b" width="500"/></td>
  </tr>
</table>


## 프로젝트 회고
성은진 : 
노원재 : 깨달음을 얻었다...
전하연 : 
조해원 : 
