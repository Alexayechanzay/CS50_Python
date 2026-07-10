def main():
    string = input()
    processed_value = convert(string)
    print(processed_value)

def convert(string):
    string = string.replace(':)','🙂')
    string = string.replace(':(','🙁 ')
    return string

main()