import unittest
import single_linked_list as sll

class Test_SingleLinkedList(unittest.TestCase) :
    
    def test_create_node(self) :
        node : sll.SLLNode = sll.SLLNode(1)
        self.assertEqual(node.value, 1)
        
    def test_create_empty_list(self) :
        list : sll.SLList = sll.SLList()
        self.assertEqual(list.root, None)
        
    def test_unshift(self) : 
        list: sll.SLList = sll.SLList()
        list.unshift(1)
        list.unshift(2)
        list.unshift(3)
        
        self.assertEqual(list.root.value, 3)
        self.assertEqual(list.root.next.value, 2)
        self.assertEqual(list.root.next.next.value, 1)
        self.assertEqual(list.length, 3)

    
    
if __name__ == '__main__' :
    unittest.main()