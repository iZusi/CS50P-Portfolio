def convert(msg):
    msg = msg.replace(':)', '🙂')
    msg = msg.replace(':(', '🙁')

    print(msg)

def main():
    prompt = input('')
    convert(prompt)

main()
