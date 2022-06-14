import numpy as np
from time import time
import pickle  # 얘는 뭐하는 애람?
from Perceptron_def import Perceptron_my
import pandas as pd


def step1_get_data():
    # 학습 데이터 준비
    df = pd.read_csv('./MachineLearning/iris.data', header=None)
    # X 데이터 준비
    X = df.iloc[:100, [2, 3]].values
    # y데이터 준비
    y = df.iloc[:100, 4].values
    y = np.where(y == 'Iris-setosa', 1, -1)
    print(y)
    return X, y
    # 예측 로직


def step2_learning():
    # 퍼셉트론 객체 생성
    ppn = Perceptron_my(eta=0.1, n_iter=10)
    data = step1_get_data()
    # print(data)
    X = data[0]
    y = data[1]
    # 학습
    ppn.fit(X, y)
    print(ppn.errors_)
    print(ppn.w_)
    # 학습 된 모델 저장
    with open('./MachineLearning/model_iris.dat', 'wb') as fp:
        pickle.dump(ppn, fp)
    print('학습이 완료 되었습니다.')
# 예측 로직


def step3_using():
    # 학습이 된 저장된 모델 파일을 불러 오기
    with open('./MachineLearning/model_iris.dat', 'rb') as fp:
        ppn = pickle.load(fp)
    while True:
        a1 = input('꽃잎의 길이를 입력해주세요 : ')
        a2 = input('꽃잎의 넓이를 입력해주세요 : ')
        X = np.array([float(a1), float(a2)])
        # 예측
        result = ppn.predict(X)
        if result == 1:
            print('결과 : Iris-setosa')
        else:
            print('결과 : Iris-versicolor')


if __name__ == "__main__":
    step1_get_data()
    step2_learning()
    step3_using()
