import { BrowserRouter, Routes, Route } from 'react-router-dom';
import FundWizard from './pages/FundCreation';
import Navbar from './components/Navbar';
import DocDash from './pages/DocDash'

export default function App() {
  return (
    <BrowserRouter>
      <Navbar />
      <Routes>
        <Route path="/" element={<FundWizard />} />
        <Route path="/docs" element={<DocDash />} />
      </Routes>
    </BrowserRouter>
  );
}
