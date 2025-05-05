import '../styles/Navbar.css';
import optoLogo from '../assets/opto.svg';

export default function Navbar() {
  return (
    <nav className="navbar">
      <div className="navbar-left">
      <a href="/"><img src={optoLogo} alt="Opto logo" className="navbar-logo" /></a>
      </div>

      <div className="navbar-center">
        <a href="#">About us</a>
        <a href="#">Careers</a>
        <a href="#">Press</a>
        <a href="#">Insights</a>
      </div>

      <div className="navbar-right">
        <a href="#" className="navbar-link">Log in</a>
        <button className="navbar-button">Learn more</button>
      </div>
    </nav>
  );
}
