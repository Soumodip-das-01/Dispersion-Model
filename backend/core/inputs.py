from dataclasses import dataclass

@dataclass
class DispersionInput:
    release_rate: float
    release_height: float
    wind_speed: float
    x:float
    y:float
    z:float

    def validate(self):
        if self.release_rate<=0:
            raise ValueError("Release rate must be greater than 0")
        if self.release_height<0:
            raise ValueError("Release height cannot be negative")
        if self.wind_speed<=0:
            raise ValueError("Wind Speed must be greater than 0")
        if self.x<=0:
            raise ValueError("Downwind distance x must be greater than 0.")
        if self.z<0:
            raise ValueError("Height z cannont be negative.")
        