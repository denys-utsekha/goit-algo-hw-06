import networkx as nx
import matplotlib.pyplot as plt
from bfs import bfs
from dfs import dfs
from dijkstra import dijkstra

users_data = {
    "Андрій": {"Богдан": 17, "Вікторія": 3, "Іван": 4},
    "Богдан": {"Галина": 5, "Андрій": 17},
    "Вікторія": {"Галина": 2, "Андрій": 3, "Катерина": 6},
    "Галина": {"Богдан": 5, "Вікторія": 2, "Дмитро": 3, "Лариса": 8},
    "Дмитро": {"Галина": 3, "Євгенія": 2, "Микола": 5, "Ігор": 1},
    "Євгенія": {"Дмитро": 2},
    "Іван": {"Андрій": 4},
    "Катерина": {"Вікторія": 6},
    "Лариса": {"Галина": 8},
    "Микола": {"Дмитро": 5, "Ігор": 1},
    "Ігор": {"Дмитро": 1, "Микола": 1}
}

G = nx.Graph()

for user in users_data.keys():
    G.add_node(user)

for user, connections in users_data.items():
    for connection, weight in connections.items():
        G.add_edge(user, connection, weight=weight)

# Завдання 1
print("Завдання 1")
num_nodes = G.number_of_nodes()
print("Кількість вершин:", num_nodes)
num_edges = G.number_of_edges()
print("Кількість ребер:", num_edges)
avg_degree = sum(dict(G.degree()).values()) / num_nodes
print("Середня ступінь вершин:", avg_degree)
max_degree = max(dict(G.degree()).values())
print("Максимальна ступінь вершин:", max_degree)
degree = [deg for node, deg in G.degree()]
print(f"Ступені вершин - {degree}")

# Завдання 2
print("\n")
print("Завдання 2")
print("Depth-First Search:")
dfs(users_data, "Галина")
print(" ")
print("Breadth-First Search:")
bfs(users_data, "Галина")

# Завдання 3
print(" ")
print("\n")
print("Завдання 3")
shortest_paths = dijkstra(users_data, "Іван")
print("Найкоротші шляхи від вершини Іван до інших вершин:")
for vertex, distance in shortest_paths.items():
    print(f"Шлях до вершини {vertex}: {distance}")

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=500,
        node_color="lightblue", font_size=8, font_weight="bold")
labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Соціальна мережа")
plt.show()
