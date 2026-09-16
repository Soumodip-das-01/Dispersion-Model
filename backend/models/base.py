from abc import ABC, abstractmethod

class DispersionModel(ABC):
    name = "Base Dispersion Model"

    @abstractmethod
    def calculate(self,data):
        pass