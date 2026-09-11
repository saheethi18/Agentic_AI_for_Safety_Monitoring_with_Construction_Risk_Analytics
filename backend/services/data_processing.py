from typing import Any, Dict, Optional

import pandas as pd


# =========================================================
# DATA PROCESSING
# =========================================================

def load_dataset(file_path: str) -> pd.DataFrame:
    """
    Load a CSV dataset.

    Parameters:
        file_path: Path to the CSV file.

    Returns:
        Pandas DataFrame.
    """

    try:
        return pd.read_csv(file_path)

    except FileNotFoundError:
        raise FileNotFoundError(
            f"Dataset not found: {file_path}"
        )

    except Exception as error:
        raise ValueError(
            f"Unable to read dataset: {error}"
        )


def clean_dataset(
    dataframe: pd.DataFrame
) -> pd.DataFrame:
    """
    Basic cleaning of construction safety data.
    """

    df = dataframe.copy()

    # Remove completely empty rows
    df = df.dropna(how="all")

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Clean column names
    df.columns = [
        str(column).strip()
        for column in df.columns
    ]

    return df


def get_dataset_info(
    dataframe: pd.DataFrame
) -> Dict[str, Any]:
    """
    Return basic information about the dataset.
    """

    return {
        "rows": int(len(dataframe)),
        "columns": [
            str(column)
            for column in dataframe.columns
        ]
    }


def _find_column(
    dataframe: pd.DataFrame,
    possible_names: list
) -> Optional[str]:
    """
    Find a column using possible column names.
    """

    column_map = {
        str(column).lower().strip(): column
        for column in dataframe.columns
    }

    for name in possible_names:

        key = name.lower().strip()

        if key in column_map:
            return column_map[key]

    return None


def _numeric_average(
    dataframe: pd.DataFrame,
    column: Optional[str],
    default: float
) -> float:
    """
    Safely calculate the average of a numeric column.
    """

    if column is None:
        return default

    values = pd.to_numeric(
        dataframe[column],
        errors="coerce"
    )

    if values.dropna().empty:
        return default

    return float(values.mean())


def process_site_data(
    dataframe: pd.DataFrame
) -> Dict[str, Any]:
    """
    Convert dataset information into the
    format required by the Site Risk Dashboard.
    """

    df = clean_dataset(dataframe)


    # -----------------------------------------------------
    # Find useful columns
    # -----------------------------------------------------

    worker_column = _find_column(
        df,
        [
            "workers",
            "worker_count",
            "number_of_workers",
            "employees"
        ]
    )


    equipment_column = _find_column(
        df,
        [
            "equipment",
            "equipment_count",
            "machines",
            "machinery"
        ]
    )


    temperature_column = _find_column(
        df,
        [
            "temperature",
            "temp",
            "temperature_c"
        ]
    )


    humidity_column = _find_column(
        df,
        [
            "humidity",
            "humidity_percent"
        ]
    )


    incident_column = _find_column(
        df,
        [
            "previous_incidents",
            "incidents",
            "incident_count",
            "accidents"
        ]
    )


    # -----------------------------------------------------
    # Calculate monitoring values
    # -----------------------------------------------------

    workers = round(
        _numeric_average(
            df,
            worker_column,
            185
        )
    )


    equipment = round(
        _numeric_average(
            df,
            equipment_column,
            24
        )
    )


    temperature = round(
        _numeric_average(
            df,
            temperature_column,
            39.0
        ),
        1
    )


    humidity = round(
        _numeric_average(
            df,
            humidity_column,
            72.0
        ),
        1
    )


    previous_incidents = round(
        _numeric_average(
            df,
            incident_column,
            4
        )
    )


    # -----------------------------------------------------
    # Generate risk factors
    # -----------------------------------------------------

    environmental_risk = min(
        100.0,
        max(
            0.0,
            (
                max(
                    0.0,
                    temperature - 20
                )
                * 4
            )
        )
    )


    equipment_risk = min(
        100.0,
        max(
            0.0,
            equipment * 2.7
        )
    )


    worker_exposure = min(
        100.0,
        max(
            0.0,
            workers * 0.43
        )
    )


    incident_history = min(
        100.0,
        max(
            0.0,
            previous_incidents * 17.5
        )
    )


    return {
        "workers": workers,
        "equipment": equipment,
        "temperature": temperature,
        "humidity": humidity,
        "previousIncidents": previous_incidents,

        "environmentalRisk": round(
            environmental_risk,
            1
        ),

        "equipmentRisk": round(
            equipment_risk,
            1
        ),

        "workerExposure": round(
            worker_exposure,
            1
        ),

        "incidentHistory": round(
            incident_history,
            1
        )
    }


def process_dataset(
    file_path: str
) -> Dict[str, Any]:
    """
    Complete dataset processing function.

    Loads, cleans and processes a CSV file.
    """

    dataframe = load_dataset(
        file_path
    )

    return process_site_data(
        dataframe
    )