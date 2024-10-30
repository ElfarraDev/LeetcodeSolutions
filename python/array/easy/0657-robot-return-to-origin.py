class Solution:
    def judgeCircle(self, moves: str) -> bool:
        instruction = {"U": (1,0),"D":(-1,0),"L":(0,-1),"R":(0,1)}
        x,y = 0,0

        for move in moves:
            dx ,dy = instruction[move]
            x += dx
            y += dy

        return x == 0 and y == 0
