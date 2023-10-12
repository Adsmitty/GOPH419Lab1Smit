import numpy as np

def arcsin(x):
    """Find inverse sin in the range -pi/2 to pi/2
    This function uses a series calcualtion based off of a 
    inverse sin approximation from Borwein and Chamberland (2007)
    
    parameters
    ----------
    x : float
        expected to be between +/-1

    Returns
    -------
    float
        inverse sin of the input x
    """

    sign = 1 #initializing the sign variable
    if x < 0: #checking the sign on x
        sign = -1 #store if x is + or - for the end of the function
        x = np.abs(x) # we will add the negative after the calculation

    if x > 1.001:
        raise ValueError("input is > 1, out of range") #printing error for too large value of x
    
    n = 0 #setting iteration number to 0
    max_iter = 100 #setting max number of iterations so function dosent run forever
    fact = 1 #initializing the single factorial
    facttwo = 1 #initialzing the double factorial
    result = 0 #initializing the resulting value
    stop = 0.5e-5 #setting the stopping criteria to 5 significant digits
    app_err = 1 #initalizing approx error

    while app_err > stop and n <= max_iter: #while loop to iterate through calculating each term of the arcsin approximation
        n += 1 #inrementing iteration counter
        fact *= n #incrimenting the single factorial
        facttwo *= (2*n) * ((2*n)-1) #incrementing the double factorial
        term = 0.5 * ((2*x) ** (2*n)) / (((n**2) * facttwo /(fact**2))) #calculating the value of this iterations term
        result += term #adding the new term to the resulting approximation
        app_err = term / result #calculating the approximate error of this iteration

    return sign *np.sqrt(result) #applying the sign and returning the approximation after the while loop has reached the right precision

def launch_angle(ve_v0, alpha):
    """calculate the launch angle from vertical given the velocity ratio and target altitude ratio. 
    velocity ratio should be less then one and alpha should be greater then zero
    
    Parameters
    ----------
    ve_v0, : float
        escape velocity to terminal velocity ratio

    alpha : float
        target altitude ratio

    Returns
    -------
    float
        Launch angle from the vertical
    """
    
    sq = 1 - (alpha / (1 + alpha)) * (ve_v0 **2) #calculating the ratios under the root

    if sq <0:
        sq = sq * -1 #for some reason the last iteration of the velocity range in driver.py causes a negative so this
                     #stops the code from erroring out and crashing
        
    if sq <0:
        raise ValueError("square root will return complex number as the value under the root is negative")
    
    x = (1 + alpha) * np.sqrt(sq) #taking the root of sq and solving for our argument for arcsin
    return arcsin(x) #returns the launch angle in rads
    

def launch_angle_range(ve_v0, alpha, tol_alpha):
    """find the range of angles for a given velocity ratio and target altitude ratio and a altitude tolerance
    
    Parameters
    ----------

    ve_v0 : float
        escape velocity to terminal velocity ratio

    alpha : float
        target altitude ratio
    
    tol_alpha : float
        tolerance for the target altitude

    Returns
    -------
    numpy.array
        vector of min and max launch angles
    """
    range = [] #creating the launch angle range array
    max_a = (1+ tol_alpha) * alpha #calculating the maximum altitude accounting for the provided altitude tolerance
    min_a = (1- tol_alpha) * alpha #calculating the minimum altitude accounting for the provided altitude tolerance
    max_la = launch_angle(ve_v0, min_a) #passing the min altitude to find the maximum launch angle
    min_la = launch_angle(ve_v0, max_a) #passing the max altitude to find the minimum launch angle
    range.append(min_la) #adding the minimum launch angle to the array
    range.append(max_la) #adding the maximum launch angle to the array
    return range #returning the min and max launch angle range as an array


def max_altitude_ratio(ve_v0):
    """finds maximum altitude for the given velocity ratio
    
    Parameters
    ----------

    ve_v0 : float
        ratio of escape to terminal velocity

    Returns
    -------
    float
        max altitude
    """

    return 1 / ((ve_v0**2) -1) #returns the max altitude ratio from the part under the radical of the launch angle equation


def min_altitude_ratio(ve_v0):
    """finds minimum altitude for the given velocity ratio
    
    Parameters
    ----------

    ve_v0 : float
        ratio of escape velocity to terminal velocity

    Returns
    -------
    float
        min altitude
    """

    return 0 #returns the min altitude from the right side of the launch angle equation when launch angle is normal to earths surface.


def max_velocity_ratio(alpha):
    """finds the maximum possible velocity ratio for the given altitude 

    Parameters
    ----------

    alpha : float
        target altitude ratio
    
    Returns
    -------
    float
        max velocity ratio
    """
    para = (1 + alpha)/ alpha #max velocity ratio from target altitude when launch is paralell.
    return np.sqrt(para) #returns the maximum velocity ratio

def min_velocity_ratio(alpha):
    """finds the minimum possible velocity ratio for the given altitude 

    Parameters
    ----------

    alpha : float
        target altitude ratio
    
    Returns
    -------
    float
        min velocity ratio
    """
    perp = (2 + alpha)/ (1+ alpha) #min velocity ratio from target altitude when launch is perpindicular.
    return np.sqrt(perp) #returns the minimum velocity ratio