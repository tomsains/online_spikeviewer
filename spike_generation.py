import numpy as np
import matplotlib.pyplot as plt

def generate_lfp_with_waveform_spikes(frequency=0.001, duration=100, spike_rate=0.1, spike_duration=0.1, spike_amplitude=5, sampling_rate=1000):
    """
    Generate an LFP signal with smooth waveform spikes.
    
    Args:
    - frequency (float): The frequency of the LFP oscillation (in Hz).
    - duration (float): The duration of the signal (in seconds).
    - spike_rate (float): The rate of waveform spikes (in spikes per second).
    - spike_duration (float): The duration of each spike waveform (in seconds).
    - spike_amplitude (float): The amplitude of the spike waveform.
    - sampling_rate (int): The sampling rate of the signal (in Hz).
    
    Returns:
    - signal (ndarray): The generated LFP signal with waveform spikes.
    - time (ndarray): The time vector.
    """
    # Time vector
    time = np.arange(0, duration, 1/sampling_rate)

    # Generate the LFP signal (a noisy sinusoid or random noise can be used)
    lfp_signal = np.sin(2 * np.pi * frequency * time) + np.random.normal(0, 0.5, len(time))

    # Number of spikes to generate
    num_spikes = int(spike_rate * duration)

    # Add waveform spikes to the LFP signal
    for _ in range(num_spikes):
        # Random time point for the spike
        spike_time = np.random.uniform(0, duration)
        # Find the index of this time point
        spike_index = int(spike_time * sampling_rate)

        # Generate a waveform spike (e.g., a sinusoidal or Gaussian pulse)
        spike_start = max(spike_index - int(spike_duration * sampling_rate / 2), 0)
        spike_end = min(spike_index + int(spike_duration * sampling_rate / 2), len(time))
        
        # Create a sinusoidal spike waveform (you can replace this with any other smooth function)
        spike_waveform = spike_amplitude * np.sin(2 * np.pi * 5 * (time[spike_start:spike_end] - time[spike_start]))  # 5 Hz wave
        
        # Alternatively, you can use a Gaussian pulse for the spike:
        # spike_waveform = spike_amplitude * np.exp(-((time[spike_start:spike_end] - time[spike_index]) ** 2) / (2 * (spike_duration / 4) ** 2))

        # Add the waveform spike to the LFP signal
        lfp_signal[spike_start:spike_end] += spike_waveform
    
    return time, lfp_signal

# Generate and plot the LFP signal with waveform spikes
time, signal = generate_lfp_with_waveform_spikes(frequency=1, duration=10, spike_rate=0.2, spike_duration=0.1, spike_amplitude=5, sampling_rate=1000)

plt.figure(figsize=(10, 6))
plt.plot(time, signal, label="LFP with Waveform Spikes")
plt.title("LFP Signal with Smooth Waveform Spikes")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()
