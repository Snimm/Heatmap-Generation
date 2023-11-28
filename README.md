# Project Name

Heatmap Generation from Simulated Data

## Description provided

Objective: Create heatmaps from simulated thermal data.
Requirements:
Process mock thermal data to extract heat information.
Generate heatmaps using data visualization tools.


## Installation

Make sure you have Python installed on your system. It is recommended to use a virtual environment. Here are the installation steps:

```bash
# Clone the repository
git clone https://github.com/Snimm/Heatmap-Generation

# Navigate to the project directory
cd Heatmap-Generation

# Create and activate a virtual environment (optional but recommended)
python -m venv .venv
source .venv/bin/activate  # For Linux/macOS
# or
.\.venv\Scripts\activate  # For Windows

# Install the required dependencies
pip install -r requirements.txt

# Run the application
python main.py
```


## Example image

Heatmap-Generation/Figure_1.png


**Insight Guide: Thermal Data Analysis Project**

*Understanding the Assignment:*

The goal of this project is to develop an algorithm for creating mock thermal data, analyzing it and generating heatmaps from it.

*Implementation Strategy:*

1. **Mock Thermal Data Generation:**
   - Before creating heatmaps, it's crucial to have mock thermal data. I employed various methods to generate synthetic data, including sinusoidal_with_noise-based generation, and gradient generation. This diverse set of data allowed for a more robust testing environment.

2. **Missing Value Handling:**
   - I anticipated that in real-world scenarios, thermal data might have missing values. To address this, I wrote a program to identify missing values in the mock thermal data and used linear interpolation to approximate those values based on the neighborhood. This step ensures a more complete dataset for heatmap generation.

   ```python
   def handle_missing_values(mock_thermal_data):
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
   ```

3. **Heatmap Generation:**
   - I used the `matplotlib` library to create heatmaps from the generated or interpolated thermal data. The choice of the 'viridis' colormap and the 'nearest' interpolation method was made for clarity and visual appeal. Adding a color bar provides a reference for temperature values associated with the colors.

   ```python
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
   ```

4. **Visualization and Interpretation:**
   - The generated heatmaps offer a visual representation of temperature distribution. Warmer colors indicate higher temperatures, while cooler colors represent lower temperatures. The visualization allows for quick insights into the thermal patterns present in the data.

5. **Documentation:**
   - Throughout the process, I ensured to document each step.

*Further Steps:*

While the current implementation successfully generates heatmaps from mock thermal data, real-world applications may involve more complex data sources and additional considerations such as noise reduction, dynamic data streams, and scalability. Further refinement of the algorithm and integration with real thermal data sources would be necessary for a comprehensive and practical solution.

**Operational Procedure: Thermal Data Analysis Code**

*Prerequisite:*
- Follow the installation steps described above.

*Step 1: Generate Mock Thermal Data*

  1.1 **Replace Sample Data (if needed):**
- Replace the sample data (`mock_thermal_data`) with your own thermal data if available.
- Replace `sinusoidal_with_noise()` with  `gradient_based()` if simpler data fits your needs better.  

*Step 2: Check Mock Thermal Data*

2.1 **Check Mock Data Generation Code:**
- Review the create_mock_data function and ensure it meets your testing requirements.

*Step 3: Handle Missing Values (Optional)*

3.1 **Ckeck Missing Value Handling Code (if needed):**
- If you have missing values in your data, review handle_missing_values function.
- This step is optional if your data is complete or you have your own method for handling missing values.

*Step 4: Create Heatmap*

4.1 **Run Heatmap Generation Code:**
- Execute the main.py file to create a heatmap from the generated or interpolated thermal data.
- The heatmap will be displayed, showcasing the temperature distribution.

4.2 **Review Heatmap:**
- Observe the heatmap to gain insights into the thermal patterns present in the data.
- Warmer colors represent higher temperatures, while cooler colors represent lower temperatures.

*Step 5: Save Heatmap*

5.1 **Save Heatmap:**
- Save the heatmap by clicking floppy disk icon at the bottom of the window.


*Conclusion:*
This operational procedure guides you through the setup, execution, and analysis of the thermal data analysis code. By following these steps, you can generate synthetic thermal data, handle missing values if necessary, and create informative heatmaps for visualization and analysis.