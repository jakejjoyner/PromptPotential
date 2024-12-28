import React from "react";
import { useState } from "react";

const ChatPage = () => {
  const [input, setInput] = useState("");
  const [messages, setMessages] = useState([]);

  const sendMessage = async () => {
    const response = await fetch("http://127.0.0.1:5000/chat", {
      method: "POST",
      mode: "cors",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: input }),
    });

    const data = await response.json();
    setMessages([...messages, { user: input, bot: data.response }]);
    setInput("");
  };

  return (
    <>
      <div>
        {messages.map((message, index) => (
          <div key={index}>
            <div>User: {message.user}</div>
            <div>Bot: {message.bot}</div>
          </div>
        ))}
      </div>
      <input
        type="text"
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Type a message..."
        onSubmit={sendMessage}
        onKeyDown={(e) => { if(e.key === "Enter") sendMessage() }}
      />
      <button onClick={sendMessage}>Send</button>
      <style>
        {`
          div {
            margin-bottom: 10px;
          }
          input {
            margin-right: 10px;
            width: 200px;
            height: 25px;
          }
          button {

          }
        `}
      </style>
    </>
  );
}

export default ChatPage;