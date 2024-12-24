"""
Теория

"""

import random
MyList = [random.randint(-20,20) for i in range(20)]
print(f'Рандомный список до сортировки: {MyList}')

def MySelectionSort(arr: list):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i]:
                arr[j], arr[i] = arr[i], arr[j]
    return arr

print(f'Отсортированный список: {MySelectionSort(MyList)}')

"""
Рандомный список до сортировки: [12, 13, 0, 16, 0, -15, -14, -5, 20, -16, -20, 11, -15, -4, -7, 5, 15, 7, 1, -13]
Отсортированный список: [-20, -16, -15, -15, -14, -13, -7, -5, -4, 0, 0, 1, 5, 7, 11, 12, 13, 15, 16, 20]
"""