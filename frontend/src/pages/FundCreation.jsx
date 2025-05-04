import { useState } from 'react';
import api from '../api/client';
import '../styles/FundCreation.css'

export default function FundWizard() {
    const [form, setForm] = useState({
        name: '',
        type: 'Private Equity',
        exemption: '506(b)',
        manager: '',
        management_fee: '',
        carry: '',
        jurisdiction: 'Delaware',
        total_raise: '',
        min_investment: '',
        manager_contact_email: '',
        term_years: 7,
        subscription_deadline: '',
        capital_call_notice_days: 10,
        preferred_return: '',
        org_expense_cap: 100000.0,
        admin_fee_percent: '',
        initial_close_date: '',
        asset_focus: 'private equity',
        target_sectors: '',
      });
  
    const [createdFund, setCreatedFund] = useState(null);
  
    const handleChange = (e) => {
      const { name, value } = e.target;
      setForm((prev) => ({ ...prev, [name]: value }));
    };
  
    const handleSubmit = async () => {
        try {
          const res = await api.post('/funds', {
            ...form,
            management_fee: parseFloat(form.management_fee),
            carry: parseFloat(form.carry),
            total_raise: parseFloat(form.total_raise) || null,
            min_investment: parseFloat(form.min_investment) || null,
            term_years: parseInt(form.term_years),
            capital_call_notice_days: parseInt(form.capital_call_notice_days),
            preferred_return: parseFloat(form.preferred_return) || null,
            org_expense_cap: parseFloat(form.org_expense_cap),
            admin_fee_percent: parseFloat(form.admin_fee_percent) || null,
            subscription_deadline: form.subscription_deadline || null,
            initial_close_date: form.initial_close_date || null,
          });
          setCreatedFund(res.data);
        } catch (err) {
          console.error('Error creating fund:', err.response?.data || err.message);
        }
      };
      
  
    return (
      <div className="fund-container">
        <h2 className="fund-title">Create a Fund</h2>
        <p className="fund-subtext">
          Use this form to configure your fund’s legal and investment details.
        </p>
  
        <div className="fund-form">

        {/* Fund Details */}
        <div className="fund-section">
            <h4>Fund Details</h4>
            <input name="name" placeholder="Fund Name" onChange={handleChange} />
            <select name="type" onChange={handleChange} defaultValue="Private Equity">
            <option value="Private Equity">Private Equity</option>
            <option value="Private Credit">Private Credit</option>
            <option value="SPV">SPV</option>
            </select>
            <input name="manager" placeholder="Manager" onChange={handleChange} />
            <input name="jurisdiction" placeholder="Jurisdiction" onChange={handleChange} />
            <input name="asset_focus" placeholder="Asset Focus" onChange={handleChange} />
            <input name="target_sectors" placeholder="Target Sectors" onChange={handleChange} />
        </div>

        {/* Financial Terms */}
        <div className="fund-section">
            <h4>Financial Terms</h4>
            <input name="management_fee" placeholder="Management Fee (%)" onChange={handleChange} />
            <input name="carry" placeholder="Carry (%)" onChange={handleChange} />
            <input name="total_raise" placeholder="Total Raise ($)" onChange={handleChange} />
            <input name="min_investment" placeholder="Min Investment ($)" onChange={handleChange} />
            <input name="preferred_return" placeholder="Preferred Return (%)" onChange={handleChange} />
            <input name="org_expense_cap" placeholder="Org Expense Cap ($)" onChange={handleChange} />
            <input name="admin_fee_percent" placeholder="Admin Fee (%)" onChange={handleChange} />
        </div>

        {/* Legal & Compliance */}
        <div className="fund-section">
            <h4>Legal & Compliance</h4>
            <select name="exemption" onChange={handleChange} defaultValue="506(b)">
            <option value="506(b)">506(b)</option>
            <option value="506(c)">506(c)</option>
            <option value="Reg A">Reg A</option>
            <option value="Reg S">Reg S</option>
            <option value="4(a)(2)">4(a)(2)</option>
            </select>
            <input name="manager_contact_email" placeholder="Manager Email" onChange={handleChange} />
            <input name="term_years" placeholder="Term Years" onChange={handleChange} />
            <input name="capital_call_notice_days" placeholder="Capital Call Notice Days" onChange={handleChange} />
            <label htmlFor="subscription_deadline">Subscription Deadline</label>
            <input
            type="date"
            id="subscription_deadline"
            name="subscription_deadline"
            onChange={handleChange}
            />

            <label htmlFor="initial_close_date">Initial Close Date</label>
            <input
            type="date"
            id="initial_close_date"
            name="initial_close_date"
            onChange={handleChange}
            />

        </div>

        <button className="fund-button" onClick={handleSubmit}>Create Fund</button>
        </div>

  
        {createdFund && (
          <div className="fund-result">
            <h3 style={{ fontFamily: 'Georgia, serif' }}>Fund Created</h3>
            <pre>{JSON.stringify(createdFund, null, 2)}</pre>
          </div>
        )}
      </div>
    );
  }