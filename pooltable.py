from datetime import datetime 
from time import time
day = datetime.now()
time = datetime.now()
# table class what attributes should be assigned to table
class Table:
    def __init__(self, number):
        self.number = number
        self.occupied = False
        self.start_time = ""
        self.end_time = ""
        self.time_played = ""
        self.current_time = ""
# checkout function
    def checkout(self):
        if self.occupied == True:
            print("")             #if/else preventing user from selecting a table that is already checked out
            input(f" Table {self.number} is currently occupied. Press enter to return to main.")
        else:
            self.occupied = True #make it true
            self.start_time = datetime.now() #start time
            self.end_time = datetime.now() #end time
            self.time_played = self.end_time - self.start_time #time elapsed

    def checkin(self): #check in function
        if self.occupied == False: #if user hits a table that is already turned in, it doesnt break to program
            print("")
            input("This table is currently unoccupied, please press enter.")
            return False
        else:
            self.occupied = False # if its an occupied table that is correct because its being turned in
            self.end_time = datetime.now() #end time
            self.time_played = self.end_time - self.start_time #elapsed time
            return True 

class Formatter():
    def __init__(self):
        self.clock = ""

    def timer_format(self, end, start): 
        time = end - start 
        sec = time.total_seconds()
        hours = round(sec / (60 * 60))
        minutes = sec % (60 * 60)                          #timer formatting
        minutes = round(minutes / 60)
        better_timer = f"{hours} hrs : {minutes} min"
        return better_timer

    def clock_format(self, time):
        hour = time.hour
        minute = time.minute
        if minute < 10:
            minute = f"0{minute}"
            self.clock = "AM"                               #more formatting
        if hour > 12:
            hour -= 12
            self.clock = "PM"
        better_time = f"{hour}:{minute} {self.clock}"
        return better_time

formatter = Formatter()   #gives an easily callable variable for time and date formatting

class TableManager():
    def __init__(self, day):
        self.day = day

    def show_menu(self): #function to call menu screen
        print("")
        print("++++++++++ University Pool Tables ++++++++++")
        print("---------------------------------------------")
        print("              New table? Enter 1 ")
        print("             Return Table? Enter 2 ")
        print("             View tables? Enter 3 ")
        print("                Quit? Enter q ")
        print("---------------------------------------------")

    def show_tables(self): #function that shows tables when use enters 3
        current_time = datetime.now()
        print("") #looks nice
        for table in tables: #looks nice
            if table.occupied == True: #if someone is using it that means its (true)ly occupied, status shows X
                status = "X"
            else:
                status = "Available Now" #otherwise, shows available
            if table.start_time != "": #!= (if start time is not "null") the time checked out and whatnot
                better_clock = formatter.clock_format(table.start_time,) 
                elapsed_time = formatter.timer_format(
                    current_time, table.start_time)
                print(f"Table-{table.number} - {status} -  Start: {better_clock} - Play time: {elapsed_time}") #display when user enters 3
            else:
                print(f"Table-{table.number} - {status}") #if it is null show available status
    
    def choose_table(self, user_input): #choose table function
        while True: #while loop so it prompts over
            try: #try thing we learned the other day
                if user_input == "1":
                    choice = int(input("Enter table number to check out: ")) - 1 #because we have int we have try/except

                else:
                    choice = int(input("Enter table number to return: ")) - 1 #same as above

                table = tables[choice] #table equals table-int user inputs in easily callable variable
                return table #calls that variable
            except ValueError: #exception to try 
                print("")
                print("Please enter a valid table number:") #nice looking except statement
                print("")

    def choices(self, user_input): #function for choices
        if user_input == "1":
            print("")
            confirmation = input("New Table? Enter y/n: ") #confirms
            if confirmation == "n":
                print("")
            elif confirmation == "y":
                self.show_tables() #calls show table availability function
                table = self.choose_table(user_input)
                table.checkout() #calls checkout function
                self.show_tables() 
                print("")
                print(f"Table {table.number} has been checked out at: {formatter.clock_format(table.start_time)}")
            else:
                print("")
                print("You did not enter a valid response. Please try again.")

        elif user_input == "2":
            print("")
            confirmation = input(
                "Return a pool table? Enter y/n: ")
            if confirmation == "n":
                print("")
            elif confirmation == "y":
                self.show_tables() #show table function
                all_available = True #if all are available
                for table in tables:
                    if table.occupied == True: #tells it how to check if all tables are available
                        all_available = False
                if all_available == True: #if its true this isnt what you want
                    print("")
                    input("All Tables are available.  Press enter to continue: ")
                else:
                    table = self.choose_table(user_input)
                    status = table.checkin() #calls check in function
                    if status == True: 
                        table.start_time = ""
                        self.show_tables()
                        print(
                            f"Table {table.number} has been returned at: {formatter.clock_format(table.end_time)}")
            else:
                print("")
                print("You did not enter a valid response.")
        elif user_input == "3":
            self.show_tables() #calls table when user selects option 3

manager = TableManager(day) 
tables = [] #nice array for the tables
for i in range(1, 13):
    table = Table(i)
    tables.append(table)
user_input = ""
while user_input != "q": #loops it to show menu and choice anytime the answer is not q...so even if its not an option, it wont quit unless you press q
    manager.show_menu()
    user_input = input("Please enter a choice from the menu above: ")
    manager.choices(user_input)