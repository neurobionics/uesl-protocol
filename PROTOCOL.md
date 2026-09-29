# UESL Measurement Protocol

**User-Experienced Sound Level (UESL): measurement, analysis & reporting checklist**
Version 1.0 · Based on Appendix I of Bons, Thiede & Rouse, *"Sound Matters: Standardizing Audible Noise Reporting for Wearable Robots"* (in preparation)

> **Objective:** Quantify the sound of a wearable assistive device during standard operation while prioritizing **practicability**, **reproducibility**, and **ecological validity**.
>
> **Target devices:** Wearable assistive technology, including (but not limited to) prostheses and exoskeletons.
>
> **Metric:** A-weighted equivalent continuous sound level, *L*<sub>eq,A</sub>, in dBA, measured at the user's ear during intended use.

---

## 1. Equipment & instrumentation

Either instrument is appropriate. Choose based on the trade-offs below.

| | Sound level meter (SLM) | Binaural sensor unit (BSU) |
|---|---|---|
| Example | PCE 322A (PCE Instruments) | SQobold + BHS II (HEAD acoustics) |
| Cost / access | Low; widely available | Higher |
| Output | Sound level only | Full audio (~48 kHz): *L*<sub>eq,A</sub> **and** psychoacoustic metrics |
| Practicality in use | Needs a tether to a laptop for ≥ 8 Hz logging | Worn as a normal headset |

- [ ] **SLM:** calibrated **Class 2** device.
  - [ ] A-weighting (dBA)
  - [ ] **FAST** time-weighting (125 ms)
  - [ ] Recording frequency **10 Hz** (must be ≥ 8 Hz to avoid gaps in the FAST moving-average filter; this usually requires a tethered laptop)
  - [ ] Microphone extension cable, if used, is **in place during calibration**
  - [ ] Head strap & mount to hold the microphone at ear level (e.g., GoPro Head Strap 2.0)
- [ ] **BSU:** calibrated device (e.g., SQobold + BHS II).
- [ ] Calibrate to the standard reference (**94 dB @ 1 kHz**) before each session.

## 2. Test environment

- [ ] **Room type:** absorptive environment (e.g., carpeted floors, soft furnishings or curtains) to minimize reverberation and standing waves.
- [ ] **Ambient sound level:** stable and **at least 6 dB below** the expected device noise (ideally < 35 dBA).
- [ ] No significant **correlated sounds** present (e.g., treadmill noise during walking).
- [ ] **Floor surface:** commercial carpet or mat on a solid surface (reduces foot-strike noise and reverberation).

## 3. Subject setup

- [ ] **Microphone placement**
  - SLM (single microphone): at the user's **ear level, at the back of the head**.
  - BSU: headphones worn **over the ears, as normal**.
  - Ensure no hair or clothing can rub against or obstruct the microphone(s).
- [ ] **Device fitting:** fit the device according to the manufacturer's instructions (by a certified prosthetist/orthotist where applicable).
- [ ] **Clothing:** avoid loose clothing that may interfere with the device, and clothing that makes noise of its own (swishing, etc.).
- [ ] **No distance or height correction.** Free-field distance corrections over-correct in real (non-anechoic) rooms. Beyond ~0.5 m source-to-sensor distance, differences of ~10 cm (e.g., user height) are negligible.

## 4. Measurement procedure

- [ ] **Task definition** (device-dependent): a cyclic repetition of the device's intended use, for example:
  - Lower-limb prosthesis or exoskeleton: walk in a large circle around the room at a consistent pace.
  - Hand prosthesis: repeatedly pick up and set down a soft, noiseless object.
- [ ] **For each trial:**
  1. Instruct the user to keep a standard posture and avoid vocalizations.
  2. **Ambient recording:** 10 s with the user (and any team members) still and silent.
  3. Silently invite the user to begin the task; allow them to reach steady-state speed.
  4. **Active recording:** 20 s of sound-level measurement while the user performs the task.
- [ ] **Repeat** for a total of **9 valid trials**: 3 each at self-selected **slow**, **normal**, and **fast** paces. UESL scales with speed, so a range of speeds keeps an individual's preferred pace from biasing the result.

## 5. Data analysis

- [ ] Trim segments containing extraneous environmental sounds unrelated to the device.
- [ ] Compute the **equivalent continuous sound level** for both the ambient and the active recording of each trial. Decibels cannot be averaged arithmetically: average the energy, then convert back (assumes a constant sampling rate):

$$L_{eq} = 10\log_{10}\left(\frac{1}{N}\sum_{i=1}^{N} 10^{L_{p,i}/10}\right)$$

- [ ] **Determine the device sound level for each trial:**
  - If (*L*<sub>active</sub> − *L*<sub>ambient</sub>) < 6 dBA **and** *L*<sub>active</sub> > 35 dBA, correct for the ambient contribution:

$$L_{device} = 10\log_{10}\left(10^{L_{active}/10} - 10^{L_{ambient}/10}\right)$$

  - Otherwise, *L*<sub>device</sub> = *L*<sub>active</sub>.
- [ ] **UESL** = arithmetic **mean** of *L*<sub>device</sub> across all trials and subjects for the device; also compute the **standard deviation**.
- [ ] *Recommended (BSU only):* supplement UESL with psychoacoustic metrics, in particular **loudness N<sub>5</sub>** (95th-percentile loudness, sone; ISO 532-1) and **sharpness S<sub>10</sub>** (90th-percentile sharpness, acum; DIN 45692). These can be computed with MATLAB Audio Toolbox (`acousticLoudness`, `acousticSharpness`) or Python's MoSQITo toolbox.
- [ ] To describe the loud tail of a device, report **percentile levels** (e.g., *L*<sub>10</sub>, *L*<sub>1</sub>) rather than peak levels, which are sensitive to outliers and sensor resolution.

## 6. Reporting

- [ ] Report UESL as a **device- and activity-specific** value (e.g., *Open-Source Leg, level-ground walking: 47.7 dBA*).
- [ ] Include the **standard deviation** and the **number of trials**.
- [ ] Document **subject mass and height**, the trial procedure, **device settings**, environmental factors, and any **deviations** from this protocol.
- [ ] Note the instrument used (SLM or BSU). In our data, the BSU read ~2.8 dBA higher than the SLM on average.
- [ ] Note that ambient subtraction is unreliable when ambient noise approaches the active level or is not steady.
- [ ] Comply with all institutional and ethical guidelines for human-subject research.

A fill-in template is provided in [`reporting_template.csv`](reporting_template.csv).

---

### Relevant standards

- IEC 61672-1:2013: Sound level meters, specifications
- ISO 1996-1:2016: Environmental noise, basic quantities (*L*<sub>eq</sub>)
- ISO 3744:2010: Sound power levels (6 dB ambient criterion)
- ISO 532-1:2017: Loudness, Zwicker method
- DIN 45692:2009: Sharpness
