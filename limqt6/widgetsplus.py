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
from PyQt6.QtGui import QColor, QPainter, QBrush, QIcon, QPaintEvent, QMouseEvent
from limqt6.theme.manager import theme_manager

_ASSETS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets")


class LimCarousel(LimWidget):
    """
    A swipeable, animated carousel component inspired by Embla Carousel.
    Add widgets as slides and swipe horizontally to navigate.
    """

    def __init__(self, parent: LimWidget | None = None):
        super().__init__(parent)
        self.setObjectName("LimCarousel")
        self.setCursor(Qt.CursorShape.OpenHandCursor)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        
        self.container = LimWidget(self)
        self.container.setObjectName("LimCarouselContainer")
        self.container_layout = LimHBoxLayout(self.container)
        self.container_layout.setContentsMargins(0, 0, 0, 0)
        self.container_layout.setSpacing(16)
        
        self.animation = QPropertyAnimation(self.container, b"pos", self)
        self.animation.setDuration(400)
        self.animation.setEasingCurve(QEasingCurve.Type.OutCubic)
        
        self._slides: list[LimWidget] = []
        
        # Dragging state
        self._is_dragging = False
        self._start_x = 0
        self._start_pos_x = 0
        self._current_index = 0

        self.prev_btn = LimButton("<", self)
        self.prev_btn.setObjectName("LimCarouselPrevBtn")
        self.prev_btn.setFixedSize(30, 30)
        self.prev_btn.clicked.connect(self.prev)
        self.prev_btn.setCursor(Qt.CursorShape.PointingHandCursor)

        self.next_btn = LimButton(">", self)
        self.next_btn.setObjectName("LimCarouselNextBtn")
        self.next_btn.setFixedSize(30, 30)
        self.next_btn.clicked.connect(self.next)
        self.next_btn.setCursor(Qt.CursorShape.PointingHandCursor)

    def add_slide(self, widget: LimWidget):
        self._slides.append(widget)
        self.container_layout.addWidget(widget)
        self._update_container_width()
        
    def _update_container_width(self):
        self.container.adjustSize()

    def sizeHint(self) -> QSize:
        # Provide a reasonable default size so it doesn't collapse to 0
        return QSize(400, 150)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self._update_container_width()
        self.snap_to(self._current_index)
        
        # Position buttons vertically centered at edges
        btn_y = (self.height() - self.prev_btn.height()) // 2
        self.prev_btn.move(10, btn_y)
        self.next_btn.move(self.width() - self.next_btn.width() - 10, btn_y)
        self.prev_btn.raise_()
        self.next_btn.raise_()

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self._is_dragging = True
            self._start_x = int(event.globalPosition().x())
            self._start_pos_x = self.container.pos().x()
            self.animation.stop()
            self.setCursor(Qt.CursorShape.ClosedHandCursor)
            event.accept()

    def mouseMoveEvent(self, event: QMouseEvent):
        if self._is_dragging:
            delta = int(event.globalPosition().x()) - self._start_x
            new_x = self._start_pos_x + delta
            
            # Simple rubber band effect
            max_x = 0
            min_x = self.width() - self.container.width()
            if min_x > 0:
                min_x = 0
                
            if new_x > max_x:
                new_x = int(max_x + (new_x - max_x) * 0.3)
            elif new_x < min_x:
                new_x = int(min_x + (new_x - min_x) * 0.3)
                
            self.container.move(new_x, self.container.pos().y())
            event.accept()

    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton and self._is_dragging:
            self._is_dragging = False
            self.setCursor(Qt.CursorShape.OpenHandCursor)
            
            current_x = self.container.pos().x()
            best_idx = 0
            min_dist = float('inf')
            
            for i, slide in enumerate(self._slides):
                slide_center = slide.pos().x() + slide.width() / 2
                viewport_center = self.width() / 2 - current_x
                
                dist = abs(slide_center - viewport_center)
                if dist < min_dist:
                    min_dist = dist
                    best_idx = i
            
            self.snap_to(best_idx)
            event.accept()
            
    def snap_to(self, index: int):
        if not self._slides:
            return
            
        index = max(0, min(index, len(self._slides) - 1))
        self._current_index = index
        
        target_slide = self._slides[index]
        viewport_center = self.width() / 2
        slide_center = target_slide.pos().x() + target_slide.width() / 2
        
        target_x = int(viewport_center - slide_center)
        
        max_x = 0
        min_x = self.width() - self.container.width()
        if min_x > 0:
            min_x = 0
            
        target_x = max(min_x, min(target_x, max_x))
        
        self.animation.setStartValue(self.container.pos())
        self.animation.setEndValue(QPoint(target_x, self.container.pos().y()))
        self.animation.start()

    def next(self):
        if not self._slides:
            return
        next_idx = self._current_index + 1
        if next_idx >= len(self._slides):
            next_idx = 0
        self.snap_to(next_idx)
        
    def prev(self):
        if not self._slides:
            return
        prev_idx = self._current_index - 1
        if prev_idx < 0:
            prev_idx = len(self._slides) - 1
        self.snap_to(prev_idx)


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
