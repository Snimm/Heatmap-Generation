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
**Operational Procedure: Thermal Data Analysis Code**

*Prerequisite:*
- Follow the installation steps described above.

*Step 1: Get Thermal Data*

  1.1 **Replace Sample Data (if needed):**
- Replace the sample data (`mock_thermal_data`) with your own thermal data if available.
- Replace `sinusoidal_with_noise()` with  `gradient_based()` if simpler data fits your needs better.  

2.1 **Check Mock Data Generation Code:**
- Review the `CreateMockData` class and ensure it meets your testing requirements if you don't use your own data.

*Step 2: Process Data*

3.1 **Check Missing Value Handling Code (if needed):**
- If you have missing values in your data, review `handle_missing_values` function. The function uses cubic method. 
- This is optional if your data is complete or you have your own method for handling missing values. 

3.2 **Check data description code:**
- check `analyze` function which returns various properties of the data.

*Step 4: Create Heatmap*

4.1 **Run Heatmap Generation Code:**
- Execute the main.py file to create a heatmap from the generated or interpolated thermal data.
- The heatmap will be displayed, showcasing the temperature distribution.

Example image
![Figure_1](https://github.com/Snimm/Heatmap-Generation/assets/53926889/eef9ef3b-c484-4ae5-bc58-eb88246292c9)

4.2 **Review Heatmap:**
- Observe the heatmap to gain insights into the thermal patterns present in the data.
- Warmer colors represent higher temperatures, while cooler colors represent lower temperatures.

4.3 **Review Data Description:**
- Observe the data description printed in the console to gain insights into the thermal patterns present in the data.


*Step 5: Save Heatmap*

5.1 **Save Heatmap:**
- Save the heatmap by clicking floppy disk icon at the bottom of the window.


*Conclusion:*
This operational procedure guides you through the setup, execution, and analysis of the thermal data analysis code. By following these steps, you can generate synthetic thermal data, handle missing values if necessary, and create informative heatmaps for visualization and analysis.



**Insight Guide: Thermal Data Analysis Project**

*Understanding the Assignment:*

The goal of this project is to develop an algorithm for creating mock thermal data, analyzing it and generating heatmaps from it.

*Implementation Strategy:*

1. **Mock Thermal Data Generation:**
   - Before creating heatmaps, it's crucial to have mock thermal data. I employed various methods to generate synthetic data, including sinusoidal_with_noise-based generation, and gradient generation. This diverse set of data allowed for a more robust testing environment.

2. **Missing Value Handling:**
   - I anticipated that in real-world scenarios, thermal data might have missing values. To address this, I wrote a program to identify missing values in the mock thermal data and used linear interpolation to approximate those values based on the neighborhood. This step ensures a more complete dataset for heatmap generation.


3. **Data description Generation:**
   - I used the various function of numpy library to extract descripton about the data. This can be used to gain insight into data along with heatmap.


4. **Heatmap Generation:**
   - I used the `matplotlib` library to create heatmaps from the generated or interpolated thermal data. The choice of the 'viridis' colormap and the 'nearest' interpolation method was made for clarity and visual appeal. Adding a color bar provides a reference for temperature values associated with the colors.


5. **Visualization and Interpretation:**
   - The generated heatmaps offer a visual representation of temperature distribution. Warmer colors indicate higher temperatures, while cooler colors represent lower temperatures. The visualization allows for quick insights into the thermal patterns present in the data.

6. **Documentation:**
   - Throughout the process, I ensured my code to be clear, concise and well commented.

*Further Steps:*

While the current implementation successfully generates heatmaps from mock thermal data, real-world applications may involve more complex data sources and additional considerations such as noise reduction, dynamic data streams, and scalability. Further refinement of the algorithm and integration with real thermal data sources would be necessary for a comprehensive and practical solution.

