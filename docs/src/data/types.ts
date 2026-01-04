export interface WidgetData {
    title: string
    description: string
    code: string
}

export type WidgetRegistry = Record<string, WidgetData>
