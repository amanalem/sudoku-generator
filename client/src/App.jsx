import { useState } from "react";
import axios from "axios";
import "./App.css";
import EmptyGrid from "./components/EmptyGrid";
import SudokuGrid from "./components/SudokuGrid";

function App() {
  const [puzzle, setPuzzle] = useState(null);
  const [solution, setSolution] = useState(null);
  const [loading, setLoading] = useState(false);
  const [emptyGrid, setEmptyGrid] = useState(true);

  const fetchPuzzle = async (difficulty) => {
    setLoading(true);
    try {
      const res = await axios.get(`http://localhost:8080/api/puzzle?difficulty=${difficulty}`);
      setEmptyGrid(null);
      setPuzzle(res.data.puzzle);
      setSolution(res.data.solution)
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
      <div>
        <button onClick={() => fetchPuzzle("easy")}>Easy</button>
        <button onClick={() => fetchPuzzle("medium")}>Medium</button>
        <button onClick={() => fetchPuzzle("hard")}>Hard</button>
        <button onClick={() => fetchPuzzle("expert")}>Expert</button>
      </div>
      {emptyGrid && <EmptyGrid/>}
      {puzzle && <SudokuGrid puzzle={puzzle} solution={solution}/>}
      <button onClick={fetchEmptyGrid}>Clear Grid</button>
    </div>
  );
}

export default App;
