from datetime import datetime

def ValidarCPF(iCPF):
    iCPF = iCPF.replace('.', '').replace('-', '')  # Remove caracteres especiais
    if len(iCPF) != 11 or not iCPF.isdigit():
        return False

    # Cálculo do primeiro dígito verificador
    soma           = sum(int(iCPF[i]) * (10 - i) for i in range(9))
    PrimeiroDigito = (soma * 10) % 11
    PrimeiroDigito = 0 if PrimeiroDigito == 10 else PrimeiroDigito

    if int(iCPF[9]) != PrimeiroDigito:
        return False

    # Cálculo do segundo dígito verificador
    soma          = sum(int(iCPF[i]) * (11 - i) for i in range(10))
    SegundoDigito = (soma * 10) % 11
    SegundoDigito = 0 if SegundoDigito == 10 else SegundoDigito

    return int(iCPF[10]) == SegundoDigito

def ValidarCNPJ(iCNPJ):
    iCNPJ = iCNPJ.replace('.', '').replace('/', '').replace('-', '')  # Remove caracteres especiais
    if len(iCNPJ) != 14 or not iCNPJ.isdigit():
        return False

    # Cálculo do primeiro dígito verificador
    soma           = sum(int(iCNPJ[i]) * (5 if i < 12 else 6) for i in range(12))
    PrimeiroDigito = (soma % 11)
    PrimeiroDigito = 0 if PrimeiroDigito < 2 else 11 - PrimeiroDigito

    if int(iCNPJ[12]) != PrimeiroDigito:
        return False

    # Cálculo do segundo dígito verificador
    soma          = sum(int(iCNPJ[i]) * (6 if i < 13 else 7) for i in range(13))
    SegundoDigito = (soma % 11)
    SegundoDigito = 0 if SegundoDigito < 2 else 11 - SegundoDigito

    return int(iCNPJ[13]) == SegundoDigito

def ValidarData(cData):
    try:
        # Tenta converter a string em um objeto datetime
        dData = datetime.strptime(cData, "%d/%m/%Y")
        return dData
    except ValueError:
        return None

def SolicitarData():
    while True:
        cData = input('Digite uma data (dd/mm/aaaa): ')
        dData     = ValidarData(cData)
        
        if dData is None:
            print('Data inválida. Tente novamente.')
            continue

        # Verifica se a data é maior que a data atual
        if dData > datetime.now():
            print('A data não pode ser maior que a data atual. Tente novamente.')
        else:
            return dData

def CalcularIRRF(salario):
    if salario <= 1903.98:
        return 0
    elif salario <= 2826.65:
        return salario * 0.075 - 142.80
    elif salario <= 3751.05:
        return salario * 0.15 - 354.80
    elif salario <= 4664.68:
        return salario * 0.225 - 636.13
    else:
        return salario * 0.275 - 869.36

def AtividadeRevisao():
    # Solicita o nome e faz a validação
    cNome = input('Digite seu nome: ')
    while len(cNome) < 3:
        print('Nome inválido. O nome deve ter pelo menos 3 caracteres.')
        cNome = input('Digite seu nome: ')

    # Solicita o tipo de pessoa e faz as validações juntamente com CPF ou CNPJ (De acordo com o tipo de pessoa digitado)
    cTipoPessoa = input('Digite o tipo de pessoa que você é, sendo F para Física (CPF) e J para Jurídica (CNPJ): ')
    while len(cTipoPessoa) != 1 or cTipoPessoa not in ['F', 'f', 'J', 'j']:
        print('Você digitou caracteres inválidos, digite apenas o referente ao tipo de pessoa que você é')
        cTipoPessoa = input('Digite o tipo de pessoa que você é, sendo F para Física (CPF) e J para Jurídica (CNPJ): ')

    if cTipoPessoa in ['F', 'f']:
        print('Você é pessoa física')
        
        while True:
            iCPF = input('Digite seu CPF (somente números): ')
            if ValidarCPF(iCPF):
                print('CPF válido!')
                break
            else:
                print('CPF inválido! Tente novamente.')

    elif cTipoPessoa in ['J', 'j']:
        print('Você é pessoa jurídica')
        
        while True:
            iCNPJ = input('Digite seu CNPJ (somente números): ')
            if ValidarCNPJ(iCNPJ):
                print('CNPJ válido!')
                break
            else:
                print('CNPJ inválido! Tente novamente.')

    # Solicita e valida a data de nascimento (deve haver barras Ex.: dd/mm/aa)
    data_valida = SolicitarData()
    print(f'Data válida: {data_valida.strftime("%d/%m/%Y")}')

    # Solicita e valida o estado civil da pessoa
    cEstadoCivil = input(f'Digite seu estado civil (s, c, v, d): ')
    while len(cEstadoCivil) != 1  or cEstadoCivil not in ['S', 's', 'C', 'c', 'V', 'v', 'D', 'd']:
        print('Estado civil inválido. Não consta nos disponiveis (s, c, v, d) ou tem mais de 1 caractere.')
        cEstadoCivil = input('Digite seu estado civil: ')

    # Solicita e valida o salário da pessoa
    while True:
        try:
            nSalario = float(input('Digite seu salário: '))
            if nSalario <= 0:  # Verifica se o salário é menor ou igual a zero
                print('Salário inválido. O mesmo deve ser maior que 0.')
            else:
                break  # Sai do laço se o salário é válido
        except ValueError:
            print('Entrada inválida. Por favor, digite um número.')

    # Cálculo do IRRF
    DescontoIRRF  = CalcularIRRF(nSalario)
    nSalarioFinal = nSalario - DescontoIRRF

    # Exibe os resultados
    print(f'\nSalário digitado: R$ {nSalario:.2f}')
    print(f'Valor de desconto do IRRF: R$ {DescontoIRRF:.2f}')
    print(f'Valor do salário final com o desconto aplicado: R$ {nSalarioFinal:.2f}')

AtividadeRevisao()