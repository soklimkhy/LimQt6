"""
Component browser for the demo app: a left sidebar with a search box and
an A-Z list of every LimQt6 widget, paired with a detail panel that shows
the selected widget's description and a usage snippet.
"""

import inspect
from dataclasses import dataclass

from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QButtonGroup,
    QScrollArea,
    QPlainTextEdit,
    QFrame,
)

from PyQt6.QtCore import pyqtSignal

from limqt6.widgets import LimLabel, LimButton, LimLineEdit, LimCheckBox, LimFrame
from limqt6.widgetsplus import LimSwitch, LimThemeSwitcher
from limqt6.layout import LimNavItem, LimSidebar, LimNavbar
from limqt6.dialog import LimDialog

# Usage snippets aren't derivable from the class itself, so they're kept here
# alongside the registry; everything else (name, description) comes straight
# from the class and its docstring.
_USAGE = {
    "LimButton": 'button = LimButton("Click Me")\nbutton.clicked.connect(handler)',
    "LimCheckBox": 'check = LimCheckBox("Accept Terms & Conditions")\ncheck.stateChanged.connect(handler)',
    "LimDialog": 'dialog = LimDialog("Confirm action", parent)\nlayout = QVBoxLayout(dialog.content)\ndialog.add_action(LimButton("OK"))',
    "LimFrame": "card = LimFrame()\nlayout = QVBoxLayout(card)\nlayout.addWidget(LimLabel(\"Card Title\"))",
    "LimLabel": 'label = LimLabel("Hello from LimQt6!")',
    "LimLineEdit": 'field = LimLineEdit()\nfield.setPlaceholderText("Type something here...")',
    "LimNavbar": 'navbar = LimNavbar("Dashboard")\nnavbar.set_menu_callback(sidebar.toggle)\nnavbar.add_action(LimButton("Action"))',
    "LimNavItem": 'item = sidebar.add_item("Dashboard", checked=True)',
    "LimSidebar": 'sidebar = LimSidebar("LimQt6")\nsidebar.add_item("Dashboard", checked=True)\nsidebar.add_item("Settings")',
    "LimSwitch": "switch = LimSwitch()\nswitch.toggled.connect(handler)",
    "LimThemeSwitcher": "switcher = LimThemeSwitcher()\nnavbar.add_action(switcher)",
}

_CLASSES = [
    LimButton,
    LimCheckBox,
    LimDialog,
    LimFrame,
    LimLabel,
    LimLineEdit,
    LimNavbar,
    LimNavItem,
    LimSidebar,
    LimSwitch,
    LimThemeSwitcher,
]


@dataclass(frozen=True)
class ComponentInfo:
    name: str
    description: str
    usage: str


COMPONENTS: list[ComponentInfo] = sorted(
    (
        ComponentInfo(
            name=cls.__name__,
            description=inspect.getdoc(cls) or "No description available.",
            usage=_USAGE.get(cls.__name__, ""),
        )
        for cls in _CLASSES
    ),
    key=lambda c: c.name,
)


############## LIST PANEL ###################


class ComponentListPanel(QWidget):
    """Search box + A-Z list of components. Emits componentSelected(name)."""

    componentSelected = pyqtSignal(str)

    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent)
        self.setObjectName("ComponentListPanel")
        self.setFixedWidth(220)

        root = QVBoxLayout(self)
        root.setContentsMargins(12, 12, 12, 12)
        root.setSpacing(8)

        self.search = LimLineEdit(self)
        self.search.setPlaceholderText("Search components...")
        self.search.textChanged.connect(self._filter)
        root.addWidget(self.search)

        scroll = QScrollArea(self)
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.Shape.NoFrame)

        list_container = QWidget()
        self._list_layout = QVBoxLayout(list_container)
        self._list_layout.setContentsMargins(0, 0, 0, 0)
        self._list_layout.setSpacing(2)
        self._list_layout.addStretch()
        scroll.setWidget(list_container)
        root.addWidget(scroll)

        self._group = QButtonGroup(self)
        self._group.setExclusive(True)
        self._items: dict[str, LimNavItem] = {}

        for component in COMPONENTS:
            item = LimNavItem(component.name)
            item.toggled.connect(
                lambda checked, name=component.name: checked and self.componentSelected.emit(name)
            )
            self._group.addButton(item)
            self._list_layout.insertWidget(self._list_layout.count() - 1, item)
            self._items[component.name] = item

    def _filter(self, query: str) -> None:
        query = query.strip().lower()
        for name, item in self._items.items():
            item.setVisible(query in name.lower())

    def select(self, name: str) -> None:
        item = self._items.get(name)
        if item is not None:
            item.setChecked(True)


############## DETAIL PANEL ###################


class ComponentDetailPanel(LimFrame):
    """Shows the title, description and usage snippet for the selected component."""

    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(8)

        self.title = LimLabel("")
        self.title.setObjectName("ComponentDetailTitle")
        layout.addWidget(self.title)

        self.description = LimLabel("")
        self.description.setObjectName("ComponentDetailDescription")
        self.description.setWordWrap(True)
        layout.addWidget(self.description)

        usage_label = LimLabel("Usage")
        usage_label.setObjectName("ComponentDetailSectionTitle")
        layout.addWidget(usage_label)

        self.usage = QPlainTextEdit(self)
        self.usage.setObjectName("ComponentDetailUsage")
        self.usage.setReadOnly(True)
        self.usage.setFixedHeight(120)
        layout.addWidget(self.usage)

        layout.addStretch()

    def show_component(self, info: ComponentInfo) -> None:
        self.title.setText(info.name)
        self.description.setText(info.description)
        self.usage.setPlainText(info.usage)


############## EXPLORER PAGE ###################


class LimComponentExplorer(QWidget):
    """Combines the list panel and detail panel into a single browsable page."""

    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.list_panel = ComponentListPanel(self)
        layout.addWidget(self.list_panel)

        self.detail_panel = ComponentDetailPanel(self)
        layout.addWidget(self.detail_panel, 1)

        self.list_panel.componentSelected.connect(self._on_select)

        if COMPONENTS:
            self.list_panel.select(COMPONENTS[0].name)

    def _on_select(self, name: str) -> None:
        info = next((c for c in COMPONENTS if c.name == name), None)
        if info is not None:
            self.detail_panel.show_component(info)
