
def num_division():
    try:
        x = int(input("Please enter a number: "))
        return x/0
    except ValueError as error:
        print("OOps you did not input a number")
        print(error)
       # raise error
    except ZeroDivisionError as e:
        print("You cannot divide by zero")
        print(e)
        #raise e
    finally:
        print("Program Finished")


num_division()
print("Done")