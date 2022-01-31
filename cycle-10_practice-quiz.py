# Author: JD 01/27/2022

#1
def food_costs(groceries,costs): 
    groceries_mod = groceries
    # Because groceries is a nested list, so this variable is created to keep track of the index of the costs list.
    index = 0
    # Using a nested for loop to go over each individual idem, then the item will be added by the corresponding cost.
    for i,v in enumerate(groceries_mod):
        for i2, v2 in enumerate(v):
            groceries_mod[i][i2] = v2 + ": $" + str(costs[index])
            # The index should be added 1 through each loop in order to go through each cost.
            index += 1


    return groceries_mod

print(food_costs([['apple','pear','banana',],['salmon','tuna','cod',],['milk','eggs','yogurt']],[1.99,2.99,0.99,9.99,10.99,6.99,3.49,2.49,1.49]) == [['apple: $1.99','pear: $2.99','banana: $0.99',],['salmon: $9.99','tuna: $10.99','cod: $6.99',],['milk: $3.49','eggs: $2.49','yogurt: $1.49',]])

#2
def factorial(x):
    # The factorial of 0 is 1
    if x == 0:
        return 1
    
    # The smallest possible result is 1, so result should start with one. Counter is used to keep track of the current working number until it reaches the n entered.
    result = 1
    counter = 1
    # Using a while loop so that the counter, i.e. the current number will not be greater than the number entered.
    # The result will then be multiplied by the current number.
    while counter <= x:
        result *= counter
        counter += 1
    
    return result

print(factorial(5))


#3
def fib_nums(x):
    # In case 1 or 2 is entered.
    if x == 1:
        return [0]
    elif x == 2:
        return[0,1]
    # Fibonacci starts with 0 and 1, so the first number equals to 0 and the second equals to 1.
    # Variable "step" keeps track of the current number of numbers that have been multiplied.
    first = 0
    second = 1
    step = 2
    # List result starts with 0 and 1.
    result = [0,1]
    # While the number of numbers multiplied is less than x, the loop will add the first and second together every single loop, and then make the first equal to the second, the second equal to the sum.
    
    while step < x:
        sum = 0
        sum += (first + second)
        result.append(sum)
        first = second
        second = sum
        step += 1
        
    return result


print(fib_nums(5) == [0,1,1,2,3], fib_nums(10) == [0,1,1,2,3,5,8,13,21,34])


# Problem_self

# There are two lists here, a lists of players and a list of 4 colors. Each player is matched with the color with the same index in the other list. Write a function color_matching(list1,list2)
# which will take the two lists as parameters to return a new list that has 4 nested list, each represents a color. The nested lists should contain the names and their representing color.
# For example: [['p1: red', 'p2: red'],['p3: green','p4: green'],['p5: blue', 'p6: blue']
# The lists to be used are:
# player_list = ['p1','p3','p4','p2','p8','p7','p5','p6']
# color_list = ['red','green','green','blue','red','yellow','red','blue']


# answer:
def matching_color(l1, l2):
    new = [[],[],[],[]]
    for i,v in enumerate(l1):
        if l2[i] == "red":
            new[0].append(l1[i] + ": " + l2[i])
        elif l2[i] == "green":
            new[1].append(l1[i] + ": " + l2[i])
        elif l2[i] == "blue":
            new[2].append(l1[i] + ": " + l2[i])
        elif l2[i] == "yellow":
            new[3].append(l1[i] + ": " + l2[i])
    
    return new

player_list = ['p1','p3','p4','p2','p8','p7','p5','p6']
color_list = ['red','green','green','blue','red','yellow','red','blue']

print(matching_color(player_list, color_list))
        
