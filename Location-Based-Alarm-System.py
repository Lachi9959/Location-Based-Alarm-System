import time
from geopy.distance import geodesic

# Define the target destination (latitude, longitude)
target_destination = (40.748817, -73.985428)  # Example: Location of the Empire State Building

# Simulate the current location (initially far from the target)
current_location = (40.748817, -73.990000)  # A location a bit further away

# Define the maximum allowed distance (in meters) to trigger the alarm
max_distance_to_target = 50  # 50 meters

def check_location(current, target):
    """Check the distance between current location and target location."""
    return geodesic(current, target).meters

def trigger_alarm():
    """Function to simulate an alarm."""
    print("ALERT: You have reached your destination! Alarm triggered!")

def move_toward_target(current, target):
    """Simulate moving towards the target location."""
    lat_current, lon_current = current
    lat_target, lon_target = target
    
    # Moving towards the target by 10% of the difference in coordinates
    new_lat = lat_current + (lat_target - lat_current) * 0.1
    new_lon = lon_current + (lon_target - lon_current) * 0.1
    
    # Ensure we do not overshoot the target (check the distance between the new point and the target)
    if geodesic((new_lat, new_lon), target).meters < geodesic(current, target).meters:
        return new_lat, new_lon
    else:
        return target  # If overshooting, return the target location

def main():
    global current_location  # Make sure to use the global current_location
    
    print("Starting journey towards the target destination...")
   
    while True:
        # Check the current distance
        distance = check_location(current_location, target_destination)
        print(f"Current distance to target: {distance:.2f} meters")
       
        # If within the target range, trigger the alarm
        if distance <= max_distance_to_target:
            trigger_alarm()
            break
       
        # Simulate movement toward the target
        current_location = move_toward_target(current_location, target_destination)
       
        # Wait a bit before checking again (simulating time passing)
        time.sleep(1)  # Update every second

if __name__ == "__main__":
    main()
