from InstructionPtr import InstructionPointer


class IntCode:
    def __init__(self, file_name):
        self.intCode_list = IntCode.from_file(file_name)
        self.instruction_ptr = InstructionPointer(0)

    @classmethod
    def from_file(cls, file_name):
        with open(file_name, "r") as f:
            storage = f.read().strip().split(',')
            return [int(element) for element in storage]

    def decrypt_int_code(self):
        while self.intCode_list[self.instruction_ptr()] != 99:
            current_opcode = self.intCode_list[self.instruction_ptr()]
            opcode, parameter1, parameter2, parameter3 = self.get_intCode_positions(
                str(current_opcode))

            if opcode == 1:
                self.intCode_list[parameter3] = self.intCode_list[parameter1] + \
                    self.intCode_list[parameter2]
                self.instruction_ptr + 4

            elif opcode == 2:
                self.intCode_list[parameter3] = self.intCode_list[parameter1] * \
                    self.intCode_list[parameter2]
                self.instruction_ptr + 4

            elif opcode == 3:
                self.intCode_list[parameter3] = parameter1
                self.instruction_ptr + 2

            elif opcode == 4:
                print(self.intCode_list[parameter1])
                self.instruction_ptr + 2

            elif opcode == 5:
                if self.intCode_list[parameter1] != 0:
                    self.instruction_ptr.set_new_value(
                        self.intCode_list[parameter2])
                else:
                    self.instruction_ptr + 3

            elif opcode == 6:
                if self.intCode_list[parameter1] == 0:
                    self.instruction_ptr.set_new_value(
                        self.intCode_list[parameter2])
                else:
                    self.instruction_ptr + 3

            elif opcode == 7:
                if self.intCode_list[parameter1] < self.intCode_list[parameter2]:
                    self.intCode_list[parameter3] = 1
                else:
                    self.intCode_list[parameter3] = 0
                self.instruction_ptr + 4

            elif opcode == 8:
                if self.intCode_list[parameter1] == self.intCode_list[parameter2]:
                    self.intCode_list[parameter3] = 1
                else:
                    self.intCode_list[parameter3] = 0
                self.instruction_ptr + 4

            else:
                raise ValueError(
                    f"Unexpected Opcode: {current_opcode} appeared")

    def get_intCode_positions(self, opcode: str):
        int_code_positions = [int(opcode[-1])]
        opcode = list(opcode)

        if opcode[-1] == "3":
            input_value = input("Give in the start number: ")
            int_code_positions.extend(
                [int(input_value), None, self.intCode_list[self.instruction_ptr() + 1]])
            return int_code_positions

        while len(opcode) < 4:
            opcode.insert(0, '0')

        for index, parameter_mode in enumerate(reversed(opcode[:2]), 1):
            if parameter_mode == "0":
                int_code_positions.append(
                    self.intCode_list[self.instruction_ptr() + index])
            elif parameter_mode == "1":
                int_code_positions.append(self.instruction_ptr() + index)
            else:
                raise ValueError(f"Wrong parameter: {parameter_mode}")
        # might be a problem if we have opcode 4
        if int(opcode[-1]) != 4:
            int_code_positions.append(
                self.intCode_list[self.instruction_ptr() + 3])
        else:
            int_code_positions.append(None)
        return int_code_positions

    def modify_instruction_pointer(self, opcode):
        pass


if __name__ == "__main__":
    try:
        code = IntCode("file_with_input.txt")
        code.decrypt_int_code()
    except ValueError as e:
        print(e)
