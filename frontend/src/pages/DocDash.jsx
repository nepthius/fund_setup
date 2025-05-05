import { useEffect, useState } from 'react';
import api from '../api/client';
import '../styles/DocDash.css';

export default function DocsDashboard() {
  const [funds, setFunds] = useState([]);
  const [selectedFundName, setSelectedFundName] = useState(null);
  const [generating, setGenerating] = useState(false);

  useEffect(() => {
    api.get('/funds')
      .then(res => setFunds(res.data))
      .catch(err => console.error('Error fetching funds:', err));
  }, []);

  const handleGenerate = async (type) => {
    if (!selectedFundName) return;
    setGenerating(true);
    try {
      const res = await api.get(`/funds/${selectedFundName}/generate/${type}`, {
        responseType: 'blob',
      });

      const pdfBlob = new Blob([res.data], { type: 'application/pdf' });
      const url = window.URL.createObjectURL(pdfBlob);
      const link = document.createElement('a');
      link.href = url;
      link.setAttribute('download', `${type}_${selectedFundName}.pdf`);
      document.body.appendChild(link);
      link.click();
      link.remove();
    } catch (err) {
      console.error('Generation failed:', err);
    } finally {
      setGenerating(false);
    }
  };

  return (
    <div className="docs-container">
      <h2>Generate Legal Documents</h2>

      <select onChange={(e) => setSelectedFundName(e.target.value)} className="docs-select">
        <option value="">Select a fund</option>
        {funds.map(fund => (
          <option key={fund.id} value={fund.name}>
            {fund.name}
          </option>
        ))}
      </select>

      <div className="docs-actions">
        <button disabled={!selectedFundName || generating} onClick={() => handleGenerate('ppm')}>
          Generate PPM
        </button>
        <button disabled={!selectedFundName || generating} onClick={() => handleGenerate('lpa')}>
          Generate LPA
        </button>
        <button disabled={!selectedFundName || generating} onClick={() => handleGenerate('sub')}>
          Generate Subscription Agreement
        </button>
      </div>
    </div>
  );
}
