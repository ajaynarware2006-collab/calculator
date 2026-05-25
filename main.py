from operations import add,multiply,divide,subtact
from utils import get_number
from history import read_history,save_history,clear_history

#MENU SYSTEM
def show_menu():
    print()
    print("Press 1 for Addition")
    print("Press 2 for subtraction")
    print("Press 3 for multiplaction")
    print("Press 4 for division")
    print("Press '=' for Answer")
    print()

def show_setting():
    print()
    print("Press 1 to show history")
    print("Press 2 to clear history")
    print("Press 3 to exit")
    print("Press any other key for another calculation")
    print()

def special_operations():
    if n==5:
        print(read_history())
    elif n==6:
        clear_history()
        print("History Cleared")


history=""
while True:

    #FUNCTION DISPATCHING
    operations={
        "1":add,
        "2":subtact,
        "3":multiply,
        "4":divide,
    }
    #FUNCTION SYMBOLE
    operations_symbol={
        "1":"+",
        "2":"-",
        "3":"x",
        "4":"/"
    }

    #PERFORMING OPEARTION
    #WITH EXCEPTION HANDLING 
    print("=====CALCULATOR====")
    print()
    num1=get_number()
    while True:
        if history =="":
            show_menu()
            n=input("Your choice --> ")
            if n=="=":
                print()
                print(f"Answer is {num1}")
                history(num1)
                break

            elif int(n)>4 or int(n)<1:
                print()
                print("Please enter number between 1 to 4 or press '=' omly ")

            else:
                try:
                    num2=get_number()
                    operation=operations[n]
                    result=operation(num1,num2)
                    history=f"{num1} {operations_symbol[n]} {num2}"
                except KeyError:
                    print("Please enter valid key")
        else:
            show_menu()
            x=input("Your choice --> ")
            if x=="=":
                history=history+f" = {result}"
                print()
                print(f"Answer is {result}")
                save_history(history)
                break

            elif int(x)>4 or int(x)<1:
                print()
                print("Please enter number between 1 to 4 or press '=' omly ")

            else:
                try:
                    num_next=get_number()
                    operation=operations[n]
                    new_result=operation(result,num_next)
                    history=history+f" {operations_symbol[x]} {num_next}"
                except KeyError:
                    print()
                    print("Please enter valid choice ")

    final_choice=""
    while True:
        show_setting()
        setting_choice=input("Enter your choice ")
        if setting_choice=="1":
            print(read_history())
        elif setting_choice=="2":
            clear_history()
        else:
            final_choice+=setting_choice
            break
    if final_choice=="3":
        break
