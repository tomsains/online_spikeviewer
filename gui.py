import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtCore import QTimer
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar,
)
import matplotlib.pyplot as plt
import pandas as pd
import time

class RealTimePlotter(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Real-Time Timeseries Plot")
        self.start_time = time.time()
        # Set up the central widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Create a vertical layout
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # Create the Matplotlib figure and axes
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)

        # Add the Matplotlib canvas to the layout
        self.layout.addWidget(NavigationToolbar(self.canvas, self))
        self.layout.addWidget(self.canvas)

        # Data for the timeseries
        self.x_data = []
        self.y_data = []

        # Line for the plot
        self.line, = self.ax.plot([], [], 'black', label="Timeseries", alpha=0.5)
        self.mean_line, = self.ax.plot([], [], 'blue', label="rolling mean")
        self.ax.set_title("Real-Time Timeseries Plot")
        self.ax.set_xlabel("Time")
        self.ax.set_ylabel("Value")
        self.ax.legend(loc = "upper right")

        # Timer for updating the plot
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_plot)
        self.timer.start(5)  # Update every 100 ms

    def update_plot(self):
        # Simulate new data
        if len(self.x_data) == 0:
            self.x_data.append(0)
        else:
            self.x_data.append(time.time() - self.start_time)
        
        if len(self.y_data) < 1:
            self.y_data.append(random.uniform(-1, 1))
        else:
            self.y_data.append(self.y_data [-1] + random.uniform(-1, 1))
        
        self.mean_data = self.y_data
        self.mean_data = pd.Series(self.mean_data).rolling(10, center=True, min_periods=1).mean()

        # Keep only the last 100 data points
        if len(self.x_data) > 500:
            self.x_data = self.x_data[-500:]
            self.y_data = self.y_data[-500:]
            self.mean_data = self.mean_data [-500:]

        # Update the line data
        self.line.set_data(self.x_data, self.y_data)
        
        self.mean_line.set_data(self.x_data, self.mean_data)

        # Adjust the axes limits
        self.ax.set_xlim(min(self.x_data), max(self.x_data))
        self.ax.set_ylim(min(self.y_data) - 0.1, max(self.y_data) + 0.1)

        # Redraw the canvas
        self.canvas.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = RealTimePlotter()
    main_window.show()
    sys.exit(app.exec_())
