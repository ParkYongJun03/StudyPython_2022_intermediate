import numpy as np


class Perceptron:
    # 생성자
    # threshholds : 임계값, 계산된 예측값을 비교하는 값
    # eta : 학습률 #내생각 - 기울기를 조정하는 기울기
    # n_iter : 학습 횟수
    def __init__(self, thresholds=0.0, eta=0.01, n_iter=10):
        self.thresholds = thresholds
        # eta와 같이 사람이 일일이 조정해줄 수 없는 것을 Hyper Parameter라고 한다.
        self.eta = eta
        self.n_iter = n_iter

    # 학습 함수
    # X : 독립변수
    # y : 종속변수
    def fit(self, X, y):  # 사용을 하든 안 하든 def라는 메쏘드에는 self를 처음에 적어줘야 한다.
        # 가중치를 담을 변수 행렬 생성
        self.w_ = np.zeros(1 + X.shape[1])
        # +1를 하는 이유는 y=ax +b에서 b를 담을 공간을 넣기 위함이다.
        # 예측값과 실제값을 비교
        # 다른 예측값의 개수를 담을 리스트
        # '_'를 쓰는 이유는 관례적으로 외부에서 데이터를 수정하지 말라는 뜻
        self.errors_ = []
        # 지정된 횟수만큼(n_iter) 만큼 학습 반복
        for _ in range(self.n_iter):
            # 예측값과 실제값이 다른 개수를 담을 변수
            # '_'를 쓰면 변수에 데이터를 담지 않겠다. 라는 뜻
            # 메모리 관리를 위해서 씀
            errors = 0
            # 입력 받은 입력값과 결과값을 묶어 준다.
            temp1 = zip(X, y)  # zip이 뭔지 알아오기!
            # 입력값과 결과값을 묶음을 가지고 반복.
            for xi, target in temp1:
                # temp1의 X값이 xi로, y값이 target으로 간다.
                # 입력값을 가지고 예측값을 계산
                a1 = self.predict(xi)
                # 입력값과 예측값이 다르면 가중치를 재계산한다.
                if target != a1:
                    update = self.eta * (target-a1)
                    self.w_[1:] += update * xi
                    self.w_[0] += update
                    # 값이 다른 횟수를 누적
                    errors += int(update != 0.0)
            # 값이 다른 횟수를 배열에 담는다
            self.errors_.append(errors)
            print(self.w_)

    # y = ax + b 공식
    # X 벡터 데이터

    def net_input(self, X):
        a1 = np.dot(X, self.w_[1:]) + self.w_[0]  # dot은 백터 계산을 해준다.
        return a1
    # 예측된 결과를 가지고 판단.
    # X 벡터 데이터

    def predict(self, X):
        a2 = np.where(self.net_input(X) > self.thresholds, 1, -1)
        # 삼항 연산자
        return a2
