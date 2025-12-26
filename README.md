## LimQt6
LimQt6 is a simple UI component library built on top of PyQt6.
It inherits native Qt widgets and applies improved styling, theme handling, and modern UI behavior.
X LimQt6 requires PyQt6.
It will not work without PyQt6 installed.

## LimQt6 Provides 
🎨 Styled widgets with theme support

🧱 Components that extend PyQt6 (not replace it)

🌗 Light/Dark theme compatible

👇 Easy to drop into existing PyQt6 projects

## Purpose 
I just love PyQt6 

# Basic Usage
from PyQt6.QtWidgets import QApplication
from limqt6.widgets import LimButton, LimLabel
from limqt6.core.app import LimApp

app = LimApp()  # wrapper for QApplication + theme support

label = LimLabel("Hello from LimQt6")
button = LimButton("Click Me")

label.show()
button.show()

app.exec()
