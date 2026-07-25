# Firmware CI/CD with Hardware-in-the-Loop (HIL) Testing

A complete embedded firmware Continuous Integration and Continuous Delivery (CI/CD) pipeline that automatically builds, tests, flashes, validates, and deploys firmware to real hardware.

The goal of this project is to demonstrate modern DevOps practices applied to embedded systems engineering using GitHub Actions, self-hosted runners, PlatformIO, ESP32, STM32, and Hardware-in-the-Loop (HIL) testing.

---

# Project Goals

Traditional embedded development often relies on manual testing:

Developer writes code

↓

Compiles firmware

↓

Flashes hardware manually

↓

Opens Serial Monitor

↓

Checks LEDs and output

↓

Repeats

This project automates that entire workflow.

Every Git push should eventually:

```
Developer Pushes Code

↓

GitHub Repository

↓

Self-hosted GitHub Runner

↓

Compile Firmware

↓

Flash Physical Hardware

↓

Run Automated Hardware Tests

↓

Report Results

↓

(Optional)

OTA Deployment

↓

Fleet Monitoring

↓

Automatic Rollback
```

---

# Objectives

- Build firmware automatically
- Flash real embedded hardware
- Execute automated hardware tests
- Validate firmware before deployment
- Support multiple microcontroller families
- Deploy firmware over-the-air
- Provide automatic rollback on failures
- Produce a professional embedded DevOps portfolio project

---

# Hardware

Current Hardware

- Linux Build Server
- MacBook Pro (Development Machine)
- ESP32 Development Board
- STM32 Nucleo Board

Future Hardware

- Raspberry Pi 5 (Hardware Test Controller)
- Orange Pi (Network & Integration Simulator)

---

# Software Stack

## Development

- VS Code
- Git
- GitHub

## Build System

- PlatformIO
- ESP-IDF
- STM32 PlatformIO Toolchain

## Continuous Integration

- GitHub Actions
- Self-hosted GitHub Runner

## Testing

- Python
- PySerial
- PlatformIO Unit Testing

## Deployment

- Signed Firmware Images
- OTA Updates
- Rollback Logic

---

# Repository Structure

```
firmware-ci-demo/

├── .github/
│   └── workflows/
│       └── firmware.yml
│
├── docs/
│   ├── architecture.md
│   ├── roadmap.md
│   └── diagrams/
│
├── firmware/
│   ├── src/
│   ├── include/
│   ├── lib/
│   └── test/
│
├── hardware/
│   ├── esp32/
│   ├── stm32/
│   └── wiring/
│
├── scripts/
│   ├── flash.py
│   ├── serial_test.py
│   └── ota.py
│
├── platformio.ini
│
└── README.md
```

---

# Project Phases

## Phase 1

Repository Setup

Completed

- GitHub Repository
- PlatformIO Project
- Linux Build Server
- ESP32 Connected
- Serial Communication Verified
- SSH Access Configured

---

## Phase 2

Embedded Continuous Integration

Current Phase

Goal

```
Git Push

↓

GitHub

↓

Self-hosted Runner

↓

PlatformIO Build

↓

Flash ESP32

↓

Run Serial Tests

↓

PASS / FAIL
```

Tasks

- Install GitHub Runner
- Configure Runner
- Build Firmware Automatically
- Upload Firmware Automatically
- Execute Python Serial Tests
- Report Results to GitHub

Status

In Progress

Completed

- Linux server configured
- SSH working
- ESP32 connected
- /dev/ttyUSB0 verified
- PlatformIO installed
- Python configured
- PySerial installed
- GitHub Runner downloaded
- GitHub Runner configuration in progress

---

## Phase 3

Hardware-in-the-Loop Testing

Goal

Replace manual validation with automated hardware verification.

Features

- GPIO testing
- Relay controlled power cycling
- Reset control
- Boot verification
- Sensor simulation
- Failure detection

Hardware

- Raspberry Pi 5
- USB Relay Board
- ESP32
- STM32

---

## Phase 4

Multi-Board Testing

Support

- ESP32
- STM32
- Multiple firmware targets
- Parallel testing

---

## Phase 5

Docker Build Environment

Containerized builds

Benefits

- Reproducible builds
- Version isolation
- Easy onboarding
- Consistent CI

---

## Phase 6

OTA Deployment

Pipeline

```
Build

↓

Sign Firmware

↓

Upload Firmware

↓

Deploy to Test Device

↓

Health Check

↓

Deploy Fleet

↓

Rollback if Needed
```

---

## Phase 7

Production Embedded DevOps Platform

Final Features

- Hardware-in-the-loop testing
- Multi-board support
- OTA deployment
- Secure firmware signing
- Automated rollback
- Build artifacts
- Test reports
- Release management

---

# Current Architecture

```
                MacBook Pro
              Development Machine
                      │
                 git push
                      │
                      ▼
             GitHub Repository
                      │
                      ▼
        Self-hosted GitHub Runner
           Debian 13 Build Server
                      │
        ┌─────────────┴─────────────┐
        │                           │
   PlatformIO Build          Python Tests
        │                           │
        └─────────────┬─────────────┘
                      │
                  USB Serial
                      │
               /dev/ttyUSB0
                      │
                  ESP32 Board
```

---

# Future Architecture

```
                 GitHub

                    │

        Self-hosted Runner

                    │

          Docker Build Environment

                    │

         Build + Unit Tests

                    │

           Flash Firmware

                    │

      Hardware-in-the-Loop Testing

         Raspberry Pi Controller

                    │

     ┌──────────────┼───────────────┐

     │              │               │

  ESP32         STM32          Sensors

     │              │               │

      └──────────────┼───────────────┘

                     │

              Signed Firmware

                     │

             OTA Deployment

                     │

              Device Fleet
```

---

# Technologies

- Git
- GitHub
- GitHub Actions
- Self-hosted Runner
- PlatformIO
- ESP-IDF
- STM32 PlatformIO
- Python
- PySerial
- Docker
- ESP32
- STM32
- Raspberry Pi
- Linux
- Hardware-in-the-Loop Testing

---

# Project Status

Current Milestone

**Phase 2 – Embedded Continuous Integration**

Progress

- ✅ Repository created
- ✅ Linux build server configured
- ✅ SSH remote development
- ✅ ESP32 connected
- ✅ Serial communication verified
- ✅ PlatformIO installed
- ✅ Python environment configured
- ✅ GitHub Runner downloaded
- 🔄 GitHub Runner registration
- ⏳ First automated firmware build
- ⏳ Automatic flashing
- ⏳ Automated serial testing
- ⏳ GitHub Actions integration

---

# Long-Term Goal

Create a production-quality embedded firmware CI/CD pipeline demonstrating:

- Embedded Systems Engineering
- DevOps
- Firmware Automation
- Continuous Integration
- Hardware-in-the-Loop Testing
- OTA Deployment
- Embedded Software Quality Assurance

This project is intended to serve as both a learning platform and a professional portfolio demonstrating modern embedded firmware development practices.