running = True

while running:

    cpf = input('Digite seu cpf sem os ultimos dois digitos: ')
    qtd_caracteres = len(cpf)

    if cpf.isnumeric() and qtd_caracteres == 9:
        def calculate_last_two_digits_of_cpf(cpf):
            def calculate_digit(cpf, factor):
                final_value = 0
                digit = 0
                if cpf.isnumeric():
                    for number in cpf:
                        number = int(number)
                        if factor >= 2:
                            num = number * factor
                            final_value += num
                            factor -= 1
                            result = 11 - (final_value % 11)
                            digit = result if not result > 9 else 0
                        
                return str(digit)

            penultimate = calculate_digit(cpf, factor=10)
            last = calculate_digit(cpf + penultimate, factor=11)

            return penultimate + last

        def cpf_format(cpf):
            cpf += calculate_last_two_digits_of_cpf(cpf)
            result = f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'
            return result

        result = cpf_format(cpf)

        print(result)

        user_answer = input('Deseja sair do programa? se sim digite [S]im caso contrário digite [N]ão: ')

        if user_answer.lower() in ['s', 'sim']:
            print(user_answer)
            running = False
        else: 
            print('OK, vamos lá novamente')    
    else:
        print('Digite 9 digitos por favor!') if qtd_caracteres != 9 and cpf.isnumeric() else print('Digite apenas núemros por favor')        
