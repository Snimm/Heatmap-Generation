import numpy as np
from scipy.interpolate import griddata

def handle_missing_values(mock_thermal_data: np.ndarray) -> np.ndarray:
    # Find indices of missing values
    missing_indices = np.isnan(mock_thermal_data)

    # Create a meshgrid for valid data points
    rows, cols = np.indices(mock_thermal_data.shape)
    valid_points = np.array([rows[~missing_indices], cols[~missing_indices]]).T

    # Create a meshgrid for all points
    all_points = np.array([rows.flatten(), cols.flatten()]).T

    # Extract valid data values
    valid_values = mock_thermal_data[~missing_indices]

    # Perform linear interpolation
    interpolated_values = griddata(valid_points, valid_values, all_points, method='linear')

    # Reshape the interpolated values back to the original shape
    interpolated_data = interpolated_values.reshape(mock_thermal_data.shape)

    return interpolated_data


def analyze(data: np.ndarray) -> dict:

    # Create a dictionary to store the data description
    data_dict = {}

    # Add the data description to the dictionary
    data_dict["mean"] = np.mean(data)
    data_dict["std"] = np.std(data)
    data_dict["min"] = np.min(data)
    data_dict["max"] = np.max(data)
    data_dict["median"] = np.median(data)
    
    return data_dict



