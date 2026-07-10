def main():
    time = input('What time is it? ')
    time = convert(time)
    if 7 <= time <= 8:
        print('breakfast time')
    elif 12 <= time <= 13:
        print('lunch time')
    elif 18 <= time <= 19:
        print('dinner time')


def convert(time):

    hour,minute = time.split(':')
    hour = float(hour)
    hour2 = float(minute) / 60 # 1 hour = 60 minutes
    time = hour + hour2
    return time

if __name__ == '__main__':
    main()