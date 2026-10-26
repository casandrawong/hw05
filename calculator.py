

def calculating(first, operator, sec):
    if operator == "+":
        return first + sec
    elif operator == "-":
        return first - sec
    elif operator == "*":
        return first*sec
    elif operator == "/":
        if sec == 0:
           return None
        else:
           return first/sec
    else:
        return None

def main():
    while True:
        operator = ["+", "-", "*", "/"]
        first = (input("First number(or q): "))
        
        if first == "q":
         quit()
         
        first = float(first)
        operator = input("Operator (+ - * /): ")
        sec = float(input("Second number: "))
    
        answer = calculating(first, operator, sec)
        if answer == None:
           print("Cannot calculate that")
        else:
           print(f"Result {answer}")

if __name__ == "__main__":
    main()

    