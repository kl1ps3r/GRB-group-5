
import numpy as np


def Fully_Coded(d_m, d_d, D):
    FCFOV = 2 * np.arctan((d_m - d_d) / (2*D))

    return FCFOV

def Partially_Coded(d_m, d_d, D):
    PCFOV = 2 * np.arctan((d_m + d_d) / (2*D))
    return PCFOV

def AngRes(l_m, D):
    AR = np.arctan(l_m / D)
    return AR

def Localisation(l_d, D, sigma):
    PSL = (1 / sigma) * np.arctan(l_d / D)

    return PSL

def SolidAngle(angle1, angle2=None):
    return 4 * np.arcsin(np.sin(angle1 / 2) * np.sin(angle2 / 2))
