import numpy as np

import matplotlib.pyplot as plt
import simulate_data
import process_data
import heatmap


def main():
    # Create a mock thermal data array with missing values
    mock_thermal_data = simulate_data.sinusoidal_with_noise(-1, 1, (100, 100))

    # Interpolate the missing values
    interpolated_data = process_data.handle_missing_values(mock_thermal_data)

    # Create a heatmap of the interpolated data
    heatmap.create_heat_map(interpolated_data)

if __name__ == '__main__':
    main()