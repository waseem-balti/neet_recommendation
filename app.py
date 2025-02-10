import os
import pandas as pd
import numpy as np
from flask import Flask, jsonify, request
from src.data_loader import load_quiz_data
from src.analysis import analyze_performance
from src.recommendations import generate_recommendations
from src.rank_predictor import predict_neet_rank
from src.visualizer import generate_performance_graphs

# Initialize Flask app
app = Flask(__name__)

@app.route('/analyze', methods=['GET'])
def analyze():
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({'error': 'User ID is required'}), 400
    
    # Load data
    current_quiz, historical_quiz = load_quiz_data(user_id)
    
    # Analyze performance
    performance_insights = analyze_performance(current_quiz, historical_quiz)
    recommendations = generate_recommendations(performance_insights)
    
    return jsonify({
        'performance': performance_insights,
        'recommendations': recommendations
    })

@app.route('/predict-rank', methods=['GET'])
def predict_rank():
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({'error': 'User ID is required'}), 400
    
    rank_estimation = predict_neet_rank(user_id)
    return jsonify({'predicted_rank': rank_estimation})

if __name__ == '__main__':
    app.run(debug=True)
