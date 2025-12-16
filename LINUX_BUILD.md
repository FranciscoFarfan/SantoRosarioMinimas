# Build Flet Application on Linux

PyInstaller compiles for the Operating System it is running on. To create a Linux executable, you must perform the build on a Linux environment (e.g., Ubuntu, Fedora, or WSL on Windows).

## Prerequisites

1.  **Python 3.12+**: Ensure Python is installed.
2.  **Dependencies**: Install the required system libraries for Flet and GStreamer (for audio).

    ```bash
    # Ubuntu/Debian
    sudo apt-get update
    sudo apt-get install python3-pip python3-venv libgtk-3-0 libgstreamer1.0-0 gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly gstreamer1.0-libav
    ```

## Step-by-Step Build Instructions

1.  **Clone/Copy Project**: Move your project files to the Linux environment.

2.  **Create Virtual Environment**:
    ```bash
    cd /path/to/SantoRosarioMinimas
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install Requirements**:
    ```bash
    pip install -r requirements.txt
    pip install pyinstaller
    ```

4.  **Run Build**:
    Navigate to the `src` directory and run PyInstaller with the Linux-specific spec file.
    ```bash
    cd src
    pyinstaller SantoRosario_linux.spec
    ```

5.  **Run Application**:
    The executable will be in `dist/SantoRosario`.
    ```bash
    ./dist/SantoRosario
    ```
