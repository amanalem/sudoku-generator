import { useState } from "react";
import axios from "axios";
import "./App.css";
import EmptyGrid from "./components/EmptyGrid";
import SudokuGrid from "./components/SudokuGrid";

function App() {
  const [puzzle, setPuzzle] = useState(null);
  const [loading, setLoading] = useState(false);
  const [emptyGrid, setEmptyGrid] = useState(true);

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
    setPuzzle(null)
    setEmptyGrid(true)
  }


  return (
    <div className="app">
      <h1>Sudoku Generator</h1>
      <button
        
        onClick={fetchPuzzle}
        disabled={loading}
      >
        {loading ? "Generate Solution" : "Generate Solution"}
      </button>
      {emptyGrid && <EmptyGrid/>}
      {puzzle && <SudokuGrid puzzle={puzzle} />}
      <button onClick={fetchEmptyGrid}>{"Clear Grid"}</button>
    </div>
  );
}

export default App;
