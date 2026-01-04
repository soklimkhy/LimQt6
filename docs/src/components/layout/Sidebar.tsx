import { useState } from 'react'
import { Input } from "@/components/ui/input"
import { ScrollArea } from "@/components/ui/scroll-area"
import { Search } from "lucide-react"
import { ThemeToggle } from "@/components/theme/ThemeToggle"
import {
    Select,
    SelectContent,
    SelectItem,
    SelectTrigger,
    SelectValue,
} from "@/components/ui/select"
import { Version, VERSIONS } from "@/data/index"

interface SidebarProps {
    onSelect: (widgetName: string) => void
    selected: string | null
    version: Version
    onVersionChange: (v: Version) => void
}

export function Sidebar({ onSelect, selected, version, onVersionChange }: SidebarProps) {
    const [query, setQuery] = useState("")

    const widgetData = VERSIONS[version]
    const widgetKeys = Object.keys(widgetData).sort()
    const filteredWidgets = widgetKeys.filter((w) =>
        w.toLowerCase().includes(query.toLowerCase())
    )

    return (
        <div className="flex bg-background h-full w-full flex-col border-r">
            <div className="p-6 border-b space-y-4">
                <div className="flex items-center justify-between">
                    <button
                        className="text-2xl font-bold tracking-tight hover:opacity-80 transition-opacity"
                        onClick={() => onSelect('Home')}
                    >
                        LimQt6
                    </button>
                    <ThemeToggle />
                </div>

                <Select value={version} onValueChange={(v) => onVersionChange(v as Version)}>
                    <SelectTrigger className="w-full">
                        <SelectValue placeholder="Select version" />
                    </SelectTrigger>
                    <SelectContent>
                        <SelectItem value="v1">Version 1.0 (Stable)</SelectItem>
                        <SelectItem value="v2">Version 2.0 (Beta)</SelectItem>
                    </SelectContent>
                </Select>

                <div className="relative">
                    <Search className="absolute left-2 top-2.5 h-4 w-4 text-muted-foreground" />
                    <Input
                        placeholder="Search widgets..."
                        className="pl-8"
                        value={query}
                        onChange={(e) => setQuery(e.target.value)}
                    />
                </div>
            </div>
            <ScrollArea className="flex-1">
                <div className="p-4 space-y-1">
                    {filteredWidgets.length === 0 && (
                        <div className="text-sm text-muted-foreground px-4 py-2">
                            No results found.
                        </div>
                    )}
                    {filteredWidgets.map((widget) => (
                        <button
                            key={widget}
                            onClick={() => onSelect(widget)}
                            className={`w-full text-left px-4 py-2 text-sm font-medium rounded-md transition-colors ${selected === widget
                                ? "bg-primary text-primary-foreground"
                                : "hover:bg-accent hover:text-accent-foreground text-muted-foreground"
                                }`}
                        >
                            {widget}
                        </button>
                    ))}
                </div>
            </ScrollArea>
        </div>
    )
}
