import Board from "../components/Board";

const Foyer = ({ inventory, setInventory }: any) => {
  return (
    <div>
<div><h1>The Grand Foyer</h1><p>The stairs loom above you...</p></div>

      <Board 
        width={132} height={40}
        spawnPos={{ x: 1, y: 1 }} // Start safe!
        inventory={inventory}
        setInventory={setInventory}
        items={[{ x: 3, y: 3, type: "🗝️", name: "Silver Key" }]}
        doors={[{ x: 5, y: 4, target: "/portraitgallery", requiredItem: "🗝️" },
              { x: 10, y: 7, target: "/dining-room" },
              { x: 0, y: 6, target: "/library" },

        ]}
      />
    </div>
  );
};
export default Foyer;
