from dataclasses import dataclass

@dataclass
class DispersionInput:
    release_rate: float
    release_height: float
    wind_speed: float
    x:float
    y:float
    z:float
    release_duration: 1.0
    time: float = 0.0


    def validate(self):
        if self.release_rate<=0:
            raise ValueError("Release rate must be greater than 0")
        if self.release_height<0:
            raise ValueError("Release height cannot be negative")
        if self.wind_speed<=0:
            raise ValueError("Wind Speed must be greater than 0")
        if self.x<0:
            raise ValueError("Downwind distance x must be greater than 0.")
        if self.z<0:
            raise ValueError("Height z cannont be negative.")
        if self.release_duration<=0:
            raise ValueError("Release Duration must be greater than 0")
        if self.time <0:
            raise ValueError("Time cannot be negative")