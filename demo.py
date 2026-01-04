import os
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout
from limqt6.widgets import LimButton, LimLabel, LimLineEdit, LimFrame
from limqt6.widgetsplus import LimSwitch
from limqt6.core.app import LimApp
from limqt6.theme.manager import theme_manager
from limqt6.icon import LimIcon


def main():
    app = LimApp()

    window = QWidget()
    window.setWindowTitle("LimQt6 Demo")
    window.resize(400, 300)

    layout = QVBoxLayout(window)
    layout.setSpacing(15)

    # 1. Card Section
    card = LimFrame()
    card_layout = QVBoxLayout(card)
    card_layout.addWidget(LimLabel("This is a LimFrame Container"))

    # 2. Input Section
    input_field = LimLineEdit()
    input_field.setPlaceholderText("Type something here...")
    card_layout.addWidget(input_field)

    # 3. Switch Section
    switch_layout = QHBoxLayout()
    switch_layout.addWidget(LimLabel("Toggle Option:"))
    switch = LimSwitch()
    switch_layout.addWidget(switch)
    switch_layout.addStretch()
    card_layout.addLayout(switch_layout)

    layout.addWidget(card)

    # Standard elements
    label = LimLabel("Hello from LimQt6!")

    button = LimButton("Click Me")

    icon_path = os.path.abspath("assets/star.svg")
    icon_btn = LimButton("   Star Icon")
    icon_btn.setIcon(LimIcon(icon_path))

    # Theme toggle buttons
    theme_layout = QHBoxLayout()
    btn_light = LimButton("Light Theme")
    btn_dark = LimButton("Dark Theme")

    def set_theme(name):
        theme_manager.set_theme(name)
        icon_btn.setIcon(LimIcon(icon_path))
        switch.update()  # Force repaint

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
