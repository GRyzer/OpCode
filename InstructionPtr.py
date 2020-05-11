class InstructionPointer:
    def __init__(self, value):
        self.instr_ptr = value
        self.blocked = False

    def __add__(self, value):
        if self.blocked:
            raise ValueError(
                "Cant add a number to the instructionpointer because it was not called")
        self.instr_ptr += value

    def __sub__(self, value):
        if self.blocked:
            raise ValueError(
                "Cant subtract a number from the instructionpointer because it was not called")
        self.instr_ptr -= value

    def __repr__(self):
        return f'{self.instr_ptr}'

    def __call__(self):
        self.blocked = False
        return self.instr_ptr

    def set_new_value(self, value):
        self.instr_ptr = value
        self.blocked = True
