# 고려대학교 CURT 프로젝트 (악성 URL 탐지 사이트)

![CURT 로고](https://via.placeholder.com/150)

## 프로젝트 소개

CURT(Check URL in Real Time)는 머신러닝 기술을 활용하여 웹 URL의 악성 여부를 실시간으로 탐지하는 웹 서비스입니다. 사용자가 의심스러운 URL을 입력하면 AI 모델이 URL의 특성을 분석하여 악성 여부를 판단합니다.

이 프로젝트는 고려대학교 인공지능사이버보안학과 학생들이 개발했으며, 웹 보안 인식을 높이고 피싱 및 악성 웹사이트로부터 사용자를 보호하는 것을 목표로 합니다.

## 주요 기능

- **실시간 URL 분석**: 입력된 URL을 즉시 분석하여 악성 여부를 판단합니다.
- **URL 특성 분석**: URL 길이, 서브도메인 수, 특수문자 비율 등 다양한 특성을 추출하여 분석합니다.
- **직관적인 UI**: 사용자 친화적인 인터페이스로 누구나 쉽게 이용할 수 있습니다.
- **머신러닝 기반**: 앙상블 기법을 사용한 머신러닝 모델로 높은 정확도를 제공합니다.

## 기술 스택

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, JavaScript
- **Machine Learning**: scikit-learn, joblib, numpy
- **Deployment**: PythonAnywhere

## 설치 및 실행 방법

### 로컬 환경에서 실행하기

1. 저장소 클론
   ```bash
   git clone https://github.com/yourusername/curt-project.git
   cd curt-project
   ```

2. 가상환경 설정 및 패키지 설치
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. 애플리케이션 실행
   ```bash
   python app.py
   ```

4. 웹 브라우저에서 `http://localhost:5000` 접속

### 배포 방법 (PythonAnywhere)

1. PythonAnywhere 계정 생성 및 로그인

2. Bash 콘솔 열기

3. 프로젝트 클론
   ```bash
   git clone https://github.com/yourusername/curt-project.git
   ```

4. 가상환경 설정 및 패키지 설치
   ```bash
   mkvirtualenv --python=python3.9 curt-env
   pip install -r requirements.txt
   ```

5. Web 탭에서 새 웹앱 생성
   - Flask 선택
   - Python 3.9 선택
   - 소스 코드 경로 설정

6. WSGI 파일 수정
   - 올바른 경로와 앱 이름 설정

## 프로젝트 구조

```
project/
├── app.py                   # Flask 애플리케이션 메인 파일
├── templates/               # HTML 템플릿
│   └── index.html           # 메인 페이지 템플릿
├── static/                  # 정적 파일 (CSS, JS)
├── malicious_url_models.pkl # 학습된 머신러닝 모델
└── requirements.txt         # 필요한 파이썬 패키지 목록
```

## 모델 학습 방법

이 프로젝트에서 사용된 모델은 다음 특성을 기반으로 학습되었습니다:
- URL 길이
- 서브도메인 수
- 특수문자 수
- 그 외 다양한 URL 특성

모델 재학습을 원하시면 다음 단계를 따르세요:
1. 학습 데이터셋 준비
2. `train_model.py` 스크립트 실행
3. 생성된 모델 파일을 프로젝트 디렉토리에 복사

## 기여 방법

1. 이 저장소를 포크합니다.
2. 새 브랜치를 생성합니다: `git checkout -b feature-name`
3. 변경사항을 커밋합니다: `git commit -m 'Add some feature'`
4. 브랜치를 푸시합니다: `git push origin feature-name`
5. Pull Request를 제출합니다.

## 팀원

- 고건우 (인공지능사이버보안학과)
- 김재하 (인공지능사이버보안학과)
- 신승환 (인공지능사이버보안학과)
- 양진영 (인공지능사이버보안학과)
- 전성하 (인공지능사이버보안학과)

## 라이센스

이 프로젝트는 MIT 라이센스 하에 배포됩니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하세요.

## 참고 자료

- [악성 URL 탐지 관련 연구 논문](https://example.com)
- [Flask 공식 문서](https://flask.palletsprojects.com/)
- [scikit-learn 공식 문서](https://scikit-learn.org/stable/)
