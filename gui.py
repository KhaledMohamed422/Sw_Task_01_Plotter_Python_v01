from PySide2.QtWidgets import QLabel, QVBoxLayout, QHBoxLayout, QWidget
from PySide2.QtGui import QFont, QPixmap

class CustomTitleBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)
        self.title_layout = QHBoxLayout()
        self.logo_label = QLabel(self)  # New label for the logo
        self.title_label = QLabel("Function Plotter", self)

        # Load the logo image and set its size
        logo_pixmap = QPixmap("images/logo_master_micro.png")
        self.logo_label.setPixmap(logo_pixmap.scaled(32, 32))  # Set the desired logo size (e.g., 32x32 pixels)

        # Set the title label font and size
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.title_label.setFont(font)

        # Add the logo and title labels to the title layout
        self.title_layout.addWidget(self.logo_label)
        self.title_layout.addWidget(self.title_label)
        self.title_layout.addStretch(1)  # Add stretch to push the title to the right

        # Add the title layout to the main layout
        self.layout.addLayout(self.title_layout)

        # Set the layout for the custom title bar
        self.setLayout(self.layout)
