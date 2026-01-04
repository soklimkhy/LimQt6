# LimQt6

**LimQt6** is a modern, themed UI library for **PyQt6**, heavily inspired by the **shadcn/ui** and **Vercel** design aesthetic. It provides a set of pre-styled widgets and a robust theming system to instantly give your desktop applications a professional, clean look.

## Features

- 🎨 **Shadcn/UI Aesthetic**: Built-in Light and Dark modes using the Zinc color palette.
- 🧩 **Enhanced Widgets**: Drop-in replacements for standard Qt widgets with modern styling.
- 🔠 **Typography**: Integrated **Geist Sans** font support.
- 🌗 **Instant Theming**: Switch between themes dynamically at runtime.

## Installation

```bash
pip install limqt6
```

*(Note: If installed from source)*
```bash
git clone https://github.com/soklimkhy/LimQt6.git
cd LimQt6
pip install -e .
```

## Usage

### 1. Basic Setup
Initialize your application with `LimApp` to automatically load fonts and apply the default theme.

```python
from limqt6.core.app import LimApp
from PyQt6.QtWidgets import QWidget, QVBoxLayout

app = LimApp() 
window = QWidget()
# ... build your UI ...
app.exec()
```

### 2. Core Widgets (`limqt6.widgets`)
Standard widgets that have been enhanced with the LimQt6 design system.

```python
from limqt6.widgets import (
    LimButton, 
    LimLabel, 
    LimLineEdit, 
    LimFrame, 
    LimCheckBox
)

# Button
btn = LimButton("Click Me")

# Input Field
inp = LimLineEdit()
inp.setPlaceholderText("Enter text...")

# Checkbox
chk = LimCheckBox("Agree to Terms")

# Frame (Card)
card = LimFrame()
```

### 3. Advanced Widgets (`limqt6.widgetsplus`)
Complex, custom-built components that go beyond standard Qt wrappers.

```python
from limqt6.widgetsplus import LimSwitch

# Toggle Switch
toggle = LimSwitch()
toggle.toggled.connect(lambda checked: print(f"State: {checked}"))
```

### 4. Theming
Toggle between **Light** and **Dark** modes easily.

```python
from limqt6.theme.manager import theme_manager

# Switch to Dark Mode
theme_manager.set_theme("dark")

# Switch to Light Mode
theme_manager.set_theme("light")
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
