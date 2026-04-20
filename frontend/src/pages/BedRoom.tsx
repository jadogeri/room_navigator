

// pages/BedRoom.tsx
import Board from "../components/Board";
const Bedroom = (props: any) => (
    <div>

<div><h1>Master Bedroom & Nursery</h1><p>You hear a faint lullaby.</p></div>


  <Board {...props} width={20} height={20} spawnPos={{ x: 1, y: 2 }}
    doors={[
      { x: 1, y: 3, target: "/library" },
      { x: 0, y: 1, target: "/mirrors" } // Hall of mirrors
    ]} />
    </div>
);
export default Bedroom;
