# app.py
from flask import Flask, render_template, request, jsonify
import numpy as np
import joblib
import os
import logging

app = Flask(__name__)

# 로깅 설정
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

# 모델 파일 경로 설정
MODEL_PATH = 'malicious_url_models.pkl'

# 모델 로드 함수
def load_models():
    if os.path.exists(MODEL_PATH):
        return joblib.load(MODEL_PATH)
    else:
        raise FileNotFoundError(f"모델 파일을 찾을 수 없습니다: {MODEL_PATH}")

# URL 특성 추출 함수
def extract_url_features(url):
    length = len(url)
    subdomain_count = url.count('.') - 1  # 도메인 수 - 1 (보수적 추정)
    special_char_count = sum(1 for c in url if c in '-_/')
    
    return length, subdomain_count, special_char_count

# URL 예측 함수
def predict_url(url):
    # 특성 추출
    length, subdomain_count, special_char_count = extract_url_features(url)
    features = np.array([[length, subdomain_count, special_char_count]])
    
    try:
        # 모델 로드
        models = load_models()
        
        # 각 모델별 예측 확률 계산
        prob_sum = 0
        for model in models:
            prob_sum += model.predict_proba(features)[:, 1]
        
        # 앙상블 결과 (평균 확률)
        avg_prob = prob_sum / len(models)
        
        is_malicious = bool(avg_prob[0] >= 0.5)
        probability = float(avg_prob[0])
        
        # 터미널에 로그 출력
        result_text = "악성" if is_malicious else "정상"
        logger.info(f"URL 검사 결과: '{url}' - {result_text} (확률: {probability:.2f})")
        
        # 결과 생성
        result = {
            "url": url,
            "is_malicious": is_malicious,
            "probability": probability,
            "features": {
                "length": int(length),
                "subdomain_count": int(subdomain_count),
                "special_char_count": int(special_char_count)
            }
        }
        
        return result
    
    except Exception as e:
        logger.error(f"URL 검사 중 오류 발생: {url} - {str(e)}")
        return {"error": str(e)}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/check_url', methods=['POST'])
def check_url():
    data = request.json
    url = data.get('url', '')
    
    if not url:
        logger.warning("URL이 입력되지 않았습니다.")
        return jsonify({"error": "URL을 입력해주세요"}), 400
    
    # URL 형식 확인 및 수정
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url
        logger.info(f"URL 형식 수정: '{url}'")
    
    logger.info(f"URL 검사 요청: '{url}'")
    
    # URL 예측 수행
    result = predict_url(url)
    
    return jsonify(result)

if __name__ == '__main__':
    logger.info("악성 URL 탐지 서비스가 시작되었습니다.")
    app.run(debug=True)
