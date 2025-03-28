import random
import time

def spin_row():
    symbols = ["🍒", "🍉", "🍋", "🔔", "⭐"]

    return [random.choice(symbols) for _ in range(3)]
    
def print_row(row):
    print("***************")
    print(" | ".join(row))
    print("***************\n")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 3
        elif row[0] == "🍉":
            return bet * 5
        elif row[0] == "🍋":
            return bet * 10
        elif row[0] == "🔔":
            return bet * 20
        elif row[0] == "⭐":
            return bet * 50
    return 0

def main():
    balance = 100

    print("*****************************")
    print(" Welcome to the slot machine")
    print(" Symbols: 🍒 🍉 🍋 🔔 ⭐")
    print(" Made by @Dslime8 on GitHub")
    print("*****************************")

    while balance > 0:
        print(f"Balance: {balance}€")

        bet = input("Enter your bet amount: ")

        if not bet.isdigit():
            print("Invalid input, go back to school dumbass")
            continue

        bet = int(bet)

        if bet > balance:
            print("You are too broke to bet that much")
            continue

        if bet <= 0:
            print("Playing for free I see.. not in my casino")
            continue

        balance -= bet

        row = spin_row()
        print("Spinning...\n")
        time.sleep(1)
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won {payout}€!")
        else:
            print("LMAO ur so bad at luck games, u lost")

        balance += payout

        time.sleep(2)

        pro_tip = " "
        if random.randint(1, 3) == 1:
            pro_tip = "99% of gamblers quit before they win big"
        elif random.randint(1, 3) == 2:
            pro_tip = "Never stop gambling"
        else:
            pro_tip = "You can only lose 100%, but you can win up to 5000%"

        play_again = input("Tip: " + pro_tip + "\nDo you want to spin again? Y/N: ").upper()

        if play_again == "N":
            break
        
    print(" ")
    print("***************************************")
    print(f"Game over! Your balance is {balance}€")
    print("***************************************")
    print(" ")
    input("Press Enter to Exit")



if __name__ == '__main__':
    main()
