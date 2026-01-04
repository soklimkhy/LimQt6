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

    # Icon Button Test
    from limqt6.icon import LimIcon
    import os

    # Ensure assets dir exists for the demo run
    icon_path = os.path.abspath("assets/star.svg")
    icon_btn = LimButton("   Star Icon")
    icon_btn.setIcon(LimIcon(icon_path))

    # Theme toggle buttons
    theme_layout = QHBoxLayout()
    btn_light = LimButton("Light Theme")
    btn_dark = LimButton("Dark Theme")

    def set_theme(name):
        theme_manager.set_theme(name)
        # Refresh icon color manually for now
        # In a full framework, we'd use signals to auto-update
        icon_btn.setIcon(LimIcon(icon_path))

    btn_light.clicked.connect(lambda: set_theme("light"))
    btn_dark.clicked.connect(lambda: set_theme("dark"))

    theme_layout.addWidget(btn_light)
    theme_layout.addWidget(btn_dark)

    layout.addWidget(label)
    layout.addWidget(button)
    layout.addWidget(icon_btn)
    layout.addLayout(theme_layout)

    window.show()

    app.exec()


if __name__ == "__main__":
    main()
