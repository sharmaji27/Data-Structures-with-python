class Heap:
    heap_size = 10

    def __init__(self):
        self.heap = [0] * Heap.heap_size
        self.current_position = -1

    def insert(self, data):
        if self.isfull():
            print('heap is full')
            return

        self.current_position = self.current_position + 1
        self.heap[self.current_position] = data
        self.fixup(self.current_position)


    def delete_root(self):
        if self.current_position==-1:
            print('heap is empty !!!')
            return

        max_value=self.heap[0]
        self.heap[0]=self.heap[self.current_position]
        self.current_position=self.current_position-1
        self.fixdown(0,self.current_position)
        return max_value

    def isfull(self):
        return self.current_position == self.heap_size

    def fixup(self, index):
        parent_index = int((index - 1) / 2)

        while parent_index >= 0 and self.heap[parent_index] < self.heap[index]:
            temp = self.heap[parent_index]
            self.heap[parent_index] = self.heap[index]
            self.heap[index] = temp

            parent_index = int((index - 1) / 2)

    def heapsort(self):
        for i in range(0, self.current_position + 1):
            temp = self.heap[0]
            print(temp)
            self.heap[0] = self.heap[self.current_position - i]
            self.heap[self.current_position - i] = temp
            self.fixdown(0, self.current_position - i - 1)

    def fixdown(self, start_ind, end_ind):

        while start_ind <= end_ind:
            left_child = 2 * start_ind + 1
            right_child = 2 * start_ind + 2

            if left_child < end_ind:
                childtoswap = None
                if right_child > end_ind:
                    childtoswap = left_child
                else:
                    if self.heap[left_child] > self.heap[right_child]:
                        childtoswap = left_child
                    else:
                        childtoswap = right_child

                if self.heap[start_ind] < self.heap[childtoswap]:
                    temp = self.heap[start_ind]
                    self.heap[start_ind] = self.heap[childtoswap]
                    self.heap[childtoswap] = temp
                else:
                    break
                start_ind = childtoswap
            else:
                break


myheap = Heap()
myheap.insert(10)
myheap.insert(-20)
myheap.insert(0)
myheap.insert(2)

myheap.heapsort()
