class Node:
    def __init__(self, given):
        self.given=given
        self.next=None
node0=Node(1)
node1=Node(2)
node2=Node(3)
node3=Node(4)

node0.next=node1
node1.next=node2
node2.next=node3
now=node0
while now:
    print(now.given)
    now=now.next
