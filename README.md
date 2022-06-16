# StudyPython_2022_intermediate(feat. Anaconda)

cd venv/Scripts & activate & cd.. & cd..

# 0일차

## Anaconda설치 방법

https://www.anaconda.com/

## Conda 가상환경 만들기

- (base) C:\Users\june3>conda create -n py3_8 python=3.8
  py3_8(이름) 파이썬 3.8버전 가상환경 생성
- conda activate py3_8

![image](https://user-images.githubusercontent.com/83456300/173177682-2a8864cd-ab26-459d-944e-2ad2824b0a26.png)
![image](https://user-images.githubusercontent.com/83456300/173177731-66095d6f-79ff-4056-a277-4d6ac0b18a95.png)

## VS Code 가상환경 만들기

### !주의! 깃 레포지토리 바로 아래에 만들어야지 인터프리터를 인식한다.

- python -m venv {venvDir}
- {venvDir}/Scripts/activate (venv/Scripts/activate) -> 안됨 ;;

### - cd venv/Scripts & activate & cd.. & cd..

- cd {venvDif}\Scripts
- activate
- deactivate

## 내 의견

- VS Code의 venv로 만들면 작업중인 폴더 안에 바로 가상환경을 만들 수 있다는 장점이 있지만 그 버전의 Python 인터프리터가 설치 되어야 한다.
- 아나콘다는 가상환경이 .conda 거길로 가지만 원하는 파이썬 버전을 바로 바로 만들 수 있다.

## 가상 환경 .gitignore 만들기

1. 파일 생성
   먼저 원하는 repository 폴더로 이동한다.
   $ cd 경로
   해당 위치에 파일을 생성 & 편집한다.
   $ vim .gitignore
   위 명령을 입력하면, 파일 편집기가 나타나게 된다.
   여기서 키보드의 "a" 키 를 누르면, 작성을 시작할 수 있다.
   여기에 git 연동에 무시하고 싶은 파일이나 폴더의 경로를 입력한다.

'esc' key를 눌러서, 명령입력 모드로 전환한 후
':wq'를 통해 입력한 내용을 저장한다.

2. 기존 commit 기록 삭제
   👀 이 단계는 repository를 만들면서 바로 gitignore파일을 만드는 경우 생략해도 된다.
   기존 레포 수정 기록이 영향을 주지 않도록 만드는 과정이기 때문이다.

$ git rm -r --cached .

## 1일차

- 웹 크롤링
  가상환경 이름 : venv_WebCrawling
  설치한 라이브러리 : - pip install selenium beautifulsoup4
  - pip install ipykernel
  - pip install jupyter
  - pip install requests

## 2일차

- 웹 크롤링-2
- pandas문법 1~10

## 3일차

- pandas 문법 11~20
- Data Analysis

## 4일차

- Machine Learning
- Perceptron
- - Iris
- - Perceptron_my
- - Perceptron_sklearn
- - Perceptron_sklearn_Logistic Regression

## 5일차

- 감정분석(네이버 평점 러닝)

# [Large Movie Review Dataset](https://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz)

# java install

```
winget search java
winget install ojdkbuild.openjdk.11.jdk
```

# [JPype](https://www.lfd.uci.edu/~gohlke/pythonlibs/#_jpype)

```
pip install JPype1-1.1.2-cp39-cp39-win_amd64.whl
```

# [KoNLPy](https://konlpy.org/ko/latest/index.html)

```
pip install konlpy
```

# 이모티콘 정규표현식

```
'(?::|;|=)(?:-)?(?:\)|\(|D|P)|\^.?\^'
```

# 네이버 영화 댓글

```
https://movie.naver.com/movie/bi/mi/pointWriteFormList.naver?code=196367&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page=2
```
