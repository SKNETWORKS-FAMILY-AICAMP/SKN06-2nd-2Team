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
| 변수명 | 처리 방법 | 근거
| --- | --- | ---
| avg_monthly_hrs(평균 월 근무 시간) | 없음
| department(부서) | 열 삭제| 결측치가 많고, 이를 채울 수 있는 적절한 방법이 없음
| filed_complaint(불만 접수 여부) | 0으로 채우기|None과 1로 구성된 이진변수로  None값을 0으로 대체
| last_evaluation(최근 평가) | 평균값으로 대체|수치형 데이터로 데이터의 전반적인 경향 유지 및 분석 안정성 확보    
| n_projects(프로젝트 수) | 없음             
| recently_promoted(최근 승진 여부) | 0으로 채우기|None과 1로 구성된 이진변수로  None값을 0으로 대체  
| salary(급여) | 없음                  
| satisfaction(만족도) | 평균값으로 대체|수치형 데이터로 데이터의 전반적인 경향 유지 및 분석 안정성 확보        
| status(퇴사 여부) | 없음                 
| tenure(근속 기간) | 1로 채우기|2~10 범위의 수치로 1년 미만 근속자를 결측치로 처리한 것으로 추정   

### 이상치
![이상치](https://github.com/user-attachments/assets/85cc0ab3-58a4-4e2c-a738-6f8b002293c5)
>IQR 기준으로 이상치 확인시 이상치 없음
## 📊EDA

### 상관관계
![히트맵](https://github.com/user-attachments/assets/9cba910a-90a4-46a0-8a5a-578e664718d0)
> 모든 변수 쌍의 상관계수가 0.5 미만으로 나타남
> 각 변수가 모델에 고유한 정보를 제공할 수 있으므로, 현재의 모든 변수를 유지하는 것이 분석에 도움

![분포](https://github.com/user-attachments/assets/824faec9-74b1-4c06-b10c-f13975d4a8c0)
> 근무 중: 약 70%   퇴사: 약 30%
- 클래스 불균형을 보임
- 주요 평가 지표
  - ROC-AUC: 클래스 불균형에 영향을 적게 받으며, 모델의 전반적인 성능을 평가
  - Precision-Recall 곡선과 PR-AUC: 소수 클래스(퇴사)의 예측 성능을 중점적으로 평가
  - F1-score: 정밀도와 재현율의 조화평균으로, 불균형 데이터에서 모델 성능을 균형있게 평가

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


### 최종 모델 선정 : XGBoost
- 데이터셋에 클래스 불균형이 있는 경우, F1 점수나 ROC-AUC가 더 적합함. 특히 종합적으로 XGBoost가 가장 탁월하여 최적화 모델로 선택함


- 하이퍼파라미터 선정
  ```python
  # RandomizedSearchCV 활용
  randomsearch = RandomizedSearchCV(estimator=xgb_model, param_distributions=params, n_iter=50, cv=3, n_jobs=-1, scoring='accuracy', random_state=0)
  randomsearch.fit(X_train, y_train)

  # 최적의 하이퍼파라미터와 성능 출력
  print("\n최적의 하이퍼파라미터 : ", randomsearch.best_params_,'\n')
  bestrf = randomsearch.best_estimator_
  best_params = randomsearch.best_params_
  evaluate_model(bestrf, X_test, y_test, 'XGBOOST 최적 하이퍼파라미터')
  
![Before](https://github.com/user-attachments/assets/37707bbb-0410-4192-9525-b779ba037297) 

- 최적의 하이퍼파라미터 :  {'min_child_weight': 1, 'max_depth': 15, 'learning_rate': 0.15, 'gamma': 0.2, 'colsample_bytree': 0.5}

![After](https://github.com/user-attachments/assets/af2c3cec-3153-4df0-b23a-b8b9b22e90f0)
1. 초기 모델 학습 및 평가<br>
  기본 XGBoost 모델로 데이터를 학습하고 테스트 데이터를 통해 성능을 평가함. 초기 모델의 성능을 바탕으로 하이퍼파라미터 최적화를 진행할 필요성을 확인함

2. 하이퍼파라미터 튜닝<br>
  탐색 대상 하이퍼파라미터: learning_rate, max_depth, min_child_weight, gamma, colsample_bytree의 다양한 조합을 무작위로 탐색하여 최적의 값을 찾음<br>
  탐색 과정: RandomizedSearchCV로 50개의 하이퍼파라미터 조합을 3-폴드 교차 검증을 통해 평가함.<br>
  최적의 하이퍼파라미터: 각 매개변수를 조정하여 최적의 학습 속도, 트리 깊이, 분할 조건을 선정함.

3. 최적화된 모델 평가<br>
  최적화된 XGBoost 모델로 최종 평가를 진행한 결과, 예측 정확도가 향상하며 과적합을 방지하면서도 일반화 성능이 개선.

4. 결론<br>
  하이퍼파라미터 최적화를 통해 XGBoost 모델의 예측 성능을 개선, 이탈 예측의 정확성을 높임.


## 과적합 여부
<table>
  </tr>
    <th style="text-align:center;">Decision Tree</th>
    <th style="text-align:center;">Random Forest</th>
  <tr>
    <td style="text-align:center;"><img src="https://github.com/user-attachments/assets/030dd222-5c16-4ff9-bd87-9e6ce107d59d" alt="과적합dt"></td>
    <td style="text-align:center;"><img src="https://github.com/user-attachments/assets/08cc050f-4d33-416e-8aeb-4a32371daad4" alt="과적합rf"></td>
  <tr>
  <tr>
    <td style="text-align:center;">
      1. 훈련 정확도와 검증 정확도의 유사성 <br>
      2. 트리 개수 증가에 따른 안정적인 성능 <br>
      3. 검증 정확도의 안정적 수렴</td>
    <td style="text-align:center;">
      1. 테스트 정확도가 훈련 정확도보다 높거나 비슷. <br>
      2. 두 정확도가 함께 증가하고 수렴.</td>
  </tr>
  <tr>
    <th style="text-align:center;">XGBoost</th>
    <th style="text-align:center;">KNN</th>
  <tr>
    <td style="text-align:center;"><img src="https://github.com/user-attachments/assets/6c1e309c-9ad2-42cd-8132-27365750c1b2" alt="과적합xgb"></td>
    <td style="text-align:center;"><img src="https://github.com/user-attachments/assets/e5b9d34f-f501-42cb-b13e-9f56041f42e9" alt="과적합knn"></td>
  <tr>
  <tr>
    <td style="text-align:center;">
      1. 훈련 정확도와 검증 정확도 간 차이가 크지 않음. <br>
      2. 검증 정확도의 안정성</td>
    <td style="text-align:center;">
      1.과적합으로 보이는 부분이 있고 애매함. <br>
      2. KNN은 보통 최종 선정 모델로 사용하지 않음</td>
  <tr>
 
</table>

</table>


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
성은진 : 배웠던걸 실제로 써먹을 수 있어서 재밌었다. <br>
노원재 : 깨달음을 얻었다... <br>
전하연 : 다양한 러닝머신 모델들을 활용하여 어떤 모델이 더 좋은지 평가, 비교해가면서 공부할 수 있었다.<br>
조해원 : 여러 모델을 적용해봄으로써 성능을 비교해볼 수 있는 시간이었다. <br>
