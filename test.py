import unittest

from my_sum import sum


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()
    
    
if __name__ == '__main__':
    unittest.main()
    
    
    
    
    
    #bug report I see the importance of the assignment but hard to put into words 
    #really how tests inside help us as developers but its better than looking 
    #through hundreds of lines trying to find the problem.  This would help when
    #we have very big or even small projects so we dont have to pull hair out trying to find
    #the syntax problem to make the project work.