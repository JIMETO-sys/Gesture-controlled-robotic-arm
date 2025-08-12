# Wiring Instructions for Gesture-Controlled Robotic Arm

## Overview
This document describes how to connect the hardware components for the project.

---

## 1. Raspberry Pi to PCA9685 Servo Driver
- **Connection Type:** I2C
- **Pins:**
  - Pi SDA (Pin 3) → PCA9685 SDA
  - Pi SCL (Pin 5) → PCA9685 SCL
  - Pi GND (Pin 6) → PCA9685 GND
  - Pi 3.3V (Pin 1) → PCA9685 VCC (logic)

---

## 2. PCA9685 to Servos
- Connect each servo’s **signal pin** to the PCA9685 output channel.
- Connect servo **power pins** to the 5–6V output from the buck converter.
- Connect all servo **grounds** to PCA9685 GND.

---

## 3. MPU6050 to Raspberry Pi
- **Connection Type:** I2C
- **Pins:**
  - Pi SDA (Pin 3) → MPU6050 SDA
  - Pi SCL (Pin 5) → MPU6050 SCL
  - Pi GND (Pin 6) → MPU6050 GND
  - Pi 3.3V (Pin 1) → MPU6050 VCC

---

## 4. Power Supply
- **Raspberry Pi:** Powered by official 5V 3A USB-C adapter.
- **Servos:** Powered by 11.1V LiPo battery → Buck converter → 5–6V output.
- Ensure **Pi and servos have separate power sources** to prevent voltage drops.

---

## 5. Safety Notes
- Never connect the LiPo battery directly to the Raspberry Pi.
- Use heat shrink tubing or electrical tape on all exposed connections.
- Check servo power polarity before powering on.

---

**Reference Diagrams:**  
See `/docs/circuit_diagram.png` for a visual layout.
