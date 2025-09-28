def greedy_algorithm(items, budget):
    # Обчислюємо калорійність на одиницю вартості
    ratios = [(name, props["calories"] / props["cost"], props["cost"]) for name, props in items.items()]
    # Сортуємо за співвідношенням калорій/вартість (спадання)
    ratios.sort(key=lambda x: x[1], reverse=True)
    selected, total_cost, total_calories = [], 0, 0

    for name, ratio, cost in ratios:
        if total_cost + cost <= budget:
            selected.append(name)
            total_cost += cost
            total_calories += items[name]["calories"]

    return selected, total_cost, total_calories

def dynamic_programming(items, budget):
    # Перетворюємо словник у списки для зручності
    names = list(items.keys())
    costs = [items[name]["cost"] for name in names]
    calories = [items[name]["calories"] for name in names]
    n = len(names)

    dp = [0] * (budget + 1)
    picks = [[False]*n for _ in range(budget + 1)]

    for i in range(n):
        for b in range(budget, costs[i]-1, -1):
            if dp[b - costs[i]] + calories[i] > dp[b]:
                dp[b] = dp[b - costs[i]] + calories[i]
                picks[b] = picks[b - costs[i]].copy()
                picks[b][i] = True

    # Відновлюємо набір страв
    best = picks[budget]
    selected = [names[i] for i in range(n) if best[i]]
    total_calories = dp[budget]
    total_cost = sum(items[name]["cost"] for name in selected)
    return selected, total_cost, total_calories

# Приклад використання
def example():
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }
    budget = 100

    print(f"Бюджет: {budget}")
    selected_greedy, cost_greedy, cal_greedy = greedy_algorithm(items, budget)
    print("Жадібний алгоритм:")
    print(f"  Вибрано: {selected_greedy}")
    print(f"  Загальна вартість: {cost_greedy}")
    print(f"  Сумарна калорійність: {cal_greedy}")

    selected_dynamic, cost_dynamic, cal_dynamic = dynamic_programming(items, budget)
    print("\nДинамічне програмування:")
    print(f"  Вибрано: {selected_dynamic}")
    print(f"  Загальна вартість: {cost_dynamic}")
    print(f"  Сумарна калорійність: {cal_dynamic}")

if __name__ == "__main__":
    example()
