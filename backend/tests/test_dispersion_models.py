import pytest
from backend.core.inputs import DispersionInput
from backend.models.gaussian_plume import GaussianPlume
from backend.models.gaussian_puff import GaussianPuff

@pytest.fixture
def sample_input():
    return DispersionInput(
        release_rate=1.0,
        release_duration=60.0,
        release_height=50.0,
        wind_speed=5.0,
        x=1000.0,
        y=0.0,
        z=0.0,
    )

def test_gaussian_plume_returns_positive_concentration(sample_input):
    model = GaussianPlume()
    concentration = model.calculate(
        sample_input,
        sigma_y=100.0,
        sigma_z=60.0,
    )

    assert concentration is not None
    assert concentration > 0

def test_gaussian_puff_return_positive_concentration(sample_input):
    model = GaussianPuff()

    concentration = model.calculate(
        sample_input,
        sigma_x=100.0,
        sigma_y=100.0,
        sigma_z=60.0,
    )

    assert concentration is not None
    assert concentration > 0

def test_invalid_release_rate_is_rejected(sample_input):
    sample_input.release_rate = -1.0

    with pytest.raises(ValueError):
        sample_input.validate()