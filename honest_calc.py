# write your code here
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

get_result = False
memory = 0.0
msg_ = (msg_0, msg_1, msg_2, msg_3, msg_4, msg_5, msg_6, msg_7, msg_8, msg_9, msg_10, msg_11, msg_12)


def is_one_digit(v):
    return True if (-10 < v < 10 and v.is_integer()) else False


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_6
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg = msg + msg_7
    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg = msg + msg_8
    if not(msg == ""):
        msg = msg_9 + msg
        print(msg)


def calculator(x, y, operator):
    if operator == "+":
        return x + y
    elif operator == "-":
        return x - y
    elif operator == "*":
        return x * y
    elif operator == "/":
        if y == 0:
            return msg_3
        else:
            return x / y


while not get_result:
    print(msg_0)
    calc = input().split()
    x = calc[0]
    y = calc[2]
    oper = calc[1]
    if x == "M":
        x = memory
    if y == "M":
        y = memory
    if not(str(x).replace('.', '', 1).isdigit() and str(y).replace('.', '', 1).isdigit()):
        print(msg_1)
    elif not(oper in ['+', '-', '*', '/']):
        print(msg_2)
    else:
        check(float(x), float(y), oper)
        result = calculator(float(x), float(y), oper)
        print(result)
        if result == msg_3:
            get_result = False
        else:
            while True:
                print(msg_4)
                store_result = input()
                if store_result == "y":
                    if is_one_digit(result):
                        msg_index = 10
                        while True:
                            print(msg_[msg_index])
                            answer = input()
                            if answer == "y":
                                if msg_index < 12:
                                    msg_index += 1
                                else:
                                    memory = result
                                    break
                            elif answer == "n":
                                break
                            else:
                                break
                    else:
                        memory = result
                    break
                if store_result == "n":
                    break
            while True:
                print(msg_5)
                continue_calc = input()
                if continue_calc == "y":
                    get_result = False
                    break
                if continue_calc == "n":
                    get_result = True
                    break
