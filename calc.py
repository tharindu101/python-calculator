# Perform simple arithmetic encoded in an input string:
# '1 + 2' -> 3, or '1 - 2' -> -1.
def compute(expression):
    num0, operator, num1 = expression.split(' ')
    num0, num1 = float(num0), float(num1)
    if operator == '+':
        return num0 + num1
    elif operator == '-':
        return num0 - num1
    elif operator == '*':
        return num0 * num1
    elif operator == '/':
        return num0 / num1
    else:
        print('unknown operator!')
        return None

# My contribution : To accept user input
if __name__ == "__main__":
    expr = input("Enter an expression (e.g., 3 + 4): ")
    result = compute(expr)
    if result is not None:
        print("Result:", result)
