# Name : Shreyas Sanjay Nanaware
# Roll No : 41
# TE EXTC 
# DSA 

#Creating a main class for circular queue which consists of  all the fucntions
class My_circular_queue():

    def __init__(self, k):
        self.k = k
        self.queue = [None] * k
        self.head = self.tail = -1

#Function for inserting an element into the circular queue 
    def enqueue(self, data):

        if ((self.tail + 1) % self.k == self.head):
            print("The circular queue is full , thus no more elements can be added to the circular queue \n")

        elif (self.head == -1):
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data
        else:
            self.tail = (self.tail + 1) % self.k
            self.queue[self.tail] = data

#Fcuntion for deleting an element from the circular queue
    def dequeue(self):
        if (self.head == -1):
            print("No element can be deleted as the circular queue is empty\n")

        elif (self.head == self.tail):
            temp = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return temp
        else:
            temp = self.queue[self.head]
            self.head = (self.head + 1) % self.k
            return temp

#Function to display the elements from the circular queue
    def display(self):
        if(self.head == -1):
            print("Circular queue is empty at the moment")

        elif (self.tail >= self.head):
            for i in range(self.head, self.tail + 1):
                print(self.queue[i], end=" ")
            print()
        else:
            for i in range(self.head, self.k):
                print(self.queue[i], end=" ")
            for i in range(0, self.tail + 1):
                print(self.queue[i], end=" ")
            print()


#Creating an instance of the class created earlier
circular_queue_object = My_circular_queue(5)

while(True): #Using while loop to display user the operations list and aking them to choose accordingly
    print("-----Select the option of your choice from the list displayed below-----")
    print("1) Adding elements in the circular queue (ENQUEUE operation)")
    print("2) Deleting elements from the circular queue (DEQUEUE operation)")
    print("3) Displaying the elements in the circular queue")
    print("4) Exit the program")

    user_input = int(input("Enter the option of your choice : ")) # Asking for user input
    print("\n")

    #Adding an if-elif-else statements chain based on the user input given
    if(user_input == 1):
        user_input2 = int(input("Enter the number of elements you want to enqueue into the queue : "))
        if(user_input2 <= 0):
            print("The number of elements to be enqueued into the queue should be at least 1!")
        variable = int(((user_input2)/2) + 1)
        for i in range(0,variable):  #Using a for loop to take multiple elements at one time from the user
            new_element = int(input("Enter the element : " ))
            circular_queue_object.enqueue(new_element)
        print("\n")
        print("my_queue contains following elements : " )
        print(circular_queue_object.display())
        print("\n")

    elif(user_input == 2):
        user_input2 = int(input("Enter the number of elements you want to dequeue from the queue : "))
        if(user_input2 <= 0):
            print("The number of elements to be dequeued from the queue should be at least 1!")
        for i in range(0,user_input2):  #Using a for loop to take multiple elements at one time from the user
            circular_queue_object.dequeue()
        print("\n")
        print("my_queue contains following elements : " )
        print(circular_queue_object.display())
        print("\n")
       

    elif(user_input == 3):
        print("my_queue contains following elements : " )
        print(circular_queue_object.display())
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

