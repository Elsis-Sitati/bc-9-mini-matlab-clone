class Matrix(object):

    def __init__(self, list1):

        data = []
        # i assuming all inputs will be separated by commas
        # take element starting from one after opening bracket and the last
        # before closing bracket
        list2 = list1[1:len(list1) - 1]
        # collect elements separated by semicolon
        list3 = list2.split(";")

        # if it finds that it is just an array or matrix with one row
        if len(list3) == 1:
            element = list3[0]
            element1 = element.split(",")
            # converting each element in element1 into a string
            # element3 is a list of matrix
            element3 = map(int, element1)
            # appending element3 to data to make it a list of list
            data.append(element3)

        else:
            for element in list3:
                # spliting elements in list3 by coma
                element1 = element.split(",")
                # element3 is a list of matrix
                element3 = map(int, element1)
                data.append(element3)

    def create_zeros(self, rows, columns):

        pass

    def add_matrix(self, number):
        # fuction for adding
        def add_constant(data, number):
            return data + number
        # using the function in every element in data store
        result = map(add_constant, self.data)
        return result

    def transpose_matrix(self, thematrix):
        return zip(*thematrix)

    def concatenate_matrix(self, matrix):
        pass

    def find_inverse(self, original):
        pass


