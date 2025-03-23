import sys
from operation import Operation
from source.farm import Farm
import numpy as np
from source.agriculture_type import AgricultureType
from exporter import export_data_to_csv
from builtins import ValueError


def insert_data(registers):
    while 1:
        try:
            name = input("Digite o nome da fazenda: \n")
            agriculture_type: int = int(
                input("Escolha o tipo da cultura para plantação:\n(1) Soja\n(2) Cana de Açucar\n"))

            if agriculture_type == AgricultureType.SUGAR_CANE.value or agriculture_type == AgricultureType.SOYA.value:
                break

            print("Opção inválida!\n")
        except ValueError:
            print("Você não digitou um número válido.\n")

    length = float(input("Digite o comprimento da área da plantação (em metros): \n"))
    width = float(input("Digite a largura da área da plantação (em metros): \n"))

    farm = Farm(length, width, agriculture_type,name)
    farm.calculate_area()
    farm.calculate_product()
    return np.append(registers, farm)

def view_data(registers):
    if registers.size == 0:
        print("Não há registros para serem exibidos!\n")

    for register in registers:
        print(f"Fazenda {register.name}: {register.agriculture_type.describe()}")
        print(f"Área: {register.area:.2f}m²")
        print(
            f"Quantidade de {register.agriculture_type.product().describe()}: {register.quantity_product:.2f}{register.agriculture_type.product().unit()}\n")

def update_data(registers):
    if registers.size == 0:
        print("Não há registros para serem atualizados!\n")
        return registers

    print("Registros existentes:")
    for count, register in enumerate(registers):
        print(f"{count}: Fazenda {register.name} - Cultura: {register.agriculture_type.describe()} | Área: {register.area:.2f}m²")

    try:
        index = int(input("Escolha o número do registro que deseja atualizar: \n"))
        if index < 0 or index >= registers.size:
            print("Índice inválido!\n")
            return registers
    except ValueError:
        print("Entrada inválida! Informe um número.\n")
        return registers

    length = float(input(f"Digite o novo comprimento da área da plantação (atualmente {registers[index].length} metros): \n"))
    width = float(input(f"Digite a nova largura da área da plantação (atualmente {registers[index].width} metros): \n"))

    if length != registers[index].length or width != registers[index].width:
        registers[index].length = length
        registers[index].width = width
        registers[index].calculate_area()
        registers[index].calculate_product()
        print("Registro atualizado com sucesso!\n")
    else:
        print("Nenhuma alteração foi feita no registro.\n")

    return registers

def remove_data(registers):
    if registers.size == 0:
        print("Não há registros para serem excluídos!\n")
        return registers

    print("Registros existentes:")
    for count, register in enumerate(registers):
        print(f"{count}: Fazenda {register.name} - Cultura: {register.agriculture_type.describe()} | Área: {register.area:.2f}m²")

    try:
        index = int(input("Escolha o número do registro que deseja excluir: \n"))
        if index < 0 or index >= registers.size:
            print("Índice inválido!\n")
            return registers
    except ValueError:
        print("Entrada inválida! Informe um número.\n")
        return registers

    registers = np.delete(registers, index)
    print("Registro excluído com sucesso!\n")
    return registers

def main():
    # Conversa inicial e humanizada
    print("\n\n**********************************************************************")
    print("***  Seja bem-vindo(a) ao mais novo sistema da FarmTech Solutions ***")
    print("**********************************************************************")
    print("\nSou a assistente virtual Chay e vou te ajudar no cálculo da área de plantio e manejo de insumos das culturas Soja e Cana de Açucar. \n")
    print("Para começar, escolha uma das opções abaixo:\n")

    option_choice = -1
    registers = np.array([], dtype=Farm)

    while option_choice != 0:

        try:
            option_choice = int(input(" 1. Calcular dados para uma fazenda\n "
                                      "2. Visualizar registros \n "
                                      "3. Atualizar registros \n "
                                      "4. Excluir registros \n "
                                      "0. Sair do programa \n\n"))
        except ValueError:
            option_choice = -1

        match option_choice:
            case Operation.QUIT.value:
                print("Até logo! \n")
                sys.exit()

            case Operation.INSERT.value:
                registers = insert_data(registers)
                export_data_to_csv(registers)

            case Operation.VIEW.value:
                view_data(registers)

            case Operation.UPDATE.value:
                registers = update_data(registers)
                export_data_to_csv(registers)

            case Operation.REMOVE.value:
                registers = remove_data(registers)
                export_data_to_csv(registers)

            case _:
                print("Opção inválida! Selecione outra opção. \n")

# Chama a função principal
if __name__ == "__main__":
    main()
