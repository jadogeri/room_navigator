
// pages/Library.tsx
import Board from "../components/Board";
const Library = (props: any) => (
    <div>

<div><h1>The Library</h1><p>Dusty books line the walls.</p></div>


  <Board {...props} width={25} height={35} spawnPos={{ x: 2, y: 5 }}
    doors={[
      // { x: 2, y: 6, target: "/foyer" },
      { x: 2, y: 0, target: "/bedroom" }
    ]} />
    </div>
);
export default Library;