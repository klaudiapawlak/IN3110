class Array:
    def __init__(self, shape, *values):

        """
        Initialize an array.
        Elements in values can only contain one type of the following:
        - int
        - float
        - bool
        The number of values should fit with the shape.
        Args:
            shape (tuple): shape of the array as a tuple. A 1D array with n elements will have shape = (n,m).
            *values: The values in the array. These should all be the same data type. Either numeric or boolean.
        Raises:
            ValueError: If the values are not all of the same and valid type.
            ValueError: If the number of values does not fit with the shape (tuple).
        """

        if (shape[0]*shape[1]) == len(values) and isinstance(shape,tuple):
            self.shape = shape
        else:
            raise ValueError("The number of values does not fit with the shape (tuple)")
        for elements in values:
            if isinstance(elements, (int, float, bool)) and isinstance(elements, type(values[0])):
                self.values = values
            else:
                raise ValueError("Array should only contain one data type. Elements can only be of type int, float or bool")
        pass

    def __getitem__(self, item):

        """
        Returns value of item in array.
        Args :
            item (int): Index of value to return.
        Returns :
            value : Value of the given item .
        """
        values = list(self.values)
        print(values)
        s = []
        for i in range(self.shape[0]):
            m = []
            for j in range(self.shape[1]):
                m.append(values[self.shape[0] * i + j])
            s.append(m)
        return s[item]

    def __str__(self):

        """
        Returns a nicely printable string representation of the array.
        Returns:
            str: A string representation of the array.
        """
        if self.shape[1] > 1:
            values = list(self.values)
            s = []
            for i in range(self.shape[0]):
                m = []
                for j in range(self.shape[1]):
                    m.append(values[self.shape[0] * i + j])
                s.append(m)
            return str(s)
        else:
            return str(list(self.values))
        pass

    def __add__(self, other):

        """
        Element-wise adds Array with another Array or number.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to add element-wise to this array.
        Returns:
            Array: the sum as a new array.
        """

        sum = []
        if type(self) == type(other):
            if self.shape == other.shape:
                for i in range(self.shape[0]*self.shape[1]):
                    sum.append(self.values[i] + other.values[i])
        elif isinstance(other,(int, float, bool)):
            for i in range(self.shape[0]*self.shape[1]):
                sum.append(self.values[i] + other)
        else:
            NotImplemented
        return sum
        pass

    def __radd__(self, other):

        """
        Element-wise adds Array with another Array or number.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to add element-wise to this array.
        Returns:
            Array: the sum as a new array.
        """

        sum = []
        if type(self) == type(other):
            if self.shape == other.shape:
                for i in range(self.shape[0]*self.shape[1]):
                    sum.append(other.values[i] + self.values[i])
        elif isinstance(other,(int, float, bool)):
            for i in range(self.shape[0]*self.shape[1]):
                sum.append(other + self.values[i])
        else:
            NotImplemented
        return sum
        pass

    def __sub__(self, other):

        """
        Element-wise subtracts an Array or number from this Array.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to subtract element-wise from this array.
        Returns:
            Array: the difference as a new array.
        """

        difference = []
        if type(self) == type(other):
            if self.shape == other.shape:
                for i in range(self.shape[0]*self.shape[1]):
                    difference.append(self.values[i] - other.values[i])
        elif isinstance(other,(int, float, bool)):
            for i in range(self.shape[0]*self.shape[1]):
                difference.append(self.values[i] - other)
        else:
            NotImplemented
        return difference
        pass

    def __rsub__(self, other):

        """
        Element-wise subtracts this Array from a number or Array.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number being subtracted from.
        Returns:
            Array: the difference as a new array.
        """

        difference = []
        if type(self) == type(other):
            if self.shape == other.shape:
                for i in range(self.shape[0]*self.shape[1]):
                    difference.append(other.values[i] - self.values[i])
        elif isinstance(other,(int, float, bool)):
            for i in range(self.shape[0]*self.shape[1]):
                difference.append(other - self.values[i])
        else:
            NotImplemented
        return difference
        pass

    def __mul__(self, other):

        """
        Element-wise multiplies this Array with a number or array.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to multiply element-wise to this array.
        Returns:
            Array: a new array with every element multiplied with `other`.
        """

        product = []
        if type(self) == type(other):
            if self.shape == other.shape:
                for i in range(self.shape[0]*self.shape[1]):
                    product.append(self.values[i] * other.values[i])
        elif isinstance(other,(int, float, bool)):
            for i in range(self.shape[0]*self.shape[1]):
                product.append(self.values[i] * other)
        else:
            NotImplemented
        return product
        pass

    def __rmul__(self, other):

        """
        Element-wise multiplies this Array with a number or array.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to multiply element-wise to this array.
        Returns:
            Array: a new array with every element multiplied with `other`.
        """

        product = []
        if type(self) == type(other):
            if self.shape == other.shape:
                for i in range(self.shape[0]*self.shape[1]):
                    product.append(other.values[i] * self.values[i])
        elif isinstance(other,(int, float, bool)):
            for i in range(self.shape[0]*self.shape[1]):
                product.append(other * self.values[i])
        else:
            NotImplemented
        return product
        pass

    def __eq__(self, other):

        """
        Compares an Array with another Array.
        If the two array shapes do not match, it should return False.
        If `other` is an unexpected type, return False.
        Args:
            other (Array): The array to compare with this array.
        Returns:
            bool: True if the two arrays are equal (identical). False otherwise.
        """

        if type(self) == type(other):
            if self.shape == other.shape:
                return True
        else:
            return False
        pass

    def is_equal(self, other):

        """
        Compares an Array element-wise with another Array or number.
        If `other` is an array and the two array shapes do not match, this method should raise ValueError.
        If `other` is not an array or a number, it should return TypeError.
        Args:
            other (Array, float, int): The array or number to compare with this array.
        Returns:
            Array: An array of booleans with True where the two arrays match and False where they do not.
                   Or if `other` is a number, it returns True where the array is equal to the number and False
                   where it is not.
        Raises:
            ValueError: if the shape of self and other are not equal.
            TypeError: if `other` is not an array or a number
        """

        equal = []
        if type(self) == type(other):
            if self.shape == other.shape:
                for i in range(self.shape[0]*self.shape[1]):
                    equal.append(self.values[i] == other.values[i])
            else:
                raise ValueError("The shape of self and other are not equal")
        elif isinstance(other,(int, float, bool)):
            for i in range(self.shape[0]*self.shape[1]):
                equal.append(self.values[i] == other)
        else:
            raise TypeError("Both arguments should be an array or a number")
        return equal
        pass

    def min_element(self):

            """
            Returns the smallest value of the array.
            Only needs to work for type int and float (not boolean).
            Returns:
                float: The value of the smallest element in the array.
            Raises:
                TypeError: If array contains any boolean
            """

            min_element = 0
            for elements in self.values:
                if isinstance(elements, bool):
                    raise TypeError("This array contains boolean")
            return min(self.values)
            pass
