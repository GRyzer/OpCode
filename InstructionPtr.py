class InstructionPointer:
    def __init__(self, value):
        self.instr_ptr = value

    def __add__(self, value):
        self.instr_ptr += value

    def __sub__(self, value):
        self.instr_ptr -= value

    def __repr__(self):
        return f'{self.instr_ptr}'

    def __call__(self):
        return self.instr_ptr

    def set_new_value(self, value):
        self.instr_ptr = value


if __name__ == "__main__":
    instr = InstructionPointer(0)
    instr.set_new_value(6)
    print(instr())
