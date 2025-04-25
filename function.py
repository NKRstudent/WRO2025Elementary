from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Color, Direction, Port, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import StopWatch

# Initialize hub and stopwatch
hub = PrimeHub()
stopwatch = StopWatch()
start_time = stopwatch.time()

# Constants
FULL_SPEED = 1000
TOLERANCE = 30  # Tolerance for color sensor
LOCATIONS = [1, 2, 3, 4, 5]
SATELLITE_COLOR = Color.BLACK  # BLACK means no satellite

# Initialize devices
left_motor = Motor(Port.E, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.A)
front_claw = Motor(Port.B)
side_claw = Motor(Port.F)
map_sensor = ColorSensor(Port.D)
side_sensor = ColorSensor(Port.C)
robot = DriveBase(left_motor, right_motor, 86, 160)

# Enable gyro for improved accuracy
robot.use_gyro(True)

# Movement functions
def robot_straight(speed, distance):
    """Move the robot straight."""
    robot.settings(straight_speed=speed)
    robot.straight(distance)

def robot_turn(speed, angle):
    """Turn the robot."""
    robot.settings(turn_rate=speed)
    robot.turn(angle)

# Claw control functions
def run_side_claw(speed, degree):
    """Move the side claw."""
    side_claw.run_angle(speed, degree)

def run_front_claw(speed, degree):
    """Move the front claw."""
    front_claw.run_angle(speed, degree, then=Stop.HOLD)

def run_front_claw_stalled(speed):
    """Move the front claw until stalled."""
    front_claw.run_until_stalled(speed=speed)

# Calibration functions
def calibration_with_wall(distance):
    """Calibrate the robot using a wall."""
    robot.use_gyro(False)
    robot.straight(-distance, then=Stop.COAST)
    robot.reset()
    robot.use_gyro(True)

def calibrate_color():
    """Calibrate the color sensors."""
    # Define color values
    Color.NONE = Color(h=0, s=0, v=0)
    Color.BLACK = Color(h=230, s=3, v=24)
    Color.WHITE = Color(h=0, s=0, v=100)
    Color.GREEN = Color(h=163, s=55, v=37)
    Color.RED = Color(h=348, s=100, v=32)
    Color.BLUE = Color(h=218, s=89, v=40)
    Color.YELLOW = Color(h=52, s=60, v=55)

    # Save detectable colors
    detectable_colors = (
        Color.NONE, Color.BLACK, Color.WHITE, Color.GREEN,
        Color.BLUE, Color.YELLOW, Color.RED
    )
    map_sensor.detectable_colors(detectable_colors)
    side_sensor.detectable_colors(detectable_colors)

# Detect color
def detect_color():
    """Detect color using the side sensor."""
    detected_color = side_sensor.color()
    detected_hsv = side_sensor.hsv()
    print("Detected Color:", detected_color)
    print("Detected HSV:", detected_hsv)

    if detected_color in (Color.BLUE, Color.RED) and detected_hsv.h < 190:
        detected_color = Color.GREEN
    elif detected_color in (Color.BLACK, Color.NONE):
        detected_color = side_sensor.color()
        detected_hsv = side_sensor.hsv()
        print("2 Detected Color:", detected_color)
        print("2 Detected HSV:", detected_hsv)
        if detected_color in (Color.BLACK, Color.NONE):
            if detected_hsv.h > 300:
                detected_color = Color.RED
            elif detected_hsv.h < 220 and detected_hsv.h > 180 and detected_hsv.s < 30 and detected_hsv.s > 15:
                detected_color = Color.RED
            elif detected_hsv.h < 80 and detected_hsv.s > 30:
                detected_color = Color.YELLOW
            elif detected_hsv.h < 300 and detected_hsv.h > 200 and detected_hsv.s > 70 and detected_hsv.v > 15:
                detected_color = Color.BLUE
            elif detected_hsv.h > 140 and detected_hsv.h < 180 and detected_hsv.s > 45:
                detected_color = Color.GREEN
        
    if detected_hsv.h < 20 and detected_hsv.s > 90:
        detected_color = Color.RED

    return detected_color

# compare hsv value with tolerance
def comparehsv(colora, colorb, tolerance):
    hresult = abs(colora.h - colorb.h) <= tolerance
    sresult = abs(colora.s - colorb.s) <= tolerance
    vresult = abs(colora.v - colorb.v) <= tolerance
    return hresult and sresult and vresult

# compare hs value with tolerance
def comparehs(colora, colorb, tolerance):
    hresult = abs(colora.h - colorb.h) <= tolerance
    sresult = abs(colora.s - colorb.s) <= tolerance
    return hresult and sresult

# stop at color line with both left/right sensor detect
# move with speed, if negative speed, move backward
def StopAtColorhsv(speed, colorstop, tolerance):
    robot.drive(speed, 0)
    map_hsv = map_sensor.hsv()

    # compare map color sensor detect hsv to colorstop with tolerance
    while not comparehsv(map_hsv, colorstop, tolerance):
        map_hsv = map_sensor.hsv()

    print("Map hsv:", map_sensor.hsv())
    # use drive(0, 0) to stop, this is better then stop()
    robot.drive(0, 0)

    return

def test_satellite():
    #run_front_claw(100, 80)
    #satellitecolor = detect_color()
    #print("Satellite Color: ", satellitecolor)
    print("Map HSV: ", map_sensor.hsv())

# Battery monitoring
class BatteryColors:
    """ANSI color codes for battery status."""
    BATTERY_OK = '\033[32m'
    BATTERY_LOW = '\033[31m'
    ENDC = '\033[0m'

def check_battery():
    """Check and print battery voltage."""
    voltage = hub.battery.voltage()
    if voltage < 8000:
        print(BatteryColors.BATTERY_LOW + f"Battery voltage is too low: {voltage}\n"
              "-----------------------------\n"
              ">>>> Please charge robot <<<<\n"
              "-----------------------------\n" + BatteryColors.ENDC)
    else:
        print(BatteryColors.BATTERY_OK + f"Battery voltage: {voltage}" + BatteryColors.ENDC)