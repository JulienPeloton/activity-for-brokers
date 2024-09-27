# Photometric Data for Cometary Lightcurves

This repository contains `.csv` files with photometric data for selected cases of interest. The filenames follow the format: `<objname>_<surveyname>.csv`

## Column Headers

Each `.csv` file includes the following columns:

- **mjd**: Observation time in Modified Julian Date
- **rh**: Heliocentric distance of the target (AU)
- **delta**: Geocentric distance (AU)
- **alpha**: Phase angle (degrees)
- **aper_arcsec**: Aperture size (arcseconds)
- **mag**: Observed magnitude
- **mag_err**: Magnitude uncertainty
- **filter**: Telescope filter used

## Example Lightcurves

### Synthetic Data
*To be determined (TBD).*

### Real Data Lightcurves

- **Typical Jupiter-Family Comet (JFC)**: [`19P_ATLAS.csv`](./19P_ATLAS.csv)
- **Outburst Events**: [`46P_ZTF.csv`](./46P_ZTF.csv)
- **Seasonal Effects**: [`67P_ATLAS.csv`](./67P_ATLAS.csv)
- **High Signal-to-Noise Ratio (SNR)**: [`104P_ATLAS.csv`](./104P_ATLAS.csv)
- **Solar Conjunction and Multiple Apparitions**: [`117P_ATLAS.csv`](./117P_ATLAS.csv)
- **Low SNR**: [`179P_ATLAS.csv`](./179P_ATLAS.csv)
- **Nucleus Detection**: [`459P_ATLAS.csv`](./459P_ATLAS.csv)
- **Typical Long-Period Comet (LPC)**: [`C2021S3_LOOK.csv`](./C2021S3_LOOK.csv)
- **Fading Event**: [`C2021Y1_LOOK.csv`](./C2021Y1_LOOK.csv)
- **Unique Case (Gault)**: [`Gault_ZTF.csv`](./Gault_ZTF.csv)

## Data Sources

The data presented in this repository comes from the following publications:

- Holt et al., 2024 (LOOK)
- Kelley et al., 2021 (ZTF - 46P)
- Gillan et al., *in prep* (ATLAS)

