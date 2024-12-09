import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt

def extract_audio_features(file_path):
    # Load audio file
    y, sr = librosa.load(file_path, sr=None)
    
    # Plot waveform
    plt.figure(figsize=(12, 4))
    librosa.display.waveshow(y, sr=sr)
    plt.title("Waveform")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.show()

    # Compute spectrogram
    D = librosa.stft(y)  # Short-time Fourier Transform
    S_db = librosa.amplitude_to_db(np.abs(D), ref=np.max)

    plt.figure(figsize=(12, 6))
    librosa.display.specshow(S_db, sr=sr, x_axis="time", y_axis="hz", cmap="viridis")
    plt.colorbar(format="%+2.0f dB")
    plt.title("Spectrogram")
    plt.show()

    # Compute MFCCs
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)

    plt.figure(figsize=(12, 6))
    librosa.display.specshow(mfccs, x_axis="time", sr=sr, cmap="magma")
    plt.colorbar()
    plt.title("MFCC")
    plt.ylabel("MFCC Coefficients")
    plt.xlabel("Time (s)")
    plt.show()

    # Compute Zero Crossing Rate
    zcr = librosa.feature.zero_crossing_rate(y)

    plt.figure(figsize=(12, 4))
    plt.plot(zcr[0], label="Zero Crossing Rate")
    plt.title("Zero Crossing Rate Over Time")
    plt.xlabel("Frames")
    plt.ylabel("Rate")
    plt.legend()
    plt.show()

    # Spectral Centroid
    spectral_centroid = librosa.feature.spectral_centroid(y=y, sr=sr)

    plt.figure(figsize=(12, 4))
    frames = range(len(spectral_centroid[0]))
    t = librosa.frames_to_time(frames, sr=sr)
    plt.semilogy(t, spectral_centroid[0], label="Spectral Centroid")
    plt.title("Spectral Centroid Over Time")
    plt.xlabel("Time (s)")
    plt.ylabel("Frequency (Hz)")
    plt.legend()
    plt.show()

    # Combine features into a single vector
    features = np.concatenate([
        mfccs.mean(axis=1),          # Mean of MFCCs
        zcr.mean(axis=1),            # Mean of ZCR
        spectral_centroid.mean(axis=1)  # Mean of Spectral Centroid
    ], axis=0)
    
    return features

if __name__ == "__main__":
    # Replace with the path to your audio file
    file_path = r"D:\LAST PROJECT\src_code\audio\ai_voiced_Sora\Sora.mp3"
    features = extract_audio_features(file_path)
    print(f"Extracted feature vector (size {features.shape[0]}):")
    print(features)
