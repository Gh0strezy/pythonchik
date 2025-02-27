import zov

def test_addition1():
    assert zov.findListRecursion([1, 2, [3, 4, [5, [6, []]]]], 4) == 3 
    assert zov.findListRecursion([1, 2, [3, 4, [5, [6, []]]]], 'spam') == None
    assert zov.findListWithoutRecursion2([1, 2, [3, 4, [5, [6, []]]]], 4) == 3 
    assert zov.findListWithoutRecursion2([1, 2, [3, 4, [5, [6, []]]]], 'spam') == None 
    assert zov.findNumberWithoutRecursion(1, 1, 3) == (9, 21)
    assert zov.findNumberWithRecursion(1, 1, 3) == (9, 21)