from dataclasses import dataclass


@dataclass
class ThemePalette:
    name: str
    primary: str
    primary_foreground: str  # Text color on top of primary
    primary_hover: str
    primary_pressed: str
    background: str
    surface: str
    text: str
    text_secondary: str
    border: str
    input_border: str
    ring: str
    checkbox_background: str


# Shadcn/UI "Zinc" Theme

DARK_THEME = ThemePalette(
    name="dark",
    primary="#fafafa",  # Zinc 50 (White-ish)
    primary_foreground="#18181b",  # Zinc 900 (Black text on white btn)
    primary_hover="#e4e4e7",  # Zinc 200
    primary_pressed="#d4d4d8",  # Zinc 300
    background="#09090b",  # Zinc 950 (Deep Black)
    surface="#09090b",  # Zinc 950 (Cards blend in, defined by border)
    text="#fafafa",  # Zinc 50
    text_secondary="#a1a1aa",  # Zinc 400 (Muted)
    border="#27272a",  # Zinc 800
    input_border="#27272a",  # Zinc 800
    ring="#d4d4d8",  # Zinc 300 (Focus ring)
    checkbox_background="#fafafa",  # 18181b
)

LIGHT_THEME = ThemePalette(
    name="light",
    primary="#171717",  # Zinc 900 (Black)
    primary_foreground="#fafafa",  # Zinc 50 (White text on black btn)
    primary_hover="#27272a",  # Zinc 800
    primary_pressed="#3f3f46",  # Zinc 700
    background="#ffffff",  # White
    surface="#ffffff",  # White
    text="#09090b",  # Zinc 950
    text_secondary="#71717a",  # Zinc 500 (Muted)
    border="#e4e4e7",  # Zinc 200
    input_border="#919191",  # Zinc 200
    ring="#171717",  # Zinc 900
    checkbox_background="transparent",  # transparent
)
