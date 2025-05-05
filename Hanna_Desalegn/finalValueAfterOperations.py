class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x=0
        for k in operations:
            if '+' in k:
                x+=1
            elif '-' in k:
                x-=1
        return x
       