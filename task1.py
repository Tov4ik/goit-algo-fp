class Node:
    def __init__(self, value):
        self.value = value
        self.next = None  # Посилання на наступний вузол

class LinkedList:
    def __init__(self):
        self.head = None  # Початок списку

    def append(self, value):
        new_node = Node(value)
        if self.head is None:  # Якщо список пустий, новий вузол стає головою
            self.head = new_node
            return
        current = self.head
        while current.next:  # Ідемо до кінця списку
            current = current.next
        current.next = new_node  # Додаємо новий вузол в кінець

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")  # Кінець списку

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev  # Міняємо напрямок посилання
            prev = current
            current = next_node
        self.head = prev

    def insertion_sort(self):
        if not self.head:
            return
        sorted_head = self.head
        current = self.head.next
        sorted_head.next = None
        while current:
            next_to_check = current.next
            sorted_current = sorted_head
            prev = None
            while sorted_current and sorted_current.value < current.value:
                prev = sorted_current
                sorted_current = sorted_current.next
            if prev is None:
                current.next = sorted_head
                sorted_head = current
            else:
                current.next = sorted_current
                prev.next = current
            current = next_to_check
        self.head = sorted_head

def merge_two_sorted_lists(list1, list2):
    if not list1.head:
        return list2
    if not list2.head:
        return list1
    merged = LinkedList()
    current1 = list1.head
    current2 = list2.head
    if current1.value <= current2.value:
        merged.head = current1
        current1 = current1.next
    else:
        merged.head = current2
        current2 = current2.next
    current_merged = merged.head
    while current1 and current2:
        if current1.value <= current2.value:
            current_merged.next = current1
            current1 = current1.next
        else:
            current_merged.next = current2
            current2 = current2.next
        current_merged = current_merged.next
    if current1:
        current_merged.next = current1
    if current2:
        current_merged.next = current2
    return merged

# Приклади
# 1) Додавання і друк списку
print("Приклад: Додавання елементів і друк списку")
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.print_list()

# 2) Реверс списку
print("\nПриклад: Реверс списку")
ll.reverse()
ll.print_list()

# 3) Сортування вставками
print("\nПриклад: Сортування вставками")
ll2 = LinkedList()
ll2.append(4)
ll2.append(1)
ll2.append(3)
ll2.append(2)
ll2.print_list()  # Перед сортуванням
ll2.insertion_sort()
ll2.print_list()  # Після сортування

# 4) Об'єднання двох відсортованих списків
print("\nПриклад: Об'єднання двох відсортованих списків")
ll3 = LinkedList()
ll3.append(1)
ll3.append(3)
ll4 = LinkedList()
ll4.append(2)
ll4.append(4)
merged = merge_two_sorted_lists(ll3, ll4)
merged.print_list()
