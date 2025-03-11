from enum import Enum
from product import Product


class AgricultureType(Enum):
    SOYA = 1
    SUGAR_CANE = 2

    def describe(self):
        description = {
            self.SOYA: "Soja",
            self.SUGAR_CANE: "Cana de açucar"
        }
        return description[self]

    def product(self):
        if self == AgricultureType.SOYA:
            return Product.WATER

        elif self == AgricultureType.SUGAR_CANE:
            return Product.NITROGEN
