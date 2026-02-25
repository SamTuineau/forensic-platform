import React from "react"
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom"
import Ingestion from "./Ingestion"

export default function App() {
  return (
    <Router>
      <div style={{ padding: "40px" }}>
        <h1>Forensic Environment Explorer</h1>
        <nav>
          <Link to="/">Home</Link> | <Link to="/ingestion">Ingestion</Link>
        </nav>
        <Routes>
          <Route path="/" element={<p>UI running successfully.</p>} />
          <Route path="/ingestion" element={<Ingestion />} />
        </Routes>
      </div>
    </Router>
  )
}