import random
import timeit

# Функція сортування злиттям (Взяв з конспекту)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи, 
		# додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


# Функція сортування вставками (Взяв з коспекту)
def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key 
    return lst


# Функція для вимірювання часу
def measure_time(sort_function, data):
    setup_code = f'arr = {data}'
    test_code = f'{sort_function.__name__}(arr)'
    return timeit.timeit(test_code, setup=setup_code, globals=globals(), number=100)


sizes = [250, 1000, 12500]
results = {}

for size in sizes:
    data = [random.randint(1, 10000) for _ in range(size)]
    results[size] = {
        'merge_sort': measure_time(merge_sort, data.copy()),
        'insertion_sort': measure_time(insertion_sort, data.copy()),
        'timsort': measure_time(sorted, data.copy())
    }

# Виведення результатів
for size, times in results.items():
    print(f"Size: {size}")
    for sort_name, time in times.items():
        print(f"{sort_name}: {time:.6f} seconds")
    print()
print("Висновок: Алгоритм Timsort працює ефективно,\n"
      "особливо з великими масивами. Він швидко\n"
      "сортує дані, якщо вони вже частково впорядковані.")
