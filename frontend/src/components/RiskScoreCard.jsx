import React from "react";

const RiskScoreCard = ({
  score = 0,
  level = ""
}) => {

  const numericScore = Number(score);

  const riskScore = Number.isFinite(
    numericScore
  )
    ? Math.min(
        100,
        Math.max(0, numericScore)
      )
    : 0;


  const getRiskLevel = () => {

    if (riskScore >= 81) {
      return "CRITICAL";
    }

    if (riskScore >= 61) {
      return "HIGH";
    }

    if (riskScore >= 31) {
      return "MEDIUM";
    }

    return "LOW";
  };


  const riskLevel =
    typeof level === "string" &&
    level.trim()
      ? level.toUpperCase()
      : getRiskLevel();


  return (
    <div className="risk-score-card">

      <div className="risk-score-header">

        <div>

          <p className="risk-score-title">
            Overall Site Risk
          </p>

          <p className="risk-score-subtitle">
            Site Risk Agent Analysis
          </p>

        </div>

        <div className="risk-score-icon">
          ⚠️
        </div>

      </div>


      <div className="risk-score-content">

        <div className="risk-score-number">

          {riskScore}

          <span>
            /100
          </span>

        </div>


        <span
          className={
            `risk-level-badge ${
              riskLevel.toLowerCase()
            }`
          }
        >
          {riskLevel}
        </span>

      </div>


      <div className="risk-score-progress">

        <div
          className={
            `risk-score-progress-bar ${
              riskLevel.toLowerCase()
            }`
          }
          style={{
            width: `${riskScore}%`
          }}
        />

      </div>


      <div className="risk-score-description">

        {riskLevel === "CRITICAL" && (
          <p>
            ⚠️ Critical risk detected.
            Immediate action is required.
          </p>
        )}

        {riskLevel === "HIGH" && (
          <p>
            ⚠️ High site risk detected.
            Additional monitoring is recommended.
          </p>
        )}

        {riskLevel === "MEDIUM" && (
          <p>
            Site has moderate risks.
            Continue regular monitoring.
          </p>
        )}

        {riskLevel === "LOW" && (
          <p>
            Site risk is currently low.
            Continue routine monitoring.
          </p>
        )}

      </div>


      <div className="risk-score-footer">

        <span>
          Risk Monitoring
        </span>

        <strong>
          ● Active
        </strong>

      </div>

    </div>
  );
};

export default RiskScoreCard;