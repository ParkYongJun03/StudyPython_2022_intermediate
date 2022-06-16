from http.client import ImproperConnectionState
from konlpy.tag import Kkma, Komoran, Hannanum, Mecab, Twitter, Okt
from step1_GetData import step1_GetData
from step2_preprocessing import step2_preprocessing
from step3_learning import step3_learning, tokenizer
import pickle
import numpy as np


def word_tokenizer(text):
    # 형태소 분석기
    okt = Okt()
    #['아버지', '가방', '에', '들어가신다']
    # okt = Hannanum()
    #['아버지가방에들어가', '이', '시ㄴ다']
    # okt = Komoran()
    # ['아버지', '가방', '에', '들어가', '시', 'ㄴ다']
    # okt = Kkma()
    # ['아버지가방에 들어가신다']
    return okt.morphs(text)


def step4_using():
    with open('./감정분석/model.dat', 'rb') as fp:
        pipeline = pickle.load(fp)
    while True:
        text = input('한글로 리뷰를 작성해주세요. : ')
        y = pipeline.predict([text])
        rate = pipeline.predict_proba([text]) * 100
        rate = np.max(rate)

        if y == 1:
            print('긍정 리뷰')
        else:
            print('부정 리뷰')
        print('정확도 : %d' % rate)


if __name__ == "__main__":
    # text = '아버지가방에들어가신다'
    # result = word_tokenizer(text)
    # print(result)
    # step1_GetData()
    # step2_preprocessing()
    step3_learning()
    # step4_using()
