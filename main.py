import random

MAX_LINES = 3                                           # Max amount of lines
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():        # Loop thru the dictionaries key and values
        for _ in range(symbol_count):                   # Iterate n times for the symbol count/ A->2->iterate 2 times
            all_symbols.append(symbol)                  # Append every itteration to all_symbols

    columns = []
    for _ in range(cols):                               #Generate a column for every single column we have
        column = []
        current_symbols = all_symbols[:]                # Make a copy of the symbols list 
        for _ in range(rows):                           # Loop thru the number of values we need to generate which is the number of rows
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns):                        # Transpose the columns
    for row in range(len(columns[0])):                  #Loop thru the lenght of the columns thus making rows
        for i, column in enumerate(columns):            # loop and enumerate thru every column
            if i != len(columns) - 1:                   # Cheks if its the last item
                print(column[row], end=" | ")           # Prints every first item on the column thus making a row
            else:
                print(column[row], end="")              # Prints without "|" if its the last item
            
        print()                                         # Prints a new line for the next row



def deposit():
    while True:
        user_deposit = input("What would you like to deposit? $") # Get the user deposit amount
        if user_deposit.isdigit():
            user_deposit = int(user_deposit) # Converts string to int for later arithmetic
            if user_deposit > 0: # Chekcs if the deposit amount is greater than 0.
                break
            else:
                print("Deposit must be greater than $0.")
        else:
            print("Deposit must be a number.")

    return user_deposit


def get_number_of_lines():
    while True:
        number_of_lines = input(f"Enter the number of lines to bet on (1 - {MAX_LINES}): ")
        if number_of_lines.isdigit():
            number_of_lines = int(number_of_lines)
            if 1 <= number_of_lines <= MAX_LINES: # Cheks if number of lines is greater than zero and less than or equal to MAX_LINES->3
                break
            else:
                print(f"Please enter a valid number of lines (1 - {MAX_LINES})")
        else:
            print("Please enter a number.")

    return number_of_lines


def get_bet_amount():
    while True:
        bet_amount = input(f"Enter the amount you want to bet on each line (${MIN_BET} - ${MAX_BET}): $")
        if bet_amount.isdigit():
            bet_amount = int(bet_amount)
            if MIN_BET <= bet_amount <= MAX_BET: # Check if the bet amount is greater than the MIN and equal or less than the MAX
                break
            else:
                print(f"Please enter a valid amount for a bet (${MIN_BET} - ${MAX_BET})")
        else:
            print("Please enter a number.")

    return bet_amount


def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet_amount()
        total_bet = bet * lines
        if total_bet <= balance:                        # Checks if the total bet is greater than the deposit
            break
        else:
            print(f"You do not have enough to bet that amount, balance: ${balance}")

 
    print(f"You are betting ${bet} on {lines} lines. Total bet is ${total_bet}.")

    slots =  get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)

main()
