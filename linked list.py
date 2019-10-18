class node:
    def __init__(self,data):
        self.data = data
        self.nextnode = None

class LinkedList:

    def __init__(self):
        self.head=None
        self.size=0

    def insertion_in_the_beginning(self,data):
        self.size=self.size+1
        newnode=node(data)

        if self.head==None: #it means if the list is empty
            self.head=newnode
        else:
            newnode.nextnode=self.head
            self.head=newnode

    def  insertion_in_the_end(self,data):
        self.size = self.size + 1
        newnode=node(data)

        currentnode=self.head

        while currentnode.nextnode!=None:
            currentnode=currentnode.nextnode

        currentnode.nextnode=newnode

    def remove(self,data):

        if self.head==None:
            return

        self.size = self.size - 1
        currentnode=self.head
        prevnode=None

        while currentnode.data!=data:
            prevnode = currentnode
            currentnode=currentnode.nextnode

        if prevnode==None:
            self.head=currentnode.nextnode

        else:
            prevnode.nextnode=currentnode.nextnode

    def view(self):
        presentnode=self.head
        if self.head==None:
            print('LIST IS EMPTY !!!')
        else:
            while presentnode !=None:
                print(presentnode.data)
                presentnode=presentnode.nextnode

    # complexity O(1)
    def size1(self):
        return self.size

    #complexity O(N)
    def size2(self):
        actualnode=self.head
        s=0
        while actualnode!=None:
            s=s+1
            actualnode=actualnode.nextnode
        return s

    def bubble_sort_exinfo(self):
        end=None

        while end!=self.head.nextnode:
            p=self.head
            while p.nextnode!=end:
                q=p.nextnode
                if p.data > q.data:
                    p.data,q.data=q.data,p.data
                p=p.nextnode
            end=p

    def reverse(self):
        prev=None
        p=self.head
        while p is not None:
            next=p.nextnode
            p.nextnode=prev
            prev=p
            p=next
        self.head=prev

    def has_cycle(self):
        if self.find_cycle==None:
            return False
        else:
            return True

    def find_cycle(self):
        if self.head==None or self.head.nextnode==None:
            return None

        hare_pointer=self.head
        tortoise_pointer=self.head

        while hare_pointer!=None or hare_pointer.nextnode!=None:
            hare_pointer=hare_pointer.nextnode.nextnode
            tortoise_pointer=tortoise_pointer.nextnode
            if hare_pointer==tortoise_pointer:
                return hare_pointer
            return None

    



mylist=LinkedList()



while 1:
    print('MENU \n1. insert in the beginning \n2. insert in the end \n3. remove \n4. view \n5. size \n6. Bubble sort \n7. Reverse \n8. EXIT')
    choice=input()
    if choice=='1':
        print('please enter data to insert in beginning')
        d=input()
        mylist.insertion_in_the_beginning(d)
    elif choice=='2':
        print('please enter data to insert in end')
        d=input()
        mylist.insertion_in_the_end(d)
    elif choice=='3':
        print('please enter data to remove')
        d=input()
        mylist.remove(d)
    elif choice=='4':
        mylist.view()
    elif choice=='5':
        print(mylist.size1())
    elif choice=='6':
        mylist.bubble_sort_exinfo()
        mylist.view()
    elif choice=='7':
        mylist.reverse()
        mylist.view()
    elif choice=='8':
        break