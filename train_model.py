# train_model.py
import pandas as pd
import numpy as np
from sklearn.model_selection import KFold
from sklearn.metrics import roc_auc_score
from xgboost import XGBClassifier
import joblib
import warnings
warnings.filterwarnings(action='ignore')

def train_and_save_models(train_path):
    # 학습 데이터 로드
    train_df = pd.read_csv(train_path)
    
    # '[.]'을 '.'으로 복구
    train_df['URL'] = train_df['URL'].str.replace(r'\[\.\]', '.', regex=True)
    
    # 특성 생성
    train_df['length'] = train_df['URL'].str.len()
    train_df['subdomain_count'] = train_df['URL'].str.split('.').apply(lambda x: len(x) - 2)
    train_df['special_char_count'] = train_df['URL'].apply(lambda x: sum(1 for c in x if c in '-_/'))
    
    # 학습을 위한 학습 데이터의 피처와 라벨 준비
    X = train_df[['length', 'subdomain_count', 'special_char_count']]
    y = train_df['label']
    
    # K-Fold 설정
    kf = KFold(n_splits=4, shuffle=True, random_state=42)
    models = []
    auc_scores = []
    
    for idx, (train_idx, val_idx) in enumerate(kf.split(X)):
        X_train, X_val = X.iloc[train_idx].values, X.iloc[val_idx].values
        y_train, y_val = y.iloc[train_idx].values, y.iloc[val_idx].values
        
        print('-'*40)
        print(f'Fold {idx + 1} 번째 XGBoost 모델을 학습합니다.')
        
        model = XGBClassifier(
            n_estimators=100,
            max_depth=6,
            learning_rate=0.1,
            random_state=42,
            use_label_encoder=False,
            eval_metric="auc",
        )
        
        eval_set = [(X_train, y_train), (X_val, y_val)]
        model.fit(
            X_train, y_train,
            eval_set=eval_set,
            verbose=False,
        )
        
        models.append(model)
        
        y_val_pred_prob = model.predict_proba(X_val)[:, 1]
        auc = roc_auc_score(y_val, y_val_pred_prob)
        print(f"Fold {idx + 1} CV ROC-AUC: {auc:.4f}")
        print('-'*40)
        auc_scores.append(auc)
    
    print(f"K-Fold 평균 ROC-AUC: {np.mean(auc_scores):.4f}")
    
    # 모델 저장
    joblib.dump(models, 'malicious_url_models.pkl')
    print("모델이 'malicious_url_models.pkl'로 저장되었습니다.")

if __name__ == "__main__":
    # 여기에 train.csv 파일 경로를 입력하세요
    train_path = 'train.csv'
    train_and_save_models(train_path)
