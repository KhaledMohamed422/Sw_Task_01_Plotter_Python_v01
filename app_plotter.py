from PySide2.QtWidgets import QWidget, QVBoxLayout,QMessageBox
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class AppPlotter(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)

        # Create the figure and canvas for the matplotlib plot
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)

        self.layout.addWidget(self.canvas)

        self.setLayout(self.layout)

    def plot_function(self, function, range_min, range_max):
        
        # Validate user input
        if not function or not range_min or not range_max:
            QMessageBox.warning(self, "Input Error", "Please enter all the required fields.")
            return
        try:
            range_min = float(range_min)
            range_max = float(range_max)
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Invalid range values. Please enter numeric values.")
            return
        
        if float(range_min) > float(range_max):
            QMessageBox.warning(self, "Logical Error", "Enter logical values, the max must be greater than the minimum.")
            return


        # Plot the function
        try:
            x = []
            y = []
            step = 0.1
            current_x = range_min
            while current_x <= range_max:
                x.append(current_x)
                y.append(eval(function.replace("^", "**").replace("x", str(current_x))))
                current_x += step

            self.figure.clear()
            ax = self.figure.add_subplot(111)
            ax.plot(x, y)
            ax.set_title(function)
            ax.set_xlabel("x")
            ax.set_ylabel("y")
            self.canvas.draw()

        except:
            QMessageBox.warning(self, "Plotting Error", f"Error occurred while plotting the equation. Please check the syntax")
