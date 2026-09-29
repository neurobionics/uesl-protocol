"""Reference implementation of the UESL calculations (PROTOCOL.md, Section 5).

Usage as a library:
    from uesl import leq, device_level, uesl
    L_active  = leq(active_spl_dba)    # time series of A-weighted, FAST SPL (constant sample rate)
    L_ambient = leq(ambient_spl_dba)
    L_dev     = device_level(L_active, L_ambient)
    mean, sd, n = uesl([L_dev_trial1, L_dev_trial2, ...])

Usage from the command line (CSV with columns device, L_active, L_ambient; one row per trial):
    python uesl.py trials.csv
"""
import csv
import math
import sys
from collections import defaultdict


def leq(levels_db):
    """Equivalent continuous sound level of a time series of sound levels (dB).

    Energy-averages the samples and converts back to dB. Assumes a constant sampling rate.
    """
    levels_db = list(levels_db)
    if not levels_db:
        raise ValueError("empty time series")
    mean_energy = sum(10 ** (L / 10) for L in levels_db) / len(levels_db)
    return 10 * math.log10(mean_energy)


def device_level(L_active, L_ambient, margin_db=6.0, floor_db=35.0):
    """Device sound level for one trial, with ambient correction when needed.

    Corrects for the ambient contribution only if (L_active - L_ambient) < margin_db
    and L_active > floor_db; otherwise returns L_active unchanged.
    """
    if (L_active - L_ambient) < margin_db and L_active > floor_db:
        diff = 10 ** (L_active / 10) - 10 ** (L_ambient / 10)
        if diff <= 0:
            raise ValueError("ambient level >= active level; ambient correction is not valid")
        return 10 * math.log10(diff)
    return L_active


def uesl(device_levels):
    """UESL = arithmetic mean of per-trial device levels. Returns (mean, sample SD, n)."""
    x = list(device_levels)
    n = len(x)
    if n == 0:
        raise ValueError("no trials")
    m = sum(x) / n
    sd = math.sqrt(sum((v - m) ** 2 for v in x) / (n - 1)) if n > 1 else float("nan")
    return m, sd, n


def _main(path):
    groups = defaultdict(list)
    with open(path, newline="") as f:
        for row in csv.DictReader(f):
            groups[row["device"]].append(device_level(float(row["L_active"]), float(row["L_ambient"])))
    print(f"{'device':<30}{'UESL (dBA)':>12}{'SD (dBA)':>10}{'n':>6}")
    for dev, vals in groups.items():
        m, sd, n = uesl(vals)
        print(f"{dev:<30}{m:>12.1f}{sd:>10.1f}{n:>6d}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)
    _main(sys.argv[1])
