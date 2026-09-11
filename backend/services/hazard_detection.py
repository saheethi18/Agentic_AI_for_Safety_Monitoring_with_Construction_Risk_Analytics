import pandas as pd
from typing import List, Dict, Any


# =========================================================
# HAZARD SEVERITY LEVELS
# =========================================================

CRITICAL = "CRITICAL"
HIGH = "HIGH"
MEDIUM = "MEDIUM"
LOW = "LOW"


# =========================================================
# HAZARD DETECTION CLASS
# =========================================================

class HazardDetector:
    """
    Detects construction-site hazards from processed
    monitoring data.
    """

    def __init__(self):
        self.hazards = []


    # =====================================================
    # RESET HAZARDS
    # =====================================================

    def reset(self):
        self.hazards = []


    # =====================================================
    # ADD HAZARD
    # =====================================================

    def add_hazard(
        self,
        name: str,
        category: str,
        severity: str,
        zone: str,
        description: str = ""
    ):
        """
        Add a detected hazard to the result.
        """

        hazard_id = len(self.hazards) + 1

        self.hazards.append({

            "id": hazard_id,

            "name": name,

            "category": category,

            "severity": severity,

            "zone": zone,

            "description": description,

            "status": "Detected"

        })


    # =====================================================
    # ENVIRONMENTAL HAZARDS
    # =====================================================

    def detect_environmental_hazards(
        self,
        data: Dict[str, Any]
    ):
        """
        Detect hazards caused by environmental conditions.
        """

        temperature = float(
            data.get("temperature", 0) or 0
        )

        humidity = float(
            data.get("humidity", 0) or 0
        )

        environmental_risk = float(
            data.get("environmentalRisk", 0) or 0
        )


        # -------------------------------------------------
        # Extreme temperature
        # -------------------------------------------------

        if temperature >= 40:

            self.add_hazard(
                name="Extreme Temperature",
                category="Environmental",
                severity=CRITICAL,
                zone="Zone B",
                description=(
                    "Extremely high temperature may increase "
                    "heat-related worker safety risks."
                )
            )


        elif temperature >= 38:

            self.add_hazard(
                name="High Temperature",
                category="Environmental",
                severity=HIGH,
                zone="Zone B",
                description=(
                    "High temperature may increase worker "
                    "heat exposure."
                )
            )


        elif temperature >= 35:

            self.add_hazard(
                name="Elevated Temperature",
                category="Environmental",
                severity=MEDIUM,
                zone="Zone B",
                description=(
                    "Elevated temperature requires continued "
                    "environmental monitoring."
                )
            )


        # -------------------------------------------------
        # High humidity
        # -------------------------------------------------

        if humidity >= 85:

            self.add_hazard(
                name="Extreme Humidity",
                category="Environmental",
                severity=HIGH,
                zone="Zone B",
                description=(
                    "High humidity may increase heat stress "
                    "and reduce worker comfort."
                )
            )


        elif humidity >= 70:

            self.add_hazard(
                name="High Humidity",
                category="Environmental",
                severity=MEDIUM,
                zone="Zone B",
                description=(
                    "High humidity requires additional "
                    "environmental monitoring."
                )
            )


        # -------------------------------------------------
        # Overall environmental risk
        # -------------------------------------------------

        if environmental_risk >= 81:

            self.add_hazard(
                name="Critical Environmental Risk",
                category="Environmental",
                severity=CRITICAL,
                zone="Site Wide",
                description=(
                    "Overall environmental conditions indicate "
                    "critical site risk."
                )
            )


    # =====================================================
    # EQUIPMENT HAZARDS
    # =====================================================

    def detect_equipment_hazards(
        self,
        data: Dict[str, Any]
    ):
        """
        Detect equipment-related hazards.
        """

        equipment_risk = float(
            data.get("equipmentRisk", 0) or 0
        )

        equipment_count = int(
            data.get("equipment", 0) or 0
        )


        # -------------------------------------------------
        # Critical equipment risk
        # -------------------------------------------------

        if equipment_risk >= 81:

            self.add_hazard(
                name="Critical Equipment Risk",
                category="Equipment",
                severity=CRITICAL,
                zone="Zone A",
                description=(
                    "Equipment conditions indicate a "
                    "critical safety risk."
                )
            )


        # -------------------------------------------------
        # High equipment risk
        # -------------------------------------------------

        elif equipment_risk >= 61:

            self.add_hazard(
                name="Heavy Equipment Risk",
                category="Equipment",
                severity=HIGH,
                zone="Zone A",
                description=(
                    "Equipment requires additional inspection "
                    "and monitoring."
                )
            )


        # -------------------------------------------------
        # Medium equipment risk
        # -------------------------------------------------

        elif equipment_risk >= 31:

            self.add_hazard(
                name="Equipment Condition Warning",
                category="Equipment",
                severity=MEDIUM,
                zone="Zone A",
                description=(
                    "Equipment condition requires routine "
                    "inspection."
                )
            )


        # -------------------------------------------------
        # Large equipment activity
        # -------------------------------------------------

        if equipment_count >= 40:

            self.add_hazard(
                name="High Equipment Activity",
                category="Equipment",
                severity=MEDIUM,
                zone="Zone A",
                description=(
                    "Large numbers of active equipment units "
                    "require increased monitoring."
                )
            )


    # =====================================================
    # WORKER EXPOSURE HAZARDS
    # =====================================================

    def detect_worker_hazards(
        self,
        data: Dict[str, Any]
    ):
        """
        Detect worker exposure hazards.
        """

        worker_exposure = float(
            data.get("workerExposure", 0) or 0
        )

        workers = int(
            data.get("workers", 0) or 0
        )


        # -------------------------------------------------
        # Critical worker exposure
        # -------------------------------------------------

        if worker_exposure >= 81:

            self.add_hazard(
                name="Critical Worker Exposure",
                category="Worker Safety",
                severity=CRITICAL,
                zone="Zone B",
                description=(
                    "Workers are exposed to conditions "
                    "associated with critical safety risk."
                )
            )


        # -------------------------------------------------
        # High worker exposure
        # -------------------------------------------------

        elif worker_exposure >= 61:

            self.add_hazard(
                name="High Worker Exposure",
                category="Worker Safety",
                severity=HIGH,
                zone="Zone B",
                description=(
                    "High worker exposure requires additional "
                    "safety supervision."
                )
            )


        # -------------------------------------------------
        # Medium worker exposure
        # -------------------------------------------------

        elif worker_exposure >= 31:

            self.add_hazard(
                name="Worker Exposure Warning",
                category="Worker Safety",
                severity=MEDIUM,
                zone="Zone B",
                description=(
                    "Worker exposure should be monitored "
                    "during site activities."
                )
            )


        # -------------------------------------------------
        # Large workforce
        # -------------------------------------------------

        if workers >= 250:

            self.add_hazard(
                name="High Worker Density",
                category="Worker Safety",
                severity=MEDIUM,
                zone="Site Wide",
                description=(
                    "High worker density may require "
                    "additional site supervision."
                )
            )


    # =====================================================
    # INCIDENT HAZARDS
    # =====================================================

    def detect_incident_hazards(
        self,
        data: Dict[str, Any]
    ):
        """
        Detect risks based on previous incidents.
        """

        incidents = int(
            data.get("previousIncidents", 0) or 0
        )

        incident_risk = float(
            data.get("incidentHistory", 0) or 0
        )


        # -------------------------------------------------
        # Critical incident history
        # -------------------------------------------------

        if incident_risk >= 81:

            self.add_hazard(
                name="Critical Incident History",
                category="Incident",
                severity=CRITICAL,
                zone="Site Wide",
                description=(
                    "Previous incidents indicate a critical "
                    "historical safety risk."
                )
            )


        # -------------------------------------------------
        # High incident history
        # -------------------------------------------------

        elif incident_risk >= 61:

            self.add_hazard(
                name="High Incident History",
                category="Incident",
                severity=HIGH,
                zone="Zone C",
                description=(
                    "Previous incidents indicate increased "
                    "site safety risk."
                )
            )


        # -------------------------------------------------
        # Previous incidents
        # -------------------------------------------------

        elif incidents > 0:

            self.add_hazard(
                name="Previous Safety Incidents",
                category="Incident",
                severity=MEDIUM,
                zone="Zone C",
                description=(
                    "Previous incidents require corrective "
                    "action and continued monitoring."
                )
            )


    # =====================================================
    # REMOVE DUPLICATES
    # =====================================================

    def remove_duplicate_hazards(self):

        unique_hazards = []

        seen = set()


        for hazard in self.hazards:

            key = (
                hazard["name"],
                hazard["category"],
                hazard["zone"]
            )


            if key not in seen:

                seen.add(key)

                unique_hazards.append(
                    hazard
                )


        # Reassign IDs
        for index, hazard in enumerate(
            unique_hazards,
            start=1
        ):

            hazard["id"] = index


        self.hazards = unique_hazards


    # =====================================================
    # SORT HAZARDS
    # =====================================================

    def sort_hazards(self):

        severity_order = {

            CRITICAL: 1,

            HIGH: 2,

            MEDIUM: 3,

            LOW: 4

        }


        self.hazards.sort(
            key=lambda hazard:
                severity_order.get(
                    hazard["severity"],
                    5
                )
        )


    # =====================================================
    # DETECT ALL HAZARDS
    # =====================================================

    def detect(
        self,
        data: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """
        Run all hazard detection workflows.
        """

        self.reset()


        # Environmental
        self.detect_environmental_hazards(
            data
        )


        # Equipment
        self.detect_equipment_hazards(
            data
        )


        # Worker safety
        self.detect_worker_hazards(
            data
        )


        # Incidents
        self.detect_incident_hazards(
            data
        )


        # Clean results
        self.remove_duplicate_hazards()

        self.sort_hazards()


        return self.hazards


# =========================================================
# SIMPLE FUNCTION
# =========================================================

def detect_hazards(
    site_data: Dict[str, Any]
) -> List[Dict[str, Any]]:
    """
    Simple function that can be imported by other
    backend modules.
    """

    detector = HazardDetector()

    return detector.detect(
        site_data
    )


# =========================================================
# DATAFRAME HAZARD DETECTION
# =========================================================

def detect_hazards_from_dataframe(
    df: pd.DataFrame
) -> List[Dict[str, Any]]:
    """
    Detect hazards from the first row of a processed
    pandas DataFrame.

    Useful when working directly with Kaggle CSV data.
    """

    if df is None or df.empty:

        return []


    # Convert first row to dictionary

    row = df.iloc[0].to_dict()


    return detect_hazards(
        row
    )


# =========================================================
# HAZARD SUMMARY
# =========================================================

def get_hazard_summary(
    hazards: List[Dict[str, Any]]
) -> Dict[str, int]:

    summary = {

        "total": len(hazards),

        "critical": 0,

        "high": 0,

        "medium": 0,

        "low": 0

    }


    for hazard in hazards:

        severity = (
            hazard.get(
                "severity",
                LOW
            )
            .lower()
        )


        if severity in summary:

            summary[severity] += 1


    return summary


# =========================================================
# TEST
# =========================================================

if __name__ == "__main__":

    print(
        "\n========================================"
    )

    print(
        "BuildSure AI - Hazard Detection"
    )

    print(
        "========================================\n"
    )


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


    hazards = detect_hazards(
        sample_data
    )


    print(
        f"Total hazards detected: {len(hazards)}\n"
    )


    for hazard in hazards:

        print(
            f"[{hazard['severity']}] "
            f"{hazard['name']} | "
            f"{hazard['category']} | "
            f"{hazard['zone']}"
        )


    print(
        "\nHazard Summary:"
    )


    summary = get_hazard_summary(
        hazards
    )


    for key, value in summary.items():

        print(
            f"{key}: {value}"
        )