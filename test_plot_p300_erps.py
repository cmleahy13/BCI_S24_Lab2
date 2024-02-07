#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 23:17:08 2024

@authors: Claire Leahy and Lexi Reinsborough
"""

""" TODO:
    
    - documentation, commenting
    - cleaning up, formatting
    - ensuring variable names are intuitive
    
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
plot_erps(target_erp, nontarget_erp, erp_times)

#%% Part 6: Discuss the ERPs

# run code for subjects 3-10
for subject_index in range(3,11):
    
    # call relevant functions
    eeg_time, eeg_data, rowcol_id, is_target = load_training_eeg(subject_index) # default path
    event_sample, is_target_event = get_events(rowcol_id, is_target)
    eeg_epochs, erp_times = epoch_data(eeg_time, eeg_data, event_sample, epoch_start_time=-0.5, epoch_end_time=1)
    target_erp, nontarget_erp = get_erps(eeg_epochs, is_target_event)
    plot_erps(target_erp, nontarget_erp, erp_times, subject_index)
    
"""

1. Repeated up/down patterns of channels?
   
    Brainwaves have a general set frequency (for multiple waves that sum, each at a different frequency). Consequently, there will likely be a repetitive nature of baseline activity. Variation (i.e. peaks) may occur due to some change in activity, whether related to the event itself, related thoughts, motion, or artifacts.
    
2. Patterns more pronounced in some channels and not others?

    Consistency of the repetitive patterns may have occurred in some channels more than others due to the relevance, or lack thereof, to the assignment at hand. For example, the central channel is located in an area that may be more closely linked to motor control compared with language, so while the proximity of the electrodes causes the overall activity to likely have extensive effects, behavior that is less concerned with the task (language, counting, concentrating, etc.) may be more rhythmic.

3. Why do some channels have positive peak ~0.5s after event?
    
    These channels may be more involved in the processing of the information presented (target or nontarget). This positive peak is most noticeable for subject 3 and occurs in channels 1, 2, 3, 5, and 6 (0-based). Subject 5 has a noticeable negative peak around 0.5 seconds after the event, however, on all channels except channel 4, which appears to be some sort of artifact. Subjects 8 and 10 also observe that negative peak around the same time for all channels except channel 7. Post-synaptic potentials, the voltage measured by EEG is measured as it serves to likely initiate (excite) an action potential. The peaks were almost always associated with the targets rather than the nontargets, suggesting the activation of neurons related to language or concentration.
    
4. Which EEG channels are these (ones above) and why?

    Visual processing of the flashes likely occurred in the occipital lobe, which only corresponded to a single channel. Frontal lobe involved in concentrating/thinking, which would be necessary for the spelling to occur; only one channel was placed on the frontal lobe. Five of the channels are involved with the parietal lobe, however, which corresponds to the number of channels exhibiting peaks for subject 3, which could make sense seeing as the parietal lobe is often involved with language and attention. Because of the poor spatial resolution of EEG, many of the electrodes are likely to measure similar occurrences, and given the proximity of the parietal lobe electrodes to one another, they could be observing the behavior of the neurons near each other's electrodes.

Using the data from all of the subjects permitted an overarching view of the general behavior. For each subject, the data produced was unique; however, some general patterns could be obsered, such as the positive or negative peaks that occurred at specific points in time relative to the event.

"""
    