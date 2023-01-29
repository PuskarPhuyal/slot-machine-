import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count ={
    "A":4,
    "B":5,
    "C":7,
    "D":9
}

symbol_value ={
    "A":5,
    "B":4,
    "C":3,
    "D":2   
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines



def get_slot_machine_spin(rows, cols, symbols):
    all_symbol = []
    for symbol, symbol_count in symbols.items():
        all_symbol.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbol = all_symbol[:]
        for _ in range(rows):
            value = random.choice(current_symbol)
            current_symbol.remove(value)
            column.append(value)
        columns.append(column)
        
    return columns

def print_slot(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()       


def deposit():
    while True:
        amount=input("How much would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Please enter amount greater then 0.")
        else:
            print("Please enter number.")

    return amount

def get_number_of_lines():
    while True:
        lines=input("Enter the number of lines you would like to select from 1-"+str(MAX_LINES)+" :")
        if lines.isdigit():
            lines = int(lines)
            if 1<= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid lines")
        else:
            print("Please enter a number")
    return lines

def get_bet():
    while True:
        amount=input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET<= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET}-${MAX_BET}.")
        else:
            print("Please enter a number")
    return amount    

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not have enough to bet that amount.Your total balance is ${balance}.")
        else:
            break
    print(f"You are betting ${bet} on {lines} line. Total bet is:${total_bet}")
    slots= get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot(slots)
    winnings, winnings_lines= check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}")
    print(f"You won on:", *winnings_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (press q to quit)")
        if answer == "q":
            break
        balance += spin(balance)
    print(f"You left with ${balance}")




main()

