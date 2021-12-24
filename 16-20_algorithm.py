# 选择排序
def select_sort(items, comp=lambda x,y: x<y):
    items = items[:]
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i + 1, len(items)):
            if comp(items[j], items[min_index]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
    return items
# print(select_sort([1,23,4,6,3,4523]))

# 冒泡排序
def bubble_sort(items, comp=lambda x,y: x>y):
    items = items[:]
    for i in range(len(items) - 1):
        swapped = False
        for j in range(len(items) - 1 - i):
            if comp(items[j], items[j + 1]):
                items[j], items[j+1] = items[j+1], items[j]
                swapped = True
        if not swapped:
            break
    return items
# print(bubble_sort([1,23,4,6,3,4523]))

# 搅拌排序（冒泡排序升级版）
def bubble_sort(items, comp=lambda x,y: x>y):
    items = items[:]
    for i in range(len(items) - 1):
        swapped = False
        for j in range(len(items) - 1):
            if comp(items[j], items[j+1]):
                items[j], items[j+1] = items[j+1], items[j]
                swapped = True
        if swapped:
            swapped = False
            for j in range(len(items) - 2 - i,i,-1):
                if comp(items[j-1], items[j]):
                    items[j], items[j-1] = items[j-1], items[j]
                    swapped = True
        if not swapped:
            break
    return items
# print(bubble_sort([1,23,4,6,3,4523]))

# 归并排序
## 归并
def merge(items1, items2, comp=lambda x,y: x<y):
    items = []
    index1, index2 = 0, 0
    while index1 < len(items1) and index2 < len(items2):
        if comp(items1[index1], items2[index2]):
            items.append(items1[index1])
            index1 += 1
        else:
            items.append(items2[index2])
            index2 += 1
    items += items1[index1:]
    items += items2[index2:]
    return items

## 归并排序
def merge_sort(items, comp=lambda x,y: x<y):
    return _merge_sort(list(items), comp)

def _merge_sort(items, comp):
    if len(items) < 2:
        return items
    mid = len(items) // 2
    left = _merge_sort(items[:mid], comp)
    right = _merge_sort(items[mid:], comp)
    return merge(left, right, comp)
# print(merge_sort([1,23,4,6,3,4523]))

# 顺序查找
def seq_search(items, key):
    for index, item in enumerate(items):
        if item == key:
            return index
    return -1
# print(seq_search([1,23,4,6,3,4523], 6))

def bin_search(items, key):
    start, end = 0, len(items)-1
    while start <= end:
        mid = (start + end) // 2
        if key > items[mid]:
            start = mid + 1
        elif key < items[mid]:
            end = mid - 1
        else:
            return mid
    return -1
# print(seq_search(bubble_sort([1,23,4,6,3,4523]), 3))

# 背包问题--贪心算法
class Things_item(object):

    def __init__(self, name, value, weight):
        self.name = name
        self.value = value
        self.weight = weight
    
    def __getattr__(self, name):
        return (self.value, self.weight)
    
    def value_rate(self):
        return self.value/self.weight

def bag_max_value(capacity):
    L = [Things_item('computer', 200, 20), Things_item('radio', 20, 4), Things_item('clock', 175, 10), Things_item('bottle', 50, 2), Things_item('book', 10, 1), Things_item('paint', 90, 9)]
    L.sort(key=lambda x: x.value_rate(), reverse=True)
    total_weight = 0
    total_value = 0
    for thing in L:
        if total_weight + thing.weight <= capacity:
            print('take away: %s' % thing.name)
            total_weight += thing.weight
            total_value += thing.value
    print('total_value : %s' % total_value)
# bag_max_value(20)

# 快速排序
def quick_sort(items, comp=lambda x,y: x<=y):
    items = list(items)[:]
    _quick_sort(items, 0, len(items)-1, comp)
    return items

def _quick_sort(items, start, end, comp):
    if start < end:
        pos = _partition(items, start, end, comp)
        _quick_sort(items, start, pos-1, comp)
        _quick_sort(items, pos+1, end, comp)

def _partition(items,start, end, comp):
    pivot = items[end]
    i = start - 1
    for j in range(start,end):
        if comp(items[j], pivot):
            i += 1
            items[i], items[j] = items[j], items[i]
    items[i+1], items[end] = items[end], items[i+1]
    return i+1

# print(quick_sort([1,23,4,6,3,4523]))

# 字列表元素之和的最大值
# def max_sub_list(L):
#     l = len(L)
#     return _max_sub_list(L, 0, l-1, l)

# def _max_sub_list(L, a, b, l):
#     if a>=l or b>=l or a>b:
#         return 0
#     elif a == 0 and b == 0:
#         return L[0]
#     elif a == l-1 and b == l-1:
#         return L[l-1]
#     else:
#         result = max(_max_sub_list(L, a+1, b, l) + L[a], _max_sub_list(L, a, b-1, l) + L[b], L[a], L[b], _max_sub_list(L, a+1, b, l), _max_sub_list(L, a, b-1, l))
#         return result
# L = [1,-2,3,5,-3,2]
# print(max_sub_list(L))
def max_sub_list(L):
    overall = partial = L[0]
    for i in range(1,len(L)):
        partial = max(L[i], partial+L[i])
        overall = max(partial, overall)
    print(overall)
L = [1,-2,3,5,-3,2]
print(max_sub_list(L))