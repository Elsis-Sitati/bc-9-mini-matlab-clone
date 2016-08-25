from __future__ import unicode_literals
from prompt_toolkit import prompt
from prompt_toolkit.history import InMemoryHistory
from matrix_operations import Matrix

variables = {}


def main():
    history = InMemoryHistory()

    while True:
        text = prompt("> ", history=history)
        text = text.strip()
        if text == 'exit':
            print('GoodBye!')
            break

        # if an equal sign is in text then is making an assignment
        
        elif "=" in text:
            container = text.split('=')
            # putting data to variables dictionary
            variables[container[0].strip()] = Matrix(container[1].strip())

        elif text in variables.keys():
            print variables[text].data

        elif "\'" in text:
            print variables[text[0]].transpose_matrix()




if __name__ == '__main__':
    main()
