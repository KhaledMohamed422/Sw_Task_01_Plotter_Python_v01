from PySide2.QtWidgets import (QMainWindow, QVBoxLayout,
                               QFormLayout, QLineEdit,
                               QLabel, QPushButton,
                               QWidget)
from PySide2.QtCore import Qt

from gui import CustomTitleBar
from app_plotter import AppPlotter

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Function Plotter")
        self.setGeometry(400, 400, 800, 600)

        # Create a custom title bar
        title_bar = CustomTitleBar(self)
        self.setMenuWidget(title_bar)

        # Create the main layout
        main_layout = QVBoxLayout()

        # Create form layout for function and range inputs
        form_layout = QFormLayout()

        # Create labels and line edits for function and range inputs
        self.function_label = QLabel("Function of x:")
        self.function_input = QLineEdit()
        self.function_input.setPlaceholderText("e.g : 5*(x^2)+10")  # Placeholder text for guidance
        self.range_min_label = QLabel("Minimum value of x:")
        self.range_min_input = QLineEdit()
        self.range_min_input.setPlaceholderText("e.g : numbers 1 2 8 ...")  # Placeholder text for guidance
        self.range_max_label = QLabel("Maximum value of x:")
        self.range_max_input = QLineEdit()
        self.range_max_input.setPlaceholderText("e.g : numbers 1 2 8 ...")  # Placeholder text for guidance

        # Add labels and line edits to form layout
        form_layout.addRow(self.function_label, self.function_input)
        form_layout.addRow(self.range_min_label, self.range_min_input)
        form_layout.addRow(self.range_max_label, self.range_max_input)

        # Set alignment of labels
        form_layout.setLabelAlignment(Qt.AlignLeft)

        # Add the plot button
        self.plot_button = QPushButton("Plot")
        self.plot_button.clicked.connect(self.plot_button_clicked)

        # Create the AppPlotter instance
        self.app_plotter = AppPlotter()

        main_layout.addLayout(form_layout)
        main_layout.addWidget(self.plot_button)
        main_layout.addWidget(self.app_plotter)

        # Create a central widget and set the main layout
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # Set the stylesheet for the main window
        self.setStyleSheet("""
            QMainWindow {
                background-color: #292929;
            }
            QLabel {
                color: #FFFFFF;
            }
            QLineEdit {
                background-color: #616161;
                border: 1px solid #CCCCCC;
                color: #FFFFFF;
                padding: 5px; 
            }
            QPushButton {
                background-color: #2B609E;
                color: white;
                font-weight: bold;
                border: none;
                padding: 8px 16px;
            }
            QMessageBox {
                background-color: #292929;
            }
        """)

    def plot_button_clicked(self):
        # Retrieve user input
        function = self.function_input.text()
        range_min = self.range_min_input.text()
        range_max = self.range_max_input.text()

        self.app_plotter.plot_function(function, range_min, range_max)
