def get_number():
    while True:
        try:
            n=int(input("Enter number : "))
            return n
        except ValueError:
            print("Enter number only ")

