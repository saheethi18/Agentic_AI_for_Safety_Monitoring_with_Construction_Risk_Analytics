from pathlib import Path
from typing import Optional

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel


# =========================================================
# PATHS
# =========================================================

PROJECT_DIR = Path(__file__).resolve().parent.parent.parent

MODEL_PATH = (
    PROJECT_DIR
    / "backend"
    / "models"
    / "best.pt"
)

TEST_IMAGES_PATH = (
    PROJECT_DIR
    / "datasets"
    / "css-data"
    / "test"
    / "images"
)


# =========================================================
# LOAD YOLO MODEL (LAZY LOADING)
# =========================================================

model = None
model_loaded = False

def get_model():
    """Lazy load YOLO model on first request"""
    global model, model_loaded
    
    if model_loaded:
        return model
    
    model_loaded = True
    
    try:
        from ultralytics import YOLO
        
        if MODEL_PATH.exists():
            model = YOLO(str(MODEL_PATH))
            print("========================================")
            print("BuildSure AI - YOLO Model")
            print("========================================")
            print("Model loaded successfully:")
            print(MODEL_PATH)
            print("Classes:")
            print(model.names)
            print("========================================")
        else:
            print("WARNING: YOLO model not found:")
            print(MODEL_PATH)
    except ImportError:
        print("ERROR: ultralytics not installed")
        print("Install with: pip install ultralytics")
    except Exception as error:
        print("ERROR loading YOLO model:")
        print(error)
    
    return model


# =========================================================
# ROUTER
# =========================================================

router = APIRouter(
    prefix="/site-risk",
    tags=["Site Risk"]
)


# =========================================================
# DATA MODEL
# =========================================================

class SiteRiskData(BaseModel):

    projectId: Optional[str] = "P001"

    projectName: Optional[str] = (
        "ABC Construction Project"
    )

    location: Optional[str] = "Hyderabad"

    workers: Optional[int] = 185

    equipment: Optional[int] = 24

    temperature: Optional[float] = 39.0

    humidity: Optional[float] = 72.0

    previousIncidents: Optional[int] = 4

    environmentalRisk: Optional[float] = 75.0

    equipmentRisk: Optional[float] = 65.0

    workerExposure: Optional[float] = 80.0

    incidentHistory: Optional[float] = 70.0


# =========================================================
# RISK LEVEL
# =========================================================

def calculate_risk_level(
    score: float
):

    if score >= 81:
        return "CRITICAL"

    if score >= 61:
        return "HIGH"

    if score >= 31:
        return "MEDIUM"

    return "LOW"


# =========================================================
# YOLO HAZARD DETECTION
# =========================================================

def detect_yolo_hazards():

    hazards = []
    
    # Lazy load model
    model = get_model()

    if model is None:

        print(
            "YOLO model is not available."
        )

        return hazards

    if not TEST_IMAGES_PATH.exists():

        print(
            "Dataset images folder not found:"
        )

        print(
            TEST_IMAGES_PATH
        )

        return hazards

    # -----------------------------------------------------
    # Find dataset images
    # -----------------------------------------------------

    image_files = []

    for extension in [
        "*.jpg",
        "*.jpeg",
        "*.png",
        "*.JPG",
        "*.JPEG",
        "*.PNG"
    ]:

        image_files.extend(
            TEST_IMAGES_PATH.glob(
                extension
            )
        )

    if not image_files:

        print(
            "No images found in test dataset."
        )

        return hazards

    # -----------------------------------------------------
    # Search multiple images for an actual safety violation
    # -----------------------------------------------------

    selected_results = None

    selected_image = None

    max_images_to_check = min(
        len(image_files),
        50
    )

    for image_path in image_files[
        :max_images_to_check
    ]:

        print(
            f"Checking dataset image: "
            f"{image_path.name}"
        )

        try:

            results = model.predict(
                source=str(
                    image_path
                ),
                conf=0.25,
                verbose=False
            )

        except Exception as error:

            print(
                f"YOLO error for "
                f"{image_path.name}:"
            )

            print(error)

            continue

        found_violation = False

        for result in results:

            if result.boxes is None:

                continue

            for box in result.boxes:

                try:

                    class_id = int(
                        box.cls[0].item()
                    )

                except Exception:

                    continue

                if isinstance(
                    model.names,
                    dict
                ):

                    class_name = (
                        model.names.get(
                            class_id,
                            f"Class {class_id}"
                        )
                    )

                else:

                    try:

                        class_name = (
                            model.names[
                                class_id
                            ]
                        )

                    except Exception:

                        class_name = (
                            f"Class {class_id}"
                        )

                class_name = str(
                    class_name
                )

                if class_name in [
                    "NO-Hardhat",
                    "NO-Mask",
                    "NO-Safety Vest",
                    "machinery",
                    "vehicle"
                ]:

                    found_violation = True

                    break

            if found_violation:

                break

        if found_violation:

            selected_results = results

            selected_image = image_path

            print(
                "========================================"
            )

            print(
                "Safety violation image found:"
            )

            print(
                selected_image.name
            )

            print(
                "========================================"
            )

            break

    # -----------------------------------------------------
    # If no violation was found, analyze first image
    # -----------------------------------------------------

    if selected_results is None:

        selected_image = image_files[0]

        print(
            "No safety violation found in "
            f"first {max_images_to_check} images."
        )

        print(
            "Using first test image:"
        )

        print(
            selected_image.name
        )

        try:

            selected_results = model.predict(
                source=str(
                    selected_image
                ),
                conf=0.25,
                verbose=False
            )

        except Exception as error:

            print(
                "YOLO prediction error:"
            )

            print(error)

            return hazards

    # -----------------------------------------------------
    # Process detections
    # -----------------------------------------------------

    hazard_id = 1

    for result in selected_results:

        if result.boxes is None:

            continue

        for box in result.boxes:

            try:

                class_id = int(
                    box.cls[0].item()
                )

                confidence = float(
                    box.conf[0].item()
                )

            except Exception:

                continue

            # -------------------------------------------------
            # Get class name
            # -------------------------------------------------

            if isinstance(
                model.names,
                dict
            ):

                class_name = (
                    model.names.get(
                        class_id,
                        f"Class {class_id}"
                    )
                )

            else:

                try:

                    class_name = (
                        model.names[
                            class_id
                        ]
                    )

                except Exception:

                    class_name = (
                        f"Class {class_id}"
                    )

            class_name = str(
                class_name
            )

            # -------------------------------------------------
            # Actual hazard classes
            # -------------------------------------------------

            safety_violations = [
                "NO-Hardhat",
                "NO-Mask",
                "NO-Safety Vest"
            ]

            equipment_hazards = [
                "machinery",
                "vehicle"
            ]

            # Ignore normal detections
            if (
                class_name
                not in safety_violations
                and class_name
                not in equipment_hazards
            ):

                continue

            # -------------------------------------------------
            # Severity
            # -------------------------------------------------

            if class_name in safety_violations:

                if confidence >= 0.75:

                    severity = "CRITICAL"

                else:

                    severity = "HIGH"

            else:

                if confidence >= 0.75:

                    severity = "HIGH"

                else:

                    severity = "MEDIUM"

            # -------------------------------------------------
            # Category
            # -------------------------------------------------

            if class_name in safety_violations:

                category = "Worker Safety"

            else:

                category = "Equipment"

            # -------------------------------------------------
            # Description
            # -------------------------------------------------

            if class_name == "NO-Hardhat":

                description = (
                    "Worker detected without "
                    "required hardhat protection."
                )

            elif class_name == "NO-Mask":

                description = (
                    "Worker detected without "
                    "required mask protection."
                )

            elif class_name == "NO-Safety Vest":

                description = (
                    "Worker detected without "
                    "required safety vest."
                )

            elif class_name == "machinery":

                description = (
                    "Construction machinery "
                    "detected in the monitored area."
                )

            elif class_name == "vehicle":

                description = (
                    "Construction vehicle "
                    "detected in the monitored area."
                )

            else:

                description = (
                    "Potential construction "
                    "safety hazard detected."
                )

            # -------------------------------------------------
            # Add hazard
            # -------------------------------------------------

            hazards.append({

                "id":
                    hazard_id,

                "name":
                    class_name,

                "category":
                    category,

                "severity":
                    severity,

                "zone":
                    "Detected Zone",

                "description":
                    description,

                "status":
                    "Detected",

                "confidence":
                    round(
                        confidence * 100,
                        2
                    ),

                "image":
                    selected_image.name

            })

            hazard_id += 1

    print(
        "Actual YOLO hazards detected: "
        f"{len(hazards)}"
    )

    return hazards


# =========================================================
# RULE-BASED HAZARDS
# =========================================================

def detect_rule_hazards(
    data: SiteRiskData
):

    hazards = []

    if (
        data.temperature or 0
    ) >= 38:

        hazards.append({

            "id": 1,

            "name":
                "High Temperature",

            "category":
                "Environmental",

            "severity":
                "HIGH",

            "zone":
                "Zone B",

            "description":
                (
                    "High temperature may "
                    "increase heat-related "
                    "safety risks."
                ),

            "status":
                "Detected"

        })

    if (
        data.equipmentRisk or 0
    ) >= 60:

        hazards.append({

            "id": 2,

            "name":
                "Heavy Equipment Risk",

            "category":
                "Equipment",

            "severity":
                "HIGH",

            "zone":
                "Zone A",

            "description":
                (
                    "Equipment risk level "
                    "requires additional "
                    "inspection."
                ),

            "status":
                "Detected"

        })

    if (
        data.workerExposure or 0
    ) >= 60:

        hazards.append({

            "id": 3,

            "name":
                "High Worker Exposure",

            "category":
                "Worker Safety",

            "severity":
                "HIGH",

            "zone":
                "Zone B",

            "description":
                (
                    "Workers are exposed "
                    "to elevated site risks."
                ),

            "status":
                "Detected"

        })

    if (
        data.previousIncidents or 0
    ) > 0:

        hazards.append({

            "id": 4,

            "name":
                "Previous Safety Incidents",

            "category":
                "Incident",

            "severity":
                "MEDIUM",

            "zone":
                "Zone C",

            "description":
                (
                    "Previous incidents "
                    "require corrective "
                    "action review."
                ),

            "status":
                "Detected"

        })

    return hazards


# =========================================================
# COMBINED HAZARD DETECTION
# =========================================================

def detect_hazards(
    data: SiteRiskData
):

    yolo_hazards = (
        detect_yolo_hazards()
    )

    # If YOLO finds actual hazards,
    # use YOLO results.
    if yolo_hazards:

        return yolo_hazards

    # Otherwise use site-condition risks.
    return detect_rule_hazards(
        data
    )


# =========================================================
# RISK SCORE
# =========================================================

def calculate_risk_score(
    data: SiteRiskData,
    hazards=None
):

    # -----------------------------------------------------
    # Base site risk
    # -----------------------------------------------------

    environmental = (
        data.environmentalRisk or 0
    )

    equipment = (
        data.equipmentRisk or 0
    )

    worker = (
        data.workerExposure or 0
    )

    incidents = (
        data.incidentHistory or 0
    )

    base_score = (
        environmental
        + equipment
        + worker
        + incidents
    ) / 4

    # -----------------------------------------------------
    # YOLO contribution
    # -----------------------------------------------------

    yolo_penalty = 0

    if hazards:

        for hazard in hazards:

            name = str(
                hazard.get(
                    "name",
                    ""
                )
            ).lower()

            confidence = float(
                hazard.get(
                    "confidence",
                    0
                )
            )

            # PPE violations
            if name in [
                "no-hardhat",
                "no-mask",
                "no-safety vest"
            ]:

                yolo_penalty += (
                    15
                    * confidence
                    / 100
                )

            # Equipment hazards
            elif name in [
                "machinery",
                "vehicle"
            ]:

                yolo_penalty += (
                    5
                    * confidence
                    / 100
                )

    # Limit YOLO contribution
    yolo_penalty = min(
        yolo_penalty,
        30
    )

    final_score = (
        base_score
        + yolo_penalty
    )

    return round(
        min(
            final_score,
            100
        )
    )


# =========================================================
# RECOMMENDATIONS
# =========================================================

def generate_recommendations(
    data: SiteRiskData,
    hazards=None
):

    recommendations = []

    # -----------------------------------------------------
    # Temperature
    # -----------------------------------------------------

    if (
        data.temperature or 0
    ) >= 38:

        recommendations.append(
            "Increase safety monitoring during high-temperature conditions."
        )

    # -----------------------------------------------------
    # Equipment
    # -----------------------------------------------------

    if (
        data.equipmentRisk or 0
    ) >= 60:

        recommendations.append(
            "Conduct additional equipment inspections."
        )

    # -----------------------------------------------------
    # Worker exposure
    # -----------------------------------------------------

    if (
        data.workerExposure or 0
    ) >= 60:

        recommendations.append(
            "Provide additional safety supervision in high-risk zones."
        )

    # -----------------------------------------------------
    # Incidents
    # -----------------------------------------------------

    if (
        data.previousIncidents or 0
    ) > 0:

        recommendations.append(
            "Review previous incidents and implement corrective actions."
        )

    # -----------------------------------------------------
    # YOLO recommendations
    # -----------------------------------------------------

    if hazards:

        violation_names = [
            str(
                hazard.get(
                    "name",
                    ""
                )
            )
            for hazard in hazards
        ]

        if "NO-Hardhat" in violation_names:

            recommendations.append(
                "Ensure all workers wear approved hardhats."
            )

        if "NO-Mask" in violation_names:

            recommendations.append(
                "Ensure workers use required face protection."
            )

        if (
            "NO-Safety Vest"
            in violation_names
        ):

            recommendations.append(
                "Ensure workers wear required safety vests."
            )

        if "machinery" in violation_names:

            recommendations.append(
                "Inspect machinery and maintain safe operating distances."
            )

        if "vehicle" in violation_names:

            recommendations.append(
                "Maintain safe separation between workers and construction vehicles."
            )

    # -----------------------------------------------------
    # Default
    # -----------------------------------------------------

    if not recommendations:

        recommendations.append(
            "Continue routine site monitoring."
        )

    return recommendations


# =========================================================
# BUILD RESPONSE
# =========================================================

def build_response(
    data: SiteRiskData
):

    # IMPORTANT:
    # Detect hazards before calculating risk.
    hazards = detect_hazards(
        data
    )

    # Calculate risk using the detected hazards.
    risk_score = calculate_risk_score(
        data,
        hazards
    )

    risk_level = calculate_risk_level(
        risk_score
    )

    recommendations = (
        generate_recommendations(
            data,
            hazards
        )
    )

    return {

        "projectId":
            data.projectId or "P001",

        "projectName":
            data.projectName
            or "ABC Construction Project",

        "location":
            data.location
            or "Hyderabad",

        "riskScore":
            risk_score,

        "riskLevel":
            risk_level,

        "monitoring": {

            "workers":
                data.workers or 0,

            "equipment":
                data.equipment or 0,

            "temperature":
                data.temperature or 0,

            "humidity":
                data.humidity or 0,

            "previousIncidents":
                data.previousIncidents or 0

        },

        "riskFactors": {

            "environmental":
                data.environmentalRisk or 0,

            "equipment":
                data.equipmentRisk or 0,

            "workerExposure":
                data.workerExposure or 0,

            "incidentHistory":
                data.incidentHistory or 0

        },

        "hazards":
            hazards,

        "recommendations":
            recommendations

    }


# =========================================================
# GET SITE RISK
# =========================================================

@router.get(
    "/{project_id}"
)
def get_site_risk(
    project_id: str
):

    valid_projects = [
        "P001",
        "P002",
        "P003"
    ]

    if (
        project_id
        not in valid_projects
    ):

        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    data = SiteRiskData(
        projectId=project_id
    )

    return build_response(
        data
    )


# =========================================================
# ANALYZE SITE RISK
# =========================================================

@router.post(
    "/analyze"
)
def analyze_site_risk(
    data: SiteRiskData
):

    return build_response(
        data
    )