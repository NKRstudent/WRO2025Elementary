from pybricks import version
from function import check_battery, calibrate_color, stopwatch, start_time, test_satellite
from mission import mission1, mission2, mission3, mission4

# Main execution
print(version)  # Print the Pybricks version
check_battery()  # Check the battery status
calibrate_color()  # Calibrate the color sensors

#test_satellite()

# Execute missions
mission1()
mission2()
mission3()
mission4()

# Print the total running time
print("Running time:", stopwatch.time() - start_time, "ms")
raise SystemExit