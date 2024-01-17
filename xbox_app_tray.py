import threading
import ctypes
from infi.systray import SysTrayIcon
import time
from plyer import notification
# Use the 'ctypes' library to access the Xbox controller information on Windows
try:
    import ctypes.wintypes
    from ctypes import Structure, byref

    class XINPUT_BATTERY_INFORMATION(Structure):
        _fields_ = [("BatteryType", ctypes.c_ubyte),
                    ("BatteryLevel", ctypes.c_ubyte)]
    
    xinput = ctypes.windll.xinput1_3

    def get_battery_level(controller_index):
        battery_info = XINPUT_BATTERY_INFORMATION()
        result = xinput.XInputGetBatteryInformation(controller_index, 0, byref(battery_info))
        if result == 0:
            if battery_info.BatteryLevel == 0:
                return 25
            if battery_info.BatteryLevel == 1:
                return 50
            if battery_info.BatteryLevel == 2:
                return 75
            if battery_info.BatteryLevel == 3:
                return 100
except ImportError:
    messagebox.showerror("Error", "This script requires Windows and ctypes library.")
    exit()

def update_tooltip(systray):
    battery_percentage1 = get_battery_level(0)  # Battery level of the first controller
    battery_percentage2 = get_battery_level(1)  # Battery level of the second controller
    if battery_percentage1 is not None and battery_percentage2 is not None:
        systray.update(hover_text=f"Controller 1 Battery: {battery_percentage1}%, Controller 2 Battery: {battery_percentage2}%")
        if battery_percentage1 == 25:
            notification.notify(title="Controller 1 Battery Low", message="Battery is at 25%", timeout=10)
        if battery_percentage2 == 25:
            notification.notify(title="Controller 2 Battery Low", message="Battery is at 25%", timeout=10)
    elif battery_percentage1 is not None:
        systray.update(hover_text=f"Controller 1 Battery: {battery_percentage1}%")
        if battery_percentage1 == 25:
            notification.notify(title="Controller 1 Battery Low", message="Battery is at 25%", timeout=10)
    elif battery_percentage2 is not None:
        systray.update(hover_text=f"Controller 2 Battery: {battery_percentage2}%")
        if battery_percentage2 == 25:
            notification.notify(title="Controller 2 Battery Low", message="Battery is at 25%", timeout=10)
    else:
        systray.update(hover_text="No controllers connected")

def on_quit_callback(systray):
    systray.shutdown()

if __name__ == "__main__":
    image = "tray_icon.ico"
    systray = SysTrayIcon(image, "Xbox Controller Battery App", ())
    threading.Thread(target=systray.start).start()
    while True:
        update_tooltip(systray)
        time.sleep(10)  # Update every 10 seconds