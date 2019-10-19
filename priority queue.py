class Node:
    def __init__(self, data, pr):
        self.data = data
        self.priority = pr
        self.nextnode = None


class Priority_Q:
    def __init__(self):
        self.head = None

    def enqueue(self, x, priority):
        temp = Node(x, priority)
        if self.head is None or priority < self.head.priority:
            temp.nextnode = self.head
            self.head = temp
        else:
            p = self.head
            while p.nextnode != None and p.nextnode.priority <= priority :  # p.nextnode is not None this condition will stop the pointer at last and enqueue in last
                p = p.nextnode
            temp.nextnode = p.nextnode
            p.nextnode = temp

    def dequeue(self):
        if self.head is None:
            print('Queue is empty !!')
            return

        x = self.head.data
        self.head = self.head.nextnode
        return x

    def display(self):
        if self.head is None:
            print('Queue is empty !!')
            return
        p = self.head
        print('Queue is ')
        while p is not None:
            print(p.data, ' ', p.priority)
            p = p.nextnode

    def size(self):
        s = 0
        p = self.head
        while p is not None:
            s = s + 1
            p = p.nextnode
        return s


pq = Priority_Q()

while 1:
    print('MENU \n1. Display \n2. Enqueue \n3. Dequeue \n4. Size \n5. Exit')
    n = input('Enter your choice : ')
    if n == '1':
        pq.display()
    elif n == '2':
        data = input('enter the data ')
        prio = input('enter the data priority ')
        pq.enqueue(data, prio)
    elif n == '3':
        print('dequeued element is ',pq.dequeue())
    elif n == '4':
        print(pq.size())
    else:
        break
