# 학습용 데이터
from sklearn import datasets
# 데이터를 학습용과 테스트용으로 나누는 함수
from sklearn.model_selection import train_test_split
# 데이터 표준화
from sklearn.preprocessing import StandardScaler
# Perceptron 머신러닝 클래스
from sklearn.linear_model import Perceptron
from sklearn.linear_model import LogisticRegression
# 'from sklearn.naive_bayes import  어쩌구'도 사용 할 수 있음
# 정확도 계산을 위한 함수
from sklearn.metrics import accuracy_score
# 파일저장
import pickle
import numpy as np
from Perceptron_def import Perceptron_my

namse = None


def step1_get_data():
    # 아이리스 데이터 가져오기
    iris = datasets.load_iris()
    # print(iris)
    # 꽃잋정보(독립변수)
    X = iris.data[:150, [2, 3]]
    # 꽃 종류(종속변수)
    y = iris.target[:150]
    # 꽃 이름
    names = iris.target_names[:3]
    print(y)
    print(names)
    return X, y


def step2_learning():
    X, y = step1_get_data()
    # 학습데이터와 테스트 데이터 분리
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=0)
    # random_state : 데이터셋의 순서를 고정시키는 시드
    # 표준화 작업 : 데이터들을 표준 정규분포로 변환하여 적은 학습횟수와 높은 학습 정확도를 갖기 위한 작업
    sc = StandardScaler()
    sc.fit(X_train)
    X_train_std = sc.transform(X_train)
    ##########################################################
    ml = LogisticRegression(C=1.0, random_state=0)
    ml.fit(X_train_std, y_train)
    ##########################################################
    # 테스트
    # 학습 정확도 확인
    X_test_std = sc.transform(X_test)
    y_pred = ml.predict(X_test_std)
    print('학습 정확도 : ', accuracy_score(y_test, y_pred))
    # 학습 완료 객체를 저장
    with open('./MachineLearning/model_LogisticRegression.dat', 'wb') as fp:
        pickle.dump(ml, fp)
        pickle.dump(sc, fp)
    print('학습완료')


def step3_using():
    with open('./MachineLearning/model_LogisticRegression.dat', 'rb') as fp:
        ml = pickle.load(fp)
        sc = pickle.load(fp)
    X = [
        [1.4, 0.2], [1.3, 0.2], [1.5, 0.2],
        [4.5, 1.5], [4.1, 1.0], [4.5, 1.5],
        [5.2, 2.0], [5.4, 2.3], [5.1, 1.8]]
    X_std = sc.transform(X)
    y_pred = ml.predict(X_std)
#    print(len(y_pred))
    for value in y_pred:
        if value == 0:
            print('Iris-setosa')
        elif value == 1:
            print('Iris-versicolor')
        if value == 2:
            print('Iris-virginica')


if __name__ == "__main__":
    #    step1_get_data()
    step2_learning()
    step3_using()
