prompt = input('What is the answer to the Great Question of Life, the Universe, and Everything? ').lower().strip()

match prompt:
    case '42'|'forty two'|'forty-two':
        print('Yes')
    case _:
        print('No')
