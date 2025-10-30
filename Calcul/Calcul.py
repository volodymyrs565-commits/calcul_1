def calc(a, op, b):
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        return "Error: enter numbers."
    if op == '+':
        return a + b
    if op == '-':
        return a - b
    if op == '*':
        return a * b
    if op == '/':
        if b == 0:
            return "Error: division by zero."
        return a / b
    return "Unknown operator. Use + - * /"

def repl():
    print("Console calculator. Format: number operator number (e.g. 2 + 3)")
    print("Type 'exit' or 'quit' to leave.")
    while True:
        try:
            s = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExit.")
            break
        if not s:
            continue
        if s.lower() in ('exit','quit'):
            print("Exit.")
            break
        parts = s.split()
        if len(parts) == 3:
            a, op, b = parts
            print(calc(a, op, b))
        else:
            for op in ['+','-','*','/']:
                if op in s:
                    left, right = s.split(op, 1)
                    print(calc(left.strip(), op, right.strip()))
                    break
            else:
                print("Invalid format. Use: number operator number")

if __name__ == "__main__":
    repl()
