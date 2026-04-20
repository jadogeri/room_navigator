// Square.tsx
import React from 'react';

interface SquareProps {
  x: number;
  y: number;
  content?: string; // e.g., "👻", "🗝️", "🚪"
}

const Square = ({ x, y, content }: SquareProps) => {
  return (
    <div style={{
      width: '40px',
      height: '40px',
      border: '1px solid #222',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      fontSize: '20px',
      backgroundColor: 'rgba(20, 20, 20, 0.8)'
    }}>
      {content}
    </div>
  );
};

export default Square;
