from PyQt6.QtWidgets import QCheckBox
from PyQt6.QtCore import Qt, QPropertyAnimation, QEasingCurve, QPoint, pyqtProperty
from PyQt6.QtGui import QColor, QPainter, QBrush
from limqt6.theme.manager import theme_manager


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
        rect = self.rect()

        # Track Color
        if self.isChecked():
            bg_color = QColor(t.primary)
            border_color = Qt.GlobalColor.transparent
        else:
            bg_color = QColor(t.input_border)
            border_color = Qt.GlobalColor.transparent
            # Enhance definition if input border is too light
            # For shadcn, the unchecked switch is usually a dark gray (input)

        painter.setBrush(QBrush(bg_color))
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawRoundedRect(0, 0, rect.width(), rect.height(), 13, 13)

        # Thumb Color
        # Checked: Thumb is color of text on primary (usually white or black)
        # Unchecked: Thumb is usually white
        if self.isChecked():
            thumb_color = QColor(t.primary_foreground)
        else:
            thumb_color = QColor("#ffffff")

        painter.setBrush(QBrush(thumb_color))
        painter.drawEllipse(QPoint(int(self._position) + 10, 13), 10, 10)

    def hitButton(self, pos):
        return self.contentsRect().contains(pos)
