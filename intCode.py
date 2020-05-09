
class IntCode:
    def __init__(self, file_name):
        self.intCode_list = IntCode.from_file(file_name)
        self.instruction_ptr = 0

    @classmethod
    def from_file(cls, file_name):
        with open(file_name, "r") as f:
            storage = f.read().strip().split(',')
            return [int(element) for element in storage]

    def decrypt_int_code(self):
        while self.intCode_list[self.instruction_ptr] != 99:
            current_opcode = self.intCode_list[self.instruction_ptr]
            opcode, parameter1, parameter2, parameter3 = self.get_intCode_positions(str(current_opcode))

            if opcode == 1:
                self.intCode_list[parameter3] = self.intCode_list[parameter1] + self.intCode_list[parameter2]
            elif opcode == 2:
                self.intCode_list[parameter3] = self.intCode_list[parameter1] * self.intCode_list[parameter2]
            elif opcode == 3:
                self.intCode_list[parameter3] = parameter1
                self.instruction_ptr -= 2
            elif opcode == 4:
                print(self.intCode_list[parameter1])
                self.instruction_ptr -= 2
            else:
                raise ValueError(f"Unexpected Opcode: {current_opcode} appeared")

            self.instruction_ptr += 4

    def get_intCode_positions(self, opcode: str):
        int_code_positions = [int(opcode[-1])]
        opcode = list(opcode)

        if opcode[-1] == "3":
            input_value = input("Give in the start number: ")
            int_code_positions.extend([int(input_value), None, self.intCode_list[self.instruction_ptr + 1]])
            return int_code_positions

        while len(opcode) < 4:
            opcode.insert(0, '0')

        for index, parameter_mode in enumerate(reversed(opcode[:2]), 1):
            if parameter_mode == "0":
                int_code_positions.append(self.intCode_list[self.instruction_ptr + index])
            elif parameter_mode == "1":
                int_code_positions.append(self.instruction_ptr + index)
            else:
                raise ValueError(f"Wrong parameter: {parameter_mode}")
        int_code_positions.append(self.intCode_list[self.instruction_ptr + 3])  # might be a problem if we have opcode 4
        return int_code_positions


if __name__ == "__main__":
    try:
        code = IntCode("file_with_input.txt")
        code.decrypt_int_code()
    except ValueError as e:
        print(e)
