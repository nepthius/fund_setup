import { useNavigate } from 'react-router-dom';
import '../styles/Home.css';

export default function Home() {
  const navigate = useNavigate();

  return (
    <div className="home-container">
      <div className="home-hero">
        <h1>Legal Fund Dash</h1>
        <p>
          Welcome to Opto's automation assisted legal fund setup tool! With this tool, creating new funds and the legal infrastructure to support them is quick and easy!!
        </p>
      </div>

      <div className="home-grid">
        <div className="home-card" onClick={() => navigate('/fund-creation')}>
          <h2>Fund Creation Wizard</h2>
          <p>
            Configure and launch private funds with structured data. Set fees, exemptions, and structure — in minutes.
          </p>
          <span>Go to Fund Creation →</span>
        </div>

        <div className="home-card" onClick={() => navigate('/docs')}>
          <h2>Generate Legal Docs</h2>
          <p>
            Instantly generate PDFs of your PPM, LPA, and Subscription Agreement based on your fund details.
          </p>
          <span>Go to Docs Dashboard →</span>
        </div>

        <div className="home-card" onClick={() => navigate('/chat')}>
          <h2>Legal Llama Index</h2>
          <p>
            Trained on the database dynamically, ask any questions you have about legal aspects of the fund.
          </p>
          <span>Go to Legal Llama Index →</span>
        </div>
      </div>
    </div>
  );
}
