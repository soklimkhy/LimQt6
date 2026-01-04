from PyQt6.QtGui import QIcon, QPixmap, QPainter, QColor
from PyQt6.QtCore import Qt
from limqt6.theme.manager import theme_manager


class LimIcon(QIcon):
    def __init__(self, icon_path: str):
        super().__init__()
        self.icon_path = icon_path
        self._generate_pixmap()

        # We might want to listen to theme changes in a real app,
        # but for now, we'll rely on widgets re-requesting icons or manual refresh.
        # A more advanced system would use a global signal.

    def _generate_pixmap(self):
        """
        Loads the image and recolors it to match the current theme's text color.
        """
        # Load the base pixmap (assuming transparent PNG or SVG rendered to pixmap)
        pixmap = QPixmap(self.icon_path)

        if pixmap.isNull():
            return

        # Create a new pixmap to draw on
        colored_pixmap = QPixmap(pixmap.size())
        colored_pixmap.fill(Qt.GlobalColor.transparent)

        painter = QPainter(colored_pixmap)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Get the target color from the theme manager
        color_hex = theme_manager.current_theme.text
        color = QColor(color_hex)

        # Draw the original pixmap
        painter.drawPixmap(0, 0, pixmap)

        # Use CompositionMode to tint the non-transparent pixels
        painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_SourceIn)
        painter.fillRect(colored_pixmap.rect(), color)

        painter.end()

        # Add the generated pixmap to this QIcon
        # We add it for different states if needed, but for now just Normal
        self.addPixmap(colored_pixmap)

    def update_color(self):
        """Force regeneration of the icon color (useful after theme switch)"""
        # Clear existing pixmaps (QIcon doesn't have a clear(), so we might need to create a new instance
        # or just add the new one on top. QIcon behaves a bit purely, often easier to recreate the object.)
        # However, for this implementation, let's just re-add the new pixmap.
        # A cleaner usage pattern is: btn.setIcon(LimIcon("path")) every time theme changes.
        self._generate_pixmap()
