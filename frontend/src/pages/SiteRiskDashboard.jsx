import React, { useEffect, useState } from "react";

const API_URL = "http://localhost:8000";

function SiteRiskDashboard() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    const fetchSiteRisk = async () => {
      try {
        setLoading(true);
        setError("");

        const response = await fetch(
          `${API_URL}/site-risk/P001`
        );

        if (!response.ok) {
          throw new Error(
            `Backend returned status ${response.status}`
          );
        }

        const result = await response.json();
        setData(result);
      } catch (err) {
        console.error("Site Risk Error:", err);

        setError(
          "Unable to connect to the FastAPI backend."
        );
      } finally {
        setLoading(false);
      }
    };

    fetchSiteRisk();
  }, []);

  if (loading) {
    return (
      <div style={styles.loadingPage}>
        <div style={styles.loadingBox}>
          <div style={styles.loadingIcon}>🤖</div>

          <h2>BuildSure AI</h2>

          <p>
            Loading construction site risk data...
          </p>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div style={styles.errorPage}>
        <div style={styles.errorBox}>
          <div style={styles.errorIcon}>⚠️</div>

          <h2>Backend Connection Error</h2>

          <p>{error}</p>

          <p>
            Make sure the FastAPI backend is running:
          </p>

          <code>
            python -m uvicorn main:app --reload
          </code>

          <br />

          <button
            onClick={() => window.location.reload()}
            style={styles.retryButton}
          >
            Retry
          </button>
        </div>
      </div>
    );
  }

  const riskScore = Number(data?.riskScore || 0);

  const riskLevel = String(
    data?.riskLevel || "LOW"
  ).toUpperCase();

  const monitoring = data?.monitoring || {};

  const riskFactors = data?.riskFactors || {};

  const hazards = Array.isArray(data?.hazards)
    ? data.hazards
    : [];

  const recommendations = Array.isArray(
    data?.recommendations
  )
    ? data.recommendations
    : [];

  const getRiskColor = (level) => {
    switch (level) {
      case "CRITICAL":
        return "#dc2626";

      case "HIGH":
        return "#f97316";

      case "MEDIUM":
        return "#eab308";

      default:
        return "#16a34a";
    }
  };

  const riskColor = getRiskColor(riskLevel);

  const getFactorLevel = (value) => {
    const number = Number(value || 0);

    if (number >= 81) {
      return "CRITICAL";
    }

    if (number >= 61) {
      return "HIGH";
    }

    if (number >= 31) {
      return "MEDIUM";
    }

    return "LOW";
  };

  const getHazardIcon = (severity) => {
    switch (
      String(severity || "").toUpperCase()
    ) {
      case "CRITICAL":
        return "🔴";

      case "HIGH":
        return "🟠";

      case "MEDIUM":
        return "🟡";

      case "LOW":
        return "🟢";

      default:
        return "⚪";
    }
  };

  return (
    <div style={styles.page}>

      {/* HEADER */}
      <header style={styles.header}>

        <div>
          <h1 style={styles.logo}>
            BuildSure AI
          </h1>

          <p style={styles.subtitle}>
            Construction Site Risk Monitoring
          </p>
        </div>

        <div style={styles.projectInfo}>

          <strong>
            {data?.projectName ||
              "ABC Construction Project"}
          </strong>

          <span>
            📍 {data?.location || "Hyderabad"}
          </span>

        </div>

      </header>

      {/* MAIN CONTENT */}
      <main style={styles.main}>

        {/* TOP SECTION */}
        <section style={styles.topGrid}>

          {/* RISK SCORE */}
          <div style={styles.card}>

            <div style={styles.cardHeader}>

              <div>
                <h2 style={styles.cardTitle}>
                  Overall Site Risk
                </h2>

                <p style={styles.cardSubtitle}>
                  Site Risk Agent Analysis
                </p>
              </div>

              <span style={styles.headerIcon}>
                ⚠️
              </span>

            </div>

            <div style={styles.scoreArea}>

              <div>

                <span
                  style={{
                    ...styles.score,
                    color: riskColor
                  }}
                >
                  {riskScore}
                </span>

                <span style={styles.scoreMax}>
                  /100
                </span>

              </div>

              <span
                style={{
                  ...styles.badge,
                  backgroundColor:
                    `${riskColor}20`,
                  color: riskColor
                }}
              >
                {riskLevel}
              </span>

            </div>

            <div style={styles.progressBackground}>

              <div
                style={{
                  ...styles.progressBar,
                  width: `${Math.min(
                    100,
                    Math.max(0, riskScore)
                  )}%`,
                  backgroundColor: riskColor
                }}
              />

            </div>

            <p style={styles.description}>

              {riskLevel === "CRITICAL" &&
                "⚠️ Critical risk detected. Immediate action is required."}

              {riskLevel === "HIGH" &&
                "⚠️ High site risk detected. Additional monitoring is recommended."}

              {riskLevel === "MEDIUM" &&
                "Site has moderate risks. Continue regular monitoring."}

              {riskLevel === "LOW" &&
                "Site risk is currently low. Continue routine monitoring."}

            </p>

            <div style={styles.footer}>

              <span>
                Risk Monitoring
              </span>

              <strong style={styles.active}>
                ● Active
              </strong>

            </div>

          </div>

          {/* SITE MONITORING */}
          <div style={styles.card}>

            <h2 style={styles.cardTitle}>
              Site Monitoring
            </h2>

            <p style={styles.cardSubtitle}>
              Current construction-site conditions
            </p>

            <div style={styles.monitorGrid}>

              <MonitoringItem
                icon="👷"
                label="Workers"
                value={
                  monitoring.workers ?? 0
                }
              />

              <MonitoringItem
                icon="🚜"
                label="Equipment"
                value={
                  monitoring.equipment ?? 0
                }
              />

              <MonitoringItem
                icon="🌡️"
                label="Temperature"
                value={`${monitoring.temperature ?? 0}°C`}
              />

              <MonitoringItem
                icon="💧"
                label="Humidity"
                value={`${monitoring.humidity ?? 0}%`}
              />

              <MonitoringItem
                icon="⚠️"
                label="Previous Incidents"
                value={
                  monitoring.previousIncidents ?? 0
                }
              />

            </div>

          </div>

        </section>

        {/* RISK FACTOR ANALYSIS */}
        <section style={styles.card}>

          <div style={styles.cardHeader}>

            <div>

              <h2 style={styles.cardTitle}>
                Risk Factor Analysis
              </h2>

              <p style={styles.cardSubtitle}>
                Contribution of individual risk factors
              </p>

            </div>

            <span style={styles.headerIcon}>
              📊
            </span>

          </div>

          <div style={styles.factorList}>

            <RiskFactor
              name="Environmental Risk"
              value={
                riskFactors.environmental ?? 0
              }
              level={getFactorLevel(
                riskFactors.environmental
              )}
            />

            <RiskFactor
              name="Equipment Risk"
              value={
                riskFactors.equipment ?? 0
              }
              level={getFactorLevel(
                riskFactors.equipment
              )}
            />

            <RiskFactor
              name="Worker Exposure"
              value={
                riskFactors.workerExposure ?? 0
              }
              level={getFactorLevel(
                riskFactors.workerExposure
              )}
            />

            <RiskFactor
              name="Incident History"
              value={
                riskFactors.incidentHistory ?? 0
              }
              level={getFactorLevel(
                riskFactors.incidentHistory
              )}
            />

          </div>

        </section>

        {/* DETECTED HAZARDS */}
        <section style={styles.card}>

          <div style={styles.cardHeader}>

            <div>

              <h2 style={styles.cardTitle}>
                Detected Hazards
              </h2>

              <p style={styles.cardSubtitle}>
                Hazards identified by the Site Risk Agent
              </p>

            </div>

            <span style={styles.hazardCount}>
              {hazards.length}{" "}
              {hazards.length === 1
                ? "Hazard"
                : "Hazards"}
            </span>

          </div>

          {hazards.length === 0 ? (

            <div style={styles.emptyState}>

              <div style={styles.safeIcon}>
                ✓
              </div>

              <div>

                <h3 style={styles.emptyTitle}>
                  No Hazards Detected
                </h3>

                <p style={styles.emptyText}>
                  The Site Risk Agent has not detected
                  any active hazards.
                </p>

              </div>

            </div>

          ) : (

            <div style={styles.hazardList}>

              {hazards.map(
                (hazard, index) => {

                  const severity =
                    String(
                      hazard?.severity ||
                      "LOW"
                    ).toUpperCase();

                  const severityColor =
                    getRiskColor(
                      severity
                    );

                  return (
                    <div
                      key={
                        hazard?.id ??
                        index
                      }
                      style={styles.hazardItem}
                    >

                      <div
                        style={
                          styles.hazardNumber
                        }
                      >
                        {index + 1}
                      </div>

                      <div
                        style={
                          styles.hazardMain
                        }
                      >

                        <div
                          style={
                            styles.hazardTitle
                          }
                        >

                          <span>
                            {getHazardIcon(
                              severity
                            )}
                          </span>

                          <strong>
                            {
                              hazard?.name ||
                              "Unknown Hazard"
                            }
                          </strong>

                        </div>

                        <div
                          style={
                            styles.hazardDetails
                          }
                        >

                          <span>
                            Category:{" "}
                            {
                              hazard?.category ||
                              "General"
                            }
                          </span>

                          <span>
                            Zone:{" "}
                            {
                              hazard?.zone ||
                              "Unknown"
                            }
                          </span>

                        </div>

                      </div>

                      <span
                        style={{
                          ...styles.severityBadge,
                          color:
                            severityColor,
                          backgroundColor:
                            `${severityColor}20`
                        }}
                      >
                        {severity}
                      </span>

                    </div>
                  );
                }
              )}

            </div>

          )}

        </section>

        {/* AI RECOMMENDATIONS */}
        <section style={styles.card}>

          <div
            style={{
              display: "flex",
              alignItems: "center",
              gap: "12px",
              marginBottom: "20px"
            }}
          >

            <div style={styles.aiIcon}>
              🤖
            </div>

            <div>

              <h2 style={styles.cardTitle}>
                AI Risk Recommendations
              </h2>

              <p style={styles.cardSubtitle}>
                Recommendations generated by the
                Site Risk Agent
              </p>

            </div>

          </div>

          {recommendations.length === 0 ? (

            <div style={styles.emptyState}>

              <div style={styles.safeIcon}>
                ✓
              </div>

              <div>

                <h3 style={styles.emptyTitle}>
                  No Immediate Action Required
                </h3>

                <p style={styles.emptyText}>
                  No additional recommendations
                  have been generated.
                </p>

              </div>

            </div>

          ) : (

            <div>

              {recommendations.map(
                (recommendation, index) => {

                  let message =
                    recommendation;

                  if (
                    typeof recommendation ===
                    "object" &&
                    recommendation !== null
                  ) {
                    message =
                      recommendation.message ||
                      "Safety recommendation";
                  }

                  return (
                    <div
                      key={index}
                      style={
                        styles.recommendation
                      }
                    >

                      <div
                        style={
                          styles.recommendationNumber
                        }
                      >
                        {index + 1}
                      </div>

                      <p
                        style={
                          styles.recommendationText
                        }
                      >
                        {message}
                      </p>

                    </div>
                  );
                }
              )}

            </div>

          )}

          <div style={styles.footer}>

            <span>
              AI Analysis Status
            </span>

            <strong style={styles.active}>
              ● Active
            </strong>

          </div>

        </section>

      </main>

    </div>
  );
}


/* =========================================================
   MONITORING ITEM
========================================================= */

function MonitoringItem({
  icon,
  label,
  value
}) {
  return (
    <div style={styles.monitorItem}>

      <span style={styles.monitorIcon}>
        {icon}
      </span>

      <div>

        <span style={styles.monitorLabel}>
          {label}
        </span>

        <strong style={styles.monitorValue}>
          {value}
        </strong>

      </div>

    </div>
  );
}


/* =========================================================
   RISK FACTOR
========================================================= */

function RiskFactor({
  name,
  value,
  level
}) {
  const number = Math.min(
    100,
    Math.max(
      0,
      Number(value || 0)
    )
  );

  const getColor = () => {

    switch (level) {

      case "CRITICAL":
        return "#dc2626";

      case "HIGH":
        return "#f97316";

      case "MEDIUM":
        return "#eab308";

      default:
        return "#16a34a";
    }
  };

  const color = getColor();

  return (
    <div style={styles.factorRow}>

      <div style={styles.factorLabel}>

        <strong>
          {name}
        </strong>

        <span
          style={{
            color: "#6b7280"
          }}
        >
          {number}/100
        </span>

      </div>

      <div
        style={
          styles.factorBarBackground
        }
      >

        <div
          style={{
            ...styles.factorBar,
            width: `${number}%`,
            backgroundColor: color
          }}
        />

      </div>

      <span
        style={{
          ...styles.factorLevel,
          color: color
        }}
      >
        {level}
      </span>

    </div>
  );
}


/* =========================================================
   STYLES
========================================================= */

const styles = {

  page: {
    minHeight: "100vh",
    background: "#f5f7fa",
    color: "#111827",
    fontFamily:
      "Arial, Helvetica, sans-serif"
  },

  header: {
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
    padding: "24px 40px",
    background: "#ffffff",
    borderBottom:
      "1px solid #e5e7eb"
  },

  logo: {
    margin: "0 0 6px",
    fontSize: "28px",
    fontWeight: "700"
  },

  subtitle: {
    margin: 0,
    color: "#6b7280",
    fontSize: "14px"
  },

  projectInfo: {
    display: "flex",
    flexDirection: "column",
    alignItems: "flex-end",
    gap: "5px",
    fontSize: "14px"
  },

  main: {
    maxWidth: "1200px",
    margin: "0 auto",
    padding: "30px 40px"
  },

  topGrid: {
    display: "grid",
    gridTemplateColumns:
      "repeat(2, minmax(0, 1fr))",
    gap: "24px",
    marginBottom: "24px"
  },

  card: {
    background: "#ffffff",
    border:
      "1px solid #e5e7eb",
    borderRadius: "14px",
    padding: "25px",
    marginBottom: "24px"
  },

  cardHeader: {
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center"
  },

  cardTitle: {
    margin: "0 0 5px",
    fontSize: "20px",
    color: "#111827"
  },

  cardSubtitle: {
    margin: 0,
    color: "#6b7280",
    fontSize: "13px"
  },

  headerIcon: {
    fontSize: "28px"
  },

  scoreArea: {
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
    margin: "25px 0 18px"
  },

  score: {
    fontSize: "48px",
    fontWeight: "700"
  },

  scoreMax: {
    marginLeft: "5px",
    color: "#9ca3af",
    fontSize: "18px"
  },

  badge: {
    padding: "7px 14px",
    borderRadius: "20px",
    fontSize: "12px",
    fontWeight: "700"
  },

  progressBackground: {
    width: "100%",
    height: "12px",
    background: "#e5e7eb",
    borderRadius: "10px",
    overflow: "hidden"
  },

  progressBar: {
    height: "100%",
    borderRadius: "10px",
    transition:
      "width 0.5s ease"
  },

  description: {
    margin:
      "18px 0 0",
    color: "#4b5563",
    fontSize: "13px",
    lineHeight: "1.5"
  },

  footer: {
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
    marginTop: "20px",
    paddingTop: "15px",
    borderTop:
      "1px solid #e5e7eb",
    color: "#6b7280",
    fontSize: "12px"
  },

  active: {
    color: "#15803d"
  },

  monitorGrid: {
    display: "grid",
    gridTemplateColumns:
      "repeat(2, minmax(0, 1fr))",
    gap: "14px",
    marginTop: "20px"
  },

  monitorItem: {
    display: "flex",
    alignItems: "center",
    gap: "12px",
    padding: "15px",
    background: "#f9fafb",
    border:
      "1px solid #e5e7eb",
    borderRadius: "10px"
  },

  monitorIcon: {
    fontSize: "24px"
  },

  monitorLabel: {
    display: "block",
    marginBottom: "4px",
    color: "#6b7280",
    fontSize: "12px"
  },

  monitorValue: {
    display: "block",
    color: "#111827",
    fontSize: "20px"
  },

  factorList: {
    display: "flex",
    flexDirection: "column",
    gap: "20px",
    marginTop: "20px"
  },

  factorRow: {
    display: "grid",
    gridTemplateColumns:
      "200px 1fr 90px",
    alignItems: "center",
    gap: "15px"
  },

  factorLabel: {
    display: "flex",
    flexDirection: "column",
    gap: "4px",
    fontSize: "13px"
  },

  factorBarBackground: {
    height: "14px",
    background: "#e5e7eb",
    borderRadius: "10px",
    overflow: "hidden"
  },

  factorBar: {
    height: "100%",
    borderRadius: "10px",
    transition:
      "width 0.5s ease"
  },

  factorLevel: {
    textAlign: "center",
    fontSize: "11px",
    fontWeight: "700"
  },

  hazardCount: {
    padding: "8px 14px",
    background: "#f3f4f6",
    borderRadius: "20px",
    fontSize: "12px",
    fontWeight: "600"
  },

  hazardList: {
    display: "flex",
    flexDirection: "column",
    marginTop: "10px"
  },

  hazardItem: {
    display: "flex",
    alignItems: "center",
    gap: "15px",
    padding: "16px 0",
    borderTop:
      "1px solid #e5e7eb"
  },

  hazardNumber: {
    width: "30px",
    height: "30px",
    flexShrink: 0,
    borderRadius: "50%",
    background: "#f3f4f6",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    fontSize: "12px",
    fontWeight: "700"
  },

  hazardMain: {
    flex: 1
  },

  hazardTitle: {
    display: "flex",
    alignItems: "center",
    gap: "8px",
    marginBottom: "6px"
  },

  hazardDetails: {
    display: "flex",
    flexWrap: "wrap",
    gap: "20px",
    color: "#6b7280",
    fontSize: "12px"
  },

  severityBadge: {
    padding: "6px 10px",
    borderRadius: "15px",
    fontSize: "10px",
    fontWeight: "700"
  },

  emptyState: {
    display: "flex",
    alignItems: "center",
    gap: "15px",
    padding: "25px 0",
    borderTop:
      "1px solid #e5e7eb"
  },

  safeIcon: {
    width: "42px",
    height: "42px",
    flexShrink: 0,
    borderRadius: "50%",
    background: "#dcfce7",
    color: "#15803d",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    fontWeight: "700"
  },

  emptyTitle: {
    margin: "0 0 5px",
    fontSize: "15px"
  },

  emptyText: {
    margin: 0,
    color: "#6b7280",
    fontSize: "13px"
  },

  aiIcon: {
    width: "48px",
    height: "48px",
    flexShrink: 0,
    borderRadius: "12px",
    background: "#f3f4f6",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    fontSize: "25px"
  },

  recommendation: {
    display: "flex",
    alignItems: "flex-start",
    gap: "15px",
    padding: "15px 0",
    borderTop:
      "1px solid #e5e7eb"
  },

  recommendationNumber: {
    width: "30px",
    minWidth: "30px",
    height: "30px",
    borderRadius: "50%",
    background: "#f3f4f6",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    fontSize: "13px",
    fontWeight: "700"
  },

  recommendationText: {
    margin: "5px 0",
    color: "#374151",
    fontSize: "14px",
    lineHeight: "1.5"
  },

  loadingPage: {
    minHeight: "100vh",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    background: "#f5f7fa"
  },

  loadingBox: {
    padding: "40px",
    textAlign: "center"
  },

  loadingIcon: {
    fontSize: "45px",
    marginBottom: "15px"
  },

  errorPage: {
    minHeight: "100vh",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    padding: "20px",
    background: "#f5f7fa"
  },

  errorBox: {
    width: "100%",
    maxWidth: "550px",
    padding: "35px",
    background: "#ffffff",
    border:
      "1px solid #e5e7eb",
    borderRadius: "14px",
    textAlign: "center"
  },

  errorIcon: {
    fontSize: "45px",
    marginBottom: "10px"
  },

  retryButton: {
    marginTop: "20px",
    padding: "10px 20px",
    border: "none",
    borderRadius: "8px",
    background: "#111827",
    color: "#ffffff",
    cursor: "pointer"
  }

};

export default SiteRiskDashboard;