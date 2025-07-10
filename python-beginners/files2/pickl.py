class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
node1=Node(60)
node2=Node(70)
node3=Node(80)
node1.next=node2
node2.next=node3
node3.next=node1
current=node1
while True:
    print(current.data)
    current=current.next
    if current==node1:
        break







