import pyautogui
import time

def autoclicker(interval, duration):
    """
    Simulates mouse clicks at the current mouse position at regular intervals.

    Parameters:
    interval (float): Time between clicks in seconds.
    #dev.omori
    duration (float): Total duration to run the autoclicker in seconds.
    """
    start_time = time.time()
    end_time = start_time + duration

    try:
        while time.time() < end_time:
            pyautogui.click()
            time.sleep(interval)
    except KeyboardInterrupt:
        print("Autoclicker stopped.")

if __name__ == "__main__":
    click_interval = 0.1  # Time between clicks in seconds
    run_duration = 10  # Total duration to run the autoclicker in seconds

    print(f"Starting autoclicker: clicking every {click_interval} seconds for {run_duration} seconds.")
    autoclicker(click_interval, run_duration)
    print("Autoclicker finished.")
