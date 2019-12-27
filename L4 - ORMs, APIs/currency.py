import requests

def main():
    res = requests.get("http://data.fixer.io/api/latest?access_key=70ae574887f99c29be8759108396733a&symbols=PHP")
    if res.status_code != 200:
        raise Exception("ERROR: API request unsuccessful.")
    data = res.json()
    rate = data["rates"]["PHP"]
    print(f"1 EUR is equal to {rate} PHP.")


if __name__ == "__main__":
    main()
