class Matrix(object):

    def __init__(self):
        pass

    def create_matrix(self, list1):
        # i assuming all inputs will be separated by commas
        # take element starting from one after opening bracket and the last
        # before closing bracket
        list2 = list1[1:len(list1) - 1]
        # collect elements separated by semicolon
        list3 = list2.split(";")
        # if it finds that it is just an array or matrix with one row
        if len(list3) == 1:
            element = list3[0]
            element.replace(",", " ")
            print element
        else:
            for element in list3:
                    # replace commas with spaces
                element.replace(",", " ")
                print element

    def create_vector(self, zeros, columns):
        pass

    def add_matrix(self, number, number2):
    	pass

    def transpose_matrix(self, thematrix):
        return zip(*thematrix)

    def concatenate_matrix(self, matrix):
        pass

    def find_inverse(self, original):
        pass

