#############################################Creating a class node########################################
class Node:
    def __init__(self,data):
        self.data=data
        self.nextnode=None

######################################Creating the class Sorted_Linked_List##########################################
class Sorted_Linked_List:
    def __init__(self):
        self.start=None

#######################################inserting using inorder traversal method #####################################3
    def insert_in_order(self,x):
        #this is the case when the list is empty or the data to be inserted is less than the first node data
        temp=Node(x)
        if self.start==None or self.start.data>x:
            temp.nextnode=self.start
            self.start=temp
            return

        p=self.start
        while p.nextnode!=None and p.nextnode.data<=x:
            p=p.nextnode
        temp.nextnode=p.nextnode    #these conditions can work for both insertion in last and simple adding case
        p.nextnode=temp
        
################################here we are finally creating the list to sort#############################################
    def create_list(self):
        n=int(input('enter the number of nodes '))
        if n==0:
            return

        for i in range(n):
            data=input('enter the element to be inserted : ')
            self.insert_in_order(data)
            
############################################search operation in list#######################################################
    def search(self,x):
        if self.start==None:
            print('list is empty')
            return

        p=self.start
        position=1

        while p is not None and p.data<=x:
            if p.data==x:
                break
            p=p.nextnode
            position=position+1

        if p is None or p.data!=x:
            print(x,' not found')
        else:
            print(x,' found at position ',position)
####################################### display the list #######################################################3
    def display_list(self):
        if self.start==None:
            print('list is empty')
            return
        p=self.start
        while p is not None:
            print(p.data)
            p=p.nextnode

srt=Sorted_Linked_List()
srt.create_list()

while True:
    print('MENU \n1.Display \n2.Search \n3.Insert \n4. EXIT')
    choice=input('enter your choice : ')
    if choice=='1':
        srt.display_list()
    elif choice=='2':
        x=input('enter the element you want to search : ')
        srt.search(x)
    elif choice=='3':
        d=input('enter data to insert : ')
        srt.insert_in_order(d)
    else:
        break
