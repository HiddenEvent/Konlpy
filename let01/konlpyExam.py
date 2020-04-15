from konlpy.tag import Twitter

twitter = Twitter() # 단어를 분할 해줌
korToken = twitter.morphs('아주 가장 빠른게 개발능력을 올리자') # morphs 한국어를 토큰을 나눠준다.

## 댓글 수집하기
url = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=181414&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page=2'

import  requests # 요청하는 라이브러리
from bs4 import BeautifulSoup # bs4 HTML 분석
import time

## 댓글 수집 자동화
def get_reple(page = 1):
    response = requests.get(url.format(page))
    soup = BeautifulSoup(response.text, 'html.parser')

    s, t = [], []
    parse_list = soup.find('div', {'class': 'score_result'}).find_all('li')
    for li in parse_list:
        score = int(li.em.text)
        reple = li.p.text.strip(' \r\n\t')
        t.append(reple)
        if score >= 8:
            s.append(1)
        elif score <= 5:
            s.append(0)
    return s, t
score, text = [], []

for i in range(1, 1000):
    time.sleep(1)
    print(i, end='\r')
    s, t = get_reple(i)
    score += s
    text += t

import pandas as pd
pd.DataFrame([score, text]).T