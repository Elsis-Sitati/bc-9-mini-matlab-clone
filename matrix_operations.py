class Matrix(object):

    def __init__(self, list1):

        self.data = []
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
            self.data.append(element3)

        else:
            for element in list3:
                # spliting elements in list3 by coma
                element1 = element.split(",")
                # element3 is a list of matrix
                element3 = map(int, element1)
                self.data.append(element3)

    def add_matrix(self, number):
        '''function for adding '''
        # loop through the throughs
        for row in range(len(self.data)):
            # loop through each item in the row
            for items in range(len(self.data[row])):
                # access each time in the row and then add the constant
                self.data[row][items] += number

        return self.data

    def transpose_matrix(self):
        ''' map the matrices to create a list of tuples'''

        transposed_matrix = []
        # getting a list of tuples that have been transposed
        for item in zip(*self.data):
            # converting each tuple into a list and storing them in
            # transposed_matrix
            transposed_matrix.append(list(item))
        return transposed_matrix

    def concatenate_horizontaly(self, a, b):
        '''method to return horizontal concatenation of matrices'''
        # going through the rows in the list
        for i in range(len(a)):
            # add a matching row  number from the other matrix to the rows
            a[i] = self.data.extend(b[i])
        return self.data

    def contacatenate_vertically(self, matrix):
        # going through the rows in the list
        for i in range(len(self.data)):
            # adding rows to the last element in the row
            self.data[i + len(self.data)] = matrix[i]
        return self.data

    def find_inverse(self, original):
        pass
