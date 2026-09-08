import React from "react";

const HazardTable = ({
  hazards = []
}) => {

  const criticalCount =
    hazards.filter(
      (hazard) =>
        hazard?.severity?.toUpperCase() ===
        "CRITICAL"
    ).length;


  const highCount =
    hazards.filter(
      (hazard) =>
        hazard?.severity?.toUpperCase() ===
        "HIGH"
    ).length;


  const mediumCount =
    hazards.filter(
      (hazard) =>
        hazard?.severity?.toUpperCase() ===
        "MEDIUM"
    ).length;


  const lowCount =
    hazards.filter(
      (hazard) =>
        hazard?.severity?.toUpperCase() ===
        "LOW"
    ).length;


  const getIcon = (severity) => {

    switch (
      severity?.toUpperCase()
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
    <div className="hazard-table-container">

      <div className="hazard-table-header">

        <div>

          <h2>
            Detected Hazards
          </h2>

          <p>
            Hazards identified by the
            Site Risk Agent
          </p>

        </div>


        <div className="hazard-count">

          {hazards.length}{" "}

          {hazards.length === 1
            ? "Hazard"
            : "Hazards"}

        </div>

      </div>


      {hazards.length === 0 ? (

        <div className="no-hazards">

          <div className="safe-icon">
            ✓
          </div>

          <div>

            <h3>
              No Hazards Detected
            </h3>

            <p>
              The Site Risk Agent has not
              detected any active hazards.
            </p>

          </div>

        </div>

      ) : (

        <div className="table-responsive">

          <table className="hazard-table">

            <thead>

              <tr>
                <th>#</th>
                <th>Hazard</th>
                <th>Category</th>
                <th>Severity</th>
                <th>Zone</th>
                <th>Status</th>
              </tr>

            </thead>


            <tbody>

              {hazards.map(
                (hazard, index) => {

                  const severity =
                    hazard?.severity?.toUpperCase() ||
                    "LOW";

                  return (

                    <tr
                      key={
                        hazard?.id ??
                        index
                      }
                    >

                      <td>
                        {index + 1}
                      </td>


                      <td>

                        <div className="hazard-name">

                          <span>
                            {getIcon(
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

                      </td>


                      <td>
                        {
                          hazard?.category ||
                          "General"
                        }
                      </td>


                      <td>

                        <span
                          className={
                            `severity-badge ${
                              severity.toLowerCase()
                            }`
                          }
                        >
                          {severity}
                        </span>

                      </td>


                      <td>
                        📍{" "}
                        {
                          hazard?.zone ||
                          "Unknown"
                        }
                      </td>


                      <td>

                        <span className="hazard-detected">
                          ●{" "}
                          {
                            hazard?.status ||
                            "Detected"
                          }
                        </span>

                      </td>

                    </tr>

                  );
                }
              )}

            </tbody>

          </table>

        </div>

      )}


      <div className="hazard-summary">

        <div>
          🔴 {criticalCount} Critical
        </div>

        <div>
          🟠 {highCount} High
        </div>

        <div>
          🟡 {mediumCount} Medium
        </div>

        <div>
          🟢 {lowCount} Low
        </div>

      </div>

    </div>
  );
};

export default HazardTable;