# Firmware CI/CD with Hardware-in-the-Loop Testing

A complete continuous integration and delivery pipeline for embedded firmware, from `git push` to a verified device fleet. Firmware is built, unit-tested, flashed onto real hardware, validated by automated hardware tests, then rolled out over-the-air with automatic rollback on failure.

## Why this exists

Most embedded teams still test firmware by hand: flash a board, poke at it, hope. This project answers the question every hardware team eventually asks out loud: *how do we test and ship firmware without a human in the loop every time?*

## Pipeline overview

1. **Build** — `git push` triggers a self-hosted GitHub Actions runner that compiles the firmware with PlatformIO.
2. **Unit test** — host-side logic runs on the `native` environment. No hardware required, fast feedback.
3. **Flash** — a physically attached ESP32/STM32 dev board is flashed with the new build.
4. **Hardware-in-the-loop test** — automated tests verify real on-device behavior (boot, GPIO, serial output).
5. **Signed OTA rollout** — firmware images are signed, then staged out to a device fleet with automatic rollback if a device fails health checks.

## Stack

- **PlatformIO** — build system and dependency management
- **GitHub Actions** (self-hosted runner) — CI orchestration with real hardware attached
- **ESP32 / STM32** — target boards
- **Signed firmware images** — secure boot story

## Repo structure

\`\`\`
firmware-ci-demo/
├── .github/workflows/   # CI pipeline definition
├── docs/                # architecture notes, diagrams
├── firmware/
│   └── src/             # main.cpp and firmware source
├── hardware/            # board configs, wiring, HIL test rig notes
├── scripts/             # flash, test, and OTA rollout scripts
└── platformio.ini
\`\`\`

## Getting started

\`\`\`bash
# build for ESP32
pio run -e esp32dev

# run host-side unit tests
pio test -e native

# flash to an attached board
pio run -e esp32dev -t upload

# open serial monitor
pio device monitor
\`\`\`

## Status

Active development. See `docs/` for architecture decisions and the current build-out roadmap.# firmware-ci-demo
