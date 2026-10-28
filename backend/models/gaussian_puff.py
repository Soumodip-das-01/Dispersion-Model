import math

from backend.models.base import DispersionModel

class GaussianPuff(DispersionModel):
    name = "Gaussian Puff"
    def calculate(self, data, sigma_x, sigma_y, sigma_z):
        data.validate()

        if sigma_x <= 0:
            raise ValueError("sigma_x must be greater than 0.")

        if sigma_y <= 0:
            raise ValueError("sigma_y must be greater than 0.")

        if sigma_z <= 0:
            raise ValueError("sigma_z must be greater than 0.")

        mass = data.release_rate*data.release_duration
        puff_x = data.wind_speed*data.time

        dx = data.x - puff_x
        dy = data.y

        horizontal = math.exp(
            -(dx ** 2)/(2*sigma_x**2) - (dy**2)/(2*sigma_y**2)
        )
        vertical = (math.exp(-((data.z- data.release_height)**2)/(2*sigma_z**2))+math.exp(-((data.z+data.release_height)**2/(2*sigma_z**2))))
        #Gaussian Puff Concentration
        normalization= (
            mass/(
                ((2*math.pi)**1.5)*sigma_x*sigma_y*sigma_z
            )
        )

        concentration = normalization*horizontal*vertical

        return concentration