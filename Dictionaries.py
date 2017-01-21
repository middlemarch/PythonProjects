# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 16:42:46 2016

@author: rtfly
"""

# Below is a list of dictionaries created using the associated data guide for
# the road safety dataset


ddayofwk = {
           '1':'Sunday',
           '2':'Monday',
           '3':'Tuesday',
           '4':'Wednesday',
           '5':'Thursday',
           '6':'Friday',
           '7':'Saturday'
}

dhomearea = {
            '1':'Urban',
            '2':'Small town',
            '3':'Rural'
}

dvehtype = {
           '1':'Pedal cycle',
           '2':'Motorcycle 50cc_under',
           '3':'Motorcycle 125cc_under',
           '4':'Motorcycle 125cc_500cc',
           '5':'Motorcycle over 500cc',
           '8':'Taxi/Private hire car',
           '9':'Car',
           '10':'Minibus',
           '11':'Bus_coach',
           '16':'Ridden horse',
           '17':'Agricultural vehicle',
           '18':'Tram',
           '19':'Van_Goods 3.5 tonnes_under',
           '20':'Goods 3.5t_7.5t',
           '21':'Goods 7.5 t_over',
           '22':'Mobility scooter',
           '23':'Electric motorcycle',
           '90':'Other vehicle',
           '97':'Motorcycle_unknown cc',
           '98':'Goods_unknown weight'
}

dtowartic = {
            '0':'None',
            '1':'Articulated vehicle',
            '2':'Double_multiple trailer',
            '3':'Caravan',
            '4':'Single trailer',
            '5':'Other tow'
}

dvehmano = {
           '1':'Reversing',
           '2':'Waiting to go_held up',
           '4':'Slowing_stopping',
           '5':'Moving off',
           '6':'Uturn',
           '7':'Turning left',
           '8':'Waiting turn left',
           '9':'Turning right',
           '10':'Waiting turn right',
           '11':'Changing lane left',
           '12':'Changing lane right',
           '13':'Overtaking moving vehicle_offside',
           '14':'Overtaking static vehicle_offside',
           '15':'Overtaking_nearside',
           '16':'Going ahead lefthand bend',
           '17':'Going ahead righthand bend',
           '18':'Going ahead other'
}

dvehloc = {
          '0':'On main cway_not in restricted lane',
          '1':'Tram_Light rail track',
          '2':'Bus lane',
          '3':'Busway',
          '4':'Cycle lane on main cway',
          '5':'Cycleway_shared use footway',
          '6':'On layby or hard shoulder',
          '7':'Entering layby or hard shoulder',
          '8':'Leaving layby or hard shoulder',
          '9':'Footway',
          '10':'Not on carriageway'
}

djuncloc = {
            '0':'Not at or within 20m of junction',
            '1':'Approaching junction', 
            '2':'Cleared junction',
            '3':'Leaving roundabout',
            '4':'Entering roundabout',
            '5':'Leaving main road',
            '6':'Entering main road',
            '7':'Entering from slip road',
            '8':'Mid Junction rdabout_main road'
}

dskidot = {
           '0':'None',
           '1':'Skidded',
           '2':'Skidded and overturned',
           '3':'Jackknifed',
           '4':'Jackknifed and overturned',
           '5':'Overturned'
}

dhitincw = {
            '0':'None',
            '1':'Road works',
            '4':'Parked vehicle',
            '5':'Bridge (roof)',
            '6':'Bridge (side)',
            '7':'Bollard or refuge',
            '8':'Open door of vehicle',
            '9':'Central island of roundabout',
            '10':'Kerb',
            '11':'Other object',
            '12':'Any animal except ridden horse'
}

dvehlvcw = {
            '0':'Did not leave carriageway',
            '1':'Nearside',
            '2':'Nearside and rebounded',
            '3':'Offside on to central reservation',
            '4':'Offside on to central reservation',
            '5':'Offside on to centrl res + rebounded',
            '6':'Offside crossed central reservation',
            '7':'Offside',
            '8':'Offside and rebounded'
}

dhitoffcw = {
             '0':'None',
             '1':'Road sign or traffic signal',
             '2':'Lamp post',
             '3':'Telegraph or electricity pole',
             '4':'Tree',
             '5':'Bus stop or bus shelter',
             '6':'Central crash barrier',
             '7':'Near_Offside crash barrier',
             '8':'Submerged in water',
             '9':'Entered ditch',
             '10':'Other permanent object',
             '11':'Wall or fence'
}

dfstptimp = {  
             '0':'Did not impact',
             '1':'Front',
             '2':'Back',
             '3':'Offside',
             '4':'Nearside'
}

dvehlhd = {
           '1':'No',
           '2':'Yes'
}

djrnypurp = {
             '1':'Journey as part of work',
             '2':'Commuting to/from work',
             '3':'Taking pupil to/from school',
             '4':'Pupil riding to/from school',
             '5':'Other',
             '6':'Not known'
}

dsexdrvr = {
            '1':'Male',
            '2':'Female',
            '3':'Not known'
}

dageband = {
            '1':'0_5',
            '2':'6_10',
            '3':'11_15',
            '4':'16_20',
            '5':'21_25',
            '6':'26_35',
            '7':'36_45',
            '8':'46_55',
            '9':'56_65',
            '10':'66_75',
            '11':'Over 75'
}

dvehprop = {
            '1':'Petrol',
            '2':'Heavy oil',
            '3':'Electric',
            '4':'Steam',
            '5':'Gas',
            '6':'Petrol_Gas LPG',
            '7':'Gas_Bifuel',
            '8':'Hybrid electric',
            '9':'Gas Diesel',
            '10':'New fuel technology',
            '11':'Fuel cells',
            '12':'Electric diesel'
}
