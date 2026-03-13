import re

class Solution:
    def isNumber(self, s: str) -> bool:
        pattern = re.compile(r"""
            ^[+-]?                
            (                     
              (\d+(\.\d*)?)       
              |(\.\d+)            
            )
            ([eE][+-]?\d+)?       
            $                     
        """, re.VERBOSE)
        
        return bool(pattern.match(s))
