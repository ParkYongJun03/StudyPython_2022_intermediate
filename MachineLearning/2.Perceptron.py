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
    ppn = Perceptron(eta=0.1)

    # 학습
    stime = time()  # start time
    ppn.fit(X, y)
    etime = time()  # end time
    print('학습에 걸린 시간 : ', etime-stime)
    print('학습 중 오차가 난 수:', ppn.errors_)

    # 학습 된 모델 저장
    with open('./model.dat', 'wb') as fp:
        pickle.dump(ppn, fp)

    print('학습이 완료 되었습니다.')
# 예측 로직


def step2_using():
    pass


if __name__ == "__main__":
    step1_learning()
    step2_using()
