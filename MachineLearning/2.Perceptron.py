import numpy as np
from time import time
import pickle  # 얘는 뭐하는 애람?
from Perceptron_def import Perceptron
# 학습 로직


def step1_learning():
    # 학습 데이터 준비
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([-1, -1, -1, 1])
    # 퍼셉트론 객체 생성
    ppn = Perceptron(eta=0.1, n_iter=10)

    # 학습
    stime = time()  # start time
    ppn.fit(X, y)
    etime = time()  # end time
    print('학습에 걸린 시간 : ', etime-stime)
    print('학습 중 오차가 난 수:', ppn.errors_)

    # 학습 된 모델 저장
    with open('./MachineLearning./model.dat', 'wb') as fp:
        pickle.dump(ppn, fp)

    print('학습이 완료 되었습니다.')

# 예측 로직


def step2_using():
    # 학습이 된 저장된 모델 파일을 불러 오기
    with open('model.dat', 'rb') as fp:
        ppn = pickle.load(fp)
    while True:
        a1 = input('첫 번째 2진수를 입력해 주세요 : ')
        a2 = input('두 번째 2진수를 입력해 주세요 : ')
        X = np.array([int(a1), int(a2)])
        # 예측
        result = ppn.predict(X)
        if result == 1:
            print('결과 : 1')
        else:
            print('결과 : 0')


if __name__ == "__main__":
    step1_learning()
    # step2_using()
