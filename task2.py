import turtle

# Функція для малювання однієї гілки фрактала
def draw_pythagoras_tree(branch_length, level):
    if level == 0:
        return
    # Малюємо гілку (лінію)
    turtle.forward(branch_length)
    # Ліва гілка
    turtle.left(45)
    draw_pythagoras_tree(branch_length * 0.7, level - 1)
    turtle.right(45)
    # Права гілка
    turtle.right(45)
    draw_pythagoras_tree(branch_length * 0.7, level - 1)
    turtle.left(45)
    # Повертаємось назад
    turtle.backward(branch_length)

# Основна програма
def main():
    # Встановлення параметрів turtle
    turtle.speed("fastest")
    turtle.left(90)
    turtle.up()
    turtle.backward(100)  # Відступаємо вниз, щоб дерево вмістилося
    turtle.down()
    
    # Запитуємо рівень рекурсії у користувача
    try:
        level = int(input("Введіть рівень рекурсії (наприклад, 7): "))
    except:
        level = 7  # Якщо введено некоректно, ставимо 7

    print(f"Малюю дерево Піфагора з рівнем рекурсії: {level}")
    draw_pythagoras_tree(100, level)

    turtle.done()

if __name__ == "__main__":
    main()
