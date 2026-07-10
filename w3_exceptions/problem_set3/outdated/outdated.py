months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True: # infinte loop until the user enters correct format
    user = input("Date: ").strip()
    try:
        # separate by slash (Given that slash is the common delimiter when user enters numerical format for month)
        mm,dd,yyyy = user.split('/')
        if  (1 <= int(mm) <= 12 ) and (1 <= int(dd) <= 31):
            break
    except:
        try:
            # separate by space (Given that space is the common delimiter when use enters textual format for month)
            mm,dd,yyyy = user.split()

            for i in range(len(months)):
                if months[i] == mm.capitalize():
                    mm = int(i+1)

            dd = dd.replace(',','')  # to get rid of , in the date

            if  (1 <= int(mm) <= 12 ) and (1 <= int(dd) <= 31):
                break
        except:
            print()
            pass

print(f"{(yyyy)}-{int(mm):02}-{int(dd):02}")
