# Xbox Controller Battery App

This is a Python application that shows the battery levels of two Xbox controllers in the system tray. It also sends a system notification when the battery level of a controller is at 25%.

## Requirements

- Python 3
- `ctypes` library
- `infi.systray` library
- `plyer` library

## Installation

1. Clone this repository.
2. Install the required libraries:

```bash
pip install infi.systray plyer
pip install plyer
```

Usage
Run the xbox_app_tray.py script:
Check the system tray for the battery levels of the controllers.
If the battery level of a controller is at 25%, a system notification is shown.
Note
This application only works on Windows because it uses the XInput API to get the battery levels of the Xbox controllers.
