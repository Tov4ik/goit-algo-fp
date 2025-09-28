import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

# Клас вузла дерева
class Node:
    def __init__(self, key, color="#1296F0"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

# Додає вузли у граф
def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

# Малює дерево з кольорами вузлів
def draw_tree(tree_root, title=""):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)
    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}
    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.title(title)
    plt.show()

# Генерація відтінків для кольорів (з темного до світлого)
def generate_gradient_colors(n, base="#1296F0"):
    # Базовий — яскраво-синій; будемо збільшувати яскравість, залишаючи відтінок
    base = base.lstrip("#")
    r, g, b = int(base[0:2], 16), int(base[2:4], 16), int(base[4:6], 16)
    step = int((255 - r) / max(n-1,1))
    colors = []
    for i in range(n):
        new_r = min(r + step * i, 200)
        new_g = min(g + step * i, 200)
        new_b = min(b + step * i, 250)
        colors.append(f"#{new_r:02X}{new_g:02X}{new_b:02X}")
    return colors

# DFS обхід (ітеративний)
def dfs(root):
    order = []
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            order.append(node)
            stack.append(node.right)
            stack.append(node.left)
    return order

# BFS обхід (ітеративний)
def bfs(root):
    order = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            order.append(node)
            queue.append(node.left)
            queue.append(node.right)
    return order

# Приклад використання
def example():
    # Побудова дерева
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)

    # DFS та BFS
    dfs_order = dfs(root)
    bfs_order = bfs(root)
    
    print("DFS порядок обходу:", [node.val for node in dfs_order])
    print("BFS порядок обходу:", [node.val for node in bfs_order])

    # Фарбуємо вузли відповідно до порядку обходу
    for order, mode in zip([dfs_order, bfs_order], ["DFS", "BFS"]):
        colors = generate_gradient_colors(len(order))
        for node, color in zip(order, colors):
            node.color = color
        draw_tree(root, title=f"Обхід {mode} (cтек/черга, унікальне фарбування вузлів)")

if __name__ == "__main__":
    example()
