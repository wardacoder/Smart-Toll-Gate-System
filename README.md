# Smart Toll Gate System

## 📌 Overview
An automated Raspberry Pi–based toll gate solution designed to detect vehicles, identify them via RFID and optional license plate recognition, measure speed and weight, calculate toll fees, and upload data to ThingSpeak for cloud monitoring and analytics.
The goal is to improve toll collection efficiency, reduce congestion, minimize human error, and enable **real-time monitoring** of toll transactions.

---

## 🚀 Features
- **Automatic Vehicle Detection** – Uses sensors and camera modules to detect vehicles approaching the toll gate.
- **License Plate Recognition** – Captures an image of the vehicle’s plate and processes it using image recognition.
- **Automated Fee Calculation** – Determines toll fees based on vehicle type or predefined rules.
- **Cloud Integration (ThingSpeak)** – Stores toll transaction data in the cloud for analytics and monitoring.
- **Real-time Dashboard** – Allows authorities to track toll operations remotely.
- **Low Latency Operation** – Processes and uploads data in seconds for smooth traffic flow.
- **Scalable Design** – Can be adapted for multiple toll booths or integrated with smart city systems.

---

## 🛠 Hardware Requirements
- Raspberry Pi (or equivalent microcontroller)
- Camera module for plate recognition
- Vehicle detection sensor (IR sensor, ultrasonic, or similar)
- Servo motor for gate control
- Internet connectivity (Wi-Fi module or Ethernet)
- Power supply for Raspberry Pi and peripherals

---

## 💻 Software Requirements
- Python 3.x
- OpenCV (for image processing & ANPR)
- ThingSpeak API
- GPIO library for hardware control
- Requests library (for API communication)

---

## 📂 File Structure
Smart-Toll-Gate-System/
- docs/
  - Smart Toll Gate System.pdf
- hardware/
  - bill_of_materials.md
- src/
  - main.py
  - config.py
  - hardware_setup.py
  - sensors.py
  - camera_module.py
  - rfid.py
  - thingspeak.py
  - alerts.py
  - keypad_module.py
  - flask_server.py
- README.md
- .gitignore
- LICENSE

---

## ⚙️ Installation
1. **Clone the Repository**
    ```bash
    git clone https://github.com/username/SmartTollGate.git
    cd SmartTollGate
    ```

2. **Install Required Packages**
    ```bash
    pip install -r requirements.txt
    ```

3. **Update Configuration**
    Open `config.py` and update:
    ```python
    WRITE_KEY = "YOUR_WRITE_KEY_HERE"
    Ch_ID = "YOUR_CHANNEL_ID_HERE"
    ```

---

## ▶️ Usage
1. Connect the Raspberry Pi to the camera and sensors.
2. Ensure internet access for cloud uploads.
3. Run the system:
    ```bash
    python src/main.py
    ```
4. Vehicle approaches ➡ plate is detected ➡ toll is calculated ➡ data is uploaded to ThingSpeak ➡ gate opens.

---

## 📊 How the System Works
1. **Vehicle Detection**  
   Sensors detect a vehicle approaching the toll gate.

2. **Plate Recognition**  
   The camera captures an image, OpenCV processes it, and extracts the license plate number.

3. **Fee Calculation**  
   The system checks the plate against vehicle type rules to determine the toll fee.

4. **Data Upload**  
   Transaction details (plate number, timestamp, toll fee) are sent to **ThingSpeak** via API.

5. **Gate Operation**  
   Servo motor opens the gate automatically if payment rules are satisfied.

---

## 🎯 Benefits
- **Faster Processing** – No manual toll collection delays.
- **Error Reduction** – Eliminates human entry mistakes.
- **Remote Access** – Cloud dashboard accessible from anywhere.
- **Scalability** – Easily deployable in multiple toll booths.
- **Data Analytics** – Historical toll data can be analyzed for traffic patterns, peak hours, and revenue forecasting.

---

## 📜 License
This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.
