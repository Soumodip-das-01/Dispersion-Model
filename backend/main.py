from backend.core.inputs import DispersionInput
from backend.models.gaussian_plume import GaussianPlume
from backend.models.passquill_gifford import PassquillGifford
from backend.models.gaussian_puff import GaussianPuff

def main():
    data = DispersionInput(
        release_rate=1.0,
        release_height=30.0,
        wind_speed=5.0,
        x = 1000.0,
        y = 0.0,
        z = 0.0,
        release_duration=10.0,
        time=100.0
    )
    puff = GaussianPuff()

    sigma_x = 100.0
    sigma_y = 100.0
    sigma_z = 60.0

    concentration = puff.calculate(
        data,
        sigma_x=sigma_x,
        sigma_y=sigma_y,
        sigma_z=sigma_z
    )

    print("=" * 50)
    print("CHEMICAL DISPERSION ANALYSIS SYSTEM")
    print("=" * 50)
    print(f"Model: {puff.name}")
    print(f"Time: {data.time:.1f} s")
    print(f"Puff center: {data.wind_speed * data.time:.1f} m")
    print(f"Sigma X: {sigma_x:.2f} m")
    print(f"Sigma Y: {sigma_y:.2f} m")
    print(f"Sigma Z: {sigma_z:.2f} m")
    print(f"Concentration: {concentration:.10f} kg/m^3")
    print(f"Concentration: {concentration * 1e6:.6f} mg/m^3")
    # stability = PassquillGifford("D")
    # sigma_y,sigma_z = stability.calculate(data.x)
    # plume = GaussianPlume()
    # c = plume.calculate(data=data,sigma_z=sigma_z,sigma_y=sigma_y)

    # print("=" * 50) 
    # print("CHEMICAL DISPERSION ANALYSIS SYSTEM")
    # print("=" * 50)
    # print(f"Model: {plume.name}")
    # print(f"Stability Class: {stability.stability_class}")
    # print(f"Downwind Distance: {data.x} m")
    # print(f"Sigma Y: {sigma_y:.2f} m")
    # print(f"Sigma Z: {sigma_z:.2f} m")
    # print(f"Concentration: {c:.10f} kg/m^3")
    # print(f"Concentration: {c * 1e6:.6f} mg/m^3")


if __name__ == "__main__":
    main()