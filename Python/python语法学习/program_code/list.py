# blank list -- 空列表
lt = []

# list of integers
lt = [1, 2, 3, 4, 5]

# List of heterogenous data types
lt = [1, 'hello',  5.8]
print(lt)


# Also, you can make use of the list constructor list()
theList = list([1, 2])
print(theList)


#Syntax - How to use List Comprehension
#   theList = [expression(iter) for iter in oldList if filter(iter)]
listofCountries = ["India","America","England","Germany","Brazil","Vietnam"]
firstLetters = [ country[0] for country in listofCountries ]
print(firstLetters) # ['I', 'A', 'E', 'G', 'B', 'V']