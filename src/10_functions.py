
# Write a function is_even that will return true if the passed-in number is even.


# YOUR CODE HERE

def is_even(n):
    if n%2 == 0: 
        return true 

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

def is_even_printer(n):
    if n%2 == 0: 
        print('Even!')
    else:
        print('Odd')

is_even_printer(num)




###############

# def mult2(n):
#     return n*2

# num = 50 

# print(mult2(num))

# def multlist(l):
#     # affect original list 
#     for i in range(len(l)):
#         # l[i] = l[i] * 2
#         l[i] *= 2

# nums = [10, 60, 4, 15]

# multlist(nums)

# print(nums)

# def multlistnew(l):
#     newList = []
#     for i in range(len(l)):
#         newList.append(l[i] * 2)
#     return newList 

# print(multlistnew([3, 5, 34, 10, 15]))

