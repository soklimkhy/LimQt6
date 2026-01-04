from PyQt6.QtWidgets import QApplication
from .palette import DARK_THEME, LIGHT_THEME


class ThemeManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ThemeManager, cls).__new__(cls)
            cls._instance.current_theme = DARK_THEME
        return cls._instance

    def set_theme(self, theme_name: str):
        if theme_name.lower() == "light":
            self.current_theme = LIGHT_THEME
        else:
            self.current_theme = DARK_THEME

        self.apply()

    def apply(self):
        """Generates and applies the global stylesheet."""
        app = QApplication.instance()
        if app:
            stylesheet = self.generate_stylesheet()
            app.setStyleSheet(stylesheet)

    def generate_stylesheet(self) -> str:
        t = self.current_theme

        # We define the styles using f-strings to inject theme colors
        style = f"""
            QWidget {{
                background-color: {t.background};
                color: {t.text};
                font-family: 'Segoe UI', sans-serif;
                font-size: 14px;
            }}

            LimLabel {{
                color: {t.text};
                font-size: 16px; 
                background-color: transparent;
            }}

            LimButton {{
                background-color: {t.primary};
                color: #ffffff;
                border: none;
                border-radius: 6px;
                padding: 8px 16px;
                font-weight: bold;
            }}
            LimButton:hover {{
                background-color: {t.primary_hover};
            }}
            LimButton:pressed {{
                background-color: {t.primary_pressed};
            }}
            LimButton:disabled {{
                background-color: {t.surface};
                color: {t.text_secondary};
            }}

            LimCard {{
                background-color: {t.surface};
                border-radius: 12px;
                border: 1px solid {t.border};
            }}

            LimInput {{
                background-color: {t.surface};
                border: 1px solid {t.border};
                border-radius: 8px;
                color: {t.text};
                padding: 5px;
            }}
            LimInput:focus {{
                border: 2px solid {t.primary};
            }}
        """
        return style


# Global instance for easy access
theme_manager = ThemeManager()
