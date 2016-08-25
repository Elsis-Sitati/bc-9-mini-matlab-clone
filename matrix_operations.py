class Matrix(object):

    def __init__(self):
        pass

    def create_matrix(self, arguments):
        arguments = str(arguments)
        # i am assuming its a 2*3 matrix
        if arguments.find(";"):
            arguments.replace("[", "")
            arguments.replace("]", "")
            a, b = arguments.split(";")
            return a, b
        else:
                # if its just a list being passed
            arguments.replace("[", "")
            arguments.replace("]", "")
            return arguments

    def create_vector(self, zeros, columns):
        pass

    def add_matrix(self, number):
        pass

    def transpose_matrix(self, matrix):
        pass

    def concatenate_matrix(self, matrix):
        pass

    def find_inverse(self, original):
        pass
