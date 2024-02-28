given = input()

def balance(given_input):
    char = []
    if len(given_input) == 1:
        print(0)
        return
    for symbol in given:
        if symbol == "(" or symbol == "[":
            char.append(symbol)
        elif symbol == ")":
            if len(char)==0 or char.pop() != "(":
                print(0)
                return
                
        elif symbol == "]":
            if len(char)==0 or char.pop() != "[":
                print(0)
                return

    if len(char) != 0:
        print(0)
    else:
        print(1)
    

balance(given)