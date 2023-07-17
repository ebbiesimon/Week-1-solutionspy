def usd_to_naira_converter():
    usd = float(input("Enter the amount in USD: "))
    exchange_rate = 424.55  # Assuming the exchange rate is 1 USD = 424.55 NGN
    naira = usd * exchange_rate
    print(f"{usd} USD is equivalent to {naira} NGN.")

usd_to_naira_converter()
