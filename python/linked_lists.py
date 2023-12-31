class LinkedList:
    def __init__(self, nodes=None):
        self.head = None

        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            
            for node_data in nodes:
                node.next = Node(data=node_data)
                node = node.next
                
    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        
        for current_node in self:
            pass
        
        current_node.next = Node(data)

        return current_node.next     
    
    def add_first(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
        
        return node
        
    def add_last(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        
        for current_node in self:
            pass
        
        current_node.next = Node(data)
        
        return current_node.next
        
    def add_after(self, target_node_data, data):
        nodes = self.find_node(target_node_data)
        
        new_node = Node(data)
        
        next_node = nodes['node'].next
        new_node.next = next_node
        nodes['node'].next = new_node
        
        return new_node
    
    def add_before(self, target_node_data, data):
        nodes = self.find_node(target_node_data)

        new_node = Node(data)
        new_node.next = nodes['node']
        nodes['previousNode'].next = new_node
        
        return new_node

    def remove(self, target_node_data):
        nodes = self.find_node(target_node_data)
        
        node = nodes['node']
        previous_node = nodes['previousNode']
                
        if previous_node is None:
            self.head = node.next
            node.next = None
            
        elif node.next is None:
            previous_node.next = None
        
        else:
            previous_node.next = node.next
            node.next = None
                
        return node
            
                
    def pops(self):
        if self.head is None:
            raise Exception("Cannot remove element from empty list.")
        
        current_head = self.head
        last_node = None
        
        node = current_head
        while node.next is not None:
            last_node = node
            node = node.next
        
        last_node.next = None
        
        return node

    def find_node(self, target_node_data):
        #TODO transform return dictionary in Object
        if self.head is None:
            raise Exception('Cannot find element because the list is empty.')

        index = 0
        previous_node = None
        for node in self:
            if node.data == target_node_data:
                return {
                    'previousNode': previous_node,
                    'node': node,
                    'index': index
                }
            index += 1
            previous_node = node
                
        raise Exception('Cannot find element because the list is empty.')
        
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
    
    def __del__(self):
        self.data = None
        self.next = None
    
def main():
    llist = LinkedList(['a', 'b', 'c', 'd', 'e', 'f'])
    
    llist.remove('f')
    
    print(llist)
    
if __name__ == "__main__":
    main()