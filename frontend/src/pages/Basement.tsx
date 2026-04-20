// pages/Basement.tsx
import Board from "../components/Board";
const Basement = (props: any) => (
    <div>

<div><h1>The Basement</h1><p>It's pitch black down here.</p></div>

        <Board 
        {...props} 
        width={25} 
        height={30} 
        spawnPos={{ x: 2, y: 1 }}
        doors={[
            { x: 2, y: 0, target: "/kitchen" },
            { x: 4, y: 5, target: "/ritual-room" } // Match the route path above
        ]} 
        />
</div>
);
export default Basement;

