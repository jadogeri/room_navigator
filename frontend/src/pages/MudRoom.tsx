

// pages/MudRoom.tsx
import Board from "../components/Board";
const MudRoom  = (props: any) => (
    <div>


<div><h1>The Mudroom</h1><p>The air is thick with the scent of wet earth and ancient rain.</p></div>

  <Board {...props} width={20} height={20} spawnPos={{ x: 2, y: 1 }}
    doors={[{ x: 2, y: 0, target: "/portraitgallery" }]} />
    </div>

);
export default MudRoom;
