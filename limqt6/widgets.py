from PyQt6.QtWidgets import QPushButton, QLabel


class LimLabel(QLabel):
    def __init__(self, text="", parent=None):
        super().__init__(text, parent)
        # Style is now handled globally by ThemeManager via CSS selectors


class LimButton(QPushButton):
    def __init__(self, text="", parent=None):
        super().__init__(text, parent)
        # Style is now handled globally by ThemeManager via CSS selectors
