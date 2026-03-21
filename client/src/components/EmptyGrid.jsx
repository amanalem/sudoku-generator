import React from "react";

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

export default EmptyGrid;