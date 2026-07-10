import re

locations = {
    "+1": "United States and Canada",
    "+62": "Indonesia",
    "+505": "Nicaragua",
}

def main():
    number = input("Enter Ph Number: ")
    pattern = r"(?P<country_code>\+\d{1,3}) \d{3}-\d{3}-\d{4}"

    match = re.search(pattern, number)
    if match:
        country_code = match.group("country_code")
        print(f"Valid.\nCalling from {locations[country_code]}")
    else:
        print("Invalid")

main()