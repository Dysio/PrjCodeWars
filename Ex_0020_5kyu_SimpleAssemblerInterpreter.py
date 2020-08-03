def simple_assembler(program):
	# return a dictionary with the registers
    reg_name = program[0].split()[1]
    reg_val = program[0].split()[2]

    index = 1
    # while index < len(program):
    #     pass

    return {reg_name:reg_val}


if __name__ == '__main__':
    index = 0
    command = 'mov a 5'
    if command.split()[0] == 'mov':
        command.split()[1] = command.split()[2]
        print(command.split())
        index += 1
        print(index)

    program = ['mov a 5']
    print(simple_assembler(['mov a 5']))
    print(len(program))