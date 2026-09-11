from typing import Dict, Any, List


# =========================================================
# RISK LEVELS
# =========================================================

LOW = "LOW"
MEDIUM = "MEDIUM"
HIGH = "HIGH"
CRITICAL = "CRITICAL"


# =========================================================
# RISK WEIGHTS
# =========================================================
#
# The total weight = 100%
#
# Environmental Risk  -> 25%
# Equipment Risk      -> 25%
# Worker Exposure     -> 30%
# Incident History    -> 20%
#
# These weights can later be adjusted based on the
# actual Kaggle datasets and ML model.
# =========================================================

RISK_WEIGHTS = {

    "environmental": 0.25,

    "equipment": 0.25,

    "workerExposure": 0.30,

    "incidentHistory": 0.20

}


# =========================================================
# VALIDATE RISK VALUE
# =========================================================

def validate_risk_value(value: Any) -> float:
    """
    Convert a risk value into a number between 0 and 100.
    """

    try:

        value = float(value)

    except (TypeError, ValueError):

        value = 0


    # Keep value within 0-100

    value = max(
        0,
        min(100, value)
    )


    return value


# =========================================================
# GET RISK LEVEL
# =========================================================

def get_risk_level(score: float) -> str:
    """
    Convert the numerical risk score into a risk level.
    """

    score = validate_risk_value(score)


    if score >= 81:

        return CRITICAL


    elif score >= 61:

        return HIGH


    elif score >= 31:

        return MEDIUM


    return LOW


# =========================================================
# CALCULATE RISK SCORE
# =========================================================

def calculate_risk_score(
    risk_factors: Dict[str, Any]
) -> int:
    """
    Calculate the overall site risk score.

    Formula:

    Overall Risk =
        Environmental × 25%
        +
        Equipment × 25%
        +
        Worker Exposure × 30%
        +
        Incident History × 20%
    """

    environmental = validate_risk_value(
        risk_factors.get(
            "environmental",
            0
        )
    )


    equipment = validate_risk_value(
        risk_factors.get(
            "equipment",
            0
        )
    )


    worker_exposure = validate_risk_value(
        risk_factors.get(
            "workerExposure",
            0
        )
    )


    incident_history = validate_risk_value(
        risk_factors.get(
            "incidentHistory",
            0
        )
    )


    # -----------------------------------------------------
    # Weighted calculation
    # -----------------------------------------------------

    score = (

        environmental
        * RISK_WEIGHTS["environmental"]

        +

        equipment
        * RISK_WEIGHTS["equipment"]

        +

        worker_exposure
        * RISK_WEIGHTS["workerExposure"]

        +

        incident_history
        * RISK_WEIGHTS["incidentHistory"]

    )


    return round(score)


# =========================================================
# CALCULATE RISK FACTOR CONTRIBUTIONS
# =========================================================

def calculate_contributions(
    risk_factors: Dict[str, Any]
) -> Dict[str, float]:
    """
    Calculate how much each factor contributes to the
    final risk score.
    """

    contributions = {}


    for factor, weight in RISK_WEIGHTS.items():

        value = validate_risk_value(
            risk_factors.get(
                factor,
                0
            )
        )


        contributions[factor] = round(
            value * weight,
            2
        )


    return contributions


# =========================================================
# FIND MAIN RISK FACTORS
# =========================================================

def get_top_risk_factors(
    risk_factors: Dict[str, Any],
    limit: int = 3
) -> List[Dict[str, Any]]:
    """
    Return the highest contributing risk factors.
    """

    contributions = calculate_contributions(
        risk_factors
    )


    factor_names = {

        "environmental":
            "Environmental Risk",

        "equipment":
            "Equipment Risk",

        "workerExposure":
            "Worker Exposure",

        "incidentHistory":
            "Incident History"

    }


    results = []


    for factor, contribution in contributions.items():

        results.append({

            "factor": factor_names.get(
                factor,
                factor
            ),

            "value": validate_risk_value(
                risk_factors.get(
                    factor,
                    0
                )
            ),

            "weight": (
                RISK_WEIGHTS[factor] * 100
            ),

            "contribution": contribution

        })


    # Sort highest contribution first

    results.sort(
        key=lambda item:
            item["contribution"],
        reverse=True
    )


    return results[:limit]


# =========================================================
# GENERATE RISK MESSAGE
# =========================================================

def generate_risk_message(
    score: int,
    level: str
) -> str:
    """
    Generate a simple explanation of the overall risk.
    """

    if level == CRITICAL:

        return (
            "Critical site risk detected. "
            "Immediate safety intervention is required."
        )


    if level == HIGH:

        return (
            "High site risk detected. "
            "Additional monitoring and preventive action "
            "are recommended."
        )


    if level == MEDIUM:

        return (
            "Moderate site risk detected. "
            "Continue regular monitoring and preventive measures."
        )


    return (
        "Low site risk detected. "
        "Continue routine site monitoring."
    )


# =========================================================
# COMPLETE RISK ANALYSIS
# =========================================================

def analyze_risk(
    risk_factors: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Perform complete site risk analysis.
    """

    # -----------------------------------------------------
    # Calculate score
    # -----------------------------------------------------

    score = calculate_risk_score(
        risk_factors
    )


    # -----------------------------------------------------
    # Determine level
    # -----------------------------------------------------

    level = get_risk_level(
        score
    )


    # -----------------------------------------------------
    # Calculate contributions
    # -----------------------------------------------------

    contributions = calculate_contributions(
        risk_factors
    )


    # -----------------------------------------------------
    # Find top risk factors
    # -----------------------------------------------------

    top_factors = get_top_risk_factors(
        risk_factors
    )


    # -----------------------------------------------------
    # Generate explanation
    # -----------------------------------------------------

    message = generate_risk_message(
        score,
        level
    )


    return {

        "riskScore": score,

        "riskLevel": level,

        "message": message,

        "contributions": contributions,

        "topRiskFactors": top_factors

    }


# =========================================================
# COMPLETE SITE RISK SCORING
# =========================================================

def calculate_site_risk(
    site_data: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Calculate risk directly from processed site data.

    Expected input:

    {
        "environmentalRisk": 75,
        "equipmentRisk": 65,
        "workerExposure": 80,
        "incidentHistory": 70
    }
    """

    risk_factors = {

        "environmental":
            site_data.get(
                "environmentalRisk",
                0
            ),

        "equipment":
            site_data.get(
                "equipmentRisk",
                0
            ),

        "workerExposure":
            site_data.get(
                "workerExposure",
                0
            ),

        "incidentHistory":
            site_data.get(
                "incidentHistory",
                0
            )

    }


    result = analyze_risk(
        risk_factors
    )


    # Add original monitoring information

    result["monitoring"] = {

        "workers":
            site_data.get(
                "workers",
                0
            ),

        "equipment":
            site_data.get(
                "equipment",
                0
            ),

        "temperature":
            site_data.get(
                "temperature",
                0
            ),

        "humidity":
            site_data.get(
                "humidity",
                0
            ),

        "previousIncidents":
            site_data.get(
                "previousIncidents",
                0
            )

    }


    result["riskFactors"] = risk_factors


    return result


# =========================================================
# GENERATE RISK SCORE SUMMARY
# =========================================================

def get_risk_summary(
    risk_result: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Create a compact summary for the dashboard.
    """

    return {

        "score":
            risk_result.get(
                "riskScore",
                0
            ),

        "level":
            risk_result.get(
                "riskLevel",
                LOW
            ),

        "message":
            risk_result.get(
                "message",
                ""
            ),

        "topFactors":
            risk_result.get(
                "topRiskFactors",
                []
            )

    }


# =========================================================
# TEST
# =========================================================

if __name__ == "__main__":

    print(
        "\n========================================"
    )

    print(
        "BuildSure AI - Risk Scoring"
    )

    print(
        "========================================\n"
    )


    # -----------------------------------------------------
    # Sample processed data
    # -----------------------------------------------------

    sample_data = {

        "workers": 185,

        "equipment": 24,

        "temperature": 39,

        "humidity": 72,

        "previousIncidents": 4,

        "environmentalRisk": 75,

        "equipmentRisk": 65,

        "workerExposure": 80,

        "incidentHistory": 70

    }


    # -----------------------------------------------------
    # Calculate risk
    # -----------------------------------------------------

    result = calculate_site_risk(
        sample_data
    )


    # -----------------------------------------------------
    # Display result
    # -----------------------------------------------------

    print(
        f"Risk Score : {result['riskScore']}/100"
    )

    print(
        f"Risk Level : {result['riskLevel']}"
    )

    print(
        f"Message    : {result['message']}"
    )


    # -----------------------------------------------------
    # Display risk factors
    # -----------------------------------------------------

    print(
        "\nRisk Factors:"
    )


    for factor, value in result[
        "riskFactors"
    ].items():

        print(
            f"  {factor}: {value}"
        )


    # -----------------------------------------------------
    # Display contributions
    # -----------------------------------------------------

    print(
        "\nRisk Contributions:"
    )


    for factor, value in result[
        "contributions"
    ].items():

        print(
            f"  {factor}: {value}"
        )


    # -----------------------------------------------------
    # Display top factors
    # -----------------------------------------------------

    print(
        "\nTop Risk Factors:"
    )


    for factor in result[
        "topRiskFactors"
    ]:

        print(

            f"  {factor['factor']} "
            f"({factor['value']}/100) "
            f"- contribution: "
            f"{factor['contribution']}"

        )