"""
About algorithm:
In this file i create Depth First Search algorithm.
Depth search
Depth-first traversal consists of systematically looking at the vertices
of a graph and traversing it by branches.
In other words, the idea of depth-first search is that when the possible
paths along the edges coming out of the vertices are branched,
one should first fully explore one branch and only then move on to other
branches (if they remain unexplored).

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



# recursive approach
def dfs_recursive(graph_obj, v, used=None, result=None):
    """
    Performs a Depth-First Search (DFS) on a graph, starting from vertex 'v'.  This is the recursive implementation.

    Args:
        graph_obj (Graph):  A graph object, which should have methods like 'get_neighbors' and an 'adjacency_list' attribute.
        v (int): The starting vertex for the DFS traversal.
        used (dict, optional): A dictionary to keep track of visited vertices.  Defaults to None, and is initialized if not provided.
                               Keys are vertices, and values are booleans (True if visited, False if not).
        result (list, optional): A list to store the order in which vertices are visited. Defaults to None, and is initialized if not provided.

    Returns:
        list: A list containing the vertices in the order they were visited during the DFS.
    """
    # Initialize the 'used' dictionary if it's the first call
    if used is None:
        used = {vertex: False for vertex in graph_obj.adjacency_list}
    # Initialize the 'result' list if it's the first call
    if result is None:
        result = []

    # Mark the current vertex as visited
    used[v] = True
    # Add the current vertex to the result list
    result.append(v)

    # Iterate through the neighbors of the current vertex
    for u in graph_obj.get_neighbors(v):
        # If a neighbor hasn't been visited yet, recursively call DFS on it
        if not used[u]:
            dfs_recursive(graph_obj, u, used, result)

    # Return the list of visited vertices in order
    return result

# iterative approach
def dfs_iterative(graph, start):
    """
    Performs a Depth-First Search (DFS) on a graph using an iterative (non-recursive) approach.

    Args:
        graph (Graph): A graph object.  Assumed to have a method like 'get_neighbors'.
        start: The vertex to start the DFS from.

    Returns:
        list:  A list containing the vertices in the order they were visited.
    """
    # Initialize a set to track visited vertices
    visited = set()
    # Initialize a stack to simulate the call stack in a recursive DFS.  Starts with the 'start' vertex.
    stack = [start]
    # Initialize a list to store the DFS result
    result = []

    # Mark the starting vertex as visited
    visited.add(start)

    # Continue while there are vertices on the stack (i.e., still vertices to explore)
    while stack:
        # Pop a vertex from the stack (LIFO - Last In, First Out)
        v = stack.pop()
        # Add the popped vertex to the result
        result.append(v)
        # Iterate through the neighbors of the current vertex, in *reverse* order.
        # This is done to make the iterative version's order of visiting nodes
        # match the recursive version more closely.  This ensures the same ordering if a tie exists.
        for neighbor in reversed(graph.get_neighbors(v)):
            # If a neighbor hasn't been visited...
            if neighbor not in visited:
                # Mark it as visited
                visited.add(neighbor)
                # Push the neighbor onto the stack to be explored later
                stack.append(neighbor)

    # Return the list of visited vertices
    return result


result_recursive = dfs_recursive(g, 0)
result_iterative = dfs_iterative(g, 0)
print(g)
print("DFS обход с рекурсией:", result_recursive)
print("DFS обход без рекурсии:", result_iterative)

"""
0: [4]
1: [2, 4]
2: [1, 5]
3: []
4: [0, 1, 5, 6]
5: [2, 4, 7]
6: [4, 7]
7: [5, 6]
DFS обход с рекурсией: [0, 4, 1, 2, 5, 7, 6]
DFS обход без рекурсии: [0, 4, 1, 2, 5, 7, 6]
"""