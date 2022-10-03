"""
Оценить асимптотическую сложность приведенного ниже алгоритма:
"""

a = len(arr) - 1  # 1
out = list()  # 1
while a > 0:  # N
    out.append(arr[a])  # N
    a = a // 1.7  # 1
out.merge_sort()  # 1

# Ответ - O(N)
