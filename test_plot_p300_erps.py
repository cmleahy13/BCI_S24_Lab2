#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 23:17:08 2024

@authors: Claire Leahy and Lexi Reinsborough
"""

#%% Part 1: Load the Data

# import functions
from load_p300_data import load_training_eeg
from plot_p300_erps import get_events, epoch_data, get_erps, plot_erps

# load training data from subject 3
eeg_time, eeg_data, rowcol_id, is_target = load_training_eeg() # defaulting subject 3, P300Data directory

#%% Part 2: Extract the Event Times and Labels

# call get_events(rowcol_id, is_target)
event_sample, is_target_event = get_events(rowcol_id, is_target)

#%% Part 3: Extract the Epochs

# call epoch_data
eeg_epochs, erp_times = epoch_data(eeg_time, eeg_data, event_sample, epoch_start_time=-0.5, epoch_end_time=1)

#%% Part 4: Calculate the ERPs

# call get_erps
target_erp, nontarget_erp = get_erps(eeg_epochs, is_target_event)

#%% Part 5: Plot the ERPs

# call plot_erps
#plot_erps(target_erp, nontarget_erp, erp_times)

#%% Part 6: Discuss the ERPs

# # run code for subjects 3-10
# for subject_index in range(3,11):
    
#     # call relevant functions
#     eeg_time, eeg_data, rowcol_id, is_target = load_training_eeg(subject_index) # default path
#     event_sample, is_target_event = get_events(rowcol_id, is_target)
#     eeg_epochs, erp_times = epoch_data(eeg_time, eeg_data, event_sample, epoch_start_time=-0.5, epoch_end_time=1)
#     target_erp, nontarget_erp = get_erps(eeg_epochs, is_target_event)
#     plot_erps(target_erp, nontarget_erp, erp_times)
    
# """

# 1.
# 2.
# 3.
# 4. 

# """
    