import matplotlib.pyplot as plt
import os
import matplotlib
matplotlib.use('Agg')

def generate_performance_graphs(historical_quiz, user_id):
    os.makedirs("static", exist_ok=True)  # Ensure 'static' folder exists

    # Calculate accuracy trend
    historical_quiz['is_correct'] = historical_quiz['selected_option'] == historical_quiz['correct_option']
    accuracy_trend = historical_quiz.groupby('quiz_id')['is_correct'].mean() * 100

    # Mistakes per topic
    mistakes_per_topic = historical_quiz[historical_quiz['is_correct'] == False].groupby('question_id').size()

    # Save Accuracy Trend Graph
    accuracy_plot_path = f"static/accuracy_trend_{user_id}.png"
    plt.figure(figsize=(10, 5))
    plt.plot(accuracy_trend.index, accuracy_trend.values, marker='o', linestyle='-', color='b')
    plt.xlabel('Quiz ID')
    plt.ylabel('Accuracy (%)')
    plt.title('Student Accuracy Trend Over Time')
    plt.grid(True)
    plt.savefig(accuracy_plot_path)  # Save the plot as an image
    plt.close()

    # Save Mistakes Per Topic Graph
    mistakes_plot_path = f"static/mistakes_per_topic_{user_id}.png"
    plt.figure(figsize=(8, 5))
    mistakes_per_topic.plot(kind='bar', color='red')
    plt.xlabel('Question ID')
    plt.ylabel('Number of Mistakes')
    plt.title('Mistakes Per Question')
    plt.savefig(mistakes_plot_path)  # Save the plot as an image
    plt.close()

    return {
        "accuracy_trend": accuracy_plot_path,
        "mistakes_per_topic": mistakes_plot_path
    }
