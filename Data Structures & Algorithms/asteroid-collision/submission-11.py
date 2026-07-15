class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            while stack and stack[-1]>0 and ast<0:
            # if stack and stack[-1]*ast<0:
                if stack[-1]>-ast:
                    ast=0
                elif stack[-1]==-ast:
                    ast = 0
                    stack.pop()
                else:
                    stack.pop()

            if ast:            
                stack.append(ast)
        return stack        