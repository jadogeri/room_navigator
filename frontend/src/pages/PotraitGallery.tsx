
// pages/PotraitGallery.tsx
import Board from "../components/Board";
const PortraitGallery = (props: any) => (
    <div>

<div><h1>Portrait Gallery</h1><p>The eyes are definitely following you.</p></div>

  <Board {...props} width={10} height={40} spawnPos={{ x: 0, y: 1 }}
    doors={[
      { x: 0, y: 0, target: "/foyer" },
      { x: 0, y: 7, target: "/solarium" }
    ]} />
    </div>
);
export default PortraitGallery;
