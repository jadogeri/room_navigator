import Board from "../components/Board";

const RitualRoom = (props: any) => (
  <div>
    <h1>Ritual Room</h1>
    <p>A hidden stone room. The air feels heavy.</p>
    <Board 
      {...props} 
      width={15} 
      height={15} 
      spawnPos={{ x: 1, y: 1 }} // One step below the door
      doors={[
        { x: 1, y: 0, target: "/basement" }
      ]} 
    />
  </div>
);

export default RitualRoom;
