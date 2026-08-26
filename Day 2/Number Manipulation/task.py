import numbers

bmi = 84 / 1.65 ** 2
print(bmi)

# flooring a number (removes all decimal places to convert float into int-- no rounding)
print(int(bmi))

# round(): rounding
print(round(bmi))
print(round(bmi, 2))

# assignment operators
score = 0
# user scores a point
score /=1
print(score)

# f-strings = converts different data types into a string
score = 0 #int
height = 1.8 #float
is_winning = True #bool
print(f"your score is = {score}, your height is = {height}. You are winning is {is_winning}")
