import { useState } from "react"
import { Check, Copy } from "lucide-react"
import { Button } from "@/components/ui/button"
import { cn } from "@/lib/utils"

interface CodeBlockProps {
    code: string
    className?: string
}

export function CodeBlock({ code, className }: CodeBlockProps) {
    const [hasCopied, setHasCopied] = useState(false)

    const copyToClipboard = async () => {
        await navigator.clipboard.writeText(code)
        setHasCopied(true)
        setTimeout(() => {
            setHasCopied(false)
        }, 2000)
    }

    return (
        <div className={cn("relative group rounded-md border bg-muted font-mono text-sm", className)}>
            <div className="absolute right-4 top-4 opacity-0 transition-opacity group-hover:opacity-100">
                <Button
                    variant="ghost"
                    size="icon"
                    className="h-8 w-8 text-muted-foreground hover:bg-background/50 hover:text-foreground"
                    onClick={copyToClipboard}
                >
                    {hasCopied ? (
                        <Check className="h-4 w-4" />
                    ) : (
                        <Copy className="h-4 w-4" />
                    )}
                    <span className="sr-only">Copy code</span>
                </Button>
            </div>
            <div className="overflow-x-auto p-4">
                <pre>
                    <code className="text-foreground">{code}</code>
                </pre>
            </div>
        </div>
    )
}
