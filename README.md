# LimQt6

[![PyQt6 Required](https://img.shields.io/badge/Requires-PyQt6-blue.svg)]()
[![Status-Development](https://img.shields.io/badge/status-early_dev-orange)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)]()
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)]()

**LimQt6** is a simple UI component library built on top of **PyQt6**.  
It inherits native Qt widgets and applies improved styling, theme handling, and modern UI behavior.

> ⚠️ **LimQt6 requires PyQt6**.  
> It will not run if PyQt6 is not installed.

---

## ✨ What LimQt6 Provides
- 🎨 Styled widgets with theme support  
- 🧱 Components that extend PyQt6 (not replace it)  
- 🌗 Light/Dark theme ready  
- 🚀 Easy to drop into existing PyQt6 projects  

---

## 💡 Purpose
I just love PyQt6.  
LimQt6 exists to make it easier and prettier to build with it.

---

## 📦 Basic Usage

```python
from PyQt6.QtWidgets import QApplication
from limqt6.widgets import LimButton, LimLabel
from limqt6.core.app import LimApp

app = LimApp()  # Wrapper for QApplication + theme support

label = LimLabel("Hello from LimQt6")
button = LimButton("Click Me")

label.show()
button.show()

app.exec()
