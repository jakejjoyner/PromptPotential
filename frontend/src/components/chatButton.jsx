import React from "react";
import { useNavigate } from 'react-router-dom';

const ChatButton = () => {
  const navigate = useNavigate();

  const handleClick = () => {
    navigate("/chat");
  }

  return (
    <div>
      <button onClick={handleClick}>Chat</button>
    </div>
  );
}

export default ChatButton;