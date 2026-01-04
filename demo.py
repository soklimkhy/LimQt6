from PyQt6.QtWidgets import QWidget, QVBoxLayout
from limqt6.widgets import LimButton, LimLabel
from limqt6.core.app import LimApp


def main():
    app = LimApp()

    window = QWidget()
    window.setWindowTitle("LimQt6 Demo")
    window.resize(400, 300)

    layout = QVBoxLayout(window)

    label = LimLabel("Hello from LimQt6!")
    button = LimButton("Click Me")

    layout.addWidget(label)
    layout.addWidget(button)

    window.show()

    app.exec()


if __name__ == "__main__":
    main()
