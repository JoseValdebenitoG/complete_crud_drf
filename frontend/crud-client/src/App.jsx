import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom"
import { Navigation } from "./components/Navigation"
import { Toaster } from "react-hot-toast"

function App() {

  return (
    <BrowserRouter>
      <main className="container mx-auto">
        <Navigation/>
        <h1>home</h1>
      </main>
    </BrowserRouter>
  )
}

export default App
