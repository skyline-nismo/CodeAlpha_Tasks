# Importing library
import yfinance as yf


def add_stock():  # function for adding stock in portfolio
    print(f"{' ':{'*'}^60}")
    symbol = input("Enter stock symbol: ")
    quantity = int(input("Enter number of stocks: "))
    try:
        stock_data = yf.Ticker(symbol)
        current_price = stock_data.history(period="1d")["Close"].iloc[0]
        portfolio[symbol] = {"quantity": quantity, "price": current_price}
        print(f"{quantity} {symbol} stocks added to your portfolio at ${current_price:.2f} each.")
        print(f"{' ':{'*'}^60}")
    except:
        print(f"Error fetching data for {symbol}. Please check the stock symbol.")
        print(f"{' ':{'*'}^60}")


def display_portfolio():  # function for displaying complete portfolio
    print(f"{' ':{'*'}^60}")
    print("\nYour portfolio:")
    for symbol, data in portfolio.items():
        print(f"{symbol}: {data['quantity']} stocks at ${data['price']:.2f} each")
    print(f"{' ':{'*'}^60}")


def delete_stock():  # function for deleting stock from portfolio
    print(f"{' ':{'*'}^60}")
    symbol = input("Enter stock symbol to delete: ")
    if symbol in portfolio:
        quantity = int(input("Enter number of stocks to delete: "))
        if portfolio[symbol]["quantity"] >= quantity:
            portfolio[symbol]["quantity"] -= quantity
            print(f"{quantity} {symbol} stocks removed from your portfolio.")
            print(f"{' ':{'*'}^60}")
        else:
            print(f"Insufficient {symbol} stocks in your portfolio.")
            print(f"{' ':{'*'}^60}")
    else:
        print(f"{symbol} not found in your portfolio.")
        print(f"{' ':{'*'}^60}")


print(f"{' ':{'*'}^60}")
print(f"{'WELCOME TO THE STOCK PORTFOLIO MANAGER':{' '}^60}")
print(f"{' ':{'*'}^60}")
portfolio = {}  # Dictionary to store stock data
while True:  # While loop for continuously repetition
    print("\nOPTIONS :\n")  # Options for performing tasks
    print("Enter  1 | TO ADD STOCKS IN PORTFOLIO")
    print("Enter  2 | TO DISPLAY PORTFOLIO")
    print("Enter  3 | TO DELETE STOCKS")
    print("Enter  4 | TO EXIT")
    choice = input("Enter Your Choice :- ")  # Taking input from the user
    if choice == "1":
        add_stock()
    elif choice == "2":
        display_portfolio()
    elif choice == "3":
        delete_stock()
    elif choice == "4":
        print(f"{' ':{'*'}^60}")
        print("Exiting the program.\n\nHave a great day!")
        print(f"{' ':{'*'}^60}")
        break
    else:
        print(f"{' ':{'*'}^60}")
        print("Invalid choice!!!\nPlease select from 1, 2, 3, or 4.")
        print(f"{' ':{'*'}^60}")
