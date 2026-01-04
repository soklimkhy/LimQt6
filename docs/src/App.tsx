import { useState } from 'react'
import { DocsLayout } from "@/components/layout/DocsLayout"
import { Sidebar } from "@/components/layout/Sidebar"
import { WidgetPage } from "@/pages/WidgetPage"
import { useVersion } from "@/hooks/useVersion"

function App() {
    const [view, setView] = useState("Home")
    const { version, setVersion } = useVersion()

    return (
        <DocsLayout
            sidebar={
                <Sidebar
                    selected={view}
                    onSelect={(name) => setView(name)}
                    version={version}
                    onVersionChange={setVersion}
                />
            }
        >
            <WidgetPage name={view} version={version} />
        </DocsLayout>
    )
}

export default App
