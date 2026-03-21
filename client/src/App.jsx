import { useState } from "react";
import axios from "axios";
import "./App.css";
import EmptyGrid from "./components/EmptyGrid";
import SudokuGrid from "./components/SudokuGrid";

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
      {emptyGrid && <EmptyGrid emptyGrid={emptyGrid} />}
      {puzzle && <SudokuGrid puzzle={puzzle} />}
    </div>
  );
}

export default App;
