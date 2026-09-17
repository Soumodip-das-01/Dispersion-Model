import math

class PassquillGifford:
    name = "Passquill Gifford"

    def __init__(self,stability_class):
        self.stability_class = stability_class.upper()

        if self.stability_class not in "ABCDEF":
            raise ValueError("Stability Class must be A,B,C,D,E or F")

    def calculate(self,x):
        if x<=0:
            raise ValueError("Downing distance must be Greater than 0.")

        sy_params = {
            "A": (0.22, 0.0001),
            "B": (0.16, 0.0001),
            "C": (0.11, 0.0001),
            "D": (0.08, 0.0001),
            "E": (0.06, 0.0001),
            "F": (0.04, 0.0001),
        }

        sz_params = {
            "A": (0.20, 0.0),
            "B": (0.12, 0.0),
            "C": (0.08, 0.0),
            "D": (0.06, 0.0),
            "E": (0.03, 0.0),
            "F": (0.016, 0.0),
        }

        ay,by = sy_params[self.stability_class]
        az,bz = sz_params[self.stability_class]

        sy = ay*x*(1+by*x)**-0.5
        sz = az*x*(1+bz*x)**-0.5

        return sy,sz
