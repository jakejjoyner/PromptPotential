import './App.css'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import HomePage from './components/homePage.jsx'
import ChatPage from './components/chatPage.jsx'

const App = () => {

  return (
    <>
      <Router>
        <Routes>
          <Route path="/" element={ <HomePage /> } />
          <Route path="/chat" element={ <ChatPage /> } />
        </Routes>
      </Router>
    </>
  )
}

export default App;
