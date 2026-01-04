import { ReactNode, useState } from 'react'
import { Menu } from 'lucide-react'
import { Button } from '@/components/ui/button'

interface DocsLayoutProps {
    children: ReactNode
    sidebar: ReactNode
}

export function DocsLayout({ children, sidebar }: DocsLayoutProps) {
    const [isSidebarOpen, setIsSidebarOpen] = useState(false)

    return (
        <div className="flex min-h-screen flex-col">
            {/* Mobile Header */}
            <header className="sticky top-0 z-30 flex items-center border-b bg-background px-4 h-14 md:hidden">
                <Button variant="ghost" size="icon" onClick={() => setIsSidebarOpen(!isSidebarOpen)}>
                    <Menu className="h-5 w-5" />
                </Button>
                <div className="ml-4 font-bold">LimQt6</div>
            </header>

            <div className="flex-1 md:flex">
                {/* Sidebar */}
                <aside className={`
                    fixed inset-y-0 left-0 z-40 w-[260px] border-r bg-background transition-transform duration-200 ease-in-out
                    ${isSidebarOpen ? "translate-x-0" : "-translate-x-full"}
                    md:translate-x-0 md:block md:sticky md:top-0 md:h-screen
                `}>
                    {sidebar}
                </aside>

                {/* Backdrop for mobile */}
                {isSidebarOpen && (
                    <div className="fixed inset-0 z-30 bg-black/80 md:hidden animate-in fade-in" onClick={() => setIsSidebarOpen(false)} />
                )}

                {/* Main Content */}
                <main className="flex-1 md:pl-0">
                    <div className="container py-8 max-w-5xl mx-auto px-4 md:px-8">
                        {children}
                    </div>
                </main>
            </div>
        </div>
    )
}
