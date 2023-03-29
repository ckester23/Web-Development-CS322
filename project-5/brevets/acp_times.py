"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders

Algorithm
https://rusa.org/pages/acp-brevet-control-times-calculator
"""
import arrow
import math

# If control_dist is longer than brev_dist_km, just use brev_dist_km
# open time is the fastest a person can go
# close time is the slowest a person can go

#  You MUST provide the following two functions
#  with these signatures. You must keep
#  these signatures even if you don't use all the
#  same arguments.
# DONE


def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
   """
    Args:
       control_dist_km:  number, control distance in kilometers
       brevet_dist_km: number, nominal distance of the brevet
           in kilometers, which must be one of 200, 300, 400, 600,
           or 1000 (the only official ACP brevet distances)
       brevet_start_time:  An arrow object
    Returns:
       An arrow object indicating the control open time.
       This will be in the same time zone as the brevet start time.

       34 km/hr max speed 0-200
       ctrl loc.    max sp.   min sp. 
       0-200        34         15 // should we do french for low dists?
       200-400      32         15
       400-600      30         15
       600 - 1000   28         11.428
       1000-1300    26         13.333
   """
   

   # SPECIAL CASES/CONDITIONS FIRST
   # if control is over brev_dist, use brev_dist-control_dist for calculations
   if (control_dist_km > brevet_dist_km):
      control_dist_km = brevet_dist_km

   # first checkpoint is always at 0
   if (control_dist_km == 0):
      return brevet_start_time

   # NOW ONTO REGULAR CALCULATIONS
   hours = 0
   minutes = 0
   if (control_dist_km <= 200):
      temp = control_dist_km / 34

      hours = math.floor(temp)
      minutes = (temp - hours) * 60
      minutes = round(minutes)

   elif (control_dist_km <= 400):
      minus_200 = control_dist_km - 200 
      temp = (200 / 34) + (minus_200 / 32)

      hours = math.floor(temp)
      minutes = (temp - hours) * 60
      minutes = round(minutes) 

   elif (control_dist_km <= 600):
      minus_200_1 = control_dist_km - 200 
      minus_200_2 = minus_200_1 - 200 
      temp = (200/34) + (200/32) + (minus_200_2/30)

      hours = math.floor(temp)
      minutes = (temp - hours) * 60
      minutes = round(minutes)

   else:
      minus_200_1 = control_dist_km - 200 
      minus_200_2 = minus_200_1 - 200
      minus_200_3 = minus_200_2 - 200 
      temp = (200/34) + (200/32) + (200/30) + (minus_200_3/28)

      hours = math.floor(temp)
      minutes = (temp - hours) * 60
      minutes = round(minutes) 

   return brevet_start_time.shift(hours=hours, minutes=minutes)


def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
   """
    Args:
       control_dist_km:  number, control distance in kilometers
          brevet_dist_km: number, nominal distance of the brevet
          in kilometers, which must be one of 200, 300, 400, 600, or 1000
          (the only official ACP brevet distances)
       brevet_start_time:  An arrow object
    Returns:
       An arrow object indicating the control close time.
       This will be in the same time zone as the brevet start time.
   """
   # SPECIAL CONDITIONS/CASES FIRST

   # control == 0: close time is exactly one hour after brev_start
   if (control_dist_km == 0):
      return brevet_start_time.shift(hours=1)


   # control<= 60: control_dist/20 + 1 instead of all the extra stuff (French Rules)
   if (control_dist_km <= 60):
      temp = (control_dist_km/20 + 1)

      hours = math.floor(temp)
      minutes = (temp-hours) * 60
      minutes = round(minutes)
      return brevet_start_time.shift(hours=hours, minutes=minutes)

   # the very last checkpoint will close at a pre-mandated time: define the times here
   mandated_endTimes = {
      200: brevet_start_time.shift(hours=13, minutes=30),
      300: brevet_start_time.shift(hours=20, minutes=00),
      400: brevet_start_time.shift(hours=27, minutes=00),
      600: brevet_start_time.shift(hours=40, minutes=00),
      1000: brevet_start_time.shift(hours=75, minutes=00)
   }

   # the last checkpoint may be equal to or up to 20% greater than brev_dist
   if (control_dist_km >= brevet_dist_km):
      return mandated_endTimes[brevet_dist_km]

   # NOW ON TO REGULAR CALCULATIONS
   hours = 0 
   minutes = 0
   if (control_dist_km <= 600):
      temp = control_dist_km / 15

      hours = math.floor(temp)
      minutes = (temp - hours) * 60
      minutes = round(minutes)

   else:
      minus_600 = control_dist_km - 600
      temp = (600/15) + (minus_600/11.428)
      
      hours = math.floor(temp)
      minutes = (temp - hours) * 60
      minutes = round(minutes)

   return brevet_start_time.shift(hours=hours, minutes=minutes)
