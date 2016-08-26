from __future__ import unicode_literals
from prompt_toolkit import prompt
from prompt_toolkit.history import InMemoryHistory
from matrix_operations import Matrix
import pickle
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

        elif "+" in text:
            container = text.split("+")
            print variables[container[0].strip()].add_matrix(int(container[1].strip()))

        elif "zeros" in text:
            # find value for column in string and convert it to an integer
            columns = int(text[-2])
            # find value for row in a string and convert it to an integer
            rows = int(text[-4])
            # loop through rows
            for row in range(rows):
                # loop through the column
                for col in range(columns):
                    print "0 \t",
                # outer loop
                print "\n"

        elif "," in text:
            a = Matrix()
            b = int(text[-2])
            matrix = Matrix()
            concat = matrix.concatenate_horizontaly(a, b)
            print concat


if __name__ == '__main__':
    main()
