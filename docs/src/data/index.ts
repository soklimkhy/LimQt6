import { WIDGET_DATA as V1 } from "./v1/widgets"
import { WIDGET_DATA as V2 } from "./v2/widgets"
import { WidgetRegistry } from "./types"

export const VERSIONS: Record<string, WidgetRegistry> = {
    "v1": V1,
    "v2": V2
}

export type Version = keyof typeof VERSIONS
