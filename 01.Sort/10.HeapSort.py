"""
На данный момент идеально я данную сортировку не понял, работаю над этим.

Пока что я понял, что она работает:
- с построением и использованием деревьев
- по типу сортировки выбором "выталкивает" наибольший элемент
- неустойчивая (элементы с одинаковым значением могут поменяться местами)
- так же может быть реализована с помощью списков
- Асимптотика O(NlogN)

Глобально алгоритм состоит из двух этапов:
    1. Построение max-heap(максимальной кучи)
    2. Поочередное извлечение максимального элемента и восстановление кучи
"""

def heapify(arr, n, i):
    largest = i # Инициализируем наибольший элемент как корень
    left = 2 * i + 1 # Левый потомок
    right = 2 * i + 2 # Правый потомок

    # Проверяем, существует ли левый дочерний элемент и больше ли он, чем корень
    if left < n and arr[left] > arr[largest]:
        largest = left

    #  Проверяем, существует ли правый дочерний элемент
    #  и больше ли он, чем текущий наибольший элемент
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Если наибольший элемента не корень, меняем местами и продолжаем heapify
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i] # Обмен
        heapify(arr, n , largest) # Рекурсивный вызов heapify

def heap_sort(arr):
    n = len(arr)

    # построение max-heap
    # Начинаем с середины, двигаясь к началу массива
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    # Один за другим извлекаем элементы из кучи
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] # меняем корень с последним элементом
        heapify(arr, i,0) # Восстанавливаем max-heap для оставшейся части

# Пример использования:
arr = [12, 11, 13, 5, 6, 7]
heap_sort(arr)
print("Отсортированный массив:", arr)