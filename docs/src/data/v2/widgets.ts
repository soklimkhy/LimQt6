import { WidgetRegistry } from "@/data/types"

export const WIDGET_DATA: WidgetRegistry = {
    "LimButton": {
        title: "LimButton v2",
        description: "The next generation button component. Features improved accessibility, new variants, and faster rendering.",
        code: `from limqt6.v2.widgets import LimButton

# v2 Button with icons
btn = LimButton("Next Gen", icon="arrow-right")
btn.variant = "gradient"`
    },
    "LimLabel": {
        title: "LimLabel v2",
        description: "Updated typography engine with dynamic scaling and new font weights.",
        code: `from limqt6.v2.widgets import LimLabel

title = LimLabel("Dynamic Title")
title.scale = 1.5`
    },
    "LimCard": {
        title: "LimCard v2",
        description: "Now supports glassmorphism and nested layouts out of the box.",
        code: `from limqt6.v2.widgets import LimCard

card = LimCard(glass=True)`
    }
}
