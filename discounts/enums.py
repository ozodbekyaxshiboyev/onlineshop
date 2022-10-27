from enum import Enum


class DiscountTypes(Enum):
    percentage = 'percentage'
    amount = 'amount'

    @classmethod
    def choices(cls):
        return ((i.name, i.value) for i in cls)
