from datetime import  date
import sys
import inflect
p = inflect.engine()


def calculate_dob(dob_input):
    try:
        # Validate input date format 
        year, mm, dd = int(dob_input [0]), int(dob_input [1]), int(dob_input [2])
    except ValueError:
        sys.exit("Invalid date")
    else:
        # convert to datetime object
        dob = date(year, mm, dd)

        now = date.today()

        # finding the difference
        difference = now - dob

        # return only day attribtue (int type)
        # Assumption: Both time of dob and now is 00:00:00
        return difference.days

def output(day_diff):
    # convert to minutes
    time_diff = day_diff * 24 * 60
    return f"{p.number_to_words(time_diff).replace(" and ",' ')} {p.plural_noun("minute",time_diff)}".capitalize()

def main():
    dob_input = input("Date of Birth: ").strip().split("-")
    day_diff = calculate_dob(dob_input)
    print(output(day_diff))


if __name__ == "__main__":
    main()
