# Name : Shreyas Sanjay Nanaware
# Roll No : 41
# TE EXTC 
# DSA 

#Creating an empty list which resembles the stack
my_stack = []

#Asking the user for performing the operations of their choice
while(True):
    print("-----Select the option of your choice from the list displayed below-----")
    print("1) Adding elements in the stack (PUSH operation)")
    print("2) Deleting elements from the stack (POP operation)")
    print("3) Displaying the elements in the stack")
    print("4) Exit the program")

    user_input = int(input("Enter the option of your choice : ")) # Asking for user input
    print("\n")

#Adding an if-elif-else statements chain based on the user input given
    if(user_input == 1):
        user_input2 = int(input("Enter the number of elements you want to push into the stack  : "))
        if(user_input2 <= 0):
            print("The number of elements to be pushed into the stack should be at least 1!")
        for i in range(0,user_input2):  #Using a for loop to take multiple elements at one time from the user
            new_element = int(input("Enter the element : " ))
            my_stack.append(new_element)
        print("\n")
        print("my_stack contains following elements : " )
        for i in range(0,len(my_stack)): # Using for loops for displaying the elements of the stack after every operation
            print(my_stack[i])
        print("\n")


    elif(user_input == 2):
        if(len(my_stack) == 0):
            print("The stack is empty and thus the pop operation cant be done!")
        else:
            user_input3 = int(input("Enter the number of elements you want to pop from the stack : "))
            if(user_input3 > len(my_stack)):
                print("The number of elements to be popped should be less than the total elements in the stack")
            print("The elements popped out of stack are as follows : \n")
            for i in range(0,user_input3):
                print(my_stack.pop())
        print("my_stack contains following elements : " )
        for i in range(0,len(my_stack)): # Using for loops for displaying the elements of the stack after every operation
            print(my_stack[i])
        print("\n")
    elif(user_input == 3):
        if(len(my_stack) == 0):
            print("The stack is empty! ")
            print("\n")
        else:
            print("my_stack contains following elements : " )
            for i in range(0,len(my_stack)): # Using for loops for displaying the elements of the stack after every operation
                print(my_stack[i])
            print("\n")
    elif(user_input == 4):
        user_input4 = input("Are you sure you want to exit the program ( Y / N ) : ")
        if(user_input4 == "Y" or user_input4 == "y"):
            print("Exited the program successfully , Have a nice day !")
            break
        elif(user_input4 == "N" or user_input4 == "n"):
            pass
        else:
            print("Please enter Y/N only!")
            print("\n")
        

    else: # Keeping an condition ust in case that user enter any value outside the list of options displayed
        print("Please select from the options displayed!")
        print("\n")


        

            
