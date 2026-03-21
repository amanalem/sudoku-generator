import React from "react";

function EmptyGrid() {
    const emptyGrid = []

    for (let i = 0; i < 9; i++) {
        const row = []
        for (let i = 0; i < 9; i++) {
            row[i] = ' '
        }
        emptyGrid[i] = row
    }
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

export default EmptyGrid;