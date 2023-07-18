import pytest
from PySide2.QtWidgets import QMessageBox
from app_plotter import AppPlotter

# Fixture to create an instance of AppPlotter for each test
@pytest.fixture
def app_plotter(qtbot):
    app_plotter = AppPlotter()
    qtbot.addWidget(app_plotter)
    return app_plotter


# Test valid plotting
def test_plot_valid_function_and_range(app_plotter, qtbot):
    function = "x**2"
    range_min = "0"
    range_max = "5"

    app_plotter.plot_function(function, range_min, range_max)
    qtbot.waitForWindowShown(app_plotter)

    # Assert the plot is not empty
    assert len(app_plotter.figure.axes) == 1
    assert len(app_plotter.figure.axes[0].lines) == 1

    # Assert the plot title and labels
    assert app_plotter.figure.axes[0].get_title() == function
    assert app_plotter.figure.axes[0].get_xlabel() == "x"
    assert app_plotter.figure.axes[0].get_ylabel() == "y"


# Test invalid inputs and error messages
@pytest.mark.parametrize(
    "function, range_min, range_max, error_msg",
    [
        ("x**2", "", "5", "Please enter all the required fields."),
        ("x**2", "1", "a", "Invalid range values. Please enter numeric values."),
        ("x**2", "5", "3", "Enter logical values, the max must be greater than the minimum."),
        ("x^2", "1", "5", "Error occurred while plotting the equation. Please check the syntax"),
    ],
)
def test_invalid_inputs_and_error_messages(app_plotter, qtbot, function, range_min, range_max, error_msg):
    app_plotter.plot_function(function, range_min, range_max)
    qtbot.waitForWindowShown(app_plotter)

    # Check if the error message dialog is shown
    assert len(qtbot.get_captured_widgets()) > 0
    last_widget = qtbot.get_captured_widgets()[-1]
    assert isinstance(last_widget, QMessageBox)
    assert last_widget.text() == error_msg


