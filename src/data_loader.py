import pandas as pd
import numpy as np

def load_quiz_data(user_id):
    # Simulated quiz data
    current_quiz = pd.DataFrame({
        'question_id': [1, 2, 3, 4, 5],
        'topic': ['Physics', 'Chemistry', 'Biology', 'Physics', 'Biology'],
        'selected_option': [1, 3, 2, 4, 2],
        'correct_option': [1, 2, 2, 4, 3]
    })
    
    historical_quiz = pd.DataFrame({
        'quiz_id': [101, 102, 103, 104, 105],
        'question_id': [1, 2, 3, 4, 5],
        'selected_option': [1, 2, 2, 3, 2],
        'correct_option': [1, 2, 2, 4, 3]
    })
    
    return current_quiz, historical_quiz
