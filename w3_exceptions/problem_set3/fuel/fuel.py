def fuel():
    while True:
        try:
            fuel = input('Fraction: ').split('/')
            fuel = [int(i) for i in fuel]
            x = round((fuel[0]/fuel[1]) * 100)
            if fuel[0] <= fuel[1]:
                if x <= 1:
                    return 'E'
                elif x >= 99:
                    return 'F'
                else:
                    return f'{x}%'
        except (ValueError,ZeroDivisionError):
            pass



print(fuel())
