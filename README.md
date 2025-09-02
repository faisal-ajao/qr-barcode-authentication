# QR & Barcode Authentication

This project uses **OpenCV** and **Pyzbar** to scan QR codes and barcodes in real-time from a webcam feed.  
It can work in two modes:  
1. **Basic Scanner** – detects and displays the decoded data.  
2. **Authentication Mode** – compares scanned codes against an authorized list and displays **Authorized / Un-Authorized** status.

---

## Features
- Real-time QR/Barcode scanning from webcam
- Adjustable brightness using an on-screen trackbar
- Polygon overlay on detected codes
- Authentication check against stored data
- Works with both QR codes and barcodes

---

## Installation

```bash
# Clone the repository
git clone https://github.com/faisal-ajao/qr-barcode-authentication.git
cd qr-barcode-authentication
```

## Usage

### **1. Basic QR/Barcode Scanner**
```bash
python basic_scanner.py
```

### **2. Authentication Mode**
```bash
python authentication_scanner.py
```
> **Note:** For authentication mode, add authorized codes (one per line) to `authentication_data.txt`.

---

## Output Example (Video)
[![Watch the output](https://img.youtube.com/vi/rwAKQziR8cU/hqdefault.jpg)](https://youtu.be/rwAKQziR8cU?feature=shared)

---

## Project Structure
```
qr-barcode-authentication/
│
├── basic_scanner.py                # Basic QR/Barcode detection
├── authentication_scanner.py       # Authentication version
├── authentication_data.txt         # List of authorized codes
├── README.md                        # Project documentation
└── requirements.txt                 # Dependencies
```

---

## Tech Stack
- Python 3.11.5
- OpenCV
- Pyzbar
- NumPy

---

## License
This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

## Install dependencies
```bash
pip install -r requirements.txt
```
