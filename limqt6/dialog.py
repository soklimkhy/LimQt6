from typing import Optional

from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtGui import QMouseEvent
from PyQt6.QtWidgets import (
    QDialog,
)
from limqt6.widgets import (
    LimWidget,
    LimFrame,
    LimLabel,
    LimButton,
)
from limqt6.layout import (
    LimVBoxLayout,
    LimHBoxLayout,
)


class _LimDialogHeader(LimWidget):
    """
    Title bar area of LimDialog. Dragging it moves the dialog window,
    since the dialog itself is frameless.
    """

    def __init__(self, parent: Optional[LimWidget] = None):
        super().__init__(parent)
        self._drag_offset: Optional[QPoint] = None

    def mousePressEvent(self, a0: Optional[QMouseEvent]) -> None:
        if a0 is not None and a0.button() == Qt.MouseButton.LeftButton:
            self._drag_offset = a0.globalPosition().toPoint() - self.window().pos()
            a0.accept()

    def mouseMoveEvent(self, a0: Optional[QMouseEvent]) -> None:
        if a0 is not None and self._drag_offset is not None:
            self.window().move(a0.globalPosition().toPoint() - self._drag_offset)
            a0.accept()

    def mouseReleaseEvent(self, a0: Optional[QMouseEvent]) -> None:
        self._drag_offset = None


class LimDialog(QDialog):
    """
    Frameless, draggable modal dialog matching the theme system. Has a
    header (title + close button), a content area you build via
    `dialog.content` (e.g. LimVBoxLayout(dialog.content)), and a footer you
    add buttons to with add_action().
    """

    def __init__(self, title: str = "", parent: Optional[LimWidget] = None):
        super().__init__(parent)
        self.setObjectName("LimDialog")
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.Dialog)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setModal(True)

        outer = LimVBoxLayout(self)
        outer.setContentsMargins(0, 0, 0, 0)

        self.card = LimFrame(self)
        self.card.setObjectName("LimDialogCard")
        outer.addWidget(self.card)

        card_layout = LimVBoxLayout(self.card)
        card_layout.setContentsMargins(0, 0, 0, 0)
        card_layout.setSpacing(0)

        # Header: title + close button, also the drag handle.
        self.header = _LimDialogHeader(self.card)
        self.header.setObjectName("LimDialogHeader")
        self.header.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        header_layout = LimHBoxLayout(self.header)
        header_layout.setContentsMargins(16, 12, 12, 12)
        header_layout.setSpacing(8)

        self.title_label = LimLabel(title, self.header)
        self.title_label.setObjectName("LimDialogTitle")
        header_layout.addWidget(self.title_label)
        header_layout.addStretch()

        self.close_btn = LimButton("✕", self.header)
        self.close_btn.setObjectName("LimDialogCloseButton")
        self.close_btn.setFixedSize(24, 24)
        self.close_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.close_btn.clicked.connect(self.reject)
        header_layout.addWidget(self.close_btn)

        card_layout.addWidget(self.header)

        # Content: caller fills this in, e.g. LimVBoxLayout(dialog.content).
        self.content = LimWidget(self.card)
        self.content.setObjectName("LimDialogContent")
        self.content.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        card_layout.addWidget(self.content)

        # Footer: action buttons, right-aligned.
        self.footer = LimWidget(self.card)
        self.footer.setObjectName("LimDialogFooter")
        self.footer.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self._footer_layout = LimHBoxLayout(self.footer)
        self._footer_layout.setContentsMargins(16, 12, 16, 12)
        self._footer_layout.setSpacing(8)
        self._footer_layout.addStretch()
        card_layout.addWidget(self.footer)

    def add_action(self, widget: LimWidget) -> LimWidget:
        self._footer_layout.addWidget(widget)
        return widget
