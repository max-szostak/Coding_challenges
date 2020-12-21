""" On an infinite plane, a robot initially stands at (0, 0) and faces north.  The robot can receive one of three instructions:

"G": go straight 1 unit;
"L": turn 90 degrees to the left;
"R": turn 90 degress to the right.
The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the robot never leaves the circle. """

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dirs = [[0,1],[-1,0],[0,-1],[1,0]]
        dir_i = 0
        pos = [0,0]
        for c in instructions:
            if c == 'G':
                pos[0] += dirs[dir_i][0]
                pos[1] += dirs[dir_i][1]
            elif c == 'L':
                dir_i = (dir_i + 1) % 4
            elif c == 'R':
                dir_i = (dir_i - 1) % 4
        delta_dir = [dirs[dir_i][0], dirs[dir_i][1] - 1]
        if pos == [0,0]:
            return True
        elif delta_dir == [0,0]:
            return False
        else:
            return True

sol = Solution()
print(sol.isRobotBounded("G"))
print(sol.isRobotBounded("GL"))
print(sol.isRobotBounded("GLLG"))