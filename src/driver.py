
import numpy as np
import matplotlib.pyplot as plt

from launch import min_altitude_ratio
from launch import max_altitude_ratio
from launch import min_velocity_ratio
from launch import max_velocity_ratio
from launch import launch_angle
from launch import launch_angle_range

def main():
    """plots launch angle range based on the given parameters ve_v0, alpha, and tol_alpha"""

    #keeping velocity ratio and the altitude tolerance constant
    ve_v0 = 2
    tol_alpha = 0.04
    min_angle = []
    max_angle = []
    alpha_range = np.arange(min_altitude_ratio(ve_v0), max_altitude_ratio(ve_v0), 0.05) #setting the angle range
    
    for n in alpha_range: #iterates over the possible launch angles for each n in relation to the altitude
        y = launch_angle_range(ve_v0, n, tol_alpha) #calculates the launch angle for each iteration of n
        min_angle.append(y[0]) #adding minimum angles to the array
        max_angle.append(y[1]) #adding maximum angles to the array
    
    #plotting
    plt.figure(1)
    plt.xlabel("Altitude Ratio")
    plt.ylabel("Launch Angle")
    plt.title("Maximum and Minimum launch angles for ve_v0 = 2 and tol_alpha = 0.04")
    plt.plot(alpha_range, max_angle, label = "Maximum launch angle")
    plt.plot(alpha_range, min_angle, label = "Minimum launch angle")
    plt.legend()
    plt.savefig("Graph of Launch angles vs Altitude ratio")
    

    #keeping alpha and tol_alpha constant
    alpha = 0.25
    tol_alpha = 0.04
    min_angle = []
    max_angle = []
    velocity_range = np.arange(min_velocity_ratio(alpha), max_velocity_ratio(alpha), 0.025)
    
    for n in velocity_range: #iterates over the possible launch angles for each n in relation to the velocity
        y = launch_angle_range(n, alpha, tol_alpha) #calculates the launch angle for each iteration of n
        min_angle.append(y[0]) #adding minimum angles to the array
        max_angle.append(y[1]) #adding maximum angles to the array
    
    #plotting
    plt.figure(2)
    plt.xlabel("Velocity Ratio")
    plt.ylabel("Launch Angle")
    plt.title("Maximum and Minimum launch angles for alpha = 0.25 and tol_alpha = 0.04")
    plt.plot(velocity_range, max_angle, label = "Maximum launch angle")
    plt.plot(velocity_range, min_angle, label = "Minimum launch angle")
    plt.legend()
    plt.savefig("Graph of Launch angles vs Velocity ratio")

if __name__ == "__main__":
    main()
    