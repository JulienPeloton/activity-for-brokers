"""
Simple activity models.

To simplify things:
- Aperture effects are ignored.
- Models are agnostic to color.

"""

import numpy as np


def schleicher_marcus(phase):
    """Schleicher-Marcus phase function for cometary comae.

    The model is a combination of comet Halley at low phase angles and near-Sun
    comets at high phase angles.  For details:
    https://asteroid.lowell.edu/comet/dustphase/

    This implementation is a polynomial fit to the phase function in log-space
    as a function of degrees.


    Parameters
    ----------
    phase : array
        Sun-target-observer (phase) angle in units of deg.


    Return
    ------
    Phi : array

    """

    log_Phi = (
        -8.1755e-11 * phase**5
        + 1.6782e-8 * phase**4
        - 1.3820e-6 * phase**3
        + 0.0002205 * phase**2
        - 0.0185308 * phase
        + 0.00096156
    )
    return 10.0**log_Phi


def Hy(H, y, rh, delta, phase):
    """Active object apparent magnitude assuming activity varies as rh**y.

    .. math::

        m = H + (5 - 2.5 y) log10(rh) + 5 log10(delta)

    An inactive object has :math:`y = 0`.

    A typical comet will have :math:`y < 0`.


    Parameters
    ----------
    H : array
        Absolute magnitude.

    y : array
        Activity as a power-law function of heliocentric distance.

    rh : array
        Heliocentric distance in units of au.

    delta : array
        Observer-target distance in units of au.

    phase : array
        Sun-target-observer (phase) angle in units of deg.


    Returns
    -------
    m : array
        Apparent magnitude.

    """

    return (
        H
        + 5 * np.log10(rh * delta)
        - (2.5 * y) * np.log10(rh)
        - 2.5 * np.log10(schleicher_marcus(phase))
    )
