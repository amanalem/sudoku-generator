import { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [puzzle, setPuzzle] = useState(null);
  const [loading, setLoading] = useState(false);
  const [emptyGrid, setEmptyGrid] = useState(null);

  const fetchPuzzle = async () => {
    setLoading(true);
    try {
      const res = await axios.get("http://localhost:8080/api/puzzle");
      setEmptyGrid(null);
      setPuzzle(res.data.puzzle);
    } catch (error) {
      console.error("Error fetching puzzle:", error);
    }
    setLoading(false);
  };

  const fetchEmptyGrid = async () => {
    try {
      const res = await axios.get("http://localhost:8080/api/puzzle");
      setEmptyGrid(res.data.blank);
    } catch (error) {
      console.error("Error fetching blank puzzle:", error);
    }
  };

  return (
    <div className="app">
      <h1>Sudoku Generator</h1>
      <button
        onBeforeInput={fetchEmptyGrid}
        onClick={fetchPuzzle}
        disabled={loading}
      >
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

function EmptyGrid({ emptyGrid }) {
  return (
    <div className="grid">
      {emptyGrid.map((row, rowIndex) => (
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
