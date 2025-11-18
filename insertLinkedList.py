class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
def traverseAndPrint(head):
    currentNode = head
    while currentNode:
        print(currentNode.data, end=" -> ")
        currentNode = currentNode.next
    print("null")
    
def insertNodeAtPosition(head,newNode,position):
    if position == 1:
        newNode.next = head
        return newNode
        
    currentNode = head
    for _ in range(position - 2):
        if currentNode is None:
            break
        currentNode = currentNode.next
        
    newNode.next = currentNode.next
    currentNode.next = newNode
    return head

node1 = Node(5)
node2 = Node(10)
node3 = Node(2)
node4 = Node(15)
node5 = Node(3)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("Original List : ")
traverseAndPrint(node1)

newNode = Node(50)
node1 = insertNodeAtPosition(node1,newNode,3)
print("After insertion : ")
traverseAndPrint(node1)
