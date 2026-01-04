from PyQt6.QtGui import QFontDatabase, QFont
import os


class FontManager:
    @staticmethod
    def load_font(font_path: str) -> str:
        """
        Loads a font from a file path and returns its family name.
        """
        if not os.path.exists(font_path):
            print(f"Warning: Font file not found at {font_path}")
            return "Segoe UI"

        font_id = QFontDatabase.addApplicationFont(font_path)
        if font_id == -1:
            print(f"Warning: Failed to load font {font_path}")
            return "Segoe UI"

        families = QFontDatabase.applicationFontFamilies(font_id)
        if families:
            return families[0]
        return "Segoe UI"

    @staticmethod
    def load_project_fonts():
        """
        Scans the project 'fonts' directory relative to this package and loads them.
        Returns the primary font family name if Geist is found.
        """
        # Assuming fonts are in the root 'fonts' folder relative to the package installation
        # Or better yet, we might bundle them inside 'limqt6/assets/fonts'
        # But user said "LimQt6\fonts\Geist-Regular.ttf" which implies root.

        # Let's try to find the root dir relative to this file
        # current: limqt6/core/fonts.py -> root is ../..
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        font_path = os.path.join(base_dir, "fonts", "Geist-Regular.ttf")

        return FontManager.load_font(font_path)
