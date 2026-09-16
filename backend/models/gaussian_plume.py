import math
from backend.models.base import DispersionModel

class GaussianPlume(DispersionModel):
    name="Gaussian Plume"
    def calculate(self, data, sigma_y, sigma_z):
        data.validate()
        if sigma_y <=0 or sigma_z<=0:
            raise ValueError("Dispersion coefficient must be greater than 0")
        q = data.release_rate
        u = data.wind_speed
        h = data.release_height

        x = data.x
        y = data.y
        z = data.z

        a = q / (2*math.pi*u*sigma_z*sigma_y)
        crosswind = math.exp(-(y**2)/(2*sigma_y**2))
        vertical = (
            math.exp(
                -((z-h)**2)/(2*sigma_z**2)
            ) + math.exp(
                -((z+h)**2)/(2*sigma_z**2)
            )
        )

        return a*crosswind*vertical