import { useEffect, useState } from "react"
import { Version } from "@/data/index"

export function useVersion() {
    const [version, setVersion] = useState<Version>(() => {
        if (typeof window !== "undefined") {
            const stored = localStorage.getItem("doc_version") as Version
            if (stored && (stored === "v1" || stored === "v2")) return stored
        }
        return "v1"
    })

    useEffect(() => {
        localStorage.setItem("doc_version", version)
    }, [version])

    return { version, setVersion }
}
