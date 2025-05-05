import { useState } from 'react';
import api from '../api/client';
import '../styles/Chat.css';

export default function ChatAssistant() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMessage = { sender: 'user', text: input };
    setMessages((prev) => [...prev, userMessage]);
    setInput('');
    setLoading(true);

    try {
      const res = await api.post('/chat', { message: userMessage.text });
      const botMessage = { sender: 'bot', text: res.data.response };
      setMessages((prev) => [...prev, botMessage]);
    } catch (err) {
      setMessages((prev) => [...prev, { sender: 'bot', text: 'Error responding to your question.' }]);
    } finally {
      setLoading(false);
    }
  };

  const handleKeyDown = (e) => {
    if (e.key === 'Enter') sendMessage();
  };

  return (
    <div className="chat-container">
      <h2>Legal Assistant</h2>
      <div className="chat-window">
        {messages.map((msg, idx) => (
          <div key={idx} className={`chat-message ${msg.sender}`}>
            {msg.text}
          </div>
        ))}
        {loading && <div className="chat-message bot">Typing...</div>}
      </div>
      <div className="chat-input">
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder="Ask something about your funds or investors..."
        />
        <button onClick={sendMessage} disabled={loading}>Send</button>
      </div>
    </div>
  );
}
