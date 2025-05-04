import { BrowserRouter, Routes, Route } from 'react-router-dom';
import FundWizard from './pages/FundCreation';
import Navbar from './components/Navbar';

export default function App() {
  return (
    <BrowserRouter>
      <Navbar />
      <Routes>
        <Route path="/" element={<FundWizard />} />
        
      </Routes>
    </BrowserRouter>
  );
}
