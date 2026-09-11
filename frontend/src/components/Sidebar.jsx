import React from "react";
import { NavLink } from "react-router-dom";

const links = [
  ["/dashboard", "Overview"],
  ["/safety-intelligence", "Safety Intelligence"],
  ["/ppe-compliance", "PPE Compliance"],
  ["/workers", "Workers"],
  ["/alerts", "Alerts"],
  ["/analytics", "Analytics"],
  ["/reports", "Reports"]
];

function Sidebar() {
  return (
    <aside className="app-sidebar">
      <p className="sidebar-label">Workspace</p>
      <nav aria-label="Primary navigation">
        {links.map(([to, label]) => (
          <NavLink key={to} to={to} className={({ isActive }) => isActive ? "nav-link active" : "nav-link"}>
            {label}
          </NavLink>
        ))}
      </nav>
    </aside>
  );
}

export default Sidebar;
