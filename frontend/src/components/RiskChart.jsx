import React from "react";

const RiskChart = ({
  riskFactors = {}
}) => {

  const factors = [
    {
      name: "Environmental",
      value:
        Number(
          riskFactors.environmental
        ) || 0
    },

    {
      name: "Equipment",
      value:
        Number(
          riskFactors.equipment
        ) || 0
    },

    {
      name: "Worker Exposure",
      value:
        Number(
          riskFactors.workerExposure
        ) || 0
    },

    {
      name: "Incident History",
      value:
        Number(
          riskFactors.incidentHistory
        ) || 0
    }
  ];


  const getLevel = (value) => {

    if (value >= 81) {
      return "critical";
    }

    if (value >= 61) {
      return "high";
    }

    if (value >= 31) {
      return "medium";
    }

    return "low";
  };


  return (
    <div className="risk-chart-card">

      <div className="risk-chart-header">

        <div>

          <h2>
            Risk Factor Analysis
          </h2>

          <p>
            Contribution of individual
            site risk factors
          </p>

        </div>

        <div className="chart-icon">
          📊
        </div>

      </div>


      <div className="risk-chart">

        {factors.map((factor) => {

          const level =
            getLevel(factor.value);

          return (

            <div
              className="risk-chart-row"
              key={factor.name}
            >

              <div className="risk-chart-label">

                <span>
                  {factor.name}
                </span>

                <strong>
                  {factor.value}/100
                </strong>

              </div>


              <div className="risk-chart-bar-background">

                <div
                  className={
                    `risk-chart-bar ${level}`
                  }
                  style={{
                    width:
                      `${factor.value}%`
                  }}
                />

              </div>


              <div
                className={
                  `risk-chart-level ${level}`
                }
              >
                {level.toUpperCase()}
              </div>

            </div>

          );
        })}

      </div>


      <div className="risk-chart-legend">

        <div>
          <span className="legend-dot low" />
          LOW
        </div>

        <div>
          <span className="legend-dot medium" />
          MEDIUM
        </div>

        <div>
          <span className="legend-dot high" />
          HIGH
        </div>

        <div>
          <span className="legend-dot critical" />
          CRITICAL
        </div>

      </div>

    </div>
  );
};

export default RiskChart;