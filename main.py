import sys
from operation import Operation
from farm import Farm
import numpy as np
from agriculture_type import AgricultureType
from builtins import ValueError


def insert_data(registers):
    while 1:
        try:
            agriculture_type: int = int(
                input("Escolha o tipo da cultura para plantação:\n(1) Soja\n(2) Cana de Açucar\n"))

            if agriculture_type == AgricultureType.SUGAR_CANE.value or agriculture_type == AgricultureType.SOYA.value:
                break

            print("Opção inválida!\n")
        except ValueError:
            print("Você não digitou um número válido.\n")

    length = float(input("Digite o comprimento da áre da plantação (em metros): \n"))
    width = float(input("Digite a largura da área da plantação (em metros): \n"))

    farm: Farm = Farm(length, width, agriculture_type)
    farm.calculate_area()
    farm.calculate_product()
    return np.append(registers, farm)


def view_data(registers):
    if registers.size == 0:
        print("Não há registros para serem exibidos!\n")

    count = 0
    for register in registers:
        print(f"Fazenda {count:}: {register.agriculture_type.describe()}")
        print(f"Área: {register.area:.2f}m2")
        print(
            f"Quantidade de {register.agriculture_type.product().describe()}: {register.quantity_product:.2f}{register.agriculture_type.product().unit()}\n")
        count = count + 1


def update_data(registers):
    # TODO: implementar a lógica de ediçao
    if registers.size == 0:
        print("Não há registros para serem atualizados!\n")
    return registers


def remove_data(registers):
    # TODO: implementar a lógica de remoção
    if registers.size == 0:
        print("Não há registros para serem excluídos!\n")
    return registers


# Função principal
def main():
    # Conversa inicial e humanizada
    print("\n\n**********************************************************************")
    print("***  Seja bem vindo (a) ao mais novo sistema da FarmTech Solutions ***")
    print("**********************************************************************")

    print(
        "\nSou a assistente virtual Chay e vou te ajudar no cálculo da área de plantio e manejo de insumos das culturas Soja e Cana de Açucar. \n")

    print("Para começar, escolha uma das opções abaixo:\n")

    option_choice = -1
    registers = np.array([], dtype=Farm)

    while option_choice != 0:

        try:
            option_choice = int(input("1) Calcular dados para uma fazenda\n "
                                      "2) Visualizar registros \n "
                                      "3) Atualizar registros \n "
                                      "4) Excluir registros \n "
                                      "0) Sair do programa \n"))
        except ValueError:
            option_choice = -1

        match option_choice:
            case Operation.QUIT.value:
                print("Até logo! \n")
                sys.exit()

            case Operation.INSERT.value:
                registers = insert_data(registers)

            case Operation.VIEW.value:
                view_data(registers)

            case Operation.UPDATE.value:
                registers = update_data(registers)

            case Operation.REMOVE.value:
                registers = remove_data(registers)

            case _:
                print("Opção inválida! Selecione outra opção. \n")


# Chama a função principal
if __name__ == "__main__":
    main()
