from PyQt6.QtWidgets import QApplication
import sys


class LimApp(QApplication):
    def __init__(self, argv=None):
        if argv is None:
            argv = sys.argv
        super().__init__(argv)
        self.apply_theme()

    def apply_theme(self):
        # Apply the default theme (Dark) via the manager
        from limqt6.theme.manager import theme_manager

        theme_manager.apply()
