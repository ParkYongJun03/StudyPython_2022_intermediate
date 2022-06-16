from regex import B
import requests
from bs4 import BeautifulSoup
from time import time, sleep
import pandas as pd


def step1_GetData():
    # 영화코드
    code_list = [1676638, 109906]
    # 현재 크롤링 중인 영화가 첫 번째 영화인지 여부
    chk = False
    # 영화 코드 목록 만큼 반복
    for code in code_list:
        # 1 : 해당 영화의 평점 페이지 수 계산
        site1 = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.naver?code=%d&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page=1' % code
        res1 = requests.get(site1)
        if res1.status_code == requests.codes.ok:
            bs1 = BeautifulSoup(res1.text, 'html.parser')
            score_total = bs1.find(class_='score_total')
            ems = score_total.find('em')
            score_total = int(ems.text.replace(',', ''))
            # print(score_total)
            # 페이지 계산
            pageCnt = score_total // 10
            if score_total % 10 > 0:
                pageCnt += 1
            print(pageCnt)

            # 현재 페이지 전송
            now_page = 1

            # 2 : 평점 글 정보와 평점을 가져온다.
            while now_page <= pageCnt:
                sleep(0.5)
                site2 = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.naver?code=%d&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page=%d' % (
                    code, now_page)
                res2 = requests.get(site2)
                if res2.status_code == requests.codes.ok:
                    bs2 = BeautifulSoup(res2.text, 'html.parser')
                    score_result = bs2.find(class_='score_result')
                    lis = score_result.find_all('li')
                    df = pd.DataFrame()
                    for obj in lis:
                        # 평점
                        star_score = obj.find(class_='star_score')
                        star_em = star_score.find('em')
                        star_score = int(star_em.text)

                        # 댓글
                        score_reple = obj.find(class_='score_reple')
                        reple_p = score_reple.find('p')
                        score_reple = reple_p.text

                        df = df.append([[score_reple, star_score]])

                    # 저장
                    if chk == False:  # 첫 번째 영화이면
                        df.columns = ['text', 'star']
                        df.to_csv('./감정분석/naver_data.csv',
                                  index=False, encoding='UTF-8')
                        chk = True
                    else:  # 두 번째 영화부터
                        df.to_csv('./감정분석/naver_data.csv', index=False,
                                  encoding='UTF-8', mode='a', header=False)
                    print('%d / %d' % (now_page, pageCnt))
                    now_page += 1


if __name__ == "__main__":
    step1_GetData()
