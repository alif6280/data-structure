class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def traverseAndPrint(head):
    while head:
        print(head.data,end=" -> ")
        head=head.next
    print("NULL")

def insertNode(head,newNode,pos):
    if pos==1:
        newNode.next=head
        return newNode
    
    temp=head
    for _ in range(pos-2):
        temp=temp.next
    newNode.next=temp.next
    temp.next=newNode
    return head    

def deleteNode(head,target):
    if head==target:
        return head.next
    prev=head
    while prev.next!=target and prev.next is not None:
        prev=prev.next

    if prev.next==target:
        prev.next=target.next

    return head

node1=Node(10)
node2=Node(20)
node3=Node(30)
node4=Node(40)
node5=Node(50)

node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5


while True:
    print("\nMENU")
    print("1. Traverse List")
    print("2. Insert Node")
    print("3. Delete Node")
    print("4. Exit")

    choice=int(input("Enter Your Choice : "))

    if choice==1:
        traverseAndPrint(node1)

    elif choice==2:
        value=int(input("Enter the value to insert : "))
        loc=int(input("Enter the postion to insert : "))
        newNode=Node(value)
        node1=insertNode(node1,newNode,loc)
        print("Node inserted...........!")
        traverseAndPrint(node1)

    elif choice==3:
        pos=int(input("Enter postion to delete node : "))
        temp = node1
        for _ in range(pos-1):
            prev = temp
            temp = temp.next
        
        target = temp
        node1=deleteNode(node1,target)
        print("Node deleted......!")
        traverseAndPrint(node1)
    elif choice==4:
        print("Exiting......! Good Bye!")
        break
    
    else:
        print("Invalid Choice... Please try again!")
