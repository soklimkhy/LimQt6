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



---

## 📜 **LICENSE (MIT Recommended)**

Create a file named `LICENSE` and paste:

```text
MIT License

Copyright (c) 2025 LimQt6

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
