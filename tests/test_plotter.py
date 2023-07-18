import sys
from PySide2.QtWidgets import QApplication
from test_plotter import PlotterApp


def test_plotter_input_validation(qtbot):
    app = QApplication(sys.argv)
    plotter = PlotterApp()
    qtbot.addWidget(plotter)
    plotter.show()

    # Simulate clicking the Plot button without entering any data
    qtbot.mouseClick(plotter.plot_button, Qt.LeftButton)

    # Check if a warning message box is displayed
    warning_message_box = plotter.findChild(QMessageBox, "Input Error")
    assert warning_message_box is not None
    assert "Please enter all the required fields." in warning_message_box.text()

    # Close the warning message box
    qtbot.mouseClick(warning_message_box.button(QMessageBox.Close), Qt.LeftButton)

    # Simulate entering invalid range values
    qtbot.keyClicks(plotter.range_min_input, "2")
    qtbot.keyClicks(plotter.range_max_input, "1")
    qtbot.mouseClick(plotter.plot_button, Qt.LeftButton)

    # Check if a logical error message box is displayed
    logical_error_message_box = plotter.findChild(QMessageBox, "Logical Error")
    assert logical_error_message_box is not None
    assert "Enter logical values, the max must be greater than the minimum." in logical_error_message_box.text()

    # Close the logical error message box
    qtbot.mouseClick(logical_error_message_box.button(QMessageBox.Close), Qt.LeftButton)

    # Simulate entering valid inputs and clicking the Plot button
    qtbot.keyClicks(plotter.function_input, "x**2")
    qtbot.keyClicks(plotter.range_min_input, "0")
    qtbot.keyClicks(plotter.range_max_input, "5")
    qtbot.mouseClick(plotter.plot_button, Qt.LeftButton)

    # Check if the plot was displayed
    assert plotter.figure is not None

    # Close the main window
    plotter.close()
