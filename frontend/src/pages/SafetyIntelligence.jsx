import React, { useEffect, useState } from "react";
import AppShell from "../components/AppShell.jsx";
import { getDatasetSummary, getSiteRisk } from "../services/siteRiskAPI.js";
import "./SafetyIntelligence.css";

function SafetyIntelligence() {
  const [dataset, setDataset] = useState(null);
  const [datasetLoading, setDatasetLoading] = useState(true);
  const [datasetMessage, setDatasetMessage] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState("Run an analysis to review the latest site risk signals.");

  useEffect(() => {
    let active = true;

    getDatasetSummary()
      .then((summary) => {
        if (active) {
          setDataset(summary);
        }
      })
      .catch(() => {
        if (active) {
          setDatasetMessage("Dataset metrics are unavailable. Start the FastAPI backend and refresh.");
        }
      })
      .finally(() => {
        if (active) {
          setDatasetLoading(false);
        }
      });

    return () => {
      active = false;
    };
  }, []);

  const analyze = async () => {
    setLoading(true);
    setMessage("");
    try {
      setResult(await getSiteRisk());
    } catch (error) {
      setMessage("The risk service is unavailable. Start the FastAPI backend and try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <AppShell>
      <PageHeader 
        title="Safety Intelligence" 
        description="Turn observations into prioritized safety decisions."
      />

      <section className="dataset-overview" aria-labelledby="dataset-overview-title">
        <div className="dataset-overview-header">
          <div>
            <span className="eyebrow">Dataset Overview</span>
            <h2 id="dataset-overview-title">Construction Site Safety Metrics</h2>
          </div>
          {dataset?.dataset && <span className="dataset-name">{dataset.dataset}</span>}
        </div>

        <div className="dataset-metrics-grid">
          <DatasetMetric label="Total Workers" value={dataset?.workers} detail="Person annotations" tone="blue" />
          <DatasetMetric label="PPE Compliant" value={dataset?.ppeCompliant} detail="Hardhat and safety vest" tone="green" />
          <DatasetMetric label="Violations" value={dataset?.violations} detail="Missing PPE annotations" tone="red" />
          <DatasetMetric label="High Risk" value={dataset?.highRisk} detail="Machinery and vehicle" tone="orange" />
        </div>
        {!dataset && !datasetLoading && (
          <p className="dataset-status dataset-error">{datasetMessage}</p>
        )}
      </section>
      
      <div className="safety-intelligence-container">
        {/* Analysis Panel */}
        <section className="analysis-panel">
          <div className="panel-header">
            <span className="eyebrow">Site Risk Agent</span>
            <h2>Analyze Current Conditions</h2>
            <p>Review hazards, worker exposure, equipment risk, and recommended controls for the active project.</p>
          </div>
          <button 
            className="analyze-button" 
            onClick={analyze} 
            disabled={loading}
          >
            {loading ? "Analyzing..." : "Run Site Analysis"}
          </button>
        </section>

        {/* Results Panel */}
        <section className="results-panel">
          <div className="panel-header">
            <span className="eyebrow">Latest Result</span>
            <h2>Site Risk Analysis</h2>
          </div>

          {result ? (
            <div className="results-content">
              {/* Risk Score Card */}
              <div className={`risk-card risk-${(result.riskLevel || "LOW").toLowerCase()}`}>
                <div className="score-display">
                  <span className="score-number">{result.riskScore ?? 0}</span>
                  <span className="score-max">/100</span>
                </div>
                <p className="risk-label">Risk Score</p>
                <p className="risk-level">{result.riskLevel || "LOW"}</p>
              </div>

              {/* Monitoring Metrics */}
              <div className="metrics-grid">
                <div className="metric-card">
                  <h4>Total Workers</h4>
                  <p className="metric-value">{result.monitoring?.workers || 0}</p>
                </div>
                <div className="metric-card">
                  <h4>Equipment Units</h4>
                  <p className="metric-value">{result.monitoring?.equipment || 0}</p>
                </div>
                <div className="metric-card">
                  <h4>Temperature</h4>
                  <p className="metric-value">{result.monitoring?.temperature?.toFixed(1) || 0}°C</p>
                </div>
                <div className="metric-card">
                  <h4>Humidity</h4>
                  <p className="metric-value">{result.monitoring?.humidity || 0}%</p>
                </div>
              </div>

              {/* Hazards Section */}
              <div className="hazards-section">
                <h3>Detected Hazards ({result.hazards?.length || 0})</h3>
                {result.hazards && result.hazards.length > 0 ? (
                  <div className="hazards-list">
                    {result.hazards.map((hazard, idx) => (
                      <div key={idx} className={`hazard-item hazard-${hazard.severity?.toLowerCase() || "medium"}`}>
                        <div className="hazard-info">
                          <h4>{hazard.name}</h4>
                          <p className="hazard-location">📍 {hazard.location}</p>
                          <p className="hazard-confidence">Confidence: {(hazard.confidence * 100).toFixed(0)}%</p>
                        </div>
                        <span className="hazard-severity">{hazard.severity}</span>
                      </div>
                    ))}
                  </div>
                ) : (
                  <p className="no-hazards">No hazards detected - Site appears safe.</p>
                )}
              </div>

              {/* Recommendations */}
              <div className="recommendations-section">
                <h3>Recommendations</h3>
                <ul className="recommendations-list">
                  {result.recommendations?.map((rec, idx) => (
                    <li key={idx}>{rec}</li>
                  ))}
                </ul>
              </div>
            </div>
          ) : (
            <div className="empty-state">
              <p>{message}</p>
            </div>
          )}
        </section>
      </div>
    </AppShell>
  );
}

function DatasetMetric({ label, value, detail, tone }) {
  return (
    <article className={`dataset-metric dataset-metric-${tone}`}>
      <div className="dataset-metric-icon" aria-hidden="true" />
      <div>
        <p className="dataset-metric-label">{label}</p>
        <p className="dataset-metric-value">{Number(value ?? 0).toLocaleString()}</p>
        <p className="dataset-metric-detail">{detail}</p>
      </div>
    </article>
  );
}

export function PageHeader({ title, description }) {
  return (
    <div className="page-header">
      <div>
        <span className="eyebrow">BuildSure Workspace</span>
        <h1>{title}</h1>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default SafetyIntelligence;
