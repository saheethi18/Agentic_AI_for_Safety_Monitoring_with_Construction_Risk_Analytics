from pathlib import Path
from ultralytics import YOLO


# =========================================================
# MODEL PATH
# =========================================================

BASE_DIR = Path(__file__).resolve().parent

MODEL_PATH = BASE_DIR / "models" / "best.pt"


# =========================================================
# LOAD MODEL
# =========================================================

if not MODEL_PATH.exists():
    raise FileNotFoundError(
        f"YOLO model not found: {MODEL_PATH}"
    )

model = YOLO(str(MODEL_PATH))


# =========================================================
# DETECT HAZARDS
# =========================================================

def detect_hazards(image_path: str):
    """
    Detect construction safety hazards
    using the trained YOLO model.
    """

    image = Path(image_path)

    if not image.exists():
        raise FileNotFoundError(
            f"Image not found: {image}"
        )

    results = model.predict(
        source=str(image),
        conf=0.25,
        verbose=False
    )

    hazards = []

    for result in results:

        if result.boxes is None:
            continue

        for box in result.boxes:

            class_id = int(
                box.cls[0].item()
            )

            confidence = float(
                box.conf[0].item()
            )

            class_name = model.names.get(
                class_id,
                f"class_{class_id}"
            )

            coordinates = (
                box.xyxy[0]
                .tolist()
            )

            hazards.append({
                "classId": class_id,
                "name": class_name,
                "confidence": round(
                    confidence,
                    3
                ),
                "box": coordinates
            })

    return hazards


# =========================================================
# TEST MODEL
# =========================================================

if __name__ == "__main__":

    print("=" * 50)
    print("BuildSure AI - YOLO Hazard Detection")
    print("=" * 50)

    print(
        f"Model: {MODEL_PATH}"
    )

    print(
        "Classes:"
    )

    for class_id, class_name in model.names.items():
        print(
            f"{class_id}: {class_name}"
        )

    print()
    print("YOLO model loaded successfully!")