import numpy as np

from launch import launch_angle
from launch import arcsin
from launch import launch_angle_range

#testing functions from launch

#test arcsin both positve and negative against numpys arcsin
x = 0.5
y = -0.5
actualx = arcsin(x)
actualy = arcsin(y)
expx = np.arcsin(x)
expy = np.arcsin(y)

print(f"\nTesting arcsin function of 0.5: Expected = {expx} Actual = {actualx}")
print(f"Testing arcsin function of -0.5: Expected = {expy} Actual = {actualy}")

#test launch angle
ve_v0 = 2
alpha = 0.25
actual = launch_angle(ve_v0, alpha)
#doing raw calculations for launch angle
exp = np.arcsin((1 + alpha) * (np.sqrt(1 - (alpha / (1 + alpha)) * (ve_v0**2))))

print(f"\nTesting Launch Angle function at ve_v0 = 2 and alpha = 0.25.\nExpected = {exp} Actual = {actual}")

#test launch angle range
ve_v0 = 2
alpha = 0.25
tol_alpha = 0.04
actual = launch_angle_range(ve_v0, alpha, tol_alpha)
#doing raw calculations involved in launch angle range
range = []
max_a = (1+ tol_alpha) * alpha 
min_a = (1- tol_alpha) * alpha 
max_la = np.arcsin((1 + min_a) * (np.sqrt(1 - (min_a / (1 + min_a)) * (ve_v0**2))))
min_la = np.arcsin((1 + max_a) * (np.sqrt(1 - (max_a / (1 + max_a)) * (ve_v0**2))))
range.append(min_la)
range.append(max_la)
exp = range

print(f"\nTesting Launch Angle Range function at ve_v0 = 2, alpha = 0.25 and tol_alpha = 0.04. \nExpected = {exp} Actual = {actual}")