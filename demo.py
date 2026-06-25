
from limqt6.widgets import LimWidget
from limqt6.layout import LimVBoxLayout
from limqt6.widgetsplus import LimThemeSwitcher
from limqt6.layout import LimNavbar
from limqt6.core.app import LimApp
from explorer import LimComponentExplorer

def main():
    app = LimApp()

    window = LimWidget()
    window.setWindowTitle("LimQt6")
    window.resize(840, 520)

    root_layout = LimVBoxLayout(window)
    root_layout.setContentsMargins(0, 0, 0, 0)
    root_layout.setSpacing(0)

    # Navbar on top
    navbar = LimNavbar("Component Explorer")
    theme_switcher = LimThemeSwitcher()
    navbar.add_action(theme_switcher)
    root_layout.addWidget(navbar)

    # Component explorer
    explorer = LimComponentExplorer()
    root_layout.addWidget(explorer)

    window.show()

    app.exec()

if __name__ == "__main__":
    main()
