class LinkedList:
    def __init__(self, nodes=None):
        self.head = None

        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            
            for node_data in nodes:
                node.next = Node(data=node_data)
                node = node.next
                
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
    
    def __repr__(self):
        node = self.head
        nodes = []
        
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        
        return " -> ".join(nodes)
        
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
    def __repr__(self):
        return self.data
    
    def __str__(self):
        return str(self.data)
    
def main():
    llist = LinkedList()
    
    print(llist)
    
    first_node = Node("a")
    llist.head = first_node
    
    sec_node = Node(1)
    first_node.next = sec_node
    
    print(llist)
    
    llist2 = LinkedList([1, 2, 3, 4, 5,10])
    print(llist2)
    
if __name__ == "__main__":
    main()