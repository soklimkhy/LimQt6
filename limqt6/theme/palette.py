from dataclasses import dataclass


@dataclass
class ThemePalette:
    name: str
    primary: str
    primary_hover: str
    primary_pressed: str
    background: str
    surface: str
    text: str
    text_secondary: str
    border: str


# Define default palettes
DARK_THEME = ThemePalette(
    name="dark",
    primary="#3b82f6",  # Blue 500
    primary_hover="#2563eb",  # Blue 600
    primary_pressed="#1d4ed8",  # Blue 700
    background="#18181b",  # Zinc 900
    surface="#27272a",  # Zinc 800
    text="#f4f4f5",  # Zinc 100
    text_secondary="#a1a1aa",  # Zinc 400
    border="#3f3f46",  # Zinc 700
)

LIGHT_THEME = ThemePalette(
    name="light",
    primary="#2563eb",  # Blue 600
    primary_hover="#1d4ed8",  # Blue 700
    primary_pressed="#1e40af",  # Blue 800
    background="#ffffff",  # White
    surface="#f4f4f5",  # Zinc 100
    text="#18181b",  # Zinc 900
    text_secondary="#71717a",  # Zinc 500
    border="#e4e4e7",  # Zinc 200
)
