import os
import pandas as pd
import numpy as np
from flask import Flask, jsonify, request, render_template
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




@app.route('/visualize', methods=['GET'])
def visualize():
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({'error': 'User ID is required'}), 400

    _, historical_quiz = load_quiz_data(user_id)
    graph_paths = generate_performance_graphs(historical_quiz, user_id)

    return jsonify({
        'message': 'Visualization generated successfully',
        'graphs': graph_paths
    })

@app.route('/get-graph', methods=['GET'])
def get_graph():
    filename = request.args.get('filename')
    if not filename:
        return jsonify({'error': 'Filename is required'}), 400

    file_path = os.path.join("static", filename)
    if not os.path.exists(file_path):
        return jsonify({'error': 'File not found'}), 404

    return send_file(file_path, mimetype='image/png')



@app.route('/dashboard', methods=['GET'])
def dashboard():
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({'error': 'User ID is required'}), 400

    _, historical_quiz = load_quiz_data(user_id)
    graph_paths = generate_performance_graphs(historical_quiz, user_id)

    return render_template('dashboard.html',
                           accuracy_trend="/" + graph_paths["accuracy_trend"],
                           mistakes_per_topic="/" + graph_paths["mistakes_per_topic"])


if __name__ == '__main__':
    app.run(debug=True)
