
// pages/Attic.tsx
import Board from "../components/Board";
const Attic = (props: any) => (
    <div>

<div><h1>The Attic</h1><p>Eyes watch you from the doll crates.</p></div>


        <Board {...props} width={40} height={15} spawnPos={{ x: 4, y: 1 }}
            doors={[{ x: 4, y: 2, target: "/mirrors" }]} />
    </div>
);
export default Attic;
