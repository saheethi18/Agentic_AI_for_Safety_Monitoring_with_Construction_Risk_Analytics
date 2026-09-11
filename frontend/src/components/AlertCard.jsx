import React from "react";

function AlertCard({ alert }) {
  const severity = String(alert.severity || "medium").toLowerCase();
  return (
    <article className={`alert-card severity-${severity}`}>
      <div>
        <span className="eyebrow">{severity}</span>
        <h3>{alert.title || "Safety alert"}</h3>
        <p>{alert.description || "Review this observation and assign a corrective action."}</p>
      </div>
      <time>{alert.time || "Just now"}</time>
    </article>
  );
}

export default AlertCard;
