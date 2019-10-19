class stack:
    def __init__(self):
        self.stack=[]

    def isEmpty(self):
        return self.stack==[]

    def Push(self,data):
        self.stack.append(data)
        print(self.stack)
        print('Pushed > ',data)


    def Pop(self):
        if len(self.stack)==0:
            print('Stack is Empty !!!')
        else:
            data=self.stack[-1]
            del self.stack[-1]
            print(self.stack)
            print('Popped > ',data)

    def Peek(self):
        return self.stack[-1]

    def size_of_stack(self):
        return len(self.stack)

mystack=stack()

while 1:
    print('MENU \n1. Push \n2. Pop \n3. Peek \n4. Size of stack \n5. Exit')
    choice=input()
    if choice=='1':
        print('please enter data to push ')
        d=input()
        mystack.Push(d)
    elif choice=='2':
        mystack.Pop()
    elif choice=='3':
        print(mystack.Peek())
    elif choice=='4':
        print(mystack.size_of_stack())
    elif choice=='5':
        break
