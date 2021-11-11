# function within a function

def display(venkat):
    def message():
        return "Hi "
    result=message()+venkat
    return result
print(display("\nVenkataraman"))

