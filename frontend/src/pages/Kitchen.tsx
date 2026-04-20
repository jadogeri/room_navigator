
// pages/Kitchen.tsx
import Board from "../components/Board";
const Kitchen = (props: any) => (
  <div>

<div><h1>Kitchen & Pantry</h1><p>The knives seem to be missing...</p></div>

  <Board {...props} width={15} height={20} spawnPos={{ x: 1, y: 1 }}
    doors={[
      { x: 1, y: 0, target: "/dining-room" },
      { x: 1, y: 3, target: "/basement" },
      { x: 2, y: 2, target: "/solarium", requiredItem: "🗝️" } // Locked door
    ]} />

    </div>
);
export default Kitchen;