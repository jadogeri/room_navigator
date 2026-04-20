import React, { useState, useEffect, useCallback } from 'react';
import { useNavigate } from 'react-router-dom';
import Square from './Square';

export interface Door { x: number; y: number; target: string; requiredItem?: string; }
export interface Item { x: number; y: number; type: string; name: string; }

interface BoardProps {
  width: number;
  height: number;
  doors: Door[];
  initialWalls?: string[]; 
  items?: Item[];
  inventory: string[];
  setInventory: React.Dispatch<React.SetStateAction<string[]>>;
  spawnPos: { x: number; y: number };
}

const Board = ({ width, height, doors, initialWalls = [], items = [], inventory, setInventory, spawnPos }: BoardProps) => {
  const navigate = useNavigate();
  const columns = Math.ceil(width / 5);
  const rows = Math.ceil(height / 5);
  
  const [pos, setPos] = useState(spawnPos);
  const [walls] = useState(new Set(initialWalls));
  const [currentItems, setCurrentItems] = useState<Item[]>(items);

  // Sync position and items when room changes
  useEffect(() => {
    setPos(spawnPos);
    setCurrentItems(items);
  }, [spawnPos, items]);

  const movePlayer = useCallback((dx: number, dy: number) => {
    setPos((prev) => {
      const nX = Math.max(0, Math.min(columns - 1, prev.x + dx));
      const nY = Math.max(0, Math.min(rows - 1, prev.y + dy));

      if (walls.has(`${nX},${nY}`)) return prev;

      const door = doors.find(d => d.x === nX && d.y === nY);
      if (door?.requiredItem && !inventory.includes(door.requiredItem)) {
        alert(`🔒 Locked! You need the ${door.requiredItem}`);
        return prev; 
      }
      return { x: nX, y: nY };
    });
  }, [columns, rows, walls, doors, inventory]);

  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'ArrowUp') movePlayer(0, -1);
      if (e.key === 'ArrowDown') movePlayer(0, 1);
      if (e.key === 'ArrowLeft') movePlayer(-1, 0);
      if (e.key === 'ArrowRight') movePlayer(1, 0);
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [movePlayer]);

  useEffect(() => {
    // Check for Items
    const foundItem = currentItems.find(i => i.x === pos.x && i.y === pos.y);
    if (foundItem) {
      setInventory(prev => [...prev, foundItem.type]);
      setCurrentItems(prev => prev.filter(i => i !== foundItem));
      setTimeout(() => alert(`✨ Found: ${foundItem.name}!`), 50);
    }

    // Check for Doors
    const door = doors.find(d => d.x === pos.x && d.y === pos.y);
    if (door && (!door.requiredItem || inventory.includes(door.requiredItem))) {
      navigate(door.target);
    }
  }, [pos, doors, currentItems, inventory, navigate]);

  return (
    <div style={{ display: 'grid', gridTemplateColumns: `repeat(${columns}, 40px)`, backgroundColor: '#111', padding: '10px' }}>
      {Array.from({ length: rows * columns }).map((_, i) => {
        const x = i % columns, y = Math.floor(i / columns);
        const isPlayer = x === pos.x && y === pos.y;
        const door = doors.find(d => d.x === x && d.y === y);
        const item = currentItems.find(it => it.x === x && it.y === y);
        const wall = walls.has(`${x},${y}`);
        return <Square key={i} x={x} y={y} content={isPlayer ? "🧙" : item ? item.type : door ? "🚪" : wall ? "🧱" : ""} />;
      })}
    </div>
  );
};
export default Board;
