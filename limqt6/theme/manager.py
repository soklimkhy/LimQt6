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

        # Shadcn/UI Inspired Stylesheet
        style = f"""
            QWidget {{
                background-color: {t.background};
                color: {t.text};
                font-family: 'Geist', 'Geist Sans', 'Inter', 'Segoe UI', sans-serif;
                font-size: 14px;
            }}

            LimLabel {{
                color: {t.text};
                font-size: 14px; 
                font-weight: 500;
                background-color: transparent;
            }}

            /* Primary Button (Shadcn default) */
            LimButton {{
                background-color: {t.primary};
                color: {t.primary_foreground};
                border: 1px solid transparent;
                border-radius: 6px;
                padding: 8px 16px;
                font-weight: 500;
                font-size: 14px;
            }}
            LimButton:hover {{
                background-color: {t.primary_hover};
            }}
            LimButton:pressed {{
                background-color: {t.primary_pressed};
            }}
            LimButton:disabled {{
                background-color: {t.text_secondary}; /* simplified disabled */
                opacity: 0.5;
            }}

            /* Card: Bordered, rounded, background matches surface */
            LimCard {{
                background-color: {t.surface};
                border-radius: 8px;
                border: 1px solid {t.border};
            }}

            /* Input: cleaner, focus ring */
            LimInput {{
                background-color: transparent; /* shadcn inputs are often transparent on bg */
                border: 1px solid {t.input_border};
                border-radius: 6px;
                color: {t.text};
                padding: 6px 12px;
                selection-background-color: {t.text_secondary};
            }}
            LimInput:focus {{
                border: 1px solid {t.ring};
                /* In web we use outline-ring, here we simulate with border color */
            }}
        """
        return style


# Global instance for easy access
theme_manager = ThemeManager()
