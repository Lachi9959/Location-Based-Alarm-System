# Location-Based Alarm

This Python script simulates a location-based alarm that triggers when the user (or device) is within a specified distance of a target destination. It uses the `geopy` library to calculate distances between geographic coordinates.

## Features

*   **Distance Calculation:** Calculates the geodesic distance between the current location and the target destination.
*   **Proximity Alert:** Triggers an alarm when the current location is within a defined range of the target.
*   **Simulated Movement:** Simulates movement towards the target location.
*   **Configurable:**  The target location and maximum allowed distance can be easily configured.

## Requirements

*   Python 3.x
*   `geopy` library

## Installation

1.  Clone the repository:

    ```bash
    git clone <repository_url>
    cd location-based-alarm
    ```

2.  Install the required libraries:

    ```bash
    pip install geopy
    ```

## Usage

1.  Modify the `target_destination` and `max_distance_to_target` variables in `main.py` to set your desired target location and proximity range.

2.  Run the script:

    ```bash
    python main.py
    ```

The script will simulate movement towards the target and print the current distance. When the simulated location is within the specified range, the alarm will trigger.

## Configuration

*   `target_destination`:  A tuple containing the latitude and longitude of the target destination (e.g., `(40.748817, -73.985428)`).
*   `max_distance_to_target`: The maximum allowed distance (in meters) from the target before the alarm is triggered (e.g., `50`).

## Project Structure
