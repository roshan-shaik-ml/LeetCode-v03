class Solution:
    
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        
        x = 0

        for operation in operations:

            if not operation[0].isalpha():
                
                # pre ops
                if '-' in operation:
                    x = (x - 1)
                else:
                    x = (x + 1)
            else:

                if '-' in operation:
                    x = x - 1
                else:
                    x = x + 1
            print(x)
        return x
