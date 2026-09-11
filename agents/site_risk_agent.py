from typing import Dict, Any, List


class SiteRiskAgent:
    """
    BuildSure AI - Site Risk Agent

    This agent:
    1. Reads site monitoring data
    2. Detects hazards
    3. Calculates risk score
    4. Generates recommendations
    5. Returns dashboard-ready data
    """

    def __init__(self):
        self.agent_name = "Site Risk Agent"
        self.status = "Active"
        self.last_result = None

    # =====================================================
    # RISK SCORE
    # =====================================================

    def calculate_risk_score(
        self,
        site_data: Dict[str, Any]
    ) -> int:

        environmental = float(
            site_data.get("environmentalRisk", 0)
        )

        equipment = float(
            site_data.get("equipmentRisk", 0)
        )

        worker = float(
            site_data.get("workerExposure", 0)
        )

        incidents = float(
            site_data.get("incidentHistory", 0)
        )

        score = (
            environmental * 0.25
            + equipment * 0.25
            + worker * 0.30
            + incidents * 0.20
        )

        return round(
            max(0, min(100, score))
        )

    # =====================================================
    # RISK LEVEL
    # =====================================================

    def get_risk_level(
        self,
        score: int
    ) -> str:

        if score >= 81:
            return "CRITICAL"

        if score >= 61:
            return "HIGH"

        if score >= 31:
            return "MEDIUM"

        return "LOW"

    # =====================================================
    # HAZARD DETECTION
    # =====================================================

    def detect_hazards(
        self,
        site_data: Dict[str, Any]
    ) -> List[Dict[str, Any]]:

        hazards = []

        temperature = float(
            site_data.get("temperature", 0)
        )

        humidity = float(
            site_data.get("humidity", 0)
        )

        equipment_risk = float(
            site_data.get("equipmentRisk", 0)
        )

        worker_exposure = float(
            site_data.get("workerExposure", 0)
        )

        previous_incidents = int(
            site_data.get("previousIncidents", 0)
        )

        # -------------------------------------------------
        # Temperature
        # -------------------------------------------------

        if temperature >= 40:

            hazards.append({
                "id": len(hazards) + 1,
                "name": "Extreme Temperature",
                "category": "Environmental",
                "severity": "CRITICAL",
                "zone": "Zone B",
                "description":
                    "Extreme heat conditions detected.",
                "status": "Detected"
            })

        elif temperature >= 38:

            hazards.append({
                "id": len(hazards) + 1,
                "name": "High Temperature",
                "category": "Environmental",
                "severity": "HIGH",
                "zone": "Zone B",
                "description":
                    "High temperature may increase heat exposure.",
                "status": "Detected"
            })

        # -------------------------------------------------
        # Humidity
        # -------------------------------------------------

        if humidity >= 85:

            hazards.append({
                "id": len(hazards) + 1,
                "name": "Extreme Humidity",
                "category": "Environmental",
                "severity": "HIGH",
                "zone": "Zone B",
                "description":
                    "Extreme humidity may increase heat stress.",
                "status": "Detected"
            })

        elif humidity >= 70:

            hazards.append({
                "id": len(hazards) + 1,
                "name": "High Humidity",
                "category": "Environmental",
                "severity": "MEDIUM",
                "zone": "Zone B",
                "description":
                    "High humidity requires monitoring.",
                "status": "Detected"
            })

        # -------------------------------------------------
        # Equipment
        # -------------------------------------------------

        if equipment_risk >= 81:

            hazards.append({
                "id": len(hazards) + 1,
                "name": "Critical Equipment Risk",
                "category": "Equipment",
                "severity": "CRITICAL",
                "zone": "Zone A",
                "description":
                    "Critical equipment safety risk detected.",
                "status": "Detected"
            })

        elif equipment_risk >= 61:

            hazards.append({
                "id": len(hazards) + 1,
                "name": "Heavy Equipment Risk",
                "category": "Equipment",
                "severity": "HIGH",
                "zone": "Zone A",
                "description":
                    "Equipment requires additional inspection.",
                "status": "Detected"
            })

        elif equipment_risk >= 31:

            hazards.append({
                "id": len(hazards) + 1,
                "name": "Equipment Condition Warning",
                "category": "Equipment",
                "severity": "MEDIUM",
                "zone": "Zone A",
                "description":
                    "Equipment requires routine inspection.",
                "status": "Detected"
            })

        # -------------------------------------------------
        # Worker Exposure
        # -------------------------------------------------

        if worker_exposure >= 81:

            hazards.append({
                "id": len(hazards) + 1,
                "name": "Critical Worker Exposure",
                "category": "Worker Safety",
                "severity": "CRITICAL",
                "zone": "Zone B",
                "description":
                    "Critical worker exposure detected.",
                "status": "Detected"
            })

        elif worker_exposure >= 61:

            hazards.append({
                "id": len(hazards) + 1,
                "name": "High Worker Exposure",
                "category": "Worker Safety",
                "severity": "HIGH",
                "zone": "Zone B",
                "description":
                    "High worker exposure detected.",
                "status": "Detected"
            })

        # -------------------------------------------------
        # Previous Incidents
        # -------------------------------------------------

        if previous_incidents > 0:

            severity = (
                "HIGH"
                if previous_incidents >= 5
                else "MEDIUM"
            )

            hazards.append({
                "id": len(hazards) + 1,
                "name": "Previous Safety Incidents",
                "category": "Incident",
                "severity": severity,
                "zone": "Zone C",
                "description":
                    "Previous safety incidents require review.",
                "status": "Detected"
            })

        return hazards

    # =====================================================
    # RECOMMENDATIONS
    # =====================================================

    def generate_recommendations(
        self,
        site_data: Dict[str, Any],
        hazards: List[Dict[str, Any]],
        risk_level: str
    ) -> List[str]:

        recommendations = []

        temperature = float(
            site_data.get("temperature", 0)
        )

        equipment_risk = float(
            site_data.get("equipmentRisk", 0)
        )

        worker_exposure = float(
            site_data.get("workerExposure", 0)
        )

        previous_incidents = int(
            site_data.get("previousIncidents", 0)
        )

        # Overall risk

        if risk_level == "CRITICAL":

            recommendations.append(
                "Immediate safety intervention is required."
            )

        elif risk_level == "HIGH":

            recommendations.append(
                "Increase safety monitoring in high-risk zones."
            )

        elif risk_level == "MEDIUM":

            recommendations.append(
                "Continue regular monitoring and preventive measures."
            )

        # Temperature

        if temperature >= 40:

            recommendations.append(
                "Restrict non-essential outdoor work during extreme heat."
            )

        elif temperature >= 38:

            recommendations.append(
                "Provide hydration, rest breaks, and heat monitoring."
            )

        # Equipment

        if equipment_risk >= 81:

            recommendations.append(
                "Immediately inspect high-risk equipment."
            )

        elif equipment_risk >= 61:

            recommendations.append(
                "Conduct additional equipment inspection and maintenance."
            )

        # Worker exposure

        if worker_exposure >= 81:

            recommendations.append(
                "Provide immediate safety supervision for exposed workers."
            )

        elif worker_exposure >= 61:

            recommendations.append(
                "Increase worker safety supervision."
            )

        # Incidents

        if previous_incidents > 0:

            recommendations.append(
                "Review previous incidents and implement corrective actions."
            )

        # Hazard categories

        categories = {
            hazard.get("category")
            for hazard in hazards
        }

        if "Environmental" in categories:

            recommendations.append(
                "Continue environmental monitoring across the site."
            )

        if "Equipment" in categories:

            recommendations.append(
                "Verify equipment inspection and maintenance records."
            )

        if "Worker Safety" in categories:

            recommendations.append(
                "Ensure workers follow safety procedures and use PPE."
            )

        # Remove duplicates

        recommendations = list(
            dict.fromkeys(recommendations)
        )

        if not recommendations:

            recommendations.append(
                "Continue routine construction-site monitoring."
            )

        return recommendations

    # =====================================================
    # RUN AGENT
    # =====================================================

    def run(
        self,
        site_data: Dict[str, Any]
    ) -> Dict[str, Any]:

        if not site_data:

            return {
                "agent": self.agent_name,
                "status": "No Data",
                "riskScore": 0,
                "riskLevel": "LOW",
                "hazards": [],
                "recommendations": []
            }

        # 1. Calculate risk

        risk_score = self.calculate_risk_score(
            site_data
        )

        # 2. Risk level

        risk_level = self.get_risk_level(
            risk_score
        )

        # 3. Detect hazards

        hazards = self.detect_hazards(
            site_data
        )

        # 4. Recommendations

        recommendations = self.generate_recommendations(
            site_data,
            hazards,
            risk_level
        )

        # 5. Hazard summary

        hazard_summary = {
            "total": len(hazards),
            "critical": 0,
            "high": 0,
            "medium": 0,
            "low": 0
        }

        for hazard in hazards:

            severity = hazard.get(
                "severity",
                "LOW"
            ).lower()

            if severity in hazard_summary:

                hazard_summary[severity] += 1

        # 6. Final result

        result = {

            "agent": self.agent_name,

            "status": self.status,

            "projectId": site_data.get(
                "projectId",
                "P001"
            ),

            "projectName": site_data.get(
                "projectName",
                "Construction Project"
            ),

            "location": site_data.get(
                "location",
                "Unknown"
            ),

            "riskScore": risk_score,

            "riskLevel": risk_level,

            "riskMessage":
                self.get_risk_message(
                    risk_level
                ),

            "monitoring": {

                "workers": site_data.get(
                    "workers",
                    0
                ),

                "equipment": site_data.get(
                    "equipment",
                    0
                ),

                "temperature": site_data.get(
                    "temperature",
                    0
                ),

                "humidity": site_data.get(
                    "humidity",
                    0
                ),

                "previousIncidents": site_data.get(
                    "previousIncidents",
                    0
                )
            },

            "riskFactors": {

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
            },

            "hazards": hazards,

            "hazardSummary": hazard_summary,

            "recommendations":
                recommendations
        }

        self.last_result = result

        return result

    # =====================================================
    # RISK MESSAGE
    # =====================================================

    def get_risk_message(
        self,
        risk_level: str
    ) -> str:

        messages = {

            "CRITICAL":
                "Critical site risk detected. Immediate action is required.",

            "HIGH":
                "High site risk detected. Additional monitoring is required.",

            "MEDIUM":
                "Moderate site risk detected. Continue preventive measures.",

            "LOW":
                "Low site risk detected. Continue routine monitoring."
        }

        return messages.get(
            risk_level,
            "Site risk analysis completed."
        )

    # =====================================================
    # LAST RESULT
    # =====================================================

    def get_last_result(self):

        return self.last_result


# =========================================================
# CREATE AGENT
# =========================================================

site_risk_agent = SiteRiskAgent()


# =========================================================
# API FUNCTION
# =========================================================

def run_site_risk_agent(
    site_data: Dict[str, Any]
) -> Dict[str, Any]:

    return site_risk_agent.run(
        site_data
    )


# =========================================================
# TEST
# =========================================================

if __name__ == "__main__":

    sample_data = {

        "projectId": "P001",

        "projectName":
            "ABC Construction Project",

        "location":
            "Hyderabad",

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

    result = run_site_risk_agent(
        sample_data
    )

    print("\n================================")
    print("SITE RISK AGENT RESULT")
    print("================================")

    print(
        "Project:",
        result["projectName"]
    )

    print(
        "Risk Score:",
        result["riskScore"]
    )

    print(
        "Risk Level:",
        result["riskLevel"]
    )

    print(
        "Hazards:",
        len(result["hazards"])
    )

    print("\nRecommendations:")

    for recommendation in result[
        "recommendations"
    ]:

        print(
            "-",
            recommendation
        )