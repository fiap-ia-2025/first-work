from enum import Enum


class Product(Enum):
    WATER = 1
    NITROGEN = 2

    def describe(self):
        description = {
            self.WATER: "Água",
            self.NITROGEN: "Nitrogênio"
        }
        return description[self]

    def unit(self):
        description = {
            self.WATER: "l/m2",
            self.NITROGEN: "g"
        }
        return description[self]
