
import pickle
import numpy as np


def step4_using():
    with open('./감정분석/model.dat', 'rb') as fp:
        pipeline = pickle.load(fp)
    while True:
        text = input('한글로로 리뷰를 작성해주세요. : ')
        y = pipeline.predict([text])
        rate = pipeline.predict_proba([text]) * 100
        rate = np.max(rate)

        if y == 1:
            print('긍정 리뷰')
        else:
            print('부정 리뷰')
        print('정확도 : %d' % rate)
