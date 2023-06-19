import sys
sys.path.insert(1, '/home/narcizo/Projects/Programming-Fundamentals/python')
import linked_lists

def test_create_empty_list():
    llist = linked_lists.LinkedList()
    
    assert type(llist) is linked_lists.LinkedList
    assert llist is not None
    assert llist.head is None
    
def test_create_populated_list():
    llist = linked_lists.LinkedList(['a', 'b'])

    assert type(llist) is linked_lists.LinkedList
    assert llist is not None
    assert str(llist) == "a -> b -> None" 
    
def test_iterate_through_list():
    llist = linked_lists.LinkedList(['q', 'c', 'a', 'x'])
    
    list = []
    for el in llist:
        list.append(el)
    list.append('None')
        
    assert str(llist) == ' -> '.join([el.data 
                                      if type(el) is not str 
                                      else el 
                                      for el in list])