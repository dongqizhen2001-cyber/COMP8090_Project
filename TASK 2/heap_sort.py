# Task 2: Self-study Heap Sort
# 堆排序完整实现 (Heap Sort Implementation)

def heapify(arr, n, i):
    """
    维护最大堆的性质 (Maintain max heap property)
    """
    largest = i        # 初始化最大元素为父节点
    left = 2 * i + 1   # 左子节点的索引
    right = 2 * i + 2  # 右子节点的索引

    # 如果左子节点存在，且大于当前最大元素
    if left < n and arr[left] > arr[largest]:
        largest = left

    # 如果右子节点存在，且大于当前最大元素
    if right < n and arr[right] > arr[largest]:
        largest = right

    # 如果最大元素不是父节点，说明需要交换
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i] # 交换位置
        # 递归地对受影响的子树进行堆化
        heapify(arr, n, largest)

def heap_sort(arr):
    """
    堆排序主函数 (Main function for Heap Sort)
    """
    n = len(arr)

    # 1. 构建最大堆 (Build a maxheap)
    # 从最后一个非叶子节点开始，倒序遍历进行堆化
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # 2. 一个个提取元素 (Extract elements one by one)
    for i in range(n - 1, 0, -1):
        # 将当前最大的元素（根节点）移到数组末尾
        arr[i], arr[0] = arr[0], arr[i]
        # 对剩下的元素重新进行堆化（排除已经排好序的最后一个元素）
        heapify(arr, i, 0)
        
    return arr

# 测试代码
if __name__ == "__main__":
    data = [10, 5, 3, 17, 1, 25, 8]
    print(f"Original array: {data}")
    heap_sort(data)
    print(f"Sorted array:   {data}")
