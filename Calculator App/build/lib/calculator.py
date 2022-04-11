class Calculator:
    '''
    Calculator object contains basic calculator functions.

    Attributes:
        memory (float/int): A value to pass into calculator's memory

    Methods:
        add()
        subract()
        multiply()
        divide()
        n_root()
        show_memory()
        reset_memory()
    '''
    def __init__(self, memory: float = 0.0):
        self.memory = memory

    def add(self, a: float, b: float = None):
        '''
        Addition function.

        Args:
            For two components use:
                a (float/int): The the first component
                b (float/int): The second component
            For one component use (memory use):
                a (float/int): Component to add to the memory

        Returns:
            A number after addition or a number from memory after addition
        '''
        if (b == None):
            self.memory += a
            return self.memory
        else:
            return a + b

    def subtract(self, a: float, b: float = None):
        '''
        Subtraction function.

        Args:
            For two components use:
                a (float/int): The the first component
                b (float/int): The second component
            For one component use (memory use):
                a (float/int): Component to subtract from the memory

        Returns:
            A number after subraction or a number from memory after subraction
        '''
        if (b == None):
            self.memory -= a
            return self.memory
        else:
            return a - b
    
    def multiply(self, a: float, b: float = None):
        '''
        Multiplication function.

        Args:
            For two components use:
                a (float/int): The the first component
                b (float/int): The second component
            For one component use (memory use):
                a (float/int): Component to multiply memory with

        Returns:
            A number after multiplication or a number from memory after multiplication
        '''
        if (b == None):
            self.memory *= a
            return self.memory
        else:
            return a * b

    def divide(self, a: float, b: float = None):
        '''
        Division function.

        Args:
            For two components use:
                a (float/int): The the first component
                b (float/int): The second component
            For one component use (memory use):
                a (float/int): Component to divide memory with

        Returns:
            A number after division or a number from memory after division
        '''
        if (b == None):
            if (a == 0):
               return "You cannot divide by 0"
            self.memory /= a
            return self.memory
        else:
            if (b == 0):
                return "You cannot divide by 0"
            return a / b

    def n_root(self, n: float, b: float = None):
        '''
        The n-th root function.

        Args:
            For two components use:
                n (float/int): n-th root number
                b (float/int): A base number from which to pull the root
            For one component use (memory use):
                n (float/int): n-th root number to pull root from number in memory

        Returns:
            A number after pulling the n-th root or a number from memory after pulling the n-th root
        '''
        if (b == None):
            if (n == 0):
                return "You cannot take a zeroth root of a number"
            self.memory = self.memory**(1.0/n)
            return self.memory
        else:
            if (b == 0):
                return "You cannot take a zeroth root of a number"
            return b**(1.0/n)

    def show_memory(self):
        '''
        The function that shows the number in memory.

        Returns:
            A string with a number in memory
        '''
        return f"Number in calculators memory: {self.memory}"

    def reset_memory(self):
        '''
        The function that resets the number in memory.

        Returns:
            Resets the number in memory and call show_memory() function
        '''
        self.memory = 0.0
        return self.show_memory()
        