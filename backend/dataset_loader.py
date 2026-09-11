from pathlib import Path


# Project root folder
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Dataset folder
DATASET_PATH = PROJECT_ROOT / "datasets" / "css-data"


def get_dataset_path():
    """
    Check whether the CSS dataset exists.
    """

    if not DATASET_PATH.exists():
        raise FileNotFoundError(
            f"Dataset not found at: {DATASET_PATH}"
        )

    return DATASET_PATH


def get_dataset_files():
    """
    Get all files inside the dataset.
    """

    dataset_path = get_dataset_path()

    files = []

    for file in dataset_path.rglob("*"):
        if file.is_file():
            files.append(file)

    return files


def get_dataset_summary():
    """
    Get basic information about the dataset.
    """

    dataset_path = get_dataset_path()

    train_path = dataset_path / "train"
    valid_path = dataset_path / "valid"
    test_path = dataset_path / "test"

    return {
        "dataset": str(dataset_path),
        "train_exists": train_path.exists(),
        "valid_exists": valid_path.exists(),
        "test_exists": test_path.exists(),
        "total_files": len(get_dataset_files()),
    }


if __name__ == "__main__":

    print("=" * 50)
    print("BuildSure AI - Dataset Check")
    print("=" * 50)

    try:

        summary = get_dataset_summary()

        print("Dataset location:")
        print(summary["dataset"])

        print()

        print(
            "Train folder:",
            summary["train_exists"]
        )

        print(
            "Valid folder:",
            summary["valid_exists"]
        )

        print(
            "Test folder:",
            summary["test_exists"]
        )

        print()

        print(
            "Total files:",
            summary["total_files"]
        )

        print()

        print("Dataset connection successful!")

    except Exception as error:

        print()
        print("ERROR:")
        print(error)