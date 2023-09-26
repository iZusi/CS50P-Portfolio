def main():
    while True:
        try:
            fraction = input('Fraction: ')
            percentage = convert(fraction)
            result = gauge(percentage)
            print(result)
            break
        except ValueError as ve:
            print(ve)
        except ZeroDivisionError as zde:
            print(zde)

def convert(fraction):
    try:
        x, y = fraction.split('/')
        x = int(x)
        y = int(y)

        if not (isinstance(x, int) and isinstance(y, int)):
            raise ValueError()

        if x > y:
            raise ValueError()

        if y == 0:
            raise ZeroDivisionError()

        z = (x / y) * 100
        z = round(z)

        return z
    except(ValueError, ZeroDivisionError):
        raise ValueError("Invalid fraction format.")

def gauge(percentage):
    z = percentage

    if z <= 1:
        return 'E'
    elif z < 99:
        return f'{z}%'
    elif z <= 100:
        return 'F'

if __name__ == "__main__":
    main()
