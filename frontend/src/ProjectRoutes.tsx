import React, { useState } from "react";
import { BrowserRouter, Route, Routes, Navigate } from "react-router-dom";
import Foyer from "./pages/Foyer";
import Kitchen from "./pages/Kitchen";
import Bedroom from "./pages/BedRoom";	
import Library from "./pages/Library";
import DiningRoom from "./pages/DiningRoom";
import Basement from "./pages/Basement";	
import Attic from "./pages/Attic";
import HallOfMirrors from "./pages/HallOfMirrors";
import Solarium from "./pages/Solarium";
import PortraitGallery from "./pages/PotraitGallery";
import NoPage from "./pages/NoPage";
import RitualRoom from "./pages/RitualRoom";
import MudRoom from "./pages/MudRoom";

const ProjectRoutes = () => {
  // Shared state: This keeps your keys from disappearing!
  const [inventory, setInventory] = useState<string[]>([]);

  // Helper to pass props to all components easily
  const sharedProps = { inventory, setInventory };

  return (	
    <BrowserRouter>
      <Routes>		
        <Route path="/" element={<Navigate to="/foyer" />} />
        <Route path="/foyer" element={<Foyer {...sharedProps} />} />
        <Route path="/kitchen" element={<Kitchen {...sharedProps} />} />
        <Route path="/bedroom" element={<Bedroom {...sharedProps} />} />
        <Route path="/library" element={<Library {...sharedProps} />} />
        <Route path="/dining-room" element={<DiningRoom {...sharedProps} />} />
        <Route path="/basement" element={<Basement {...sharedProps} />} />
        <Route path="/attic" element={<Attic {...sharedProps} />} />
        <Route path="/mirrors" element={<HallOfMirrors {...sharedProps} />} />
        <Route path="/solarium" element={<Solarium {...sharedProps} />} />
        <Route path="/portraitgallery" element={<PortraitGallery {...sharedProps} />} />
		<Route path="/ritual-room" element={<RitualRoom {...sharedProps} />} />
		<Route path="/mud-room" element={<MudRoom {...sharedProps} />} />
        <Route path="*" element={<NoPage />} />
      </Routes>
    </BrowserRouter>
  );
};

export default ProjectRoutes;
