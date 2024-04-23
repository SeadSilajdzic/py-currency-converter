import requests

API_KEY = "fca_live_jK9Xi6T5GSzvYr9OHXBaoNVsw09v88CyHQ25hLhP"
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

CURRENCIES = ["USD", "EUR", "CAD", "CHF"]


def convert_currency(base):
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"

    try:
        response = requests.get(url)
        data = response.json()
        return data["data"]
    except Exception as e:
        print("Invalid currency. For now we support conversions for " + ",".join(CURRENCIES))
        return None


while True:
    base = input("Enter the base currency (q for quit): ").upper()

    if base == "Q":
        break

    data = convert_currency(base)

    if not data:
        continue

    del data[base]
    for ticker, value in data.items():
        print(f"{ticker}: {value}")