import matplotlib.pyplot as plt

def create_heat_map(mock_thermal_data):

    plt.imshow(mock_thermal_data, cmap='viridis', interpolation='nearest', origin='upper')

    # Add colorbar for reference
    plt.colorbar(label='Temperature')

    # Set axis labels
    plt.xlabel('Column Index')
    plt.ylabel('Row Index')

    # Add title
    plt.title('Mock Thermal Data Heatmap')

    # Show the heatmap
    plt.show()