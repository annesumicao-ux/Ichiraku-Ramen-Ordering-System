def get_valid_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("[!] Error: Value must be a positive integer.")
        except ValueError:
            print("[!] Error: Invalid entry! Please enter numbers only.")