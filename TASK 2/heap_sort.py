# Task 2: Advanced Heap Data Structure & Heap Sort Application
# 包含了堆数据结构 (Heap Data Structure) 和 堆排序算法 (Heap Sort) 的实际应用案例

# 1. 定义一个实际的应用对象：打印任务
class PrintJob:
    def __init__(self, job_name, priority):
        self.job_name = job_name
        self.priority = priority # 优先级数字越大，越先处理

    def __repr__(self):
        return f"[{self.priority}] {self.job_name}"

# 2. 实现核心数据结构：最大堆 (Max Heap)
class MaxHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i): return (i - 1) // 2
    def left_child(self, i): return 2 * i + 1
    def right_child(self, i): return 2 * i + 2

    # 插入新任务 (对应堆化上浮)
    def insert(self, job):
        self.heap.append(job)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, i):
        while i > 0 and self.heap[self.parent(i)].priority < self.heap[i].priority:
            # 如果父节点的优先级小于当前节点，交换它们
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    # 提取最高优先级任务 (对应堆排序的核心逻辑和下沉)
    def extract_max(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop() # 将末尾元素移到根节点
        self._heapify_down(0)
        return root

    def _heapify_down(self, i):
        largest = i
        left = self.left_child(i)
        right = self.right_child(i)
        n = len(self.heap)

        if left < n and self.heap[left].priority > self.heap[largest].priority:
            largest = left
        if right < n and self.heap[right].priority > self.heap[largest].priority:
            largest = right

        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self._heapify_down(largest)

# 3. 实际应用案例 (Application Example)
def main():
    print("=== IT Department Print Queue System ===")
    printer_queue = MaxHeap()
    
    # 模拟接收各种不同优先级的打印任务
    incoming_jobs = [
        PrintJob("Intern_Report.pdf", 2),
        PrintJob("CEO_Quarterly_Speech.docx", 10),  # 最高优先级
        PrintJob("Daily_Log.txt", 1),
        PrintJob("Financial_Data_Q1.xlsx", 8)
    ]
    
    print("\n--- 1. Receiving Jobs (Building Max Heap) ---")
    for job in incoming_jobs:
        printer_queue.insert(job)
        print(f"Added to queue: {job}")
        
    print("\n--- 2. Processing Jobs (Heap Sort Extraction) ---")
    # 利用堆排序的逻辑，依次处理最高优先级的任务
    while len(printer_queue.heap) > 0:
        current_job = printer_queue.extract_max()
        print(f"Printing... {current_job}")

if __name__ == "__main__":
    main()
