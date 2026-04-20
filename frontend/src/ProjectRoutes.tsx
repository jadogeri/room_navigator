import { BrowserRouter, Route, Routes, Navigate } from "react-router-dom";
/**  ROUTES -- AUTHFLOW **/
import Foyer from "./pages/Foyer";
import Kitchen from "./pages/Kitchen";
import Bedroom from "./pages/Bedroom";	
import Library from "./pages/Library";
import DiningRoom from "./pages/DiningRoom";
import Basement from "./pages/Basement";	
import Attic from "./pages/Attic";
import HallOfMirrors from "./pages/HallOfMirrors";
import Solarium from "./pages/Solarium";
import PortraitGallery from "./pages/PotraitGallery";
import NoPage from "./pages/NoPage";


const ProjectRoutes = ({}) => {

  return (	
	<BrowserRouter >
		<Routes >		
			<Route path="/" element={<Navigate to="/foyer" />} />
			<Route path="/foyer" element={<Foyer />} />
			<Route path="/kitchen" element={<Kitchen />} />
			<Route path="/bedroom" element={<Bedroom />} />
			<Route path="/library" element={<Library />} />
			<Route path="/dining-room" element={<DiningRoom />} />
			<Route path="/basement" element={<Basement />} />
			<Route path="/attic" element={<Attic />} />
			<Route path="/mirrors" element={<HallOfMirrors />} />
			<Route path="/solarium" element={<Solarium />} />
			<Route path="/gallery" element={<PortraitGallery />} />
			<Route path="*" element={<NoPage />} />
		</Routes>
	</BrowserRouter>


  )
}



export default ProjectRoutes

