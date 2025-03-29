import pandas as pd
from sklearn.ensemble import RandomForestClassifier

def train_model():
    # Load historical attack data (CSV format)
    data = pd.read_csv('attack_data.csv')
    X = data[['severity', 'likelihood', 'relevance']]
    y = data['priority']
    
    model = RandomForestClassifier()
    model.fit(X, y)
    return model

def prioritize_threats(raw_data):
    # Train and use the model to predict priorities for threats
    model = train_model()
    
    # Convert raw data into DataFrame for predictions (mock example)
    df = pd.DataFrame(raw_data)
    
    predictions = model.predict(df[['severity', 'likelihood', 'relevance']])
    
    prioritized_data = [{'threat': t, 'priority': p} for t, p in zip(raw_data, predictions)]
    return prioritized_data
