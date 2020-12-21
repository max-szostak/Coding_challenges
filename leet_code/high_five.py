""" Given a list of the scores of different students, items, where items[i] = [IDi, scorei] represents one score from a student with IDi, calculate each student's top five average.

Return the answer as an array of pairs result, where result[j] = [IDj, topFiveAveragej] represents the student with IDj and their top five average. Sort result by IDj in increasing order.

A student's top five average is calculated by taking the sum of their top five scores and dividing it by 5 using integer division. """

class Solution:
    def highFive(self, items):
        scores = {}
        mins = {}
        for item in items:
            i = item[0] 
            score = item[1]
            if i not in scores:
                scores[i] = [score]
                mins[i] = score
            elif len(scores[i]) < 5:
                scores[i].append(score)
                if score < mins[i]:
                    mins[i] = score
            else:
                if score >= mins[i]:
                    scores[i].append(score)
                    scores[i].sort()
                    scores[i].pop(0)
                    mins[i] = scores[i][0]
        averages = []
        for key in scores:
            averages.append([key, sum(scores[key]) // 5])
        return sorted(averages, key = lambda i : i[0])

sol = Solution()
print(sol.highFive([[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]))