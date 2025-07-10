class Node:
    def __init__(self, data):
        self.data=data
        self.children=[]
root=Node(2)
child1=Node(3)
child2=Node(4)
root.children.append(child1)
root.children.append(child2)
for childs in root.children:
    print(childs.data)
