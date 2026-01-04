from PyQt6.QtWidgets import (
    QPushButton,
    QLabel,
    QLineEdit,
    QFrame,
    QCheckBox,
    QGraphicsDropShadowEffect,
)
from PyQt6.QtCore import Qt, QPropertyAnimation, QEasingCurve, QPoint, pyqtProperty
from PyQt6.QtGui import QColor, QPainter, QBrush
from limqt6.theme.manager import theme_manager


class LimLabel(QLabel):
    def __init__(self, text="", parent=None):
        super().__init__(text, parent)
        # Style handles globally


class LimButton(QPushButton):
    def __init__(self, text="", parent=None):
        super().__init__(text, parent)
        # Style handled globally


class LimCard(QFrame):
    """
    A modern container with rounded corners, background color, and optional drop shadow.
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("LimCard")
        # Shadow effect
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(15)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(4)
        self.shadow.setColor(QColor(0, 0, 0, 30))
        self.setGraphicsEffect(self.shadow)

        # Additional property to ensure it's not transparent if styled poorly
        self.setAutoFillBackground(True)


class LimInput(QLineEdit):
    """
    Enhanced QLineEdit with padding and modern styling.
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setTextMargins(10, 5, 10, 5)
        self.setMinimumHeight(40)


class LimSwitch(QCheckBox):
    """
    A Toggle Switch replacement for QCheckBox.
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(50, 26)
        self.setCursor(Qt.CursorShape.PointingHandCursor)

        self._position = 3.0
        self.animation = QPropertyAnimation(self, b"position", self)
        self.animation.setDuration(200)
        self.animation.setEasingCurve(QEasingCurve.Type.InOutQuad)

        self.stateChanged.connect(self.animate)

    @pyqtProperty(float)
    def position(self):
        return self._position

    @position.setter
    def position(self, pos):
        self._position = pos
        self.update()

    def animate(self, state):
        start = 3
        end = self.width() - 23
        if self.isChecked():
            self.animation.setStartValue(start)
            self.animation.setEndValue(end)
        else:
            self.animation.setStartValue(end)
            self.animation.setEndValue(start)
        self.animation.start()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        t = theme_manager.current_theme

        # Bbox for reference
        rect = self.rect()

        if self.isChecked():
            bg_color = QColor(t.primary)
        else:
            if t.name == "light":
                bg_color = QColor("#e4e4e7")
            else:
                bg_color = QColor("#3f3f46")

        painter.setBrush(QBrush(bg_color))
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawRoundedRect(0, 0, rect.width(), rect.height(), 13, 13)

        painter.setBrush(QBrush(QColor("#ffffff")))
        painter.drawEllipse(QPoint(int(self._position) + 10, 13), 10, 10)

    def hitButton(self, pos):
        return self.contentsRect().contains(pos)
