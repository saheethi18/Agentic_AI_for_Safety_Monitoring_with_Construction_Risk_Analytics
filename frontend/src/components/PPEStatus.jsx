import React from "react";

function PPEStatus({ item, count, status = "compliant" }) {
  return (
    <div className="ppe-status-row">
      <span>{item}</span>
      <strong>{count}</strong>
      <span className={`status-pill ${status}`}>{status}</span>
    </div>
  );
}

export default PPEStatus;
