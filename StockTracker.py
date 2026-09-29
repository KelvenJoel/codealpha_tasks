"""
Simple tracker that calculates the total investment based on manually defined stock.
Create a predefined dictionary of tickers and their unit price
User calls the stock ticker names and buy a quantity of the stock
Display total investment
Save result in a .csv or .txt file(optional):TICKER NAME,UNIT PRICE,NO BOUGHT,TOTAL PRICE
Add-ons: 
    -if ticker not in the predefined list, tell user not found
    -Don't accept wrong spelling,negative amount
"""
import csv

ticker_dict = {
                "AAPL":319.97,"NVDA":230,"MSFT":499.70,"AMZN":258.51,
                "GOOGL":342.40,"META":520.26,"AVGO":289.96,"TSLA":297.96,
                "ABBV":263.09,"ABCB":84.28,"ABCL":11.55,"ABEO":5.36,"AAL":12.70,
                "AXP":290.97,"SMTC":57.50,"KO":88.08,"MCD":250.25,"MRK":144.10,
                "INTC":101.05,"AGMH":0.71,"AAG":154.03,"AA":47.28
              }

def available_stock(sort_choice=0):#SORT IT
    """
    Pair tickers to their unit price and sort based on user's preference
    """
    stock_dict = {
                    "AAPL (Apple Inc.)":319.97,"NVDA (Nvidia Corp)":230,
                    "MSFT (Microsoft Corp)":499.70,"AMZN (Amazon.com)":258.51,
                    "GOOGL (Alphabet Inc.)":342.40,"META (Meta Platforms,Inc.)":520.26,
                    "AVGO (Broadcom Inc.)":289.96,"TSLA (Tesla, Inc)":297.96,
                    "ABBV (AbbVie Inc)":263.09,"ABCB (Ameris Bancorp)":84.28,
                    "ABCL (AbCellera Biologics Inc)":11.55,"ABEO (Abeon Therapeutics Inc.)":5.36,
                    "AAL (American Airlines Group Inc.)":12.70,"AXP (American Express Company)":290.97,
                    "SMTC (Semtech Corporation)":57.50,"KO (The Coca-Cola Company)":88.08,
                    "MCD (McDonald's Corporation)":250.25,"MRK (Merck & Co., Inc.)":144.10,
                    "INTC (Intel Corporation)":101.05,"AGMH (AGM Group Holdings Inc.)":0.71,
                    "AAG (Agilent Technologies,Inc.)":154.03,"AA (Alcoa Technologies,Inc.)":47.28
                  }

    def display_order(option):
        """
        Convert dictionary to 2D-list. Sort the list based on the ordering
        option user gives. Return the ordered choice.
        """
        stock_list= []
        for ticker,unit_price in stock_dict.items():
            stock_list.append([ticker,unit_price])

        if sort_choice == 2:
            order_by_choice = sorted(stock_list,key=lambda x:x[1],reverse=True)
        else:
            order_by_choice = sorted(stock_list,key=lambda x:x[sort_choice])
        return order_by_choice
    
    print(f'\n{"TICKER":<40}UNIT PRICE (USD)')
    for ticker,unit_price in display_order(sort_choice):
        print(f'{ticker:<40}$ {unit_price}')

    return display_order(sort_choice)

def main_program():
    with open("My Investment.csv",mode="w",newline="") as file:#create the csv file
        writer = csv.writer(file)
        writer.writerow(["Ticker","Unit price","Amount Purchased","Shares owned"])

    print(f'{"---- INVESTMENT TRACKER ----":>40}')#Cover 40 spaces.spaces on the left
    user_name = input("Enter your name:-> ").title()
    print(f"Welcome {user_name}\nBuy stocks to start investing.")
    print("Sort stocks in which order (enter the number by the choice to sort)")
    print("0. Alphabetical\n1. Ascending order of unit price\n2. Descending order of unit price")
    sort_choice = int(input("Choice: "))#any error capturing????
    available_stock(sort_choice) 
    total_investment_list = []# list for tracking the investment amounts . Try and change it by accessing the column in the csv
    another_purchase = True
    while another_purchase:
        investment_name = input("\nEnter the ticker symbol of the stock you want to invest in: ").upper()   
        if investment_name not in ticker_dict.keys():
            print("\nTicker not found")
        else:#Ticker name found
            try:
                invest_amount = float(input(f"How much do you want to pay for {investment_name} stocks: $ "))
            except ValueError:
                print(f'\nOnly digits are allowed: you included strings')
            else:    
                if invest_amount <0:
                    print("Negative amounts are NOT allowed")
                else:#positive amount
                    total_investment_list.append(invest_amount)
                    shares_owned = invest_amount/ticker_dict.get(investment_name)
                    with open("My Investment.csv",mode="a",newline="") as file: #Error:when u buy stock again,past payment disappear
                            writer = csv.writer(file)
                            writer.writerow([investment_name,ticker_dict.get(investment_name),invest_amount,f"{shares_owned:.3f}"])
                    

            print(f"\nYou have invested a total of $ {sum(total_investment_list)} across all stocks")
        try:
            another_purchase=int(input("\nDo you want to make another purchase?\n0. Exit\n1. Continue\nChoice:  "))
        except ValueError:
            print("Alphabets are not allowed. Use the numbers associated with your choice")
        
        if another_purchase == False:
            print(f"\nSee you next time, {user_name}")
main_program()
