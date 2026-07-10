def main():
    fract = input("Fraction: ")
    x = convert(fract)
    print(gauge(x))

def convert(fraction):

            fraction = fraction.split('/')
            fuel = [int(i) for i in fraction] # type conversion to int from str
            if fuel[1] != 0:
                if fuel[0] <= fuel[1]:
                    x = int((fuel[0]/fuel[1]) * 100) # nearest integer percentage
                    return x
                else:
                    raise (ValueError)
            else:
                raise (ZeroDivisionError)

def gauge(percentage):
        if percentage <= 1:
            return "E"
        elif percentage >= 99:
            return "F"
        else:
            return f'{percentage}%'

if __name__ == "__main__":
     main()
