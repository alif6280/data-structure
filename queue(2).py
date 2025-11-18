from collections import deque

if __name__ == "__main__":
    q = deque()
    q.append(100)
    q.append(200)
    q.append(300)
    q.append(400)
    q.append(500)
    print("Queue contents:", q)
    print("Front element : ",q[0])
    print("Rear element : ",q[-1])
    print("Is queue empty?", len(q)==0)
    print("Queue size :", len(q))
    print("Front element (peek) :",q[0])
