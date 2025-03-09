import sys
import array

def rectangle_area_calculate(length, width):
    return length * width

def total_plants_per_area_calculate(plants_per_meter, area):
    #Espaçamento em metro entre as linhas da lavoura
    spacing_agriculture = 0.5

    #Cáculo da quantidade de plantas por m2
    total_plants_per_m2 = plants_per_meter/spacing_agriculture

    #Cáculo da quantidade de plantas em uma area em m2
    return total_plants_per_m2 * area

def total_need_water_calculate(total_plants):
    #Se uma planta necessita de 620L/m2 de água durante todo o plantio, então:
    water_per_plant = 620
    return total_plants * water_per_plant

def input_data(farming_size, farming_types, length_array, width_array, area_array, plants_per_meter_array, plants_per_area_array, total_need_water_array):
    for i in range(farming_size):
        length_array[i] = float(input(f"Digite o comprimento da lavoura de {farming_types[i]} (em metros): \n"))
        width_array[i] = float(input(f"Digite a largura da lavoura de {farming_types[i]} (em metros): \n"))
        plants_per_meter_array[i] = int(input(f"Digite a quantidade de plantas por metro da lavoura de {farming_types[i]}: \n"))
        area_array[i] = rectangle_area_calculate(length_array[i], width_array[i])
        plants_per_area_array[i] = total_plants_per_area_calculate(plants_per_meter_array[i], area_array[i])
        total_need_water_array[i] = total_need_water_calculate(plants_per_area_array[i])

def print_data(farming_size, farming_types, area_array, plants_per_area_array, total_need_water_array):

    print("Resultados de acordo com os dados inseridos:")
    for i in range(farming_size):
        print("\n****************************************")
        print(f"\nDados da Lavoura de: {farming_types[i]} \n")

        print(f"Área: {area_array[i]:.2f}m2 \n")
        print(f"Quantidade total de plantas: {plants_per_area_array[i]} \n")
        print(f"Quantidade necessária de água: {total_need_water_array[i]:.2f} l/m2\n")
# Função principal
def main():

    # Constantes
    soya_name = "Soja"
    sugar_cane_name = "Cana de Açucar"
    farming_types = [soya_name, sugar_cane_name]
    farming_size = len(farming_types)

    # Conversa inicial e humanizada
    print("\n\n**********************************************************************")
    print("***  Seja bem vindo (a) ao mais novo sistema da FarmTech Solutions ***")
    print("**********************************************************************")

    print("\nSou a assistente virtual Chay e vou te ajudar no cálculo da área de plantio e manejo de insumos das culturas Soja e Cana de Açucar. \n")

    print("Vamos começar...\n")

    length_array = array.array('f', [0] * farming_size)
    width_array = array.array('f', [0] * farming_size)
    area_array = array.array('f', [0] * farming_size)
    plants_per_meter_array = array.array('i', [0] * farming_size)
    plants_per_area_array = array.array('f', [0] * farming_size)
    total_need_water_array = array.array('f', [0] * farming_size)

    input_data(farming_size, farming_types, length_array, width_array, area_array, plants_per_meter_array, plants_per_area_array, total_need_water_array)

    print_data(farming_size, farming_types, area_array, plants_per_area_array, total_need_water_array)

    sys.exit()

# Chama a função principal
if __name__ == "__main__":
    main()






