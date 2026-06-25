import os
from limqt6.widgets import (
    LimWidget,
    LimCheckBox,
    LimButton,
    LimLabel,
)
from limqt6.layout import LimHBoxLayout
from PyQt6.QtCore import (
    Qt,
    QSize,
    QPropertyAnimation,
    QEasingCurve,
    QPoint,
    pyqtProperty,  # pyright: ignore[reportAttributeAccessIssue, reportUnknownVariableType]
)
from PyQt6.QtGui import QColor, QPainter, QBrush, QIcon, QPaintEvent
from limqt6.theme.manager import theme_manager

_ASSETS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets")


class LimBadge(LimWidget):
    """
    A small badge component to display status or tags (e.g. 'Verified').
    Can optionally include an icon.
    """

    def __init__(self, text: str, icon_path: str | None = None, parent: LimWidget | None = None):
        super().__init__(parent)
        self.setObjectName("LimBadge")
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        
        layout = LimHBoxLayout(self)
        layout.setContentsMargins(8, 4, 8, 4)
        layout.setSpacing(6)
        
        if icon_path:
            self.icon_label = LimLabel("", self)
            self.icon_label.setPixmap(QIcon(icon_path).pixmap(14, 14))
            layout.addWidget(self.icon_label)
            
        self.text_label = LimLabel(text, self)
        self.text_label.setObjectName("LimBadgeText")
        layout.addWidget(self.text_label)


class LimSwitch(LimCheckBox):
    """
    A Toggle Switch replacement for QCheckBox.
    """

    def __init__(self, parent: LimWidget | None = None):
        super().__init__(parent)
        self.setFixedSize(50, 26)
        self.setCursor(Qt.CursorShape.PointingHandCursor)

        self._position: float = 3.0
        self.animation = QPropertyAnimation(self, b"position", self)
        self.animation.setDuration(200)
        self.animation.setEasingCurve(QEasingCurve.Type.InOutQuad)

        self.stateChanged.connect(self.animate)

    @pyqtProperty(float)  # pyright: ignore[reportUntypedFunctionDecorator]
    def position(self) -> float:  # pyright: ignore[reportRedeclaration]
        return self._position

    @position.setter  # pyright: ignore[reportFunctionMemberAccess]
    def position(self, pos: float) -> None:
        self._position = pos
        self.update()

    def animate(self, state: int) -> None:
        start = 3
        end = self.width() - 23
        if self.isChecked():
            self.animation.setStartValue(start)
            self.animation.setEndValue(end)
        else:
            self.animation.setStartValue(end)
            self.animation.setEndValue(start)
        self.animation.start()

    def paintEvent(self, a0: QPaintEvent | None) -> None:
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        t = theme_manager.current_theme
        rect = self.rect()

        # Track Color
        if self.isChecked():
            bg_color = QColor(t.primary)
        else:
            bg_color = QColor(t.input_border)

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

    def hitButton(self, pos: QPoint) -> bool:
        return self.contentsRect().contains(pos)


############## THEME SWITCHER ###################


class LimThemeSwitcher(LimButton):
    """
    Icon-only button that toggles between light/dark themes. Shows a sun
    icon while in light mode and a moon icon while in dark mode.
    """

    def __init__(self, parent: LimWidget | None = None):
        super().__init__(parent)
        self.setObjectName("LimThemeSwitcher")
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setFixedSize(32, 32)
        self.setIconSize(QSize(18, 18))

        self._sync_icon()
        self.clicked.connect(self._toggle)

    def _toggle(self):
        next_theme = "dark" if theme_manager.current_theme.name == "light" else "light"
        theme_manager.set_theme(next_theme)
        self._sync_icon()

    def _sync_icon(self):
        icon_file = (
            "sun_icon.svg" if theme_manager.current_theme.name == "light" else "moon_icon.svg"
        )
        self.setIcon(QIcon(os.path.join(_ASSETS_DIR, icon_file)))
