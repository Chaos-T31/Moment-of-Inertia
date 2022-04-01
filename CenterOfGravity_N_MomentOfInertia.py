# **************************************************************************************************************************************************************************************************** #
# ********************************************************************** 8.	Verification of force transmitted by members of given truss. ************************************************************* #
# **************************************************************************************************************************************************************************************************** #
# -@ AmiLab


'''
Note-
    - **DATA VALIDATION EXCLUDED FOR BEING CHECKED AT THE TIME OF DATA INPUT**
    - All Units of like Physical Quantities are assumed to be in same unit system.
    - All Testings have been logged into the terminal for future debuggings.
'''


# ********************************************************************** Argument / Variable Declaration (for Testing purposes) ********************************************************************** #



n_diameter = 4                                                                                                                                                  # For storing the Number of Observations made for Calculating the Radius/Diameter fo the given  knwon Disc
MSR = [8.7, 8.7, 8.7, 8.7]                                                                                                                                      # For Storing the Main Scale Reading(MSR) of the Vernier Callipers
VSR = [3, 7, 6, 4]                                                                                                                                              # For Storing the Vernier Scale Reading(VSR) of the Vernier Callipers
scale_readings = {'MSR': MSR, 'VSR': VSR}                                                                                                                       # For grouping the MSR and VSR together
lcs = [0.01, 0.01, 0.01, 0.01]                                                                                                                                  # For Storing the the Least Count fo the Verneier Callipers
n_time_period = 3                                                                                                                                               # For storing the number of Observations made for Calculating the Time Period
time4_n_vibs_turn_table = [3.56, 3.57, 3.56]                                                                                                                    # For Storing the the Time taken for the n vibrations of the Trn Table
time4_n_vibs_turn_table_N_disc = [4.10, 4.08, 4.07]                                                                                                             # For Storing the Time taken for the n vibrations of the Turn table with the given known Disc placed on top of it
time4_n_vibs_turn_table_N_specimen = [4.15, 4.16, 4.15]                                                                                                         # For Storing the Time taken for the n vibrations of the Turn table with the given unknown placed on top of it
time4_n_vibs = {'Table': time4_n_vibs_turn_table, 'TableNDisc': time4_n_vibs_turn_table_N_disc, 'TableNSpecimen': time4_n_vibs_turn_table_N_specimen}           # For grouping the above 3 time reading together
num_of_vibs = 20                                                                                                                                                # For Storing the Number of Vibrations Made
mass_of_disc = 560                                                                                                                                              # For Storing the Mass of the given known Disc



# **************************************************************************************** Section ends here ***************************************************************************************** #


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #



# ********************************************************************* For Finding the Moment of Inertia of the Unknown Specimen ******************************************************************** #


# *************************************************************** For Finding the Radius of the Given known Disc using Vernier Callipers ************************************************************** #



def findSlNo(n):                                                # For generating the Serial numbers
    return list(range(1, n + 1))

# Testing-
slno = findSlNo(4)
print(slno)


def calDiameter(scale_readings, lcs):                           # For calculating the diameters
    return list(map(lambda msr, vsr, lc: msr + vsr * lc, scale_readings[list(scale_readings.keys())[0]], scale_readings[list(scale_readings.keys())[1]], lcs))

# Testing-
diameters_of_disc = calDiameter(scale_readings, lcs)
print('Diamters =', end = ' ')
print(*diameters_of_disc, sep = ', ')


def calMean(readings, n):                                       # For calculating the Arithmetic Mean (Average) of the Readings
    return sum(readings) / n

# Testing-
mean_diameter_of_disc = calMean(diameters_of_disc, n_diameter)
print('Mean Diameter =', end = ' ')
print(mean_diameter_of_disc, sep = ', ')


def calMeanRadius(mean_diameter_of_disc):                       # For calculating the mean/average Radius of the disc
    return mean_diameter_of_disc / 2

# Testing-
mean_radius_of_disc = calMeanRadius(mean_diameter_of_disc)
print('Mean Radius =', end = ' ')
print(mean_radius_of_disc, sep = ', ')

# ********************************************************************************* Section ends here ************************************************************************************************ #

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

# ***************************** For Calculatign the Moment of Inertia of the Unkwon Specimen using the Radius of the Disc obtained in the pervious section ******************************************* #


# Finding the Mean/Average 'Time' for the n Vibration (in Seconds <Optional>)
mean_time4_n_vibs = dict.fromkeys([i for i in time4_n_vibs.keys()])
for apparatus, time in time4_n_vibs.items():
    mean_time4_n_vibs[apparatus] = calMean(time, n_time_period) * 60            # Converting Units <Minutes to Seconds> ("OPTIONAL")

print('Mean Time for Vibrations =', end = ' ')
print(mean_time4_n_vibs)


def timePeriods(mean_time4_n_vibs, num_of_vibs):                                 # For Calculating the 'Time Periods' from the Time and the number of Vibrations
    for i in mean_time4_n_vibs:
        mean_time4_n_vibs[i] = mean_time4_n_vibs[i] / num_of_vibs
    return mean_time4_n_vibs

# Testing-
time_periods = timePeriods(mean_time4_n_vibs, num_of_vibs)
print('Time Periods =', end = ' ')
print(time_periods, sep = ', ')


def calMomentOfInertiaOfDisc(mass_of_disc, radius_of_disc):                     # For calculating the Moment of Inertia(MI) of the given Disc
    return mass_of_disc * radius_of_disc ** 2 / 2

# Testing-
MI_of_disc = calMomentOfInertiaOfDisc(mass_of_disc, mean_radius_of_disc)
print('Moment of Inertia, MI of Disc (I) =', MI_of_disc)


def calMomentOfInertiaOfSpecimen(mean_time4_n_vibs, MI_of_disc):                # For calculating the Moment of Inertia(MI) of the given Unknown Specimen [by the formula: I2 = {(T2 ^ 2 - T ^ 2) * I1} / (T1 ^ 2 - T ^ 2)]
    return ((mean_time4_n_vibs[list(mean_time4_n_vibs.keys())[2]] ** 2 - mean_time4_n_vibs[list(mean_time4_n_vibs.keys())[0]] ** 2) * MI_of_disc) / (mean_time4_n_vibs[list(mean_time4_n_vibs.keys())[1]] ** 2 - mean_time4_n_vibs[list(mean_time4_n_vibs.keys())[0]] ** 2)

# Testing-
MI_of_specimen = calMomentOfInertiaOfSpecimen(mean_time4_n_vibs, MI_of_disc)
print('Moment of Inertia of the given Speciment =', MI_of_specimen)



# ********************************************************************************* Section ends here ************************************************************************************************ #

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

# ********************************************************************************* Section ends here ************************************************************************************************ #


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #




