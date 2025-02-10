def analyze_performance(current_quiz, historical_quiz):
    accuracy = (current_quiz['selected_option'] == current_quiz['correct_option']).mean()
    weak_topics = current_quiz[current_quiz['selected_option'] != current_quiz['correct_option']]['topic'].value_counts().to_dict()
    
    return {
        'accuracy': accuracy,
        'weak_topics': weak_topics
    }
