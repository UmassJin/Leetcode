'''
The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.


Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.

-2 (K)	-3	3
-5	-10	1
10	30	-5 (P)

Notes:

The knight's health has no upper bound.
Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.
'''

class Solution:
    # @param {integer[][]} dungeon
    # @return {integer}
    def calculateMinimumHP(self, dungeon):
        if not dungeon: return 0
        row = len(dungeon); cal = len(dungeon[0])
        dp = [[ 0 for i in xrange(cal)] for j in xrange(row)]
        
        dp[row-1][cal-1] = 1
        for i in xrange(row-2, -1, -1):
            dp[i][cal-1] = max (1, dp[i+1][cal-1] - dungeon[i+1][cal-1])
        
        for i in xrange(cal-2, -1, -1):
            dp[row-1][i] = max(1, dp[row-1][i+1] - dungeon[row-1][i+1])
        
        for i in xrange(row-2, -1, -1):
            for j in xrange(cal-2, -1, -1):
                right = max(1, dp[i][j+1] - dungeon[i][j+1])
                down = max(1, dp[i+1][j] - dungeon[i+1][j])
                dp[i][j] = min(right, down)
        
        return max(1, dp[0][0]-dungeon[0][0]) 
      
# 注意最后return的值需要check dp[0][0]-dungeon[0][0],而且要与1比较，不能单纯的return dp[0][0]
# 注意思路是从最后一位向dp[0][0]走
