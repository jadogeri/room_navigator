
// pages/DiningRoom.tsx
import Board from "../components/Board";
const DiningRoom = (props: any) => (
    <div>
<div><h1>The Dining Room</h1><p>The table is set for twelve.</p></div>

  <Board {...props} width={20} height={25} spawnPos={{ x: 3, y: 2 }}
    doors={[
      { x: 0, y: 0, target: "/foyer" },
      { x: 0, y: 2, target: "/kitchen" }
    ]} />
    </div>
);
export default DiningRoom;