
# temperatures = [30,38,30,35,40,28]
# 2 extra list, output and stack
# output = [1,3,1,1,0,0]
#           [t ,i]
# stack  = [[40,4],[28,5]]
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = []
        stack = [] # use [temp, index] list/pair for this stack
        # so its like a few list (pair) inside a list (stack)

        for i, temp in enumerate(temperatures):
            output.append(0)
            while stack and temp > stack[-1][0]: # gets the top of the list, access the temp of the top
                stackTemp, stackIndex = stack.pop()
                output[stackIndex] = i - stackIndex
            stack.append([temp,i])
        return output


            

        