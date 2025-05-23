from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Color
from pybricks.tools import wait
from mission import mission1, mission2, mission3, mission4
from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Color
from pybricks.tools import wait

hub = PrimeHub()

# --- Setup ---
modes = ["Mission 0", "Mission 1", "Mission 2", "Mission 3", "Mission 4"]
mode_colors = [Color.WHITE, Color.RED, Color.GREEN, Color.BLUE, Color.YELLOW]

# Import or define your mission1 to mission4 functions separately
# Only mission0 is defined here as idle
def mission0():
    hub.light.on(Color.WHITE)
    print("⚪ Idle Mode (Mission 0)")
    wait(3000)

# Link mode indexes to mission functions
missions = [mission0, mission1, mission2, mission3, mission4]

current_mode = 0
idle_timer = 0

# --- Show Initial Selection ---
hub.light.on(mode_colors[current_mode])
print("Selected:", modes[current_mode])

# --- Mode Selection Loop ---
while True:
    pressed = hub.buttons.pressed()

    if pressed:
        idle_timer = 0  # Reset timer on any input

        if Button.LEFT in pressed:
            current_mode = (current_mode - 1) % len(modes)

        elif Button.RIGHT in pressed:
            current_mode = (current_mode + 1) % len(modes)

        hub.light.on(mode_colors[current_mode])
        print("Selected:", modes[current_mode])
        wait(300)  # Debounce delay

    else:
        idle_timer += 100
        if idle_timer >= 3000:  # 3-second idle triggers mission
            break

    wait(100)

# --- Run Selected Mission ---57ko
print("⏱️ Starting:", modes[current_mode])
hub.light.off()
missions[current_mode]()