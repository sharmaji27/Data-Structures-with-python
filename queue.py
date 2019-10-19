class queue:
    def __init__(self):
        self.queue=[]

    def isEmpty(self):
        return self.queue==[]

    def Enqueue(self,data):
        self.queue.append(data)
        print(self.queue)
        print('Enqueued > ',data)


    def Dequeue(self):
        if len(self.queue)==0:
            print('Queue is Empty !!!')
        else:
            data=self.queue[0]
            del self.queue[0]
            print(self.queue)
            print('Dequeued > ',data)

    def Peek(self):
        return self.queue[0]

    def size_of_queue(self):
        return len(self.queue)

myqueue=queue()

while 1:
    print('MENU \n1. Enqueue \n2. Dequeue \n3. Peek \n4. Size of queue \n5. Exit')
    choice=input()
    if choice=='1':
        print('please enter data to enqueue ')
        d=input()
        myqueue.Enqueue(d)
    elif choice=='2':
        myqueue.Dequeue()
    elif choice=='3':
        print(myqueue.Peek())
    elif choice=='4':
        print(myqueue.size_of_queue())
    elif choice=='5':
        break