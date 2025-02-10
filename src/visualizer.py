import matplotlib.pyplot as plt

def generate_performance_graphs(performance_data):
    topics = list(performance_data['weak_topics'].keys())
    errors = list(performance_data['weak_topics'].values())
    
    plt.figure(figsize=(10, 5))
    plt.bar(topics, errors, color='red')
    plt.xlabel('Topics')
    plt.ylabel('Number of Mistakes')
    plt.title('Weak Topics Analysis')
    plt.show()
