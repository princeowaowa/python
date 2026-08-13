# def my_function():
#   print("Hello from a function")

# my_function()
# my_function()
# my_function()

#Defining a function with parameters
def add_numbers(x, y):
  print(f"Adding {x} and {y}")  
  return x + y

firstAdd = add_numbers(5, 3) # call the function with arguments 5 and 3
print(firstAdd) # print the result of the first function call
# print(add_numbers(5, 3)) # call the function with arguments 5 and 3
print(add_numbers(10, 20)) # call the function with arguments 10 and 20