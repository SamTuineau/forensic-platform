import React, { useState } from "react"
import axios from "axios"

export default function Ingestion() {
  const [path, setPath] = useState("")
  const [result, setResult] = useState(null)
  const [manifest, setManifest] = useState(null)

  const handleScan = async () => {
    try {
      const res = await axios.post("/ingest", { path })
      setResult(res.data)
      if (res.data.manifest_path) {
        const man = await axios.get("/manifest")
        setManifest(JSON.parse(man.data))
      }
    } catch (e) {
      setResult({ error: e.message })
    }
  }

  return (
    <div style={{ padding: "20px" }}>
      <h2>Ingestion</h2>
      <div>
        <input
          type="text"
          placeholder="Directory path"
          value={path}
          onChange={(e) => setPath(e.target.value)}
          style={{ width: "60%" }}
        />
        <button onClick={handleScan}>Scan</button>
      </div>
      {result && (
        <div>
          <h3>Result</h3>
          <pre>{JSON.stringify(result, null, 2)}</pre>
        </div>
      )}
      {manifest && (
        <div>
          <h3>Manifest</h3>
          <table border="1">
            <thead>
              <tr>
                <th>File Path</th>
                <th>Size</th>
                <th>Hash</th>
              </tr>
            </thead>
            <tbody>
              {manifest.files.map((f, idx) => (
                <tr key={idx}>
                  <td>{f.file_path}</td>
                  <td>{f.size}</td>
                  <td>{f.hash}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  )
}