"""
There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.
"""

class Solution:
    def findCircleNum(self, M):
        def dfs(i):
            for j in range(n):
                if M[i][j] and visited[j] == 0:
                    visited[j] = 1
                    dfs(j)
        n = len(M)
        circles = 0
        visited = [0] * n
        for i in range(n):
            if visited[i] == 0:
                circles += 1
                dfs(i)
        return circles

sol = Solution()
print(sol.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))