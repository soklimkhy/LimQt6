import os
from typing import Callable, Optional

from PyQt6.QtWidgets import (
    QFrame,
    QPushButton,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QButtonGroup,
    QWidget,
)
from PyQt6.QtCore import Qt, QSize, QPropertyAnimation, QEasingCurve, pyqtProperty
from PyQt6.QtGui import QIcon

_ASSETS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets")


############## NAV ITEM ###################


class LimNavItem(QPushButton):
    """
    A checkable button used inside LimSidebar/LimNavbar to represent a
    navigation entry. Collapses to icon-only via set_collapsed().
    """

    def __init__(self, text: str = "", icon: Optional[QIcon] = None, parent=None):
        super().__init__(text, parent)
        self._full_text = text
        self.setObjectName("LimNavItem")
        self.setCheckable(True)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setMinimumHeight(36)
        if icon is not None:
            self.setIcon(icon)

    def set_collapsed(self, collapsed: bool):
        self.setText("" if collapsed else self._full_text)
        self.setToolTip(self._full_text if collapsed else "")


############## SIDEBAR ###################


class LimSidebar(QFrame):
    """
    A collapsible vertical navigation panel. Add entries with add_item();
    only one entry is active at a time (exclusive selection).
    """

    EXPANDED_WIDTH = 220
    COLLAPSED_WIDTH = 64

    def __init__(self, title="LimQt6", parent=None):
        super().__init__(parent)
        self.setObjectName("LimSidebar")

        self._collapsed = False
        self._width = self.EXPANDED_WIDTH
        self.setFixedWidth(self._width)

        self._nav_items = []
        self._button_group = QButtonGroup(self)
        self._button_group.setExclusive(True)

        root = QVBoxLayout(self)
        root.setContentsMargins(8, 12, 8, 12)
        root.setSpacing(4)

        self.brand_label = QLabel(title)
        self.brand_label.setObjectName("LimBrandLabel")
        root.addWidget(self.brand_label)
        root.addSpacing(8)

        self._items_layout = QVBoxLayout()
        self._items_layout.setSpacing(2)
        root.addLayout(self._items_layout)
        root.addStretch()

        self.animation = QPropertyAnimation(self, b"sidebar_width", self)
        self.animation.setDuration(200)
        self.animation.setEasingCurve(QEasingCurve.Type.InOutQuad)

    @pyqtProperty(int)
    def sidebar_width(self):
        return self._width

    @sidebar_width.setter
    def sidebar_width(self, value):
        self._width = value
        self.setFixedWidth(value)

    def add_item(
        self, text: str, icon: Optional[QIcon] = None, checked: bool = False
    ) -> LimNavItem:
        item = LimNavItem(text, icon=icon)
        item.setChecked(checked)
        item.set_collapsed(self._collapsed)
        self._button_group.addButton(item)
        self._items_layout.addWidget(item)
        self._nav_items.append(item)
        return item

    def toggle(self):
        self.set_collapsed(not self._collapsed)

    def set_collapsed(self, collapsed: bool):
        self._collapsed = collapsed
        target = self.COLLAPSED_WIDTH if collapsed else self.EXPANDED_WIDTH

        self.animation.stop()
        self.animation.setStartValue(self._width)
        self.animation.setEndValue(target)
        self.animation.start()

        self.brand_label.setVisible(not collapsed)
        for item in self._nav_items:
            item.set_collapsed(collapsed)


############## NAVBAR ###################


class LimNavbar(QFrame):
    """
    A horizontal top bar with a title on the left and an actions area on
    the right. Add buttons/widgets to the right side with add_action().
    """

    def __init__(self, title="", parent=None):
        super().__init__(parent)
        self.setObjectName("LimNavbar")
        self.setFixedHeight(56)

        self._layout = QHBoxLayout(self)
        self._layout.setContentsMargins(16, 0, 16, 0)
        self._layout.setSpacing(12)

        self.menu_btn = None

        self.title_label = QLabel(title)
        self.title_label.setObjectName("LimBrandLabel")
        self._layout.addWidget(self.title_label)

        self._layout.addStretch()

        self._actions_layout = QHBoxLayout()
        self._actions_layout.setSpacing(8)
        self._layout.addLayout(self._actions_layout)

    def set_menu_callback(self, callback: Callable[[], None]) -> QPushButton:
        """
        Adds a hamburger button before the title (if not already added)
        and connects it to `callback`, e.g. navbar.set_menu_callback(sidebar.toggle).
        """
        if self.menu_btn is None:
            self.menu_btn = QPushButton()
            self.menu_btn.setObjectName("LimNavbarMenuButton")
            self.menu_btn.setIcon(QIcon(os.path.join(_ASSETS_DIR, "menu_icon.svg")))
            self.menu_btn.setIconSize(QSize(18, 18))
            self.menu_btn.setFixedSize(32, 32)
            self.menu_btn.setCursor(Qt.CursorShape.PointingHandCursor)
            self._layout.insertWidget(0, self.menu_btn)
        self.menu_btn.clicked.connect(callback)
        return self.menu_btn

    def add_action(self, widget: QWidget) -> QWidget:
        self._actions_layout.addWidget(widget)
        return widget


class LimVBoxLayout(QVBoxLayout):
    """
    A basic styled QVBoxLayout.
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("LimVBoxLayout")


class LimHBoxLayout(QHBoxLayout):
    """
    A basic styled QHBoxLayout.
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("LimHBoxLayout")

