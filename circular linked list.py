class Node:
    def __init__(self,data):
        self.data=data
        self.nextnode=None

class CLL:
    def __init__(self):
        self.last=None

    def display(self):
        if self.last==None:
            print('list is empty')
            return

        p=self.last.nextnode

        while True:
            print(p.data)
            p=p.nextnode
            if p==self.last.nextnode:
                break

    def insert_in_the_beginning(self,data):
        temp=Node(data)
        temp.nextnode=self.last.nextnode
        self.last.nextnode=temp

    def insert_in_empty_list(self,data):
        temp=Node(data)
        self.last=temp
        self.last.nextnode=self.last

    def insert_in_the_end(self,data):
        temp=Node(data)
        temp.nextnode=self.last.nextnode
        self.last.nextnode=temp
        self.last=temp

    def insert_after(self,data,x):
        p=self.last.nextnode
        while True:
            if p.data==x:
                break
            p=p.nextnode
            if p==self.last.nextnode:
                break
        if p==self.last.nextnode and p.data!=x:
            print(x,' not found')
        else:
            temp=Node(data)
            temp.nextnode=p.nextnode
            p.nextnode=temp
            if p==self.last:
                self.last=temp

    def delete_first_node(self):
        if self.last==None:                 #for empty list
            print('list is empty')
            return

        if self.last.nextnode==self.last:   #for the case when there is only one node in the list
            self.last=None
            return

        self.last.nextnode=self.last.nextnode.nextnode

    def delete_one_node_list(self):
        if self.last==None:
            print('list is empty')
            return

        self.last=None

    def delete_last_node(self):
        if self.last==None:                 #for empty list
            print('list is empty')
            return

        if self.last.nextnode==self.last:   #for the case when there is only one node in the list
            self.last=None
            return

        p=self.last.nextnode

        while p.nextnode!=self.last:
            p=p.nextnode

        p.nextnode=self.last.nextnode
        self.last=p

    def delete_node(self,x):
        if self.last==None:                 #for empty list
            print('list is empty')
            return

        if self.last.nextnode==self.last:   #for the case when there is only one node in the list
            if self.last.data==x:
                self.last=None
            return

        if self.last.nextnode.data==x:      # for deleting first element from the list
            self.last.nextnode = self.last.nextnode.nextnode

        p=self.last.nextnode

        while p.nextnode!=self.last.nextnode:
            if p.nextnode.data==x:
                break
            p=p.nextnode


        if p.nextnode==self.last.nextnode:
            print(x,' not found in list')
        elif p.nextnode == self.last:
            p.nextnode = self.last.nextnode
            self.last = p
        else:
            p.nextnode = p.nextnode.nextnode

my_circular_list=CLL()

while True:
    print('MENU \n1. Display \n2. Insert in empty list \n3. Insert a node in the beginning \n4. Insert a node at the end \n5. Delete first node \n6. Delete last node \n7. Delete any node \n8. Insert After \n9. Quit ')
    choice=input('enter your choice')

    if choice=='1':
        my_circular_list.display()
    elif choice=='2':
        data=input('enter data ')
        my_circular_list.insert_in_empty_list(data)
    elif choice == '3':
        data=input('enter data ')
        my_circular_list.insert_in_the_beginning(data)
    elif choice == '4':
        data=input('enter data ')
        my_circular_list.insert_in_the_end(data)
    elif choice == '5':
        my_circular_list.delete_first_node()
    elif choice == '6':
        my_circular_list.delete_last_node()
    elif choice == '7':
        x=input('node you want to delete ')
        my_circular_list.delete_node(x)
    elif choice == '8':
        data=input('enter data ')
        x=input('enter the element after which u want to insert ')
        my_circular_list.insert_after(data,x)
    elif choice=='9':
        break








