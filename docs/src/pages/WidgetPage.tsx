import { VERSIONS, Version } from "@/data/index"
import { CodeBlock } from "@/components/docs/CodeBlock"

interface WidgetPageProps {
    name: string
    version: Version
}

export function WidgetPage({ name, version }: WidgetPageProps) {
    if (name === 'Home') {
        return (
            <div className="max-w-3xl space-y-6">
                <h1 className="scroll-m-20 text-4xl font-extrabold tracking-tight lg:text-5xl">
                    LimQt6 Documentation {version === 'v2' && '(Beta)'}
                </h1>
                <p className="leading-7 [&:not(:first-child)]:mt-6 text-lg text-muted-foreground">
                    Welcome to the official documentation for LimQt6, a comprehensive library for styled PyQt6 components with modern UI behaviors.
                </p>
                <div className="p-4 border rounded-lg bg-muted/50">
                    <p className="text-sm">
                        You are viewing documentation for <strong>{version}</strong>.
                        Select a widget from the sidebar to view its documentation.
                    </p>
                </div>
            </div>
        )
    }

    const widgetData = VERSIONS[version]
    const widget = widgetData[name]

    if (!widget) {
        return (
            <div className="max-w-3xl space-y-6">
                <h1 className="text-2xl font-bold">Widget Not Found</h1>
                <p className="text-muted-foreground">The requested widget documentation could not be found in version {version}.</p>
            </div>
        )
    }

    return (
        <div className="max-w-3xl space-y-8 animate-in fade-in duration-500">
            <div className="space-y-4">
                <h1 className="scroll-m-20 text-3xl font-extrabold tracking-tight lg:text-4xl">
                    {widget.title}
                </h1>
                <p className="text-lg text-muted-foreground leading-relaxed">
                    {widget.description}
                </p>
            </div>

            <div className="space-y-4">
                <h2 className="scroll-m-20 text-2xl font-semibold tracking-tight">
                    Usage ({version})
                </h2>
                <CodeBlock code={widget.code} />
            </div>

            <div className="my-6 w-full overflow-y-auto">
                <h2 className="scroll-m-20 text-2xl font-semibold tracking-tight mb-4">
                    Features
                </h2>
                <table className="w-full">
                    <thead>
                        <tr className="m-0 border-t p-0 even:bg-muted">
                            <th className="border px-4 py-2 text-left font-bold [&[align=center]]:text-center [&[align=right]]:text-right">
                                Feature
                            </th>
                            <th className="border px-4 py-2 text-left font-bold [&[align=center]]:text-center [&[align=right]]:text-right">
                                Description
                            </th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr className="m-0 border-t p-0 even:bg-muted">
                            <td className="border px-4 py-2 text-left [&[align=center]]:text-center [&[align=right]]:text-right">
                                Themeable
                            </td>
                            <td className="border px-4 py-2 text-left [&[align=center]]:text-center [&[align=right]]:text-right">
                                Adapts to application-wide theme settings.
                            </td>
                        </tr>
                        <tr className="m-0 border-t p-0 even:bg-muted">
                            <td className="border px-4 py-2 text-left [&[align=center]]:text-center [&[align=right]]:text-right">
                                Signals
                            </td>
                            <td className="border px-4 py-2 text-left [&[align=center]]:text-center [&[align=right]]:text-right">
                                Standard Qt signals with enhanced behavior where applicable.
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    )
}
