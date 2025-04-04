import pandas as pd
from ucimlrepo import fetch_ucirepo
from typing import Tuple


def load_data() -> Tuple[pd.DataFrame, pd.Series]:
    """Load and prepare the Seoul Bike Sharing Demand dataset from UCI repository.

    This function fetches the dataset from the UCI Machine Learning Repository using its unique ID (560),
    adjusts the target column (as the second feature in the dataset), and merges the original `targets`
    column back into the features. It returns the adjusted features (X) and the true target (y).

    **Source**:
        Seoul Bike Sharing Demand [Dataset]. (2020). UCI Machine Learning Repository.
        https://doi.org/10.24432/C5F62R

    Returns:
        Tuple[pd.DataFrame, pd.Series]:
            - **X (pd.DataFrame)**: DataFrame containing the features of the dataset.
            - **y (pd.Series)**: Series containing the target column, "Rented Bike Count".

    Example:
        >>> X, y = load_data()
        >>> print(X.shape)  # Example output: (8760, 14)
        >>> print(y.shape)  # Example output: (8760,)
    """
    # Fetch dataset using its unique ID from the UCI repository
    seoul_bike_sharing_demand = fetch_ucirepo(id=560)

    # Extract features and targets from the dataset
    features = seoul_bike_sharing_demand.data.features
    targets = seoul_bike_sharing_demand.data.targets

    # Extract the true target (second column in features)
    true_target = features.iloc[:, 1]  # Assuming the second column is the true target
    features = features.drop(features.columns[1], axis=1)  # Drop the true target from features

    # Add the original target to the features
    features["Functioning Day"] = targets

    # Print metadata and variables for reference
    print("Metadata:")
    print(seoul_bike_sharing_demand.metadata)

    print("\nVariable Information:")
    print(seoul_bike_sharing_demand.variables)

    return features, true_target
