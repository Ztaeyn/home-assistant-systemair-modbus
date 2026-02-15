# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.0.0] – 2026-02-13
### 🚀 First stable HACS release

### Added
- First stable release of **Systemair Modbus** available via HACS
- UI-based setup via Home Assistant Config Flow
- Support for Systemair SAVE ventilation units using Modbus TCP
- Sensors for temperatures, operational status, and calculated values
- Binary sensors for alarms and unit states
- Number entities for setpoints and adjustable parameters
- Select entities for operation modes (Auto, Manual, Boost, Away, etc.)
- Full support for the Home Assistant device and entity model
- English and Norwegian translations (`en`, `nb`)
- Local polling (`iot_class: local_polling`)

### Notes
- This is an unofficial community integration and is not affiliated with Systemair


## FORK Ztaeyn: Contributions from own project for owner of project to contemplate

- Climate: Added HVAC.Heating, animating the Climate entity in HA to turn red and display heating. (This was a wanted feature in my own project)
<img width="460" height="342" alt="image" src="https://github.com/user-attachments/assets/5f353fd2-2e24-4d8d-ab58-69c91abe0245" />


### TODO
- Weekly Schedule
  Enable and configure fan settings for 2 periods per day.
  <img width="793" height="354" alt="image" src="https://github.com/user-attachments/assets/5761d8dd-280a-4cc7-8c14-b764b64c81e9" />


- Estimated power usage from the heating element / TRIAC. Sensor.py
  This might differ from the models. Some doesn't have the heater, others might have a bigger one?
  <img width="567" height="506" alt="image" src="https://github.com/user-attachments/assets/37d34865-f539-4b55-a9f5-81c636374def" />


- Fireplace mode. 

