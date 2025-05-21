import time
import random
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
from binpacking import *

matplotlib.use('TkAgg')



# измерение времени выполнения функции
def measure_time(func, values, eps):
    start = time.time()
    func(values, eps)
    return time.time() - start



# генерация случайных данных
def generate_test_data(n):
    return [random.uniform(0.01, 0.99) for _ in range(n)]


# построени графика
def visualize(max_n, step, epsilons=[0.1, 0.3, 0.5]):
    sizes = range(step, max_n + 1, step)
    results = []

    for n in sizes:
        values = generate_test_data(n)
        for eps in epsilons:
            time_taken = measure_time(bin_packing, values, eps)
            results.append({'n': n, 'eps': eps, 'time': time_taken})
    df = pd.DataFrame(results)
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(12, 6))
    ax = sns.lineplot(
        data=df,
        x='n',
        y='time',
        hue='eps',
        marker='o',
        palette='viridis',
        linewidth=2.5
    )
    ax.set_title(
        'Время выполнения алгоритма Bin Packing\n'
        f'для разных ε (шаг={step}, max_n={max_n})',
        fontsize=14,
        pad=20
    )
    ax.set_xlabel('Размер входных данных (n)', fontsize=12)
    ax.set_ylabel('Время выполнения (сек)', fontsize=12)
    ax.legend(title='ε (epsilon)', title_fontsize=12)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    visualize(max_n=1000, step=100, epsilons=[0.1, 0.25, 0.5, 0.75, 0.9])
