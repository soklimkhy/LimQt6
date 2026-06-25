"""
Component browser for the demo app: a left sidebar with a search box and
an A-Z list of every LimQt6 widget, paired with a detail panel that shows
the selected widget's description, a preview, and a usage snippet.
"""

import inspect
from dataclasses import dataclass
from typing import Callable



from PyQt6.QtCore import pyqtSignal, Qt

from limqt6.widgets import (
    LimLabel,
    LimButton,
    LimLineEdit,
    LimCheckBox,
    LimFrame,
    LimWidget,
    LimButtonGroup,
    LimScrollArea,
    LimPlainTextEdit,
)
from limqt6.widgetsplus import LimSwitch, LimThemeSwitcher, LimBadge
from limqt6.layout import (
    LimNavItem,
    LimSidebar,
    LimNavbar,
    LimVBoxLayout,
    LimHBoxLayout,
)
from limqt6.dialog import LimDialog

# Usage snippets aren't derivable from the class itself, so they're kept here
# alongside the registry; everything else (name, description) comes straight
# from the class and its docstring.
_USAGE = {
    "LimButton": 'button = LimButton("Click Me")\nbutton.clicked.connect(handler)',
    "LimCheckBox": 'check = LimCheckBox("Accept Terms & Conditions")\ncheck.stateChanged.connect(handler)',
    "LimDialog": 'dialog = LimDialog("Confirm action", parent)\nlayout = LimVBoxLayout(dialog.content)\ndialog.add_action(LimButton("OK"))',
    "LimFrame": 'card = LimFrame()\nlayout = LimVBoxLayout(card)\nlayout.addWidget(LimLabel("Card Title"))',
    "LimLabel": 'label = LimLabel("Hello from LimQt6!")',
    "LimLineEdit": 'field = LimLineEdit()\nfield.setPlaceholderText("Type something here...")',
    "LimNavbar": 'navbar = LimNavbar("Dashboard")\nnavbar.set_menu_callback(sidebar.toggle)\nnavbar.add_action(LimButton("Action"))',
    "LimNavItem": 'item = sidebar.add_item("Dashboard", checked=True)',
    "LimSidebar": 'sidebar = LimSidebar("LimQt6")\nsidebar.add_item("Dashboard", checked=True)\nsidebar.add_item("Settings")',
    "LimSwitch": "switch = LimSwitch()\nswitch.toggled.connect(handler)",
    "LimThemeSwitcher": "switcher = LimThemeSwitcher()\nnavbar.add_action(switcher)",
    "LimButtonGroup": 'group = LimButtonGroup(parent)\ngroup.addButton(btn1)\ngroup.addButton(btn2)',
    "LimBadge": 'badge = LimBadge("Verified", "assets/tick_icon.svg")',
    "LimHBoxLayout": 'layout = LimHBoxLayout()\nlayout.addWidget(btn1)',
    "LimPlainTextEdit": 'editor = LimPlainTextEdit()\neditor.setPlainText("Hello World!")',
    "LimScrollArea": 'scroll = LimScrollArea()\nscroll.setWidget(content_widget)',
    "LimVBoxLayout": 'layout = LimVBoxLayout()\nlayout.addWidget(btn1)',
    "LimWidget": 'widget = LimWidget()\nlayout = LimVBoxLayout(widget)',
}


def _preview_lim_badge():
    return LimBadge("Verified", "assets/tick_icon.svg")

def _preview_lim_button():
    return LimButton("Click Me")


def _preview_lim_checkbox():
    return LimCheckBox("Accept Terms & Conditions")


def _preview_lim_dialog():
    btn = LimButton("Open Demo Dialog")

    def on_click():
        d = LimDialog("Confirm action", btn)
        d.resize(300, 150)
        layout = LimVBoxLayout(d.content)
        layout.addWidget(LimLabel("Are you sure?"))
        ok = LimButton("OK")
        ok.clicked.connect(d.accept)
        d.add_action(ok)
        d.exec()

    btn.clicked.connect(on_click)
    return btn


def _preview_lim_frame():
    f = LimFrame()
    layout = LimVBoxLayout(f)
    layout.addWidget(LimLabel("Card Title"))
    layout.addWidget(LimLabel("This is inside a frame."))
    return f


def _preview_lim_label():
    return LimLabel("Hello from LimQt6!")


def _preview_lim_line_edit():
    le = LimLineEdit()
    le.setPlaceholderText("Type something here...")
    return le


def _preview_lim_navbar():
    n = LimNavbar("Dashboard")
    n.add_action(LimButton("Action"))
    return n


def _preview_lim_nav_item():
    item = LimNavItem("Dashboard")
    item.setChecked(True)
    return item


def _preview_lim_sidebar():
    s = LimSidebar("LimQt6")
    s.add_item("Dashboard", checked=True)
    s.add_item("Settings")
    s.setFixedHeight(200)
    return s


def _preview_lim_switch():
    return LimSwitch()


def _preview_lim_theme_switcher():
    return LimThemeSwitcher()


def _preview_lim_button_group():
    w = LimWidget()
    layout = LimHBoxLayout(w)
    grp = LimButtonGroup(w)
    b1 = LimButton("Option 1")
    b1.setCheckable(True)
    b2 = LimButton("Option 2")
    b2.setCheckable(True)
    grp.addButton(b1)
    grp.addButton(b2)
    layout.addWidget(b1)
    layout.addWidget(b2)
    return w

def _preview_lim_h_box_layout():
    w = LimWidget()
    layout = LimHBoxLayout(w)
    layout.addWidget(LimButton("Left"))
    layout.addWidget(LimButton("Right"))
    return w

def _preview_lim_plain_text_edit():
    te = LimPlainTextEdit()
    te.setPlainText("This is a LimPlainTextEdit.\nIt supports multiple lines.")
    return te

def _preview_lim_scroll_area():
    s = LimScrollArea()
    s.setFixedSize(200, 100)
    w = LimWidget()
    layout = LimVBoxLayout(w)
    for i in range(5):
        layout.addWidget(LimLabel(f"Scroll item {i+1}"))
    s.setWidget(w)
    return s

def _preview_lim_v_box_layout():
    w = LimWidget()
    layout = LimVBoxLayout(w)
    layout.addWidget(LimButton("Top"))
    layout.addWidget(LimButton("Bottom"))
    return w

def _preview_lim_widget():
    w = LimWidget()
    w.setFixedSize(100, 100)
    w.setStyleSheet("background-color: #3b82f6; border-radius: 8px;")
    return w


_PREVIEWS = {
    "LimButton": _preview_lim_button,
    "LimCheckBox": _preview_lim_checkbox,
    "LimDialog": _preview_lim_dialog,
    "LimFrame": _preview_lim_frame,
    "LimLabel": _preview_lim_label,
    "LimLineEdit": _preview_lim_line_edit,
    "LimNavbar": _preview_lim_navbar,
    "LimNavItem": _preview_lim_nav_item,
    "LimSidebar": _preview_lim_sidebar,
    "LimSwitch": _preview_lim_switch,
    "LimThemeSwitcher": _preview_lim_theme_switcher,
    "LimButtonGroup": _preview_lim_button_group,
    "LimBadge": _preview_lim_badge,
    "LimHBoxLayout": _preview_lim_h_box_layout,
    "LimPlainTextEdit": _preview_lim_plain_text_edit,
    "LimScrollArea": _preview_lim_scroll_area,
    "LimVBoxLayout": _preview_lim_v_box_layout,
    "LimWidget": _preview_lim_widget,
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
    LimButtonGroup,
    LimBadge,
    LimHBoxLayout,
    LimPlainTextEdit,
    LimScrollArea,
    LimVBoxLayout,
    LimWidget,
]


@dataclass(frozen=True)
class ComponentInfo:
    name: str
    description: str
    usage: str
    preview_factory: Callable[[], LimWidget] | None = None


COMPONENTS: list[ComponentInfo] = sorted(
    (
        ComponentInfo(
            name=cls.__name__,
            description=inspect.getdoc(cls) or "No description available.",
            usage=_USAGE.get(cls.__name__, ""),
            preview_factory=_PREVIEWS.get(cls.__name__),
        )
        for cls in _CLASSES
    ),
    key=lambda c: c.name,
)


############## LIST PANEL ###################


class ComponentListPanel(LimWidget):
    """Search box + A-Z list of components. Emits componentSelected(name)."""

    componentSelected = pyqtSignal(str)

    def __init__(self, parent: LimWidget | None = None):
        super().__init__(parent)
        self.setObjectName("ComponentListPanel")
        self.setFixedWidth(220)

        root = LimVBoxLayout(self)
        root.setContentsMargins(12, 12, 12, 12)
        root.setSpacing(8)

        self.search = LimLineEdit(self)
        self.search.setPlaceholderText("Search components...")
        self.search.textChanged.connect(self._filter)
        root.addWidget(self.search)

        scroll = LimScrollArea(self)
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(LimScrollArea.Shape.NoFrame)

        list_container = LimWidget()
        self._list_layout = LimVBoxLayout(list_container)
        self._list_layout.setContentsMargins(0, 0, 0, 0)
        self._list_layout.setSpacing(2)
        self._list_layout.addStretch()
        scroll.setWidget(list_container)
        root.addWidget(scroll)

        self._group = LimButtonGroup(self)
        self._group.setExclusive(True)
        self._items: dict[str, LimNavItem] = {}

        for component in COMPONENTS:
            item = LimNavItem(component.name)
            item.toggled.connect(
                lambda checked, name=component.name: (
                    checked and self.componentSelected.emit(name)
                )
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
    """Shows the title, description, preview, and usage snippet for the selected component."""

    def __init__(self, parent: LimWidget | None = None):
        super().__init__(parent)

        layout = LimVBoxLayout(self)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(12)

        self.title = LimLabel("")
        self.title.setObjectName("ComponentDetailTitle")
        layout.addWidget(self.title)

        self.description = LimLabel("")
        self.description.setObjectName("ComponentDetailDescription")
        self.description.setWordWrap(True)
        layout.addWidget(self.description)

        layout.addSpacing(12)

        preview_label = LimLabel("Preview")
        preview_label.setObjectName("ComponentDetailSectionTitle")
        layout.addWidget(preview_label)

        self.preview_frame = LimWidget()
        self.preview_frame.setObjectName("ComponentPreviewFrame")
        self.preview_frame.setStyleSheet(
            "LimWidget#ComponentPreviewFrame { border: 1px solid rgba(150, 150, 150, 0.4); border-radius: 8px; }"
        )
        self.preview_layout = LimVBoxLayout(self.preview_frame)
        self.preview_layout.setContentsMargins(16, 16, 16, 16)
        self.preview_layout.setAlignment(
            Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft
        )
        layout.addWidget(self.preview_frame)

        self.current_preview_widget = None

        layout.addSpacing(12)

        usage_label = LimLabel("Usage")
        usage_label.setObjectName("ComponentDetailSectionTitle")
        layout.addWidget(usage_label)

        self.usage = LimPlainTextEdit(self)
        self.usage.setObjectName("ComponentDetailUsage")
        self.usage.setStyleSheet(
            "LimPlainTextEdit#ComponentDetailUsage { border: 1px solid rgba(150, 150, 150, 0.4); border-radius: 8px; padding: 8px; }"
        )
        self.usage.setReadOnly(True)
        self.usage.setFixedHeight(120)
        layout.addWidget(self.usage)

        layout.addStretch()

    def show_component(self, info: ComponentInfo) -> None:
        self.title.setText(info.name)
        self.description.setText(info.description)
        self.usage.setPlainText(info.usage)

        # Clear old preview
        if self.current_preview_widget:
            self.preview_layout.removeWidget(self.current_preview_widget)
            self.current_preview_widget.deleteLater()
            self.current_preview_widget = None

        # Add new preview
        if info.preview_factory:
            self.current_preview_widget = info.preview_factory()
            self.preview_layout.addWidget(self.current_preview_widget)


############## EXPLORER PAGE ###################


class LimComponentExplorer(LimWidget):
    """Combines the list panel and detail panel into a single browsable page."""

    def __init__(self, parent: LimWidget | None = None):
        super().__init__(parent)

        layout = LimHBoxLayout(self)
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

    def toggle_sidebar(self) -> None:
        self.list_panel.setVisible(not self.list_panel.isVisible())

