#School Class Manager

# Username = USER
# Password = 1234

#File is created in current User folder next to Downloads folder

#Naming file
fileName = "Coding_School_Information_Sheet.txt"

#Creating template for file before it is updated
file = open(fileName, 'w')
file.write("Coding School Class and Student Information Sheet \n")
file.write(" \n")
file.write("No data has been saved to this file yet")
file.close()

#Subheadings for file
Class_A = "CLASS A:"
Class_B = "CLASS B:"
Class_C = "CLASS C:"
Class_D = "CLASS D:"

#Writing a full class in file
def Writing_File(Class, Header):
    file = open(fileName, 'a')
    #Checking class is not empty
    if Class[0] != None:
        file.write(Header)
        file.write(" \n")
        #Writing each student attribute within the class
        for i in range (len(Class)):
            file.write(Class[i].fname + " ")
            file.write(Class[i].lname + " ")
            file.write(str(Class[i].score) + " ")
            file.write(Class[i].band + " ")
            file.write(" \n")
        file.write(" \n")
    else:
        #Template for empty class
        file.write(Header + " is currently empty \n")
        file.write(" \n")
    file.close()

def Update():
    #Confirming update
    print("1 = Confirm")
    print("Enter anything else to cancel")
    print()
    Confirm = input("Would you like to update file with all current class and student information?")
    if Confirm == "1":
        #Setting new heading
        file = open(fileName, 'w')
        file.write("Coding School Class and Student Information Sheet \n")
        file.write(" \n")
        file.close()
        #Adding each class to file
        Writing_File(class1, Class_A)
        Writing_File(class2, Class_B)
        Writing_File(class3, Class_C)
        Writing_File(class4, Class_D)
        print()
        print("File has been updated with current class information")
        Menu()
    else:
        ContToMenu()
#######################################################################################################
#Variables

#Creating object type (Class)
class Student:
    def __init__(self, fname, lname, score, band):
        self.fname = fname
        self.lname = lname
        self.score = score
        self.band = band

    #Functions for editting attributes
    def setFname(self, fname):
        self.fname = fname
    
    def setLname(self, lname):
        self.lname = lname
    
    def setScore(self, score):
        self.score = score
    
    def setBand(self, band):
        self.band = band

#Setting class (size) pre input
class1 = [None] * 10
class2 = [None] * 10
class3 = [None] * 10
class4 = [None] * 10
#######################################################################################################
#Login
def Login():
    #Stating variables
    attempts = 3
    username = "USER"
    password = "1234"
    Flag = False
    while attempts > 0:
        entered_username = input("Username:")
        #Check if username is correct
        if entered_username == username:
            entered_password = input("Password:")
            #Check if passowrd is correct after username is correct
            if entered_password == password:
                Flag = True
                break
            #If entered password is incorrect
            else:
                print("Incorrect")
                attempts = attempts - 1
        #If entered username is incorrect
        else:
            print("Username not found")
            attempts = attempts - 1
    #Check if correct username and password was achieved
    if Flag == True:
        print("Correct!")
        print("")
        print("Welcome to Coding School Academic Scores System.")
        Menu()
    #If correct username and password was not achieved
    else:
        print("You have not entered the correct username and password")
        print("the program will now close.")
        exit()
#######################################################################################################
#Menu
def Menu():
    print("")
    print("--MAIN MENU--")
    print("Please select what you would like to do: (Enter the number for the corresponding action)")
    print("")
    print("1 = Enter class scores")
    print("2 = Print class information")
    print("3 = Edit class/student scores")
    print("4 = Grade students into bands")
    print("5 = Calculate percentage of students in a band")
    print("6 = Save current class and student information to file")
    print("7 = Exit")
    #Choice options and functions for available choices
    choice = input()
    if choice == "1":
        Option_1()
    elif choice == "2":
        Option_2() 
    elif choice == "3":
        Option_3()       
    elif choice == "4":
        Option_4()       
    elif choice == "5":
        Option_5() 
    elif choice == "6":
        pass
        #Export()
    elif choice == "7":
        exit()
    else:
        print("You have selected an invalid option, please try again.")
        Menu()
    
def ContToMenu():
    Next = input("Press any key to continue")
    Menu()
#######################################################################################################
#Setting Class Scores (1)
def populate_array(classToPopulate):
    for x in range (len(classToPopulate)):
        #Making new students with atributes
        classToPopulate[x] =  Student(input("firstname: "), input("lastname: "), input("Score: "), "")
        classToPopulate[x].score = int(classToPopulate[x].score)
        try:
            #Checking entered score is bewteen 1 - 100
            if 0 <= classToPopulate[x].score <= 100:
                pass
            else:
                print("You have not entered a valid number between 1 - 100")
        #What to do if entered score != int
        except:
            raise TypeError ("You can only enter integers")
        print()

    return classToPopulate

#Print out options 1 - 4 for classes
def Display_Classes():
    print()
    print("1 = Class 1")
    print("2 = Class 2")
    print("3 = Class 3")
    print("4 = Class 4")
    print()

#Choosing which class array to populate
def Option_1():
    global class1
    global class2
    global class3
    global class4
    Display_Classes()
    ClassChoice = input("Which class would you like to enter Student Names and Scores for?")
    print()
    try:
        if ClassChoice == "1":
            class1 = populate_array(class1)
            SetTheBands(class1)
        elif ClassChoice == "2":
            class2 = populate_array(class2)
            SetTheBands(class2)
        elif ClassChoice == "3":
            class3 = populate_array(class3)
            SetTheBands(class3)
        elif ClassChoice == "4":
            class4 = populate_array(class4)
            SetTheBands(class4)
        else:
            print("You have not entered a valid option, please try again.")
            Option_1()  
    finally:
        Update()
        ContToMenu()
#######################################################################################################
#Print Class Information (2)
def read_array(Class):
    global class1
    global class2
    global class3
    global class4
    print()
    try:
        #Checking if class is empty
        if Class[0] == None:
            print("This class is currently empty")
        else:
            #Printing class names and scores if not empty
            for i in range (len (Class)):
                print(Class[i].fname, Class[i].lname, Class[i].score, sep=" ")
                print()
    finally:
        ContToMenu()

#Choosing what class to read
def Option_2():
    Display_Classes()
    ClassChoice = input("Which class would you like to view scores for?")
    if ClassChoice == "1":
        read_array(class1)
    elif ClassChoice == "2":
        read_array(class2)
    elif ClassChoice == "3":
        read_array(class3)
    elif ClassChoice == "4":
        read_array(class4)
    else:
        print("You have not entered a valid option, please try again.")
#######################################################################################################
#Edit Classes/Student (3)
def Option_3():
    print("1 = Class")
    print("2 = Student")
    print()
    choice = input("What would you like to edit?")
    if choice == "1":
        #Not raising flag to say that user does not want to edit a student only
        StudentOnly = False
        Choose_Class(StudentOnly)
    elif choice == "2":
        #Raising flag to say that user wants to edit a student only
        StudentOnly = True
        Choose_Class(StudentOnly)
    else:
        print("You did not enter a valid option, please try again")
        Option_3()
    Update()
    ContToMenu()

#Asking user what class their edit will take place in
def Choose_Class(StudentOnly):
    if StudentOnly == True:
        Display_Classes()
        Choice = input("What class would you like to edit?")
        if Choice == "1":
            SelectStudent(class1)
        elif Choice == "2":
            SelectStudent(class2)
        elif Choice == "3":
            SelectStudent(class3)
        elif Choice == "4":
            SelectStudent(class4)
        else:
            print("You have not entered a valid option")
            Choose_Class(StudentOnly)
    else:
        Display_Classes()
        Choice = input("What class would you like to edit?")
        if Choice == "1":
            populate_array(class1)
        elif Choice == "2":
            populate_array(class2)
        elif Choice == "3":
            populate_array(class3)
        elif Choice == "4":
            populate_array(class4)

#Editing a single student
def SelectStudent(Class):
    if Class[0] != None:
        for x in range(len(Class)):
            print(Class[x].fname, Class[x].lname)
        #Asking to identify student in that class based on input
        Entered_Student_Number = input("Enter the position of the student you want to edit (Position in class 1-10)")
        Entered_Student_Number = int(Entered_Student_Number)
        Entered_Student_Number = Entered_Student_Number - 1
        #Setting new attributes for student based on given index
        print()
        print("You have selected:", Class[Entered_Student_Number].fname, Class[Entered_Student_Number].lname, sep=" ")
        Class[Entered_Student_Number].setFname(input("Enter new Firstname:"))
        Class[Entered_Student_Number].setLname(input("Enter new Lastname:"))
        Class[Entered_Student_Number].setScore(input("Enter new Score:"))
        Class[Entered_Student_Number].score = int(Class[Entered_Student_Number].score)
        #Setting band for new score
        if Class[Entered_Student_Number].score >= 90:
            Class[Entered_Student_Number].setBand("A")
        elif Class[Entered_Student_Number].score >= 80:
            Class[Entered_Student_Number].setBand("B")
        elif Class[Entered_Student_Number].score >= 70:
            Class[Entered_Student_Number].setBand("C")
        elif Class[Entered_Student_Number].score >= 60:
            Class[Entered_Student_Number].setBand("D")
        elif Class[Entered_Student_Number].score >= 50:
            Class[Entered_Student_Number].setBand("E")
        elif Class[Entered_Student_Number].score < 50:
            Class[Entered_Student_Number].setBand("F")
    else:
        print()
        print("This class is currently empty")
        print("You must first enter the scores for the whole class to edit single students")
#######################################################################################################
#Display bands (4)

#Setting band attribute based on score
def SetTheBands(Class):
    if Class[0] == None:
        pass
    else:
        for student in Class:
            if student.score >= 90:
                student.setBand("A")
            elif student.score >= 80:
                student.setBand("B")
            elif student.score >= 70:
                student.setBand("C")
            elif student.score >= 60:
                student.setBand("D")
            elif student.score >= 50:
                student.setBand("E")
            elif student.score < 50:
                student.setBand("F")
    
#Printing students with their score and band
def PrintTheBands(Class):
    print()
    #Checking if the class is not populated
    if Class[0] != None:
        for i in range (len (Class)):
            print(Class[i].fname, Class[i].lname, Class[i].score, Class[i].band, sep=" ")
            print()
    else:
        print("This class is currently empty")

#Printing the bands based on input
def Option_4():
    SetTheBands(class1)
    SetTheBands(class2)
    SetTheBands(class3)
    SetTheBands(class4)
    Display_Classes()
    Which_View = input("What class would you like to view bands for?")
    if Which_View == "1":
        print()
        print("CLASS A:")
        PrintTheBands(class1)
    elif Which_View == "2":
        print()
        print("CLASS B:")
        PrintTheBands(class2)
    elif Which_View == "3":
        print()
        print("CLASS C:")
        PrintTheBands(class3)
    elif Which_View == "4":
        print()
        print("CLASS D:")
        PrintTheBands(class4)
    ContToMenu()

#######################################################################################################
#Percentage of students achieving a mark (5)

#Choosing class to view
def Option_5():
    Display_Classes()
    choice = input("What class would you like to view bands/grades for?")
    if choice == "1":
        rankBands(class1)
    elif choice == "2":
        rankBands(class2)
    elif choice == "3":
        rankBands(class3)
    elif choice == "4":
        rankBands(class4)
    else:
        print("You have not entered a valid class number")
        Option_5()
    ContToMenu()

#Finding raw amount of students getting a mark (band)
def rankBands(Class):
    SetTheBands(Class)
    #Counters for students achieving the mark (band)
    number_achieved_A = 0
    number_achieved_B = 0
    number_achieved_C = 0
    number_achieved_D = 0
    number_achieved_E = 0
    number_achieved_F = 0
    #Checking that the class is not empty
    if Class[0] != None:
        for student in Class:
            #Adding to counter based on the band
            if student.band == "A":
                number_achieved_A = number_achieved_A + 1
            elif student.band == "B":
                number_achieved_B = number_achieved_B + 1
            elif student.band == "C":
                number_achieved_C = number_achieved_C + 1
            elif student.band == "D":
                number_achieved_D = number_achieved_D + 1
            elif student.band == "E":
                number_achieved_E = number_achieved_E + 1
            elif student.band == "F":
                number_achieved_F = number_achieved_F + 1
    else:
        pass
    
    #Calculating the percentage each student achieving a mark based on previous counters
    total = number_achieved_A + number_achieved_B + number_achieved_C + number_achieved_D + number_achieved_E + number_achieved_F
    if total != 0:
        percent_achieved_A = number_achieved_A / total * 100
        percent_achieved_B = number_achieved_B / total * 100
        percent_achieved_C = number_achieved_C / total * 100
        percent_achieved_D = number_achieved_D / total * 100
        percent_achieved_E = number_achieved_E / total * 100
        percent_achieved_F = number_achieved_F / total * 100

        #Printing each student with their score and calculated band
        for student in Class:
            print(student.fname, student.lname, student.score, student.band, sep=" ")

        #Printing summary of percentage achieved on each mark (band)
        print()
        print("SUMMARY")
        print(str(percent_achieved_A) + " percent of students achieved a band of A")
        print(str(percent_achieved_B) + " percent of students achieved a band of B")
        print(str(percent_achieved_C) + " percent of students achieved a band of C")
        print(str(percent_achieved_D) + " percent of students achieved a band of D")
        print(str(percent_achieved_E) + " percent of students achieved a band of E")
        print(str(percent_achieved_F) + " percent of students achieved a band of F")
    else:
        print("This class is currently empty")
#######################################################################################################
#Starting Program
Login()