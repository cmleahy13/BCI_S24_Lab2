#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 23:16:04 2024

@authors: Claire Leahy and Lexi Reinsborough
"""

#%% Part 1: Load the Data

# import statements
import numpy as np
from matplotlib import pyplot as plt

#%% Part 2: Extract the Event Times and Labels

# write function get_events(rowcol_id, is_target)
def get_events(rowcol_id, is_target):
    """
    Description
    -----------
    This function identifies sample indices in which there are events. These events can either be targets or nontargets. 

    Parameters
    ----------
    rowcol_id : Nx1 array of integers, where N is the total number of samples
        Input of current event type. Integers 1-6 correspond to the columns of the same number, 7-12 correspond to the rows numbered 1-6 in ascending order.
    is_target : Nx1 Boolean array, where N is the total number of samples
        Input of true when the row/column flashed contains the target letter, False otherwise. Serves as y axis (0 False, 1 True) for one of the subplots.

    Returns
    -------
    event_sample : Nx1 array of integers, where N is the number of samples in which an event occurred
        This array contains all of the sample numbers at which an event, a target flash or nontarget flash, occurred.
    is_target_event : Nx1 Boolean array, where N is the number of samples in which an event occurred
        This array contains a Boolean value of the event type in each of the relevant indices determined via event_sample. is_target_event[index] is True in cases in which the event was a target, False in the case that the event was not a target.

    """
    # array event_sample of samples when event ID went upward
    event_sample = np.where(np.diff(rowcol_id)>0)[0]+1 # index [0] accesses array from tuple
    # is_target_event[i] is True if event i was a target event
    is_target_event = is_target[event_sample] 
    
    # return event_sample and is_target_event
    return event_sample, is_target_event

#%% Part 3: Extract the Epochs

def epoch_data(eeg_time, eeg_data, event_sample, epoch_start_time=-0.5, epoch_end_time=1):
    """
    Description
    -----------

    Parameters
    ----------
    eeg_time : TYPE
        DESCRIPTION.
    eeg_data : TYPE
        DESCRIPTION.
    event_sample : TYPE
        DESCRIPTION.
    epoch_start_time : TYPE, optional
        DESCRIPTION. The default is -0.5.
    epoch_end_time : TYPE, optional
        DESCRIPTION. The default is 1.

    Returns
    -------
    eeg_epochs : TYPE
        DESCRIPTION.
    erp_times : TYPE
        DESCRIPTION.

    """
    
    # number of epochs (dimension 0)
    epoch_count = len(event_sample)
    # samples per epoch (dimension 1)
    samples_per_second = 1/(eeg_time[1]-eeg_time[0])
    seconds_per_epoch = epoch_end_time - epoch_start_time
    samples_per_epoch = int(samples_per_second*seconds_per_epoch) # cast as integer for dimensioning
    # number of channels (dimension 2)
    channel_count = len(eeg_data)
    
    # generate array to contain epoched data
    eeg_epochs = np.zeros((epoch_count, samples_per_epoch, channel_count))

    # load epochs into array
    for epoch_index in range(epoch_count): 
        for channel_index in range(channel_count):
            start_offset = int(event_sample[epoch_index]+(epoch_start_time*samples_per_second))
            for sample_index in range(samples_per_epoch):
                raw_sample = sample_index + start_offset
                eeg_epochs[epoch_index, sample_index, channel_index] = eeg_data[channel_index, raw_sample]
    
    # create erp_times variable
    erp_times = []
    for time_index in range(int(samples_per_epoch)): # stops 1 sample before 1s after event
        erp_times.append(epoch_start_time+(time_index*(1/samples_per_second)))
    
    return eeg_epochs, erp_times

#%% Part 4: Calculate the ERPs

def get_erps(eeg_epochs, is_target_event):
    """
    Description
    -----------

    Parameters
    ----------
    eeg_epochs : TYPE
        DESCRIPTION.
    is_target_event : TYPE
        DESCRIPTION.

    Returns
    -------
    target_erp : TYPE
        DESCRIPTION.
    nontarget_erp : TYPE
        DESCRIPTION.

    """
    
    # separate epochs by target or nontarget event
    target_epochs = eeg_epochs[is_target_event]
    nontarget_epochs = eeg_epochs[~is_target_event]
    
    # mean response on each channel for each event
    target_erp = np.mean(target_epochs,axis=2)
    nontarget_erp = np.mean(nontarget_epochs,axis=2)
    
    return target_erp, nontarget_erp

#%% Part 5: Plot the ERPs

def plot_erps(target_erp, nontarget_erp, erp_times):
    """
    Description
    -----------

    Parameters
    ----------
    target_erp : TYPE
        DESCRIPTION.
    nontarget_erp : TYPE
        DESCRIPTION.
    erp_times : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    # variables for looping
    channel_count = len(target_erp[1]) # same as nontarget
    
    # plot ERPs for target and nontarget trials on stacked for each channel
