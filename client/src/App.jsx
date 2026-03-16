import { useState } from "react";
import axios from "axios";
import reactLogo from "./assets/react.svg";
import viteLogo from "./assets/vite.svg";
import heroImg from "./assets/hero.png";
import "./App.css";

function App() {
  const [puzzle, setPuzzle] = useState(null);

  const fetchPuzzle = async () => {
    const res = await axios.get("http://localhost:5000/api/puzzle");
    setPuzzle(res.data.puzzle);
  };

  return (
    <div>
      <h1>Sudoku Generator</h1>
      <button onClick={fetchPuzzle}>Generate Sudoku</button>
      {/* Render Puzzle grid here */}
    </div>
  );
}

export default App;
