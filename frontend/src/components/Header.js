import { Link } from "react-router-dom";

function Header() {
  return (
    <div className="header">

      <div className="logo">🧠 MedAI</div>

      <div className="nav">
        <Link to="/">Home</Link>
        <Link to="/reports">Reports Summary</Link>
      </div>

    </div>
  );
}

export default Header;