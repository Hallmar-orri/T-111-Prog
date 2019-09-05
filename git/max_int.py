#we need to constantly ask the user to input a positive number until he inputs a negative
#we need to create a value for the highest number he inputs
# create a if sentance for when a new input is higher than the other inputs, that new number is the new max_input
# if the user puts in a negative number, the program stops
num_int = int(input("Input a number: "))    
max_int = 0
while num_int > 0:
    num_int = int(input("Input a number: "))
    if num_int > max_int:
        max_int = num_int
print("The maximum is", max_int)