from sklearn import pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.pipeline import Pipeline
import pickle
import pandas as pd
from time import time
from konlpy.tag import Kkma, Komoran, Hannanum, Mecab, Twitter, Okt
morphs = Komoran()


def tokenizer(text):
    return morphs.morphs(text)


def step3_learning():
    train_df = pd.read_csv('./감정분석/naver_train_data.csv')
    test_df = pd.read_csv('./감정분석/naver_test_data.csv')

    X_train = train_df['text'].tolist()
    y_train = train_df['star'].tolist()
    X_test = test_df['text'].tolist()
    y_test = test_df['star'].tolist()
    # 단어장 만들어 주는 객체 생성
    tfidf = TfidfVectorizer(lowercase=False, tokenizer=tokenizer)
    # 모델 생성
    logistic = LogisticRegression(C=10.0, random_state=0)
    pipeline = Pipeline([('vect', tfidf), ('clf', logistic)])

    # 학습
    stime = time()
    print('학습 시작')
    pipeline.fit(X_train, y_train)
    print('학습 종료')
    print('학습 시간 : %d' % (time() - stime))

    # 테스트
    y_pred = pipeline.predict(X_test)
    print('정확도 : %.3f' % accuracy_score(y_test, y_pred))

    # 학습된 모델 저장
    with open('./감정분석/model.dat', 'wb') as fp:
        pickle.dump(pipeline, fp)
    print('학습완료 및 모델 저장 완료')


if __name__ == "__main__":
    step3_learning()
