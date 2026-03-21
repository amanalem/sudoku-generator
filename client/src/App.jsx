import { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [puzzle, setPuzzle] = useState(null);
  const [loading, setLoading] = useState(false);
  const [emptyGrid, setEmptyGrid] = useState(true);

  const fetchPuzzle = async () => {
    setLoading(true);
    try {
      const res = await axios.get("http://localhost:8080/api/puzzle");
      setEmptyGrid(false);
      setPuzzle(res.data.puzzle);
    } catch (error) {
      console.error("Error fetching puzzle:", error);
    }
    setLoading(false);
  };

  return (
    <div className="app">
      <h1>Sudoku Generator</h1>
      <button onClick={fetchPuzzle} disabled={loading}>
        {loading ? "Generate Puzzle" : "Generate Puzzle"}
      </button>
      {puzzle && <SudokuGrid puzzle={puzzle} />}
    </div>
  );
}

function SudokuGrid({ puzzle }) {
  return (
    <div className="grid">
      {puzzle.map((row, rowIndex) => (
        <div key={rowIndex} className="row">
          {row.map((cell, colIndex) => (
            <div key={colIndex} className="cell">
              {cell}
            </div>
          ))}
        </div>
      ))}
    </div>
  );
}

export default App;
