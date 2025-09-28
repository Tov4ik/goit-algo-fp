import random
import matplotlib.pyplot as plt

# Функція для монте-карло симуляції
def monte_carlo_dice(trials=100000):
    counter = {s:0 for s in range(2,13)}  # Ключ — сума, значення — кількість випадань

    # Моделюємо кидки
    for _ in range(trials):
        first = random.randint(1,6)
        second = random.randint(1,6)
        s = first + second
        counter[s] += 1

    # Рахуємо ймовірності
    probabilities = {s: (counter[s]/trials)*100 for s in counter}
    return counter, probabilities

# Аналітичні ймовірності (для порівняння)
def theoretical_probabilities():
    return {
        2: 2.78, 3: 5.56, 4: 8.33, 5: 11.11, 6: 13.89,
        7: 16.67, 8: 13.89, 9: 11.11, 10: 8.33, 11: 5.56, 12: 2.78
    }

# Малюємо графіки
def plot_results(prob_mc, prob_th):
    sums = list(prob_mc.keys())
    vals_mc = [prob_mc[s] for s in sums]
    vals_th = [prob_th[s] for s in sums]

    plt.figure(figsize=(8,5))
    plt.bar(sums, vals_mc, color='skyblue', label='Монте-Карло')
    plt.plot(sums, vals_th, marker='o', color='orange', label='Теоретична')
    plt.xlabel('Сума на кубиках')
    plt.ylabel('Ймовірність, %')
    plt.title('Ймовірності сум при киданні двох кубиків')
    plt.legend()
    plt.show()

# Приклад використання
def example():
    trials = 100000
    counter, prob_mc = monte_carlo_dice(trials)
    prob_th = theoretical_probabilities()

    print(f"Результати Монте-Карло ({trials} кидків):")
    for s in sorted(prob_mc.keys()):
        print(f"  {s}: {prob_mc[s]:5.2f}% (аналітична: {prob_th[s]:5.2f}%)")
    print("\nТаблиця появи суми (кількість):", counter)
    plot_results(prob_mc, prob_th)

if __name__ == "__main__":
    example()
