
// pages/HallOfMirrors.tsx
import Board from "../components/Board";
const HallOfMirrors = (props: any) => (
    <div>

<div><h1>Hall of Mirrors</h1><p>Which reflection is the real you?</p></div>


  <Board {...props} width={15} height={25} spawnPos={{ x: 1, y: 3 }}
    doors={[
      { x: 1, y: 4, target: "/bedroom" },
      { x: 1, y: 0, target: "/attic" }
    ]} />
    </div>
);
export default HallOfMirrors;
