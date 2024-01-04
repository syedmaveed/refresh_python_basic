# def hello():
#     print("Hello")

# name=input("ENter Name : ")
# hello()
# print(name)

# #### Ex ###
# # INDENTATION is IMP in PYTHON
# def hello1(to):
#     print("Hello", to)
# name=input("Enter Name " )
# hello1(name)

# def main():
#     x=int(input("Enter x  "))
#     print("X Squared is", square(x))

# def square(n):
#    # return n * n
#    #return n**2
#    return pow(n,2)
    
# main()  

# def exp(num1, num2):
#     total=num1**num2
#     return total
# big_no=exp(33,6)
# print(big_no)




def add_numbers():
    # Get the first number from the user
    num1 = input("Enter the first number: ")
    
    # Get the second number from the user
    num2 = input("Enter the second number: ")
    
    try:
        # Convert the input strings to float numbers and add them together
        result = float(num1) ** float(num2)
        
        # Print the result
        print(f"The sum of {num1} and {num2} is: {result}")
        
    except ValueError:
        # If the input cannot be converted to float, handle the error
        print("Invalid input. Please enter valid numbers.")

# Call the function to add two numbers
add_numbers()