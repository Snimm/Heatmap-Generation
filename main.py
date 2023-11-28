import simulate_data
import process_data
import heatmap
import pprint
pp = pprint.PrettyPrinter()

def main():
    # Create a mock thermal data array with missing values
    mock_thermal_data = simulate_data.sinusoidal_with_noise(-1, 1, (100, 100))

    # Interpolate the missing values
    interpolated_data = process_data.handle_missing_values(mock_thermal_data)

    # Analyze the interpolated data
    data_description = process_data.analyze(interpolated_data)

    # Print the data description
    pp.pprint(data_description)

    # Create a heatmap of the interpolated data
    heatmap.create_heat_map(interpolated_data)

if __name__ == '__main__':
    main()