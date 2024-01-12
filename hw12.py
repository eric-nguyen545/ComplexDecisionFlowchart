class Complex:
    '''
    Purpose:
        The purpose of the class is to return a complex number.
    Instance variables:
        real: A real number
        imag: An imagniary number
        new_real: A new real number, replacing the last one
        new_imag: A new imaginary number, replacing the last one
        other: Another complex string
    Methods:
        get_real: Returns the real number 
        set_real: Sets the real number to a new real number
        get_imag: Returns the imaginary number
        set_imag: Set the imaginary number to a new imaginary number
        __str__: Replaces the string method, so it can return '(real) + (imag)i'
        __add__: Replaces the add method, and adds the complex numbers following (a + bi) + (c + di) = (a + c) + (b + d)i
        __mul__: Replaces the mul method, and multiplys the complex numbers following (a + bi)(c + di) = (ac - bd) + (ad + bc)i
        __eq__: Replces the eq method, and checks if the real and imaginary numbers are the same and returns a boolean 
    '''
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
        
    def get_real(self):
        return self.real
    
    def set_real(self, new_real):
        self.real = new_real

    def get_imag(self):
        return self.imag
    
    def set_imag(self, new_imag):
        self.imag = new_imag

    def __str__(self):
        return f'{self.real} + {self.imag}i'

    def __add__(self, other):
        total_real = self.real + other.real
        total_imag = self.imag + other.imag
        return Complex(total_real, total_imag)
    
    def __mul__(self, other):
        total_real = (self.real * other.real) - (self.imag * other.imag)
        total_imag = (self.real * other.imag) + (self.imag * other.real)
        return Complex(total_real, total_imag)
    
    def __eq__(self, other):
        if self.real == other.real and self.imag == other.imag:
            return True
        else:
            return False

class Decision:
    '''
    Purpose:
        The purpose of the class is to return a string representing a prompt correlating with the chosen option.
    Instance variables:
        prompt: A string that the user will answer
        option: An option the user can choose
        result: A result corresponding with the inputted option
    Methods:
        add_option: Add an option, and the corresponding result to the prompt
        __str__: Converts the prompt into a string
        run: This method takes in the inputted, prompt, options, and results.
                Then prints them out in a way for the user to make selections and returns strings corresponding with the selections.
    '''
    def __init__(self, prompt):
        self.prompt = prompt
        self.options = []
        self.results = []

    def add_option(self, option, result):
        self.options.append(option)
        self.results.append(result)

    def __str__(self):
        return str(self.prompt)
    
    def run(self): 
        i = 0
        j = 0
        if self.options == []:
            return 'No options available'
        else:
            print()
            print(self.prompt)
            print()
            while j != len(self.options):
                print(f'{j}. {self.options[j]}')
                j += 1
            while i != 1:
                if i == 0:
                    num = input(f'Enter a number between 0 and {len(self.options) - 1}: ')
                    if num.isdigit() == True and int(num) < len(self.options):
                        if type(self.results[int(num)]) == str:
                            i += 1
                            return self.results[int(num)]
                        else:
                            i += 1
                            return self.results[int(num)].run()
                    else:
                        print('Invalid choice, try again.')                

class Flowchart:
    '''
    Purpose:
        The purpose of the class is to return a string representing a prompt correlating with the chosen option.
        It does this by using a file, and running it through the Decision class.
    Instance variables: 
        filename: A file containing the decisions, endings, and paths. 
    Methods: 
        start: This method makes a call to the Decision method run, which then runs through the decisions prompted from the file.
    '''
    def __init__(self, filename):
        self.decisions = []
        with open(filename) as fp:
            for line in fp:
                y = line.strip()
                row = y.split(',')
                if row[0] == 'Decision':
                    dec = Decision(row[2])
                    self.decisions.append(dec)
                elif row[0] == 'Ending':
                    self.decisions[int(row[1])].add_option(row[2], row[3])
                elif row[0] == 'Path':
                    self.decisions[int(row[1])].add_option(row[2], self.decisions[int(row[3])])
        fp.close

    def start(self):
        return self.decisions[0].run()

if __name__ == '__main__':
    find_walter = Flowchart('story2.csv')
    print(find_walter.start())
