class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def traverseAndPrint(head):
    while head:
        print(head.data,end=" -> ")
        head=head.next
    print("NULL")
    
def insertNode(head, newNode, pos):
    if pos == 1:
        newNode.next = head
        return newNode

    temp = head
    for _ in range(pos - 2):
        temp = temp.next

    newNode.next = temp.next
    temp.next = newNode
    return head
    
def deleteAtPosition(head, pos):
    temp = head
    if pos == 1:
        return head.next

    for _ in range(pos - 2):
        temp = temp.next

    temp.next = temp.next.next
    return head
    
def countNodes(head):
    count = 0
    while head:
        count += 1
        head = head.next
    return count
    
def updateNode(head, pos, newValue):
    temp = head
    for _ in range(pos - 1):
        temp = temp.next
    temp.data = newValue
    return head

node1=Node(5)
node2=Node(10)
node3=Node(15)
node4=Node(20)
node5=Node(25)

node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5

print("Travers List : ")
traverseAndPrint(node1)

node1 = insertNode(node1, Node(99), 3)
print("After Inserting 99 at position 3:")
traverseAndPrint(node1)

node1 = deleteAtPosition(node1, 3)
print("Deleting node at position 3:")
traverseAndPrint(node1)

node1 = updateNode(node1, 2, 777)
print("Updating position 2 to 777:")
traverseAndPrint(node1)

print("Total Nodes =", countNodes(node1))
