"""
Simple activity models.

To simplify things:
- Aperture effects are ignored.
- Models are agnostic to color.

"""

import numpy as np
import pytest


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


def Hab(H, a, b, rh, delta, phase):
    """Active object apparent magnitude model of Holt et al. (submitted).

    .. math::

        m = H + (5 + a rh + b) log10(rh) + 5 log10(delta)

    An inactive object has :math:`a = b = 0`.

    Holt et al. (submitted) proposed a = 1, b = -1 for long-period comets.


    Parameters
    ----------
    H : array
        Absolute magnitude.

    a : array
        Activity index linear slope with heliocentric distance (au**-1).

    b : array
        Activity index y-intercept.

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

    y = -(a * rh + b)
    return Hy(H, y, rh, delta, phase)


@pytest.mark.parametrize(
    "H,y,rh,delta,phase,expected",
    (
        [0, 0, 1, 1, 0, 0],
        [0, 0, 10, 1, 0, 5],
        [0, 0, 1, 10, 0, 5],
        [0, 0, 1, 1, 23, -2.5 * np.log10(0.4765)],
        [0, 0, 1, 1, 123, -2.5 * np.log10(1.6493)],
        [0, 0, 1, 1, 153, -2.5 * np.log10(13.1662)],
        [10, 0, 1, 1, 0, 10],
        [0, -1, 1, 1, 0, 0],
        [0, -1, 10, 1, 0, 7.5],
    ),
)
def test_Hy(H, y, rh, delta, phase, expected):
    assert np.isclose(Hy(H, y, rh, delta, phase), expected, atol=0.003)


@pytest.mark.parametrize(
    "H,a,b,rh,delta,phase,expected",
    (
        [0, 0, 0, 1, 1, 0, 0],
        [0, 1, 0, 1, 1, 0, 0],
        [0, 1, 0, 10, 1, 0, 30],
        [0, 1, -1, 10, 1, 0, 27.5],
    ),
)
def test_Hy(H, a, b, rh, delta, phase, expected):
    assert np.isclose(Hab(H, a, b, rh, delta, phase), expected, atol=0.003)
