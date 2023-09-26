def main():
    prompt = input('What is the time? ').strip()

    convert(prompt)


def convert(time):
    hours, minutes = time.split(':')
    hours = float(hours)
    minutes = float(minutes)
    time = hours + (minutes/60)

    if time >= 7.0 and time <= 8.0:
      print('breakfast time')

    elif time >= 12.0 and time <= 13.0:
      print('lunch time')

    elif time >= 18.0 and time <= 19.0:
      print('dinner time')

    return time


if __name__ == "__main__":
    main()
