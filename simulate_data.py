import numpy as np


class CreateMockData:

    @staticmethod
    def sinusoidal_with_noise(lower_bound:float, upper_bound:float, shape) -> np.ndarray:
        assert lower_bound < upper_bound, "Lower bound must be less than upper bound"
        assert shape[0] > 0 and shape[1] > 0, "Shape must be greater than 0 in both dimensions"
        assert len(shape) == 2, "Shape must be a tuple of length 2"
        x, y = np.meshgrid(np.linspace(lower_bound, upper_bound, shape[0]), np.linspace(lower_bound, upper_bound, shape[1]))

        # Create a simple pattern with added random noise
        pattern = np.sin(2 * np.pi * x) * np.cos(2 * np.pi * y)
        noise = np.random.normal(0, 0.5, pattern.shape)
        mock_thermal_data = pattern + noise
        return mock_thermal_data

    @staticmethod
    def gradient_based() -> np.ndarray:
        # Create a linear temperature gradient from 20 to 30 degrees Celsius
        gradient = np.linspace(20, 30, 100)
        mock_thermal_data = np.tile(gradient, (100, 1))
        return mock_thermal_data