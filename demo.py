import os
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout
from limqt6.widgets import LimButton, LimLabel, LimLineEdit, LimFrame, LimCheckBox
from limqt6.widgetsplus import LimSwitch, LimThemeSwitcher
from limqt6.layout import LimSidebar, LimNavbar
from limqt6.core.app import LimApp
from PyQt6.QtGui import QIcon


def build_content() -> tuple[QWidget, LimSwitch]:
    content = QWidget()
    layout = QVBoxLayout(content)
    layout.setContentsMargins(20, 20, 20, 20)
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

    # 4. Checkbox
    checkbox = LimCheckBox("Accept Terms & Conditions")
    card_layout.addWidget(checkbox)

    layout.addWidget(card)

    # Standard elements
    label = LimLabel("Hello from LimQt6!")

    button = LimButton("Click Me")

    icon_path = os.path.abspath("assets/star.svg")
    icon_btn = LimButton("   Star Icon")
    icon_btn.setIcon(QIcon(icon_path))

    layout.addWidget(label)
    layout.addWidget(button)
    layout.addWidget(icon_btn)
    layout.addStretch()

    return content, switch


def main():
    app = LimApp()

    window = QWidget()
    window.setWindowTitle("LimQt6")
    window.resize(840, 520)

    root_layout = QHBoxLayout(window)
    root_layout.setContentsMargins(0, 0, 0, 0)
    root_layout.setSpacing(0)

    # Sidebar
    sidebar = LimSidebar("LimQt6")
    sidebar.add_item("Dashboard", checked=True)
    sidebar.add_item("Components")
    sidebar.add_item("Settings")
    root_layout.addWidget(sidebar)

    # Right side: Navbar on top, content below
    right_panel = QWidget()
    right_layout = QVBoxLayout(right_panel)
    right_layout.setContentsMargins(0, 0, 0, 0)
    right_layout.setSpacing(0)

    navbar = LimNavbar("Dashboard")
    navbar.set_menu_callback(sidebar.toggle)
    theme_switcher = LimThemeSwitcher()
    navbar.add_action(theme_switcher)
    right_layout.addWidget(navbar)

    content, switch = build_content()
    right_layout.addWidget(content)

    root_layout.addWidget(right_panel)

    theme_switcher.clicked.connect(switch.update)  # Force repaint after theme change

    window.show()

    app.exec()


if __name__ == "__main__":
    main()
