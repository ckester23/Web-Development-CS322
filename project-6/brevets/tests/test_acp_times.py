"""
Nose tests for acp_times.py

Write your tests HERE AND ONLY HERE.
"""
from acp_times import open_time, close_time # added these
import arrow

import nose    # Testing framework
import logging
logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)

# For each possible brevet distance, test checkpoints every 50 km

def test_brevet_200():
    brevet_start = arrow.get('2023-02-17 00:00', "YYYY-MM-DD HH:mm")
    brevet = 200
    checkpoints = {
        0: (brevet_start, brevet_start.shift(hours=1)),
        50: (brevet_start.shift(hours=1, minutes=28), brevet_start.shift(hours=3, minutes=30)),
        100: (brevet_start.shift(hours=2, minutes=56), brevet_start.shift(hours=6, minutes=40)),
        150: (brevet_start.shift(hours=4, minutes=25), brevet_start.shift(hours=10, minutes=0)),
        200: (brevet_start.shift(hours=5, minutes=53), brevet_start.shift(hours=13, minutes=30))
    }

    for km, time_tuple in checkpoints.items(): # loop through checkpoints
        check_open, check_close = time_tuple
        assert(open_time(km, brevet, brevet_start) == check_open)
        assert(close_time(km, brevet, brevet_start) == check_close)

def test_brevet_300():
    brevet_start = arrow.get('2023-02-17 00:00', "YYYY-MM-DD HH:mm")
    brevet = 300
    checkpoints = {
        0: (brevet_start, brevet_start.shift(hours=1)),
        50: (brevet_start.shift(hours=1, minutes=28), brevet_start.shift(hours=3, minutes=30)),
        100: (brevet_start.shift(hours=2, minutes=56), brevet_start.shift(hours=6, minutes=40)),
        150: (brevet_start.shift(hours=4, minutes=25), brevet_start.shift(hours=10, minutes=0)),
        200: (brevet_start.shift(hours=5, minutes=53), brevet_start.shift(hours=13, minutes=20)),
        250: (brevet_start.shift(hours=7, minutes=27), brevet_start.shift(hours=16, minutes=40)),
        300: (brevet_start.shift(hours=9, minutes=00), brevet_start.shift(hours=20, minutes=00))
    }

    for km, time_tuple in checkpoints.items(): # loop through checkpoints
        check_open, check_close = time_tuple
        print(km)
        assert(open_time(km, brevet, brevet_start) == check_open)
        assert(close_time(km, brevet, brevet_start) == check_close)

def test_brevet_400():
    brevet_start = arrow.get('2023-02-17 00:00', "YYYY-MM-DD HH:mm")
    brevet = 400
    checkpoints = {
        0: (brevet_start, brevet_start.shift(hours=1)),
        50: (brevet_start.shift(hours=1, minutes=28), brevet_start.shift(hours=3, minutes=30)),
        100: (brevet_start.shift(hours=2, minutes=56), brevet_start.shift(hours=6, minutes=40)),
        150: (brevet_start.shift(hours=4, minutes=25), brevet_start.shift(hours=10, minutes=00)),
        200: (brevet_start.shift(hours=5, minutes=53), brevet_start.shift(hours=13, minutes=20)),
        250: (brevet_start.shift(hours=7, minutes=27), brevet_start.shift(hours=16, minutes=40)),
        300: (brevet_start.shift(hours=9, minutes=00), brevet_start.shift(hours=20, minutes=00)),
        350: (brevet_start.shift(hours=10, minutes=34), brevet_start.shift(hours=23, minutes=20)),
        400: (brevet_start.shift(hours=12, minutes=8), brevet_start.shift(hours=27, minutes=00))
    }

    for km, time_tuple in checkpoints.items(): # loop through checkpoints
        check_open, check_close = time_tuple
        print(km)
        assert(open_time(km, brevet, brevet_start) == check_open)
        assert(close_time(km, brevet, brevet_start) == check_close)

def test_brevet_600():
    brevet_start = arrow.get('2023-02-17 00:00', "YYYY-MM-DD HH:mm")
    brevet = 600
    checkpoints = {
        0: (brevet_start, brevet_start.shift(hours=1)),
        50: (brevet_start.shift(hours=1, minutes=28), brevet_start.shift(hours=3, minutes=30)),
        100: (brevet_start.shift(hours=2, minutes=56), brevet_start.shift(hours=6, minutes=40)),
        150: (brevet_start.shift(hours=4, minutes=25), brevet_start.shift(hours=10, minutes=0)),
        200: (brevet_start.shift(hours=5, minutes=53), brevet_start.shift(hours=13, minutes=20)),
        250: (brevet_start.shift(hours=7, minutes=27), brevet_start.shift(hours=16, minutes=40)),
        300: (brevet_start.shift(hours=9, minutes=00), brevet_start.shift(hours=20, minutes=00)),
        
        350: (brevet_start.shift(hours=10, minutes=34), brevet_start.shift(hours=23, minutes=20)),
        400: (brevet_start.shift(hours=12, minutes=8), brevet_start.shift(hours=26, minutes=40)),
        450: (brevet_start.shift(hours=13, minutes=48), brevet_start.shift(hours=30, minutes=00)),
        500: (brevet_start.shift(hours=15, minutes=28), brevet_start.shift(hours=33, minutes=20)),
        550: (brevet_start.shift(hours=17, minutes=8), brevet_start.shift(hours=36, minutes=40)),
        600: (brevet_start.shift(hours=18, minutes=48), brevet_start.shift(hours=40, minutes=00))
    }

    for km, time_tuple in checkpoints.items(): # loop through checkpoints
        check_open, check_close = time_tuple
        print(km)
        assert(open_time(km, brevet, brevet_start) == check_open)
        assert(close_time(km, brevet, brevet_start) == check_close)

def test_brevet_1000():    
    brevet_start = arrow.get('2023-02-17 00:00', "YYYY-MM-DD HH:mm")
    brevet = 1000
    checkpoints = {
        0: (brevet_start, brevet_start.shift(hours=1)),
        50: (brevet_start.shift(hours=1, minutes=28), brevet_start.shift(hours=3, minutes=30)),
        100: (brevet_start.shift(hours=2, minutes=56), brevet_start.shift(hours=6, minutes=40)),
        150: (brevet_start.shift(hours=4, minutes=25), brevet_start.shift(hours=10, minutes=0)),
        200: (brevet_start.shift(hours=5, minutes=53), brevet_start.shift(hours=13, minutes=20)),
        250: (brevet_start.shift(hours=7, minutes=27), brevet_start.shift(hours=16, minutes=40)),
        300: (brevet_start.shift(hours=9, minutes=00), brevet_start.shift(hours=20, minutes=00)),
        350: (brevet_start.shift(hours=10, minutes=34), brevet_start.shift(hours=23, minutes=20)),
        400: (brevet_start.shift(hours=12, minutes=8), brevet_start.shift(hours=26, minutes=40)),
        450: (brevet_start.shift(hours=13, minutes=48), brevet_start.shift(hours=30, minutes=00)),
        500: (brevet_start.shift(hours=15, minutes=28), brevet_start.shift(hours=33, minutes=20)),
        
        550: (brevet_start.shift(hours=17, minutes=8), brevet_start.shift(hours=36, minutes=40)),
        600: (brevet_start.shift(hours=18, minutes=48), brevet_start.shift(hours=40, minutes=00)),
        650: (brevet_start.shift(hours=20, minutes=35), brevet_start.shift(hours=44, minutes=23)),
        700: (brevet_start.shift(hours=22, minutes=22), brevet_start.shift(hours=48, minutes=45)),
        750: (brevet_start.shift(hours=24, minutes=9), brevet_start.shift(hours=53, minutes=8)),
        800: (brevet_start.shift(hours=25, minutes=57), brevet_start.shift(hours=57, minutes=30)),
        850: (brevet_start.shift(hours=27, minutes=44), brevet_start.shift(hours=61, minutes=53)),
        900: (brevet_start.shift(hours=29, minutes=31), brevet_start.shift(hours=66, minutes=15)),
        950: (brevet_start.shift(hours=31, minutes=18), brevet_start.shift(hours=70, minutes=38)),
        1000: (brevet_start.shift(hours=33, minutes=5), brevet_start.shift(hours=75, minutes=00)) 
    }

    for km, time_tuple in checkpoints.items(): # loop through checkpoints
        check_open, check_close = time_tuple
        print(km)
        assert(open_time(km, brevet, brevet_start) == check_open)
        assert(close_time(km, brevet, brevet_start) == check_close)
        