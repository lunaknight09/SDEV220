def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"

def test_sum_tuple():
    assert sum((1, 2, 2)) == 6, "Should be 6"

if __name__ == "__main__":
    test_sum()
    test_sum_tuple()
    print("Everything passed")




#bug report it works with test_sum and then adding the tuple 
#it sent the AssertionError which red flagged me thinking its wrong which it 
#is since 1+2+2 is equal to 5