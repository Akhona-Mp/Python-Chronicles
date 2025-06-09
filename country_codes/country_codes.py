import re

locations = {"+1": "United States and Canada",
            "+44": "United Kingdom",
            "+62": "Indonesia",
            "+86": "China","+91": "India",
            "+27": "South Africa",}

def main():
    pattern = r"(\+\d{1,3})-\d{3}-\d{4}"
    number = input("Number: ")

    match = re.search(pattern, number)
    if match:
        country_code = match.group(1)
        if country_code in locations:
            print(f"Country: {locations[country_code]}")
        else:
            print("Country: Unknown")
    else:
        print("Invalid number format")

if __name__ == "__main__":
    main()