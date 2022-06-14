# 학습용 데이터
from sklearn import datasets
# 데이터를 학습용과 테스트용으로 나누는 함수
from sklearn.model_selection import train_test_split
# 데이터 표준화
from sklearn.preprocessing import StandardScaler
# Perceptron 머신러닝 클래스
from sklearn.linear_model import Perceptron
# 정확도 계산을 위한 함수
from sklearn.metrics import accuracy_score
# 파일저장
import pickle
import numpy as np

from Perceptron_def import Perceptron_my

# 무슨 싸이킷 런에 어떤 함수를 쓸거냐는걸 정하기 위해서는 '싸이킷 런 치팅 시트'를 열어서 나의 목적과 활용범위에 맞게 사용해라.


def step1_get_data():
    # iris 데이터 가져오기
    iris = datasets.load_iris()
    # print(iris)
    # 꽃잋정보(독립변수)
    X = iris.data[:100, [2, 3]]
    # 꽃 종류(종속변수)
    y = iris.target[:100]
    # 꽃 이름
    names = iris.target_names[:2]
    return X, y


def step2_learning():
    X, y = step1_get_data()
    # 학습데이터와 테스트 데이터 분리
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=0)
    # test_size=0.3 :  30%를 validation 값으로 테스트 한다는 뜻
    # validation : train데이터가 아니라 알고리즘의 강인함을 테스트하기 위해 일부러 나쁜 데이터를 넣는 것.
    # random_state : 데이터셋의 순서를 고정시키는 시드
    # 표준화 작업 : 데이터들을 표준 정규분포로 변환하여 적은 학습횟수와 높은 학습 정확도를 갖기 위한 작업
    sc = StandardScaler()
    # 데이터 값이 너무 큰 경우 스케일을 1로 줄여줌
    sc.fit(X_train)
    X_train_std = sc.transform(X_train)
    ml = Perceptron(eta0=0.01, max_iter=40, random_state=0)
    ml.fit(X_train_std, y_train)
    # 학습 정확도 확인
    X_test_std = sc.transform(X_test)
    y_pred = ml.predict(X_test_std)
    print('학습 정확도 : ', accuracy_score(y_test, y_pred))
    # 학습 완료 객체를 저장
    with open('./MachineLearning/model_sklearn.dat', 'wb') as fp:
        pickle.dump(ml, fp)
        pickle.dump(sc, fp)
    print('학습완료')


def step3_using():
    with open('./MachineLearning/model_sklearn.dat', 'rb') as fp:
        ml = pickle.load(fp)
        sc = pickle.load(fp)
    while True:
        a1 = input('꽃잎의 길이를 입력해주세요 : ')
        a2 = input('꽃잎의 넓이를 입력해주세요 : ')
        # 사이킷런은 메트릭스 구조의 데이터를 받아 들인다.
        X = np.array([[float(a1), float(a2)]])
        # 중요! SKlearn은 뭐든지 매트릭스 데이터로 만들어야 한다.[[]]
        X_std = sc.transform(X)
        # 예측
        result = ml.predict(X_std)
        if result == 0:
            print('결과 : Iris-setosa')
        elif result == 1:
            print('결과 : Iris-versicolor')


if __name__ == "__main__":
    step1_get_data()
    step2_learning()
    step3_using()
