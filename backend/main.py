from backend.core.inputs import DispersionInput
from backend.models.gaussian_plume import GaussianPlume

def main():
    data = DispersionInput(
        release_rate=1.0,
        release_height=30.0,
        wind_speed=5.0,
        x = 1000.0,
        y = 0.0,
        z = 0.0
    )
    model = GaussianPlume()
    sigma_y = 50.0
    sigma_z = 50.0

    c = model.calculate(data=data,sigma_z=sigma_z,sigma_y=sigma_y)
    print("=" * 50)
    print("CHEMICAL DISPERSION ANALYSIS SYSTEM")
    print("=" * 50)
    print(f"Model: {model.name}")
    print(f"Concentration: {c:.10f} kg/m^3")
    print(f"Concentration: {c * 1e6:.6f} mg/m^3")

if __name__=="__main__":
    main()