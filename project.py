info_dict = {}


def hello():
    return "How can I help you?"


def input_error(func):
    def inner(splitted):
        inputs = splitted[1:]
        if splitted[0].lower() == 'add' or splitted[0].lower() == 'change':
            if len(inputs) >= 2:
                return func(inputs)
            else:
                return 'Give me name and phone please'
        if splitted[0].lower() == 'phone':
            if len(inputs) >= 1:
                return func(inputs)
            else:
                return 'Enter user name'

        return 'Not correct validation'

    return inner


@input_error
def adding(inputs):
    info_dict[inputs[0]] = inputs[1]
    return 'add complited'


@input_error
def change(inputs):
    for name in info_dict.keys():
        if name.lower() == inputs[0].lower():
            info_dict[name] = inputs[1]
            return 'Number is changed'
    return 'Name is not found'

@input_error
def phone(inputs):
    for name, number in info_dict.items():
        if inputs[0].lower() == name.lower():
            return number


def show_all():
    info_line = ''
    for name, number in info_dict.items():
        info_line += name + '\t| ' + number + '\n'

    return info_line



def main():
    while True:
        user_input = input("Write your command ")
        splitted = user_input.split(' ')
        result = None
        if user_input.lower() == 'hello':
            result = hello()
        elif user_input.lower() == 'good bye' or user_input.lower() == "close" or user_input.lower() == "exit":
            print('Good Bye!')
            break
        elif splitted[0].lower() == 'add':
            result = adding(splitted)
        elif splitted[0].lower() == 'change':
            result = change(splitted)
        elif splitted[0].lower() == 'phone':
            result = phone(splitted)
        elif user_input.lower() == 'show all':
            result = show_all()
        if result:
            print(result)
        else:
            print('Not correct command')

if __name__ == "__main__":
    main()
