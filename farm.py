from agriculture_type import AgricultureType


class Farm:

    def __init__(self, length, width, agriculture_type):
        self.length = length
        self.width = width
        self.agriculture_type: AgricultureType = AgricultureType.SOYA if agriculture_type == AgricultureType.SOYA.value else AgricultureType.SUGAR_CANE
        self.area = None
        self.quantity_product = None

    def calculate_area(self):
        self.area = self.length * self.width

    def calculate_product(self):
        if self.agriculture_type == AgricultureType.SOYA:
            self.calculate_water()

        if self.agriculture_type == AgricultureType.SUGAR_CANE:
            self.calculate_nitrogen()

    def calculate_water(self):
        # Espaçamento em metro entre as linhas da lavoura
        spacing_agriculture = 0.5

        # Considerando que são 10 plantas de soja for metro linear
        # Cáculo da quantidade de plantas por m2
        total_plants_per_m2 = 10 / spacing_agriculture

        # Cáculo da quantidade de plantas em uma area em m2
        total_plants_per_area_calculate = total_plants_per_m2 * self.area

        # Se uma planta necessita de 620L/m2 de água durante o plantio, então:
        water_per_plant = 620
        self.quantity_product = total_plants_per_area_calculate * water_per_plant

    def calculate_nitrogen(self):
        # Espaçamento em metro entre as linhas da plantação de cana
        spacing_agriculture = 1.4

        # Considerando que são 8 plantas de cana for metro linear
        # Cáculo da quantidade de plantas por m2
        total_plants_per_m2 = 8 / spacing_agriculture

        # Cáculo da quantidade de plantas em uma area em m2
        total_plants_per_area_calculate = self.area * total_plants_per_m2

        # Se uma planta necessita de 30kg/ha de água durante o plantio
        # 30kg/ha = 0.3g/m2
        # 0.3g de nitrogenio são suficientes para o total de 5,71 plantas
        nitrogen_per_m2 = 0.3
        self.quantity_product = (total_plants_per_area_calculate * nitrogen_per_m2) / total_plants_per_m2
