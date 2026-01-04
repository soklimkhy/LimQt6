from PyQt6.QtWidgets import QPushButton, QLabel


class LimButton(QPushButton):
    def __init__(self, text="", parent=None):
        super().__init__(text, parent)
        self.setup_style()

    def setup_style(self):
        # Basic modern styling for the button
        self.setStyleSheet("""
            LimButton {
                background-color: #007bff;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 8px 16px;
                font-weight: bold;
            }
            LimButton:hover {
                background-color: #0056b3;
            }
            LimButton:pressed {
                background-color: #004085;
            }
        """)


class LimLabel(QLabel):
    def __init__(self, text="", parent=None):
        super().__init__(text, parent)
        self.setup_style()

    def setup_style(self):
        # Basic styling for the label
        self.setStyleSheet("""
            LimLabel {
                color: #333333;
                font-size: 16px;
            }
        """)
