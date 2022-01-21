def energy(density, coeff=1.0):
    """Energy associated with the diffusion model

    Parameters
    ----------

    density: array of positive integers
        Number of particles at each position i in the array
    coeff: float
        Diffusion coefficient.
    """
    from numpy import array,sum, int32

    density = array(density)

    if density.dtype != int32 and len(density) <= 0:
        raise TypeError("Inputs should be integers and array should be non-empty")
    elif any(density < 0):
        raise ValueError("Inputs should be positive")
    elif len(density.shape) != 1:
        raise TypeError("Density array should be 1D")
    else:
        return sum(density * (density -1))