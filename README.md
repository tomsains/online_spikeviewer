This project provides a real-time timeseries plotter built with PyQt5 and Matplotlib. The application displays a timeseries with dynamic updates, plotting random data values over time. It includes a rolling mean line to visualize trends in the data.

Features
Real-time updating plot using Matplotlib.
Simulated timeseries data with random fluctuations.
A rolling mean line to visualize data trends.
User-friendly interface with a navigation toolbar.
Automatically updates every 100 milliseconds.
Displays the latest 500 data points on the plot.
Requirements
Python 3.x
PyQt5
Matplotlib
pandas
You can install the required dependencies using pip:

bash
Copy code
pip install PyQt5 matplotlib pandas
Usage
To run the application, simply execute the Python script:

bash
Copy code
python real_time_plotter.py
Once the application starts, you will see a window displaying the real-time timeseries plot. The plot updates every 100 milliseconds with new data. The x-axis represents time, and the y-axis represents the data value, which fluctuates randomly. Additionally, a rolling mean line is displayed to show trends in the data.

Code Explanation
RealTimePlotter Class
Inherits from QMainWindow to create the main application window.
The plot is created using Matplotlib, and data is updated every 100ms via a QTimer.
Data is simulated using random values, and a rolling mean is calculated using pandas.
The plot updates dynamically, keeping only the last 500 data points.
Key Components
Matplotlib Plot: The plot updates with new data on each timer tick. The rolling mean is also updated.
Timer: A QTimer triggers the update function to simulate new data and refresh the plot.
Rolling Mean: A 10-point rolling mean is calculated and displayed alongside the timeseries.
Data Management: The x and y data are stored in lists and updated continuously. Only the most recent 500 data points are kept to avoid memory overflow.
License
This project is licensed under the MIT License - see the LICENSE file for details.
