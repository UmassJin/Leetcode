'''
1. There are a row of houses, each house can be painted with three colors red, blue and green. 
The cost of painting each house with a certain color is different. You have to paint all the houses 
such that no two adjacent houses have the same color. You have to paint the houses with minimum cost. 
How would you do it?

Note: Painting house-1 with red costs different from painting house-2 with red. The costs are different 
for each house and each color.

Reference: http://karmaandcoding.blogspot.com/2012/02/house-coloring-with-red-blue-and-green.html
'''

def sort_colors(matrix):
        if not matrix or not matrix[0]: return 0
        house_num = len(matrix)
        color_num = len(matrix[0])

        dp = [ [0 for i in xrange(color_num)] for j in xrange(house_num)]

        for i in xrange(house_num):
                for j in xrange(color_num):
                        if i == 0:
                                dp[0][j] = matrix[0][j]
                        else:
                                tmp = dp[i-1][:j] + dp[i-1][j+1:]
                                lastmin = min(tmp)
                                dp[i][j] = lastmin + matrix[i][j]
        return min(dp[house_num-1])

matrix = [[1, 2, 3], [6, 7, 5], [2, 6, 8]]
print sort_colors(matrix)


