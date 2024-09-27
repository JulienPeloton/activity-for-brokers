The file activity.py provides three photometric models that may be used for comets.  Each function takes a set of model parameters and the observing circumstances (heliocentric distance, observer-target distance, and Sun-observer-target angle), and returns apparent magnitude.

1. Hy - activity that varies as a power-law function of heliocentric distance.
2. Hab - activity that varies as a power-law function of heliocentric distance with an index that varies linearly with heliocentric distance.
3. HnHy - model for a low activity object, i.e., nucleus dominated photometry.


The functions do not account for aperture and photometric bandpass.