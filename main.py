from operations import add,multiply,divide,subtact
from utils import get_number
from history import read_history,save_history,clear_history

#MENU SYSTEM
def show_menu():
    print("======CALCULATOR======")
    print()
    print("Press 1 for Addition")
    print("Press 2 for subtraction")
    print("Press 3 for multiplaction")
    print("Press 4 for division")
    print("Press 5 to show history")
    print("Press 6 to clear history")
    print()

def performe_operation():
    operation=operations[n]
    result=operation()
    result_history=f"Result is = {result}"
    history.append(result_history)
    save_history(result_history)
    print(f"Result is -> {result}")

def special_operations():
    if n==5:
        print(read_history())
    elif n==6:
        clear_history()
        print("History Cleared")

history=[]
while True:
    show_menu()

    #TAKING OPEARTION
    #WITH EXCEPTION HANDLING
    try:
        n=int(input("-->"))
    except ValueError:
        print("Enter number only")
    print()

    #FUNCTION DISPATCHING
    operations={
        1:add,
        2:subtact,
        3:multiply,
        4:divide,
    }
    #FUNCTION SYMBOLE
    operations_symbol={
        1:"+",
        2:"-",
        3:"x",
        4:"/"
    }

    #MATH OPERATIONS
    if n in operations:
        performe_operation()

    #SPECIAL OPERATIONS
    special_operations()

    #ASKING FOR MORE OR STOP
    x=input("Do you want another calculation? (y/n): ")
    if x=="n":
        break