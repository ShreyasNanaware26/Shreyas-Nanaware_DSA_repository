# Name : Shreyas Sanjay Nanaware
# Roll No : 41
# TE EXTC 
# DSA 

#Making a main class which will consist of all the fucntions/methods
class my_queue:

    def __init__(self):
        self.queue = []

#Function for adding an element through the rear end of the queue
    def enqueue(self, new_element):
        self.queue.append(new_element)

#Function for removing an element throught the front end of the queue
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

#Function for displaying the queue elements 
    def display(self):
        if len(self.queue) < 1: #Adding an if condition so that if queue is empty then we can give proper message
            return None
        else:   
           return self.queue

#Function for determining the size of the queue
    def size(self):
        return len(self.queue)

#Creating an instance of the class created 
queue_object = my_queue()

#Displaying the user and asking them to choose the options
while(True):
    print("-----Select the option of your choice from the list displayed below-----")
    print("1) Adding elements in the queue (ENQUEUE operation)")
    print("2) Deleting elements from the queue (DEQUEUE operation)")
    print("3) Displaying the elements in the queue")
    print("4) Exit the program")

    user_input = int(input("Enter the option of your choice : ")) # Asking for user input
    print("\n")

#Adding an if-elif-else statements chain based on the user input given
    if(user_input == 1):
        user_input2 = int(input("Enter the number of elements you want to enqueue into the queue : "))
        if(user_input2 <= 0):
            print("The number of elements to be enqueued into the queue should be at least 1!")
        for i in range(0,user_input2):  #Using a for loop to take multiple elements at one time from the user
            new_element = int(input("Enter the element : " ))
            queue_object.enqueue(new_element)
        print("\n")
        print("my_queue contains following elements : " )
        print(queue_object.display())
        print("\n")

    elif(user_input == 2):
        user_input2 = int(input("Enter the number of elements you want to dequeue from the queue : "))
        if(user_input2 <= 0):
            print("The number of elements to be dequeued from the queue should be at least 1!")
        for i in range(0,user_input2):  #Using a for loop to take multiple elements at one time from the user
            queue_object.dequeue()
        print("\n")
        print("my_queue contains following elements : " )
        print(queue_object.display())
        print("\n")
       

    elif(user_input == 3):
        print("my_queue contains following elements : " )
        print(queue_object.display())
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

