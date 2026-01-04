from PyQt6.QtWidgets import (
    QPushButton,
    QLabel,
    QLineEdit,
    QFrame,
    QGraphicsDropShadowEffect,
)
from PyQt6.QtGui import QColor


class LimLabel(QLabel):
    def __init__(self, text="", parent=None):
        super().__init__(text, parent)
        # Style handles globally


class LimButton(QPushButton):
    def __init__(self, text="", parent=None):
        super().__init__(text, parent)
        # Style handled globally


class LimFrame(QFrame):
    """
    A modern container with rounded corners, background color, and optional drop shadow.
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("LimFrame")
        # Shadow effect
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(15)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(4)
        self.shadow.setColor(QColor(0, 0, 0, 30))
        self.setGraphicsEffect(self.shadow)

        # Additional property to ensure it's not transparent if styled poorly
        self.setAutoFillBackground(True)


class LimLineEdit(QLineEdit):
    """
    Enhanced QLineEdit with padding and modern styling.
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setTextMargins(3, 3, 3, 3)
        self.setMinimumHeight(33)
