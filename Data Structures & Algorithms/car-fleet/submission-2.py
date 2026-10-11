# position = [4,7,2], speed = [2,1,1], target = 10
# car1 =          a---a---a---a
# car2 =                b-b-b-b
# road =  0 1 2 3 4 5 6 7 8 9 10
# so this means car1 and car2 are a car fleet

# whateve rjust watch the solution vid
# https://www.youtube.com/watch?v=Pr6T-3yB9RM

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = []
        for i in range(len(position)):
            pair.append([position[i], speed[i]])
        
        stack = []
        # sorted(arr) = [1,2,3,4]
        # sorted(arr)[::-1] = [4,3,2,1]
        for pos, speed in sorted(pair)[::-1]:
            # an ingeneous way to solve this problem, calculating timestampArrival essentially
            # skips the need to keep track of all the position/increment manually
            # as e.g. [1.0,7.0], then a car arrives at timestamp of 5.0
            # [1.0,7.0,5.0] , we can pop the 5.0, as its already inside the fleet of 7.0
            # as its faster and got capped by the than the car that arrives at 7.0
            # [1.0,7.0]
            timestampArrival = (target - pos) / speed
            stack.append(timestampArrival)
            # the stack will sort from fastest -> slowest, bcs of our sort above
            # result will be like [1.0,7.0,12.0], which is the timestamp 
            # of when does the car arrive at the target
            # compare the top of the stack with the one below the top of the stack
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)


