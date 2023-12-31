import pytest
import sys

# sys.path.insert(1, '/home/narcizo/Projects/Programming-Fundamentals/python')
sys.path.insert(1, r"C:\Users\narci\Documents\Projects\Programming-Fundamentals\python")

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
    
def test_append_element():
    llist = linked_lists.LinkedList(['q', 'c', 'a', 'x'])
    
    list = []
    for el in llist:
        list.append(el)
    
    llist.append('a')
    
    list.append('a')
    list.append('None')
    
    assert str(llist) == ' -> '.join([el.data 
                                      if type(el) is not str 
                                      else el 
                                      for el in list])
    
def test_add_first_node():
    llist = linked_lists.LinkedList(['a', 'b'])
    
    llist.add_first('z')
    
    assert str(llist) == 'z -> a -> b -> None'
    
def test_add_last_empty_list():
    llist = linked_lists.LinkedList()
    
    llist.add_last('z')
    
    assert str(llist) == 'z -> None' 
    
def test_add_last():
    llist = linked_lists.LinkedList(['a', 'b'])
    
    llist.add_last('z')
    
    assert str(llist) == 'a -> b -> z -> None'
    
def test_add_after_empty_list():
    llist = linked_lists.LinkedList()
    
    with pytest.raises(Exception):
        llist.add_after('a', 'b')
    
    assert llist is not None
    assert llist.head is None
    
def test_add_after():
    llist = linked_lists.LinkedList(['a', 'b'])
    
    llist.add_after('a', 'z')
    
    assert str(llist) == 'a -> z -> b -> None'
    
def test_add_after_not_found():
    llist = linked_lists.LinkedList(['a', 'b'])
    
    with pytest.raises(Exception):
        llist.add_after('c', 'z')

    assert str(llist) == 'a -> b -> None'
    
def test_add_before_empty_list():
    llist = linked_lists.LinkedList()
    
    with pytest.raises(Exception):
        llist.add_before('a', 'b')
        
    assert llist is not None
    assert llist.head is None
    
def test_add_before():
    llist = linked_lists.LinkedList(['a', 'b'])
    
    llist.add_before('b', 'z')
    
    assert str(llist) == 'a -> z -> b -> None'
    
def test_add_before_not_found():
    llist = linked_lists.LinkedList(['a', 'b'])

    with pytest.raises(Exception):
        llist.add_before('z', 'x')
    
    assert str(llist) == 'a -> b -> None'

def test_append_element_empty_list():
    llist = linked_lists.LinkedList()
    
    llist.append('a')

    assert str(llist) == 'a -> None'
    
    
def test_pop_element():
    llist = linked_lists.LinkedList(['q', 'c', 'a', 'x'])
    
    list = []
    for el in llist:
        list.append(el)
    
    llist.pops()
    
    list.pop()
    list.append('None')
    
    assert str(llist) == ' -> '.join([el.data 
                                      if type(el) is not str 
                                      else el 
                                      for el in list])
    
def test_pop_element_empty_list():
    llist = linked_lists.LinkedList()
    
    with pytest.raises(Exception):
        llist.pops()
    
    assert llist is not None
    assert llist.head is None
    
def test_remove_element_empty_list():
    llist = linked_lists.LinkedList()
    
    with pytest.raises(Exception):
        llist.remove('a')
        
    assert llist is not None
    assert llist.head is None
    
def test_remove_single_element_in_list():
    llist = linked_lists.LinkedList(['a'])
    
    llist.remove('a')
    
    assert type(llist) is linked_lists.LinkedList
    assert llist is not None
    assert llist.head is None
    
def test_remove_first_element_list():
    llist = linked_lists.LinkedList(['a', 'b', 'c'])
    
    llist.remove('a')
    
    assert str(llist) == 'b -> c -> None'
    
def test_remove_last_element_list():
    llist = linked_lists.LinkedList(['a', 'b', 'c', 'd', 'e'])
    
    llist.remove('e')
    
    assert str(llist) == 'a -> b -> c -> d -> None'
    
def test_remove_element_list():
    llist = linked_lists.LinkedList()
    
    llist = linked_lists.LinkedList(['a', 'b', 'c', 'd', 'e'])
    
    llist.remove('c')
    
    assert str(llist) == 'a -> b -> d -> e -> None'
    
def test_find_element_list():
    llist = linked_lists.LinkedList()
    
    llist = linked_lists.LinkedList(['a', 'b', 'c', 'd', 'e'])
    
    node = llist.find_node('c')
    
    assert node['index'] == 2
    # TODO finish tests on indexing
    # assert node['node'] == {'node': 2, 'previousNode': 'b'}