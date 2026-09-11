from collections import Counter
from pathlib import Path

from fastapi import APIRouter


PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
DATASET_ROOT = PROJECT_ROOT / "datasets" / "css-data"
CLASS_NAMES = {
    0: "Hardhat",
    1: "Mask",
    2: "NO-Hardhat",
    3: "NO-Mask",
    4: "NO-Safety Vest",
    5: "Person",
    6: "Safety Cone",
    7: "Safety Vest",
    8: "machinery",
    9: "vehicle",
}

router = APIRouter(prefix="/dataset", tags=["Dataset"])


def summarize_dataset():
    image_count = 0
    label_count = 0
    annotation_count = 0
    class_counts = Counter()

    for split in ("train", "valid", "test"):
        image_dir = DATASET_ROOT / split / "images"
        label_dir = DATASET_ROOT / split / "labels"
        image_count += sum(1 for path in image_dir.glob("*") if path.is_file())

        for label_path in label_dir.glob("*.txt"):
            label_count += 1
            for line in label_path.read_text(encoding="utf-8").splitlines():
                fields = line.split()
                if not fields:
                    continue
                try:
                    class_id = int(fields[0])
                except ValueError:
                    continue
                class_counts[class_id] += 1
                annotation_count += 1

    workers = class_counts.get(5, 0)
    violations = sum(class_counts.get(class_id, 0) for class_id in (2, 3, 4))
    high_risk = sum(class_counts.get(class_id, 0) for class_id in (8, 9))
    compliant_ppe = class_counts.get(0, 0) + class_counts.get(7, 0)

    return {
        "dataset": "Construction Site Safety",
        "imageCount": image_count,
        "labelCount": label_count,
        "annotationCount": annotation_count,
        "workers": workers,
        "ppeCompliant": compliant_ppe,
        "violations": violations,
        "highRisk": high_risk,
        "classCounts": {
            CLASS_NAMES.get(class_id, f"class_{class_id}"): count
            for class_id, count in sorted(class_counts.items())
        },
    }


@router.get("/summary")
def get_dataset_summary():
    return summarize_dataset()