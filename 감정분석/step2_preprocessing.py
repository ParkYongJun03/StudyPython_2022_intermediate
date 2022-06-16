from argon2 import DEFAULT_RANDOM_SALT_LENGTH
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

# 댓글에서 불필요한 문자 제거


def text_preprocessing(text):
    text = text.strip().replace('\n', '').replace('\r', '').replace('\t', '')
    if text.startswith('관람객'):
        new_str = text[3:]
        return new_str
    else:
        return text

# 평점 기준으로 긍정 부정 설정


def star_preprocessing(text):
    value = int(text)
    if value > 5:
        return '1'
    else:
        return '0'


def step2_preprocessing():
    # 수집한 데이터 읽어 오기
    df = pd.read_csv('./감정분석/naver_data.csv')
    np.random.seed(0)
    df = df.reindex(np.random.permutation(df.index))
    df['text'] = df['text'].apply(text_preprocessing)
    df['star'] = df['star'].apply(star_preprocessing)
    # df.head()
    # 학습 데이터, 테스트 데이터 분리
    text_list = df['text'].tolist()
    star_list = df['star'].tolist()
    text_train, text_test, star_train, star_test = train_test_split(
        text_list, star_list, test_size=0.3, random_state=0)

    # 저장하기위해 DataFrame로 다시 변환
    dic_train = {'text': text_train, 'star': star_train}
    df_train = pd.DataFrame(dic_train)
    dic_test = {'text': text_test, 'star': star_test}
    df_test = pd.DataFrame(dic_test)
    print(df_train.shape, df_test.shape)
    df_train.to_csv('./감정분석/naver_train_data.csv', index=False)
    df_test.to_csv('./감정분석/naver_test_data.csv')
    print('전치리 완료')

    # 전처리
if __name__ == "__main__":
    step2_preprocessing()
