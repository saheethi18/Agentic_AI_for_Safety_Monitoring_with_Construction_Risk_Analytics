import React from "react";
import { useNavigate } from "react-router-dom";
import { clearSession, getCurrentUser } from "../services/authService.js";

function Navbar() {
  const navigate = useNavigate();
  const user = getCurrentUser();

  const handleLogout = () => {
    clearSession();
    navigate("/login");
  };

  return (
    <header className="app-navbar">
      <button className="brand-button" onClick={() => navigate("/dashboard")}>
        <span className="brand-mark">B</span>
        <span>BuildSure AI</span>
      </button>
      <div className="navbar-actions">
        <span className="user-label">{user?.name || "Safety Officer"}</span>
        <button className="text-button" onClick={handleLogout}>Log out</button>
      </div>
    </header>
  );
}

export default Navbar;
