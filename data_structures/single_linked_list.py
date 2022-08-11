from dataclasses import dataclass
from typing import Optional

@dataclass
class SLLNode :
    value: int
    next: Optional['SLLNode'] = None
        
@dataclass
class SLList :
    root: Optional['SLLNode'] = None
    length: int = 0
    
    def unshift(self, value: int) -> None:
        new_root = SLLNode(value, self.root or None)
        
        self.root = new_root
        self.length += 1
        
    def shift(self) -> int | None :
        if self.root is None:
            return None
         
        result = self.root
        self.root = self.root.next or None
        self.length -= 1
        
        return result.value
    
    def pop(self) -> int | None :
        if self.root is None:
            return None
        else:  
            pivot = self.root
            while pivot.next and pivot.next.next is not None:
                pivot = pivot.next

            result = pivot.next
            pivot.next = None
            
            if result: 
                return result.value
            
        return None
