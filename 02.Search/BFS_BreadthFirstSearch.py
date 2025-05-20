"""
About algorithm:
In this file i create Breadth First Search algorithm.
Breadth search
Another way of traversing a graph is traversal in width.
Its main difference is that the adjacent vertices are explored first,
and then the vertices at the next level. In other words, all vertices adjacent
to the initial vertex (the vertex from which the traversal starts)
are explored first. These vertices are at distance 1 from the initial vertex.
Then all vertices at distance 2 from the initial vertex are examined,
then all vertices at distance 3, and so on. Note that for each vertex the
length of the shortest route from the initial vertex is found at once.

Complexity:
Time: O(V+E)
Memory: O(V)
V - vertexes
E - Edges
"""

# use my class Graph on Adjacency List
class Graph:
    def __init__(self, directed=False):
        """
        Класс, представляющий граф, реализованный на основе списка смежности.
        Attributes:
            adjacency_list (dict): Словарь, где ключами являются вершины графа,
                                   а значениями - списки смежных вершин (соседей).
            directed (bool): Флаг, указывающий, является ли граф направленным (True)
                             или ненаправленным (False). По умолчанию - ненаправленный.
        """
    def __init__(self, directed=False):
        """
        Конструктор класса.
        Args:
            directed (bool, optional):  Указывает, является ли граф направленным.
                                         По умолчанию (False) создается ненаправленный граф.
        """
        self.adjacency_list = {}  # Словарь, представляющий список смежности. Ключи - вершины, значения - списки смежных вершин.
        self.directed = directed  # Флаг, указывающий на направленность графа.

    def add_vertex(self, v):
        """
        Добавляет вершину в граф.
        Args:
            v: Вершина, которую нужно добавить.
        """
        if v not in self.adjacency_list:
            self.adjacency_list[v] = []  # Инициализируем пустой список смежности для новой вершины.

    def add_edge(self, v, u):
        """
        Добавляет ребро между вершинами v и u.
        Args:
            v: Начальная вершина ребра.
            u: Конечная вершина ребра.
        """
        self.add_vertex(v)  # Добавляем вершину v, если ее еще нет в графе.
        self.add_vertex(u)  # Добавляем вершину u, если ее еще нет в графе.
        if u not in self.adjacency_list[v]:
            self.adjacency_list[v].append(u)  # Добавляем u в список смежности для v.

        if not self.directed and v not in self.adjacency_list[u]:  # Если граф ненаправленный,
                                                                   # добавляем ребро и в обратном направлении.
            self.adjacency_list[u].append(v)

    def remove_edge(self, v, u):
        """
        Удаляет ребро между вершинами v и u.
        Args:
            v: Начальная вершина ребра.
            u: Конечная вершина ребра.
        """
        if v in self.adjacency_list and u in self.adjacency_list[v]:
            self.adjacency_list[v].remove(u)  # Удаляем u из списка смежности для v.

        if not self.directed and u in self.adjacency_list and v in self.adjacency_list[u]:  # Если граф ненаправленный,
                                                                                          # удаляем ребро и в обратном направлении.
            self.adjacency_list[u].remove(v)

    def find_edge(self, v, u):
        """
        Проверяет, существует ли ребро между вершинами v и u.
        Args:
            v: Начальная вершина ребра.
            u: Конечная вершина ребра.

        Returns:
            bool: True, если ребро существует, False в противном случае.
        """
        return v in self.adjacency_list and u in self.adjacency_list[v]  # Проверяем, что v есть в графе и u есть в списке смежности для v.

    def get_neighbors(self, v):
        """
        Возвращает список соседей вершины v.
        Args:
            v: Вершина, для которой нужно получить соседей.

        Returns:
            list: Список соседей вершины v. Возвращает пустой список, если вершина не найдена.
        """
        return self.adjacency_list.get(v, [])  # Возвращает список соседей вершины v или пустой список, если вершины нет.

    def __str__(self):
        """
        Возвращает строковое представление графа.
        Returns:
            str: Строка, представляющая граф в формате: "вершина: [соседи]".
        """
        return "\n".join(f"{v}: {sorted(neighbors)}" for v, neighbors in sorted(self.adjacency_list.items()))  # Формирует строку, представляющую граф.  Сортировка для предсказуемого вывода.

# Creation Graph
g = Graph(directed=False)

# add vertexes
for v in range(8):
    g.add_vertex(v)

# add edges
edges = [
    (0, 4),
    (1, 4), (1, 2),
    (2, 5),
    (4, 5), (4, 6),
    (5, 7),
    (6, 7)
]

for v, u in edges:
    g.add_edge(v, u)

from collections import deque

def bfs(graph, start):
    """
    Performs a Breadth-First Search (BFS) on a graph, starting from a given vertex.

    Args:
        graph (Graph): A graph object, assumed to have a method 'get_neighbors' to retrieve neighbors.
        start: The vertex from which to begin the BFS traversal.

    Returns:
        list: A list of vertices in the order they were visited during the BFS.
    """
    # Initialize a set to keep track of visited vertices.  This prevents cycles and redundant processing.
    visited = set()
    # Initialize a queue (using `deque` for efficient append/popleft operations) for BFS traversal.
    queue = deque()
    # Initialize a list to store the order in which vertices are visited.  This will be the function's result.
    order = []

    # Mark the starting vertex as visited.
    visited.add(start)
    # Enqueue the starting vertex to begin the search.  It's the first vertex to be explored.
    queue.append(start)

    # While the queue is not empty (meaning there are still vertices to explore)...
    while queue:
        # Dequeue a vertex from the *front* of the queue.  BFS explores level by level.
        v = queue.popleft()
        # Add the dequeued vertex to the 'order' list (the result).  This is the current vertex being processed.
        order.append(v)
        # Iterate through the neighbors of the current vertex 'v'.
        for neighbor in graph.get_neighbors(v):
            # If a neighbor hasn't been visited yet...
            if neighbor not in visited:
                # Mark the neighbor as visited.
                visited.add(neighbor)
                # Enqueue the neighbor to be processed later. It will be explored in the next level.
                queue.append(neighbor)

    # Return the list of vertices in the order they were visited.
    return order

result = bfs(g, 0)

print(g)
print("BFS:", result)


"""
0: [4]
1: [2, 4]
2: [1, 5]
3: []
4: [0, 1, 5, 6]
5: [2, 4, 7]
6: [4, 7]
7: [5, 6]
BFS: [0, 4, 1, 5, 6, 2, 7]
"""