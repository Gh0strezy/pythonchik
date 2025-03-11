from . import adada as zov

def test_addition1():
    assert zov.find_list_recursion([1, 2, [3, 4, [5, [6, []]]]], 4) == 3
    assert zov.find_list_recursion([1, 2, [3, 4, [5, [6, []]]]], 'spam') == None
    assert zov.find_list_without_recursion2([1, 2, [3, 4, [5, [6, []]]]], 4) == 3 
    assert zov.find_list_without_recursion2([1, 2, [3, 4, [5, [6, []]]]], 'spam') == None 
    assert zov.find_number_without_recursion(1, 1, 3) == (9, 21)
    assert zov.find_number_with_recursion(1, 1, 3) == (9, 21)