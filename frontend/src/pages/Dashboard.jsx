import React from "react";
import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { getDatasetSummary } from "../services/siteRiskAPI.js";
import "./Dashboard.css";

const Dashboard = () => {
  const navigate = useNavigate();
  const [dataset, setDataset] = useState(null);
  const [datasetError, setDatasetError] = useState("");

  useEffect(() => {
    getDatasetSummary()
      .then(setDataset)
      .catch(() => setDatasetError("Start the backend to load dataset metrics."));
  }, []);

  return (
    <div className="dashboard">

      {/* Header */}
      <header className="dashboard-header">
        <div>
          <h1>BuildSure AI</h1>
          <p>Construction Safety Intelligence</p>
        </div>
      </header>

      {/* Main Content */}
      <main className="dashboard-content">

        <h2>Safety Dashboard</h2>

        <p className="dashboard-subtitle">
          Monitor construction-site safety and worker protection.
          {dataset && ` Connected to ${dataset.dataset} (${dataset.imageCount.toLocaleString()} images).`}
        </p>

        {datasetError && <p className="dashboard-error">{datasetError}</p>}

        {/* Statistics */}
        <div className="stats-grid">

          <div className="stat-card">
            <h3>Total Workers</h3>
            <p>{dataset?.workers ?? 0}</p>
            <span>Dataset annotations</span>
          </div>

          <div className="stat-card">
            <h3>PPE Compliant</h3>
            <p>{dataset?.ppeCompliant ?? 0}</p>
            <span>Hardhat and vest labels</span>
          </div>

          <div className="stat-card">
            <h3>Violations</h3>
            <p>{dataset?.violations ?? 0}</p>
            <span>Missing PPE annotations</span>
          </div>

          <div className="stat-card">
            <h3>High Risk</h3>
            <p>{dataset?.highRisk ?? 0}</p>
            <span>Equipment and vehicle annotations</span>
          </div>

        </div>

        {/* Safety Features */}
        <section className="dashboard-section">

          <h2>Safety Intelligence</h2>

          <div className="feature-grid">

            {/* AI Safety Analysis */}
            <div className="feature-card">
              <h3>AI Safety Analysis</h3>

              <p>
                Upload a construction-site image and analyze
                safety conditions using AI.
              </p>

              <button
                onClick={() => navigate("/safety-intelligence")}
              >
                Start Analysis
              </button>
            </div>

            {/* PPE Compliance */}
            <div className="feature-card">
              <h3>PPE Compliance</h3>

              <p>
                Check whether workers are using the required
                personal protective equipment.
              </p>

              <button
                onClick={() => navigate("/ppe-compliance")}
              >
                Check PPE
              </button>
            </div>

            {/* Worker Monitoring */}
            <div className="feature-card">
              <h3>Worker Monitoring</h3>

              <p>
                Monitor workers and identify safety-related
                issues at the construction site.
              </p>

              <button
                onClick={() => navigate("/workers")}
              >
                View Workers
              </button>
            </div>

            {/* Alerts */}
            <div className="feature-card">
              <h3>Safety Alerts</h3>

              <p>
                View safety violations and high-risk
                situations detected by the system.
              </p>

              <button
                onClick={() => navigate("/alerts")}
              >
                View Alerts
              </button>
            </div>

          </div>

        </section>

        {/* Analytics */}
        <section className="analytics-section">

          <div className="analytics-card">

            <h2>Safety Analytics</h2>

            <p>
              View worker safety, PPE compliance,
              risk levels and safety statistics.
            </p>

            <button
              onClick={() => navigate("/analytics")}
            >
              Open Analytics
            </button>

          </div>

        </section>

      </main>

    </div>
  );
};

export default Dashboard;