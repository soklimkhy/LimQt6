import { WidgetRegistry } from "@/data/types"

export const WIDGET_DATA: WidgetRegistry = {
    "LimButton": {
        title: "LimButton",
        description: "A customizable button component with support for various styles and states. Built on top of QPushButton, it offers a modern look with smooth hover effects and theme integration.",
        code: `from limqt6.widgets import LimButton

# Primary button
btn = LimButton("Click Me")
btn.setObjectName("primary_btn")
btn.clicked.connect(lambda: print("Button clicked!"))`
    },
    "LimLabel": {
        title: "LimLabel",
        description: "An enhanced label component providing consistent typography across your application. Supports various text styles like headings, muted text, and descriptions.",
        code: `from limqt6.widgets import LimLabel

# Heading
title = LimLabel("Dashboard Overview")
title.setProperty("class", "h1")`
    },
    "LimCard": {
        title: "LimCard",
        description: "A framed container designed to group related content. It includes a border, background color, and rounded corners to cleanly separate UI sections.",
        code: `from limqt6.widgets import LimCard
from PyQt6.QtWidgets import QVBoxLayout

# Create a card container
card = LimCard()
layout = QVBoxLayout(card)`
    },
    "LimSwitch": {
        title: "LimSwitch",
        description: "A toggle control that allows the user to switch between two states: checked and unchecked. commonly used for activation or configuration settings.",
        code: `from limqt6.widgets import LimSwitch

toggle = LimSwitch()
toggle.toggled.connect(lambda c: print("State:", c))`
    },
    "LimInput": {
        title: "LimInput",
        description: "A styled processed meant for single-line text input. It features clear focus states and placeholder text support.",
        code: `from limqt6.widgets import LimInput

text_input = LimInput()
text_input.setPlaceholderText("Enter your username...")`
    },
    "LimCheckbox": {
        title: "LimCheckbox",
        description: "A standard checkbox component for binary options, styled to match the rest of the application theme.",
        code: `from limqt6.widgets import LimCheckbox

check = LimCheckbox("Agree to Terms")
check.stateChanged.connect(handle_state_change)`
    },
    "LimRadio": {
        title: "LimRadio",
        description: "A radio button component usually used in groups where only one option can be selected at a time.",
        code: `from limqt6.widgets import LimRadio

option1 = LimRadio("Option A")
option2 = LimRadio("Option B")`
    },
    "LimProgress": {
        title: "LimProgress",
        description: "A visual indicator of an operation's progress, useful for loading states or tracking completion percentages.",
        code: `from limqt6.widgets import LimProgress

prop_bar = LimProgress()
prop_bar.setValue(45)  # Set to 45%`
    }
}
