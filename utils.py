def get_number():
    while True:
        try:
            n=int(input("Please enter your number : "))
            return n
        except ValueError:
            print("Enter number only ")

