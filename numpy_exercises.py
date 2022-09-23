import numpy as np

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

# 1. How many negative numbers are there? 4
len(a[a < 0])

# 2. How many positive numbers are there? 5
len(a[a > 0])

# 3. How many even positive numbers are there? 3
b = a[a % 2 == 0]
len(b[b>0])

# 4. If you were to add 3 to each data point, how many positive numbers would there be? 10
a2 = a + 3
len(a2[a2 > 0])

# 5. If you squared each number, what would the new mean and standard deviation be?
a_squared = a **2
a_squared.mean() # mean 74
a_squared.std() #standard deviation 144.0243035046516

# 6. A common statistical operation on a dataset is centering. This means to adjust the data such that the mean of the data is 0. This is done by subtracting the mean from each data point. Center the data set. See this link for more on centering.
centered_a = a - a.mean() #subtract the mean from each number
centered_a.mean() #check to see if the new mean is 0

# 7. Calculate the z-score for each data point.
a_mean = a.mean()
a_std = a.std()

a_zscores = [(value- a_mean) / a_std for value in a]

# Life w/o numpy to life with numpy

## Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list
sum_of_a = sum(a)
sum_of_a  55

# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list
min_of_a = min(a)
min_of_a # 1

# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list
max_of_a = max(a)
max_of_a # 10

# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list
mean_of_a = sum_of_a / len(a)
mean_of_a # 3

# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together
product_of_a = 1
x = 0
for x in a:
    product_of_a = product_of_a * x

product_of_a # 3628800

# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]
square_of_a = []
x = 0
for x in a:
    square_of_a.append(x**2)

# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers
odds_in_a = []
for n in a:
    if n % 2 == 1:
        odds_in_a.append(n)

odds_in_a

# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.
evens_in_a = []
for n in a:
    if n % 2 == 0:
        evens_in_a.append(n)

evens_in_a


## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.
b = np.array([
    [3, 4, 5],
    [6, 7, 8]
])

# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. **Hint, you'll first need to make sure that the "b" variable is a numpy array**
#sum_of_b = 0
#for row in b:
#    sum_of_b += sum(row)

sum_of_b = b.sum()
# 33

# Exercise 2 - refactor the following to use numpy. 
#min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1]) 

min_of_b = b.min()
# 3

# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
#max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])

max_of_b = b.max()
 #8

# Exercise 4 - refactor the following using numpy to find the mean of b
# mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))

mean_of_b = b.mean()
# 5.5

# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
# product_of_b = 1
# for row in b:
#    for number in row:
#        product_of_b *= number

product_of_b = b.prod()
# 20160

# Exercise 6 - refactor the following to use numpy to find the list of squares 
# squares_of_b = []
# for row in b:
#    for number in row:
#        squares_of_b.append(number**2)

squares_of_b = b**2
# array([[ 9, 16, 25],
#       [36, 49, 64]])

# Exercise 7 - refactor using numpy to determine the odds_in_b
#odds_in_b = []
#for row in b:
#    for number in row:
#        if(number % 2 != 0):
#            odds_in_b.append(number)

odds_in_b = b[b % 2 == 1]
#array([3, 5, 7])

# Exercise 8 - refactor the following to use numpy to filter only the even numbers
#evens_in_b = []
#for row in b:
#    for number in row:
#        if(number % 2 == 0):
#            evens_in_b.append(number)

evens_in_b = b[b % 2 == 0]
#array([4, 6, 8])

# Exercise 9 - print out the shape of the array b.
b.shape
#(2, 3)

# Exercise 10 - transpose the array b.
b.T
#array([[3, 6],
#       [4, 7],
#       [5, 8]])

# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)
b.reshape(1,6)
# array([[3, 4, 5, 6, 7, 8]])

# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)
b.reshape(6,1)
#array([[3],
#       [4],
#       [5],
#       [6],
3       [7],
#       [8]])


## Setup 3
c = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
# Exercise 1 - Find the min, max, sum, and product of c.
c.min() # 1
c.max() # 9
c.sum() # 45
c.prod() # 362880

# Exercise 2 - Determine the standard deviation of c.
c.std() # 2.581988897471611

# Exercise 3 - Determine the variance of c.
c.var() # .666666666666667

# Exercise 4 - Print out the shape of the array c
c.shape # (3, 3)

# Exercise 5 - Transpose c and print out transposed result.
c.T
#array([[1, 4, 7],
#       [2, 5, 8],
#       [3, 6, 9]])

# Exercise 6 - Get the dot product of the array c with c. 
np.dot(c,c)
#array([[ 30,  36,  42],
#       [ 66,  81,  96],
#       [102, 126, 150]])

# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261
(c * c.T).sum()
#261

# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.
(c * c.T).prod()
#131681894400

## Setup 4
d = np.array([
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
])

# Exercise 1 - Find the sine of all the numbers in d
np.sin(d)
'''
array([[ 0.89399666, -0.98803162,  0.85090352,  0.        ,  0.58061118,
        -0.80115264],
       [ 0.85090352, -0.89399666,  0.98803162, -0.17604595,  0.89399666,
         0.        ],
       [-0.30481062,  0.85090352, -0.85090352,  0.89399666, -0.85090352,
        -0.80115264]])
'''

# Exercise 2 - Find the cosine of all the numbers in d
np.cos(d)
'''
array([[-0.44807362,  0.15425145,  0.52532199,  1.        ,  0.81418097,
        -0.59846007],
       [ 0.52532199, -0.44807362,  0.15425145,  0.98438195, -0.44807362,
         1.        ],
       [-0.95241298,  0.52532199,  0.52532199, -0.44807362,  0.52532199,
        -0.59846007]])
'''

# Exercise 3 - Find the tangent of all the numbers in d
np.tan(d)
'''
array([[-1.99520041, -6.4053312 ,  1.61977519,  0.        ,  0.71312301,
         1.33869021],
       [ 1.61977519,  1.99520041,  6.4053312 , -0.17883906, -1.99520041,
         0.        ],
       [ 0.32004039,  1.61977519, -1.61977519, -1.99520041, -1.61977519,
         1.33869021]])
'''
# Exercise 4 - Find all the negative numbers in d
d[d <0]
# array([-90, -30, -45, -45])

# Exercise 5 - Find all the positive numbers in d
d[d >0]
#array([ 90,  30,  45, 120, 180,  45, 270,  90,  60,  45,  90, 180])

# Exercise 6 - Return an array of only the unique numbers in d.
np.unique(d)
#array([-90, -45, -30,   0,  30,  45,  60,  90, 120, 180, 270])

# Exercise 7 - Determine how many unique numbers there are in d.
len(np.unique(d))
#11

# Exercise 8 - Print out the shape of d.
d.shape
# (3, 6)

# Exercise 9 - Transpose and then print out the shape of d.
d.T.shape
# (6, 3)

# Exercise 10 - Reshape d into an array of 9 x 2
d.reshape(9,2)
'''
array([[ 90,  30],
       [ 45,   0],
       [120, 180],
       [ 45, -90],
       [-30, 270],
       [ 90,   0],
       [ 60,  45],
       [-45,  90],
       [-45, 180]])
'''


