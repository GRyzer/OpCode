class InstructionPointer:
    def __init__(self, number):
        self.instr_ptr = number

    def __add__(self, number):
        self.instr_ptr += number

    def __sub__(self, number):
        self.instr_ptr -= number

    def __repr__(self):
        return f'{self.instr_ptr}'

    def __call__(self):
        return self.instr_ptr
