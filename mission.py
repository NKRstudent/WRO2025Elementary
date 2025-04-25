from function import (
    robot_straight,
    robot_turn,
    run_front_claw,
    run_front_claw_stalled,
    run_side_claw,
    calibration_with_wall,
    detect_color,
    StopAtColorhsv,
    FULL_SPEED,
    LOCATIONS,
    TOLERANCE,
    SATELLITE_COLOR,
)
from pybricks.parameters import Color

def mission1():
    """Mission 1: Fuel."""
    calibration_with_wall(150)
    run_front_claw(500, -162)
    robot_straight(FULL_SPEED, 160)
    run_front_claw(500, 90)
    robot_turn(FULL_SPEED, 90)
    calibration_with_wall(110)
    robot_straight(FULL_SPEED, 1890)
    run_front_claw(100, -30)
    robot_straight(FULL_SPEED, -30)
    run_front_claw(100, -40)
    robot_straight(FULL_SPEED, -50)
    run_front_claw(100, -20)
    robot_straight(FULL_SPEED, -100)

def mission2():
    """Mission 2: Rocket."""
    run_front_claw(FULL_SPEED, 70)
    robot_turn(FULL_SPEED, -50)
    robot_straight(FULL_SPEED, 60)
    robot_turn(FULL_SPEED, 30)
    robot_straight(300, 180)
    robot_turn(FULL_SPEED, -90)
    run_side_claw(FULL_SPEED, 220)
    robot_straight(FULL_SPEED, 510)

def mission3():
    """Mission 3: Space debris."""
    run_side_claw(FULL_SPEED, -220)
    robot_turn(FULL_SPEED, -55)
    robot_straight(FULL_SPEED, 220)
    robot_turn(FULL_SPEED, -60)
    robot_straight(FULL_SPEED, 370)
    robot_turn(FULL_SPEED, 60)
    robot_straight(FULL_SPEED, 65)
    robot_turn(FULL_SPEED, -17)
    robot_straight(FULL_SPEED, 1270)
    robot_turn(100, -45)
    robot_straight(FULL_SPEED, 30)
    robot_turn(100, -45)
    robot_straight(FULL_SPEED, 380)
    robot_turn(100, -45)
    robot_straight(FULL_SPEED, 50)
    robot_turn(100, 45)

def mission4():
    """Mission 4: Satellite."""
    global SATELLITE_COLOR

    # for debugging mission 4 only
    #run_front_claw(500, -90)
    # for debugging mission 4 only

    robot_straight(FULL_SPEED, -100)
    robot_turn(FULL_SPEED, -90)
    calibration_with_wall(180)
    robot_straight(FULL_SPEED, 270)
    robot_turn(FULL_SPEED, -90)
    calibration_with_wall(300)
    robot_straight(FULL_SPEED, 30)
    robot_turn(FULL_SPEED, 92)
    run_front_claw(500, -90)
    robot_straight(FULL_SPEED, 130)

    collect_satellite(1)
    put_satellite(SATELLITE_COLOR)
    robot_turn(FULL_SPEED, -100)
    run_front_claw_stalled(-500)
    robot_straight(FULL_SPEED, 110)
    collect_satellite(5)
    put_satellite(SATELLITE_COLOR)
    robot_turn(FULL_SPEED, -97)
    run_front_claw_stalled(-500)
    robot_straight(FULL_SPEED, 280)
    collect_satellite(4)
    put_satellite(SATELLITE_COLOR)
    robot_turn(FULL_SPEED, -95)
    run_front_claw_stalled(-500)
    robot_straight(FULL_SPEED, 450)
    collect_satellite(3)
    put_satellite(SATELLITE_COLOR, stop = True)
    # By the rule there are only 4 satellite
    # then no need go to location 2
    #robot_turn(FULL_SPEED, -95)
    #run_front_claw_stalled(-500)
    #robot_straight(FULL_SPEED, 620)
    #collect_satellite(2)
    #put_satellite(SATELLITE_COLOR)

def collect_satellite(location):
    """Collect a satellite from a specific location."""
    global SATELLITE_COLOR

    print("Satellite location:", location)
    run_front_claw(100, 60)
    SATELLITE_COLOR = detect_color()
    print("Satellite Color:", SATELLITE_COLOR)
    print("Satellite HSV:", detect_color())

    if location == 1:
        if SATELLITE_COLOR in (Color.NONE, Color.BLACK):
            run_front_claw_stalled(-200)
            robot_straight(FULL_SPEED, 170)
            run_front_claw(100, 60)
            SATELLITE_COLOR = detect_color()
            print("Satellite Color:", SATELLITE_COLOR)
            print("Satellite HSV:", detect_color())
            robot_turn(FULL_SPEED, -90)
            calibration_with_wall(120)
            robot_straight(FULL_SPEED, 200)
            robot_turn(FULL_SPEED, 90)
            robot_straight(FULL_SPEED, 520)
        else:
            robot_turn(FULL_SPEED, -90)
            calibration_with_wall(120)
            robot_straight(FULL_SPEED, 200)
            robot_turn(FULL_SPEED, 90)
            robot_straight(FULL_SPEED, 690)
            
        StopAtColorhsv(100, Color.BLACK, TOLERANCE)
        robot_straight(FULL_SPEED, 50)
        robot_turn(FULL_SPEED, -90)
        robot_straight(FULL_SPEED, 400)
        StopAtColorhsv(100, Color.BLACK, TOLERANCE)
    elif location == 5:
        if SATELLITE_COLOR in (Color.NONE, Color.BLACK):
            robot_turn(FULL_SPEED, 2)
            run_front_claw_stalled(-200)
            robot_straight(300, 170)
            run_front_claw(100, 60)
            SATELLITE_COLOR = detect_color()
            print("Satellite Color:", SATELLITE_COLOR)
            print("Satellite HSV:", detect_color())
            robot_turn(FULL_SPEED, 90)
            calibration_with_wall(120)
            robot_straight(FULL_SPEED, 50)
            robot_turn(FULL_SPEED, -90)
            robot_straight(FULL_SPEED, -100)
        else:
            robot_turn(FULL_SPEED, 90)
            calibration_with_wall(120)
            robot_straight(FULL_SPEED, 50)
            robot_turn(FULL_SPEED, -90)
            
        StopAtColorhsv(100, Color.BLACK, TOLERANCE)
        robot_straight(FULL_SPEED, 80)
        robot_turn(FULL_SPEED, 90)
        robot_straight(FULL_SPEED, 450)
        StopAtColorhsv(100, Color.BLACK, TOLERANCE)

    elif location == 4:
        if SATELLITE_COLOR in (Color.NONE, Color.BLACK):
            #robot_turn(FULL_SPEED, 7)
            run_front_claw_stalled(-200)
            robot_straight(FULL_SPEED, 170)
            run_front_claw(100, 60)
            SATELLITE_COLOR = detect_color()
            print("Satellite Color:", SATELLITE_COLOR)
            print("Satellite HSV:", detect_color())
            robot_turn(FULL_SPEED, 90)
            calibration_with_wall(120)
            robot_straight(FULL_SPEED, 187)
            robot_turn(FULL_SPEED, 90)
            robot_straight(FULL_SPEED, 170)
        else:
            robot_turn(FULL_SPEED, 90)
            calibration_with_wall(120)
            robot_straight(FULL_SPEED, 187)
            robot_turn(FULL_SPEED, 90)
            #robot_straight(FULL_SPEED, 120)
            
        StopAtColorhsv(-100, Color.BLACK, TOLERANCE)
        robot_straight(FULL_SPEED, 40)
        robot_turn(FULL_SPEED, -90)
        robot_straight(FULL_SPEED, 450)
        StopAtColorhsv(100, Color.BLACK, TOLERANCE)
    elif location == 3:
        if SATELLITE_COLOR in (Color.NONE, Color.BLACK):
            #robot_turn(FULL_SPEED, 5)
            run_front_claw_stalled(-200)
            robot_straight(FULL_SPEED, 170)
            run_front_claw(100, 60)
            SATELLITE_COLOR = detect_color()
            print("Satellite Color:", SATELLITE_COLOR)
            print("Satellite HSV:", detect_color())
            robot_turn(FULL_SPEED, 90)
            calibration_with_wall(120)
            robot_straight(FULL_SPEED, 170)
            robot_turn(FULL_SPEED, 90)
            robot_straight(FULL_SPEED, 260)
        else:
            robot_turn(FULL_SPEED, 90)
            calibration_with_wall(120)
            robot_straight(FULL_SPEED, 170)
            robot_turn(FULL_SPEED, 90)
            robot_straight(FULL_SPEED, 90)
            
        StopAtColorhsv(100, Color.BLACK, TOLERANCE)
        robot_straight(FULL_SPEED, 50)
        robot_turn(FULL_SPEED, -90)
        robot_straight(FULL_SPEED, 450)
        StopAtColorhsv(100, Color.BLACK, TOLERANCE)

    elif location == 2:
        if SATELLITE_COLOR in (Color.NONE, Color.BLACK):
            run_front_claw_stalled(-200)
            robot_straight(FULL_SPEED, 170)
            run_front_claw(100, 60)
            SATELLITE_COLOR = detect_color()
            print("Satellite Color:", SATELLITE_COLOR)
            print("Satellite HSV:", detect_color())
            robot_turn(FULL_SPEED, 90)
            calibration_with_wall(120)
            robot_straight(FULL_SPEED, 170)
            robot_turn(FULL_SPEED, 90)
            robot_straight(FULL_SPEED, 290)
        else:
            robot_turn(FULL_SPEED, 90)
            calibration_with_wall(120)
            robot_straight(FULL_SPEED, 170)
            robot_turn(FULL_SPEED, 90)
            robot_straight(FULL_SPEED, 260)
            
        StopAtColorhsv(100, Color.BLACK, TOLERANCE)
        robot_turn(FULL_SPEED, -90)
        robot_straight(FULL_SPEED, 450)
        StopAtColorhsv(100, Color.BLACK, TOLERANCE)

def put_satellite(color, stop = False):
    """Place the satellite in the correct location based on its color."""
    #robot_straight(FULL_SPEED, 460)
    robot_turn(FULL_SPEED, -92)
    print("Placing Satellite Color:", color)

    if color == Color.WHITE:
        offset = -20
    elif color == Color.GREEN:
        offset = 210
    elif color == Color.BLUE:
        offset = 390
    elif color == Color.YELLOW:
        offset = 590
    elif color == Color.RED:
        offset = 780
    print("Placing offset:", offset)
    white_offset = 70
    robot_straight(FULL_SPEED, white_offset + offset)
    robot_turn(FULL_SPEED, 90)
    robot_straight(FULL_SPEED, 80)
    run_front_claw_stalled(-200)
    if stop == True:
        return
    robot_straight(FULL_SPEED, -105)
    run_front_claw(FULL_SPEED, 60)
    robot_turn(FULL_SPEED, -90)
    robot_straight(FULL_SPEED, -(white_offset + offset) - 290)
    robot_turn(FULL_SPEED, 90)
    robot_straight(FULL_SPEED, -700)
    calibration_with_wall(150)
