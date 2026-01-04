from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout
from limqt6.widgets import LimButton, LimLabel
from limqt6.core.app import LimApp
from limqt6.theme.manager import theme_manager


def main():
    app = LimApp()

    window = QWidget()
    window.setWindowTitle("LimQt6 Demo - Theme Test")
    window.resize(400, 300)

    layout = QVBoxLayout(window)

    label = LimLabel("Hello from LimQt6!")
    button = LimButton("Click Me")

    # Theme toggle buttons
    theme_layout = QHBoxLayout()
    btn_light = LimButton("Light Theme")
    btn_dark = LimButton("Dark Theme")

    btn_light.clicked.connect(lambda: theme_manager.set_theme("light"))
    btn_dark.clicked.connect(lambda: theme_manager.set_theme("dark"))

    theme_layout.addWidget(btn_light)
    theme_layout.addWidget(btn_dark)

    layout.addWidget(label)
    layout.addWidget(button)
    layout.addLayout(theme_layout)

    window.show()

    app.exec()


if __name__ == "__main__":
    main()
