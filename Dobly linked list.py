class Node:
    def __init__(self,data):
        self.info=data
        self.prev=None
        self.next=None

class dll:
    def __init__(self):
        self.start=None

    def display_list(self):
        if self.start==None:
            print('List is empty !!!')
            return
        print('List is : ')
        p=self.start
        while p is not None:
            print(p.info)
            p=p.next


    def insert_in_beginning(self,data):
        temp=Node(data)
        temp.next=self.start
        self.start.prev=temp
        self.start=temp

    def insert_in_empty_list(self,data):
        temp=Node(data)
        self.start=temp

    def insert_at_end(self,data):
        temp=Node(data)
        p=self.start
        while p.next is not None:
            p=p.next
        p.next=temp
        temp.prev=p

    def create_list(self):
        n=int(input('Enter the number of nodes'))
        if n==0:
            return
        data=input('Enter the first elemnt to be inserted')
        self.insert_in_empty_list(data)
        for i in range(n-1):
            data=print('Enter the next data to insert')
            self.insert_at_end(data)

    def insert_after(self,data,x):
        temp=Node(data)
        p=self.start

        while p is not None:
            if p.info==x:
                break
            p=p.next

        if p is None:
            print(x,' not present in the list')
        else:
            temp.next=p.next
            temp.prev=p
            if p.next is not None:
                p.next.prev=temp
            p.next=temp

    def insert_before(self,data,x):
        if self.start==None:
            print('List is empty')

        if self.start.info==x:
            temp=Node(data)
            p = self.start
            temp.next=p
            p.prev=temp
            self.start=temp
            return

        p=self.start

        while p is not None:
            if p.info==x:
                break
            p=p.next

        if p is None:
            print(x,' not present in the list')
        else:
            temp=Node(data)
            temp.prev=p.prev
            p.prev.next=temp
            temp.next=p
            p.prev=temp

    def delete_first_node(self):
        if self.start==None:
            print('list is empty')
            return
        if self.start.next==None:
            print('list has only one element ')
            self.start=None
            return
        self.start=self.start.next
        self.start.prev=None

    def delete_last_node(self):
        if self.start==None:
            print('list is empty')
            return
        if self.start.next==None:
            print('list has only one element ')
            self.start=None
            return
        p=self.start
        while p.next is not None:
            p=p.next
        p.prev.next=None

    def delete_node(self,x):
        if self.start==None:
            print('list is empty')
            return
        if self.start.next==None:
            print('list has only one element ')
            if self.start.info==x:
                self.start=None
            else:
                print(x,' not found')
            return

        # deletion when element is found at first node
        if self.start.info==x:
            self.start=self.start.next
            self.start.prev=None
            return

        # deletion of in-between node
        p=self.start.next
        while p.next is not None:
            if p.info==x:
                break
            p = p.next

        if p.next!=None:            # deletion of in-between node
            if p.info==x:
                p.prev.next=p.next
                p.next.prev=p.prev

        else:                       # deletion when the element is found at last node
            if p.info==x:
                p.prev.next=None
            else:
                print(x,' not found')



doll=dll()
while 1:
    print('MENU \n1. Display \n2. Insert in empty list \n3. Insert at the beginning \n4. Insert at the end \n5. Insert after a specific node \n6. Insert before a specific node \n7. Delete first node \n8. Delete last node \n9. Delete specific node')
    n=input('Enter your choice : ')
    if n=='1':
        doll.display_list()
    elif n=='2':
        data=input('enter the data')
        doll.insert_in_empty_list(data)
    elif n == '3':
        data = input('enter the data')
        doll.insert_in_beginning(data)
    elif n == '4':
        data = input('enter the data')
        doll.insert_at_end(data)
    elif n == '5':
        data = input('enter the data')
        x=input('after ')
        doll.insert_after(data,x)
    elif n == '6':
        data = input('enter the data')
        x = input('before ')
        doll.insert_before(data,x)
    elif n=='7':
        doll.delete_first_node()
    elif n == '8':
        doll.delete_last_node()
    elif n == '9':
        x=input('enter node to delete')
        doll.delete_node(x)

