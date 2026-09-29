# UESL: User-Experienced Sound Level

**A standard, low-cost protocol for measuring and reporting the audible noise of wearable robots (prostheses, exoskeletons, orthoses).**

Users care about how loud their devices are, but there have been many different approaches to measuring sound, so published numbers can't be compared directly. UESL is the A-weighted equivalent continuous sound level (*L*<sub>eq,A</sub>) measured **at the user's ear, during real use**. You need a Class 2 sound level meter, a quiet room, and 9 trials.

📋 **[Read the full protocol checklist →](PROTOCOL.md)**  ·  🖨️ **[Printable PDF](UESL_Checklist.pdf)**

## Quick start

1. **Mic at the ear:** Class 2 SLM (A-weighted, FAST 125 ms, ≥ 8 Hz) at the back of the head, or a binaural headset.
2. **Quiet, absorptive room:** ambient < 35 dBA or ≥ 6 dB below the device; carpet or mat.
3. **Each trial:** 10 s ambient (still & silent), then 20 s of steady-state use.
4. **9 trials:** 3 slow · 3 normal · 3 fast self-selected speeds.
5. **Energy-average** each trial to *L*<sub>eq</sub>; subtract ambient if within 6 dB.
6. **Report** mean ± SD over all trials & users, n trials, user mass/height, and device settings.

## Benchmark data (level-ground walking)

| Device | Category | UESL (dBA) | SD (dBA) | Trials |
|---|---|---:|---:|---:|
| No device | baseline | 35.5 | 2.3 | 72 |
| VSO – off | passive | 37.4 | 3.0 | 72 |
| MBLUE ankle exoskeleton | powered | 37.6 | 2.7 | 72 |
| Proteor Kinnex 2.0 | quasi-passive | 38.2 | 3.4 | 54 |
| Fillauer AllPro | passive | 38.6 | 2.6 | 18 |
| Ottobock Genium X4 | quasi-passive | 40.1 | 2.0 | 18 |
| Nylon pants | baseline | 41.5 | 2.8 | 72 |
| Ottobock Empower | powered | 43.6 | 2.3 | 18 |
| VSO – on | quasi-passive | 43.9 | 1.7 | 72 |
| DESR VSO | passive | 44.0 | 3.0 | 72 |
| Dephy Sidekick | powered | 44.6 | 3.4 | 72 |
| Open-Source Leg v2 – ankle | powered | 47.7 | 4.4 | 54 |
| Össur Power Knee | powered | 49.5 | 2.6 | 36 |
| Open-Source Leg v2 – knee + ankle | powered | 50.6 | 2.2 | 18 |

7 participants (4 able-bodied, 2 transtibial, 1 transfemoral). Machine-readable version: [`benchmarks.csv`](benchmarks.csv).

**Preliminary design targets:** in our (small, N = 7) cohort, the sound of a device began to have a *moderate* impact on users' willingness to wear it daily at ≈ **44.4 dBA** UESL, **12.5 sone** loudness (N<sub>5</sub>), and **1.95 acum** sharpness (S<sub>10</sub>).

## Contribute your device

Measured a device with this protocol? Please share it. Open an issue or pull request with a filled-in row of [`reporting_template.csv`](reporting_template.csv) so the benchmark can grow.

## Citation

Paper in preparation. Until it's published, please cite this repository (see [`CITATION.cff`](CITATION.cff) or the "Cite this repository" button on GitHub):

> Z. Bons, S. Thiede, and E. J. Rouse, "Sound Matters: Standardizing Audible Noise Reporting for Wearable Robots," in preparation.

## Contact

Zachary Bons · zbons@umich.edu · [Neurobionics Lab](https://neurobionics.robotics.umich.edu/), University of Michigan
Supported by the NSF Graduate Research Fellowship Program (DGE-2241144).

See [`CHANGELOG.md`](CHANGELOG.md) for protocol version history.
