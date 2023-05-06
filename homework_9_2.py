import typing as t


def input_error(func):
    def inner(command, *inputs):
        if command == 'add' or command == 'change':
            if inputs and len(inputs) == 2:
                return func(*inputs)
            else:
                return 'Give me name and phone please'
        if command == 'phone':
            if inputs and len(inputs) == 1:
                return func(*inputs)
            else:
                return 'Enter user name'
        if command == 'hello':
            if len(inputs) > 0:
                return func(inputs[0])
            return func(None)
        if command == 'show':
            if inputs and len(inputs) == 1:
                return func(*inputs)
            else:
                return 'Show must be with parameter `all` or name'

        return 'Not correct validation'

    return inner


info_dict = {}


@input_error
def hello(n):
    if n is None:
        return "How can I help you?"
    else:
        return "Hello " + n + ", how can I help you?"


@input_error
def adding(name, phone):
    info_dict[name] = phone
    return 'add complited'


@input_error
def change(n, p):
    for name in info_dict.keys():
        if name.lower() == n.lower():
            info_dict[name] = p
            return 'Number is changed'
    return 'Name is not found'


@input_error
def phone(name):
    for n, number in info_dict.items():
        if name.lower() == n.lower():
            return number


@input_error
def show(n):
    info_line = ''
    if n == 'all':
        for name, number in info_dict.items():
            info_line += name + '\t| ' + number + '\n'
    else:
        for name, number in info_dict.items():
            if n.lower() in name.lower():
                info_line += name + '\t| ' + number + '\n'
    return info_line


commands = {
    'hello': hello,
    'hi': hello,
    'add': adding,
    'show': show,
    'change': change,
}

exit_commands = [
    'good bye',
    'exit',
    'close'
]


def main_example():
    while True:
        command, *data = input().strip().split(' ', 1)
        if command in exit_commands:
            print('Good Bye!')
            break
        elif (handler := commands.get(command)) is not None:
            if data:
                data = data[0].split(',')
            result = handler(command, *data)
        else:
            result = "Not correct command"
        print(result)


if __name__ == "__main__":
    main_example()
