def generate_recommendations(performance_insights):
    recommendations = []
    for topic, count in performance_insights['weak_topics'].items():
        recommendations.append(f'Focus on {topic} as you made {count} mistakes.')
    return recommendations
