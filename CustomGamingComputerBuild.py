#Nathan Hopkins
#Data Class for Computer Parts
#Jan 31, 2023

import requirements.txt

class CustomGamingComputerBuild:
    def __init__(self, processor, graphics_card, memory_size, storage_capacity):
        self.__processor = processor
        self.__graphics_card = graphics_card
        self.__memory_size = memory_size
        self.__storage_capacity = storage_capacity

    # Getter and setter methods for each data field
    def get_processor(self):
        return self.__processor

    def set_processor(self, processor):
        self.__processor = processor

    def get_graphics_card(self):
        return self.__graphics_card

    def set_graphics_card(self, graphics_card):
        self.__graphics_card = graphics_card

    def get_memory_size(self):
        return self.__memory_size

    def set_memory_size(self, memory_size):
        self.__memory_size = memory_size

    def get_storage_capacity(self):
        return self.__storage_capacity

    def set_storage_capacity(self, storage_capacity):
        self.__storage_capacity = storage_capacity

    # Override __str__() method for a meaningful string representation
    def __str__(self):
        return f"Custom Gaming Computer Build: Processor - {self.__processor}, Graphics Card - {self.__graphics_card}, Memory Size - {self.__memory_size}, Storage Capacity - {self.__storage_capacity}"

    # Override __eq__() method for comparing instances
    def __eq__(self, other):
        if isinstance(other, CustomGamingComputerBuild):
            return (
                self.__processor == other.get_processor()
                and self.__graphics_card == other.get_graphics_card()
                and self.__memory_size == other.get_memory_size()
                and self.__storage_capacity == other.get_storage_capacity()
            )
        return False

