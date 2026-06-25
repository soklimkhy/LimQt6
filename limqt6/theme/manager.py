from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QPixmap, QPainter, QColor, QPen, QPainterPath
from PyQt6.QtCore import Qt
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

        # Locate assets
        import os

        # Assuming we are in limqt6/theme/manager.py
        # Root is ../../
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        # Adjust for installed package structure if needed, but for dev this works
        tick_icon_path = os.path.join(base_dir, "assets", "tick_icon.svg").replace(
            "\\", "/"
        )
        # Draw chevron using QPainter dynamically
        pixmap = QPixmap(24, 24)
        pixmap.fill(Qt.GlobalColor.transparent)
        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        pen = QPen(QColor(t.text_secondary))
        pen.setWidth(2)
        pen.setCapStyle(Qt.PenCapStyle.RoundCap)
        pen.setJoinStyle(Qt.PenJoinStyle.RoundJoin)
        painter.setPen(pen)
        
        path = QPainterPath()
        path.moveTo(6, 9)
        path.lineTo(12, 15)
        path.lineTo(18, 9)
        painter.drawPath(path)
        painter.end()
        
        chevron_png_path = os.path.join(base_dir, "assets", "chevron_down.png").replace("\\", "/")
        try:
            pixmap.save(chevron_png_path, "PNG")
        except Exception:
            pass

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
                padding: 5px 11px;
                font-weight: bold;
                font-size: 15px;
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
            LimFrame {{
                background-color: {t.surface};
                border-radius: 8px;
                border: 1px solid {t.border};
            }}

            /* Input: cleaner, focus ring */
            LimLineEdit {{
                background-color: transparent; /* shadcn inputs are often transparent on bg */
                border: 1px solid {t.input_border};
                border-radius: 3px;
                color: {t.text};
                font-size: 14px;
                padding: 4px 8px;
                selection-background-color: {t.text_secondary};
            }}
            LimLineEdit:focus {{
                border: 1px solid {t.ring};
                /* In web we use outline-ring, here we simulate with border color */
            }}

            /* CheckBox: Shadcn style (Rounded square) */
            LimCheckBox {{
                spacing: 8px;
                color: {t.text};
            }}
            LimCheckBox::indicator {{
                width: 16px;
                height: 16px;
                border: 1px solid {t.input_border};
                border-radius: 4px;
                background-color: transparent;
            }}
            LimCheckBox::indicator:unchecked:hover {{
                border: 1px solid {t.text_secondary}; /* Slightly darker on hover */
            }}
            LimCheckBox::indicator:checked {{
                background-color: {t.checkbox_background};
                border: 1px solid {t.primary};
                image: url({tick_icon_path});

            }}

            /* ComboBox */
            LimComboBox {{
                background-color: {t.background};
                color: {t.text};
                border: 1px solid {t.border};
                border-radius: 6px;
                padding: 6px 12px;
                min-height: 18px;
                font-size: 14px;
            }}
            LimComboBox:hover {{
                border: 1px solid {t.text_secondary};
            }}
            LimComboBox:focus {{
                border: 1px solid {t.primary};
            }}
            LimComboBox::drop-down {{
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 32px;
                border: none;
                background: transparent;
            }}
            LimComboBox::down-arrow {{
                image: url({chevron_png_path});
                width: 14px;
                height: 14px;
            }}
            LimComboBox QAbstractItemView, 
            LimComboBox QListView {{
                background-color: {t.surface};
                border: 1px solid {t.border};
                border-radius: 6px;
                selection-background-color: transparent;
                selection-color: {t.text};
                padding: 4px;
                outline: none;
            }}
            LimComboBox QAbstractItemView::item, 
            LimComboBox QListView::item {{
                min-height: 28px;
                padding-left: 8px;
                border-radius: 4px;
                margin: 2px 0px;
            }}
            LimComboBox QAbstractItemView::item:hover,
            LimComboBox QAbstractItemView::item:selected,
            LimComboBox QListView::item:hover,
            LimComboBox QListView::item:selected {{
                background-color: {t.accent};
                color: {t.accent_foreground};
            }}

            /* Sidebar: vertical nav panel */
            LimSidebar {{
                background-color: {t.surface};
                border-right: 1px solid {t.border};
            }}

            /* Navbar: horizontal top bar */
            LimNavbar {{
                background-color: {t.surface};
                border-bottom: 1px solid {t.border};
            }}

            QLabel#LimBrandLabel {{
                font-size: 16px;
                font-weight: 700;
                background-color: transparent;
            }}

            QPushButton#LimNavbarMenuButton {{
                background-color: transparent;
                border: none;
                border-radius: 6px;
                padding: 0px;
            }}
            QPushButton#LimNavbarMenuButton:hover {{
                background-color: {t.accent};
                color: {t.accent_foreground};
            }}

            QPushButton#LimThemeSwitcher {{
                background-color: transparent;
                border: none;
                border-radius: 6px;
                padding: 0px;
            }}
            QPushButton#LimThemeSwitcher:hover {{
                background-color: {t.accent};
            }}

            /* Dialog: frameless modal card with header/content/footer */
            QFrame#LimDialogCard {{
                background-color: {t.surface};
                border-radius: 12px;
                border: 1px solid {t.border};
            }}
            QWidget#LimDialogHeader {{
                background-color: transparent;
                border-bottom: 1px solid {t.border};
            }}
            QLabel#LimDialogTitle {{
                font-size: 16px;
                font-weight: 600;
                background-color: transparent;
            }}
            QPushButton#LimDialogCloseButton {{
                background-color: transparent;
                color: {t.text_secondary};
                border: none;
                border-radius: 6px;
                padding: 0px;
            }}
            QPushButton#LimDialogCloseButton:hover {{
                background-color: {t.accent};
                color: {t.accent_foreground};
            }}
            QWidget#LimDialogContent {{
                background-color: transparent;
                padding: 16px;
            }}
            QWidget#LimDialogFooter {{
                background-color: transparent;
                border-top: 1px solid {t.border};
            }}

            /* Component explorer: list panel + detail panel */
            QWidget#ComponentListPanel {{
                border-right: 1px solid {t.border};
            }}
            QLabel#ComponentDetailTitle {{
                font-size: 22px;
                font-weight: 700;
                background-color: transparent;
            }}
            QLabel#ComponentDetailDescription {{
                font-size: 14px;
                color: {t.text_secondary};
                background-color: transparent;
            }}
            QLabel#ComponentDetailSectionTitle {{
                font-size: 13px;
                font-weight: 600;
                color: {t.text_secondary};
                background-color: transparent;
                margin-top: 8px;
            }}
            QPlainTextEdit#ComponentDetailUsage {{
                background-color: {t.background};
                border: 1px solid {t.border};
                border-radius: 6px;
                padding: 10px;
                font-family: 'Consolas', 'Courier New', monospace;
                font-size: 13px;
            }}

            /* Nav item: entries inside LimSidebar/LimNavbar */
            LimNavItem {{
                background-color: transparent;
                color: {t.text_secondary};
                border: none;
                border-radius: 6px;
                padding: 8px 12px;
                text-align: left;
                font-size: 14px;
                font-weight: 500;
            }}
            LimNavItem:hover {{
                background-color: {t.accent};
                color: {t.text};
            }}
            LimNavItem:checked {{
                background-color: {t.accent};
                color: {t.accent_foreground};
                font-weight: 600;
            }}

            /* Badge: small inline label */
            LimWidget#LimBadge {{
                background-color: {t.accent};
                border-radius: 12px;
            }}
            LimLabel#LimBadgeText {{
                color: {t.accent_foreground};
                font-size: 12px;
                font-weight: 600;
                background-color: transparent;
            }}

            /* Carousel */
            LimWidget#LimCarousel {{
                background-color: transparent;
                border-radius: 8px;
            }}
            LimWidget#LimCarouselContainer {{
                background-color: transparent;
            }}
        """
        return style


# Global instance for easy access
theme_manager = ThemeManager()
