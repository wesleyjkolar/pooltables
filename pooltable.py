from datetime import datetime 
from time import time
time = datetime.now()

class Formatter():
    def __init__(self):
        self.clock = ""

    def timer_format(self, end, start): 
        time = end - start 
        sec = time.total_seconds()
        hours = round(sec / (60 * 60))
        minutes = sec % (60 * 60)                          
        minutes = round(minutes / 60)
        better_timer = f"{hours} hrs : {minutes} min"
        return better_timer

    def clock_format(self, time):
        hour = time.hour
        minute = time.minute
        if minute < 10:
            minute = f"0{minute}"
            self.clock = "AM"                               
        if hour > 12:
            hour -= 12
            self.clock = "PM"
        better_time = f"{hour}:{minute} {self.clock}"
        return better_time

formatter = Formatter()

class Table:
    def __init__(self, number):
        self.number = number
        self.occupied = False
        self.start_time = ""
        self.end_time = ""
        self.time_played = ""
        self.current_time = ""

    def checkout(self):
        if self.occupied == True:
            print("")             
            input(f" Table {self.number} is currently occupied. Press enter to return to main.")
        else:
            self.occupied = True 
            self.start_time = datetime.now() 
            self.end_time = datetime.now() 
            self.time_played = self.end_time - self.start_time 

    def checkin(self): 
        if self.occupied == False: 
            print("")
            input("This table is currently unoccupied, please press enter.")
            return False
        else:
            with open("log.txt", "a") as file:
                file.write(f"Table number:{self.number} \nStart time and Date: {self.start_time} \nEnd time and date: {self.end_time} \nTime Played: {self.time_played}")
                file.write("\n")
            self.occupied = False 
            self.end_time = datetime.now() 
            self.time_played = self.end_time - self.start_time 
            return True
            
class TableManager():
    def __init__(self): 
        self

    def show_menu(self): 
        print("")
        print("++++++++++ University Pool Tables ++++++++++")
        print("---------------------------------------------")
        print("              New table? Enter 1 ")
        print("             Return Table? Enter 2 ")
        print("             View tables? Enter 3 ")
        print("                Quit? Enter q ")
        print("---------------------------------------------")

    def show_tables(self): 
        current_time = datetime.now()
        print("") 
        for table in tables: 
            if table.occupied == True: 
                status = "XXXXXXXXXXXXXX"
            else:
                status = "Available Now" 
            if table.start_time != "": 
                better_clock = formatter.clock_format(table.start_time,) 
                elapsed_time = formatter.timer_format(
                    current_time, table.start_time)
                print(f"Table-{table.number} - {status} -  Start: {better_clock} - Play time: {elapsed_time}") 
            else:
                print(f"Table-{table.number} - {status}") 
    
    def choose_table(self, user_input): 
        while True: 
            try: 
                if user_input == "1":
                    choice = int(input("Enter table number to check out: ")) - 1 

                else:
                    choice = int(input("Enter table number to return: ")) - 1 

                table = tables[choice] 
                return table 
            except ValueError: 
                print("")
                print("Please enter a valid table number:") 
                print("")

    def choices(self, user_input): 
        if user_input == "1":
            print("")
            confirmation = input("New Table? Enter y/n: ") 
            if confirmation == "n":
                print("")
            elif confirmation == "y":
                self.show_tables() 
                table = self.choose_table(user_input)
                table.checkout() 
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
                self.show_tables() 
                all_available = True 
                for table in tables:
                    if table.occupied == True: 
                        all_available = False
                if all_available == True: 
                    print("")
                    input("All Tables are available.  Press enter to continue: ")
                else:
                    table = self.choose_table(user_input)
                    status = table.checkin() 
                    if status == True: 
                        table.start_time = ""
                        self.show_tables()
                        print(f"Table {table.number} has been returned at: {formatter.clock_format(table.end_time)}")
            else:
                print("")
                print("You did not enter a valid response.")
        elif user_input == "3":
            self.show_tables() 

manager = TableManager() 
tables = []
for i in range(1, 13):
    table = Table(i)
    tables.append(table)
user_input = ""
while user_input != "q": 
    manager.show_menu()
    user_input = input("Please enter a choice from the menu above: ")
    manager.choices(user_input)