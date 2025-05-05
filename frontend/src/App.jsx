import { BrowserRouter, Routes, Route } from 'react-router-dom';
import FundWizard from './pages/FundCreation';
import Navbar from './components/Navbar';
import DocDash from './pages/DocDash'
import Home from './pages/Home'
import Chat from './pages/Chat';


export default function App() {
  return (
    <BrowserRouter>
      <Navbar />
      <Routes>
        <Route path="/fund-creation" element={<FundWizard />} />
        <Route path="/docs" element={<DocDash />} />
        <Route path="/chat" element={<Chat />} />
        <Route path="/" element={<Home />} />
      </Routes>
    </BrowserRouter>
  );
}
