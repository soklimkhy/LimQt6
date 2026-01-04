from PyQt6.QtWidgets import QApplication
import sys


class LimApp(QApplication):
    def __init__(self, argv=None):
        if argv is None:
            argv = sys.argv
        super().__init__(argv)
        self.apply_theme()

    def apply_theme(self):
        # Placeholder for theme application
        # Setting a basic fusion style for better cross-platform look + custom palette if needed
        self.setStyle("Fusion")

        # We can add a global stylesheet here later
        self.setStyleSheet("""
            QWidget {
                font-family: 'Segoe UI', sans-serif;
                font-size: 14px;
            }
        """)
