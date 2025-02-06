"""
Экспоненциальный поиск - улучшенная версия бинарного поиска. В худшем случае работает за O(logn).

Суть заключатеся в следующем:
- Ищем границы диапазона в котором заключен таргет;
- Включаем бинарный поиск для поиска таргета в новых границах, которые могут быть существенно
меньше, чем для изначального массива.

Например, у нас есть массив из миллиарда объектов, а сам элемент находится ближе к началу,
скажем в первом миллионе. То мы очень быстро сможем определить границы, в которых элемент
находится. Соответственно, нам не нужно будет итерироваться бинарным поиском по массиву из
миллиарда объектов, достаточно проверить массив, содержащий меньше миллиона объектов.

Важно помнить:
- Если массив очень большой и часто ищутся элементы ближе к началу.
- В случаях, когда доступ к элементам ограничен** (например, поток данных, связные списки).
- В комбинации с бинарным поиском для ускорения поиска.
- Неэффективен для неотсортированных массивов (требует предварительной сортировки).
"""

def BinarySearch(arr, left, right, target):
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

def ExpSearch(arr, target):
    if arr[0] == target:
        return 0
    n = len(arr)
    # задаем начальное значение границ
    left = 0
    right = 1

    # увеличиваем значение границы экспоненциально
    while right < n and arr[right] < target:
        right *= 2 # увеличиваем правую границу, расширяя диапазон
        left = right // 2  # "подтягиваем" левую границу до правой

    # окончательно определяем правую границу (на случай, если она вышла за исходный массив)
    right = min(n-1, right)

    # применяем бинарный поиск, к диапазону массива
    return BinarySearch(arr, left, right, target)

# 📌 Пример использования:
arr = [1, 3, 5, 7, 9, 11, 15, 19, 23, 27, 31]
target = 15
index = ExpSearch(arr, target)

print(f"Элемент {target} найден на позиции {index}" if index != -1 else "Элемент не найден")

"""
>>> Элемент 15 найден на позиции 6
"""