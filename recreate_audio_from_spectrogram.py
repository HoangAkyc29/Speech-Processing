import librosa
import librosa.display
import numpy as np
import soundfile as sf

# Giả sử bạn đã có spectrogram
def generate_audio_from_spectrogram(spectrogram, sr):
    # Chuyển đổi từ dB sang biên độ
    spectrogram_amplitude = librosa.db_to_amplitude(spectrogram)

    # Dùng iSTFT để tái tạo waveform
    y = librosa.griffinlim(spectrogram_amplitude)

    return y

# Load audio để tạo spectrogram ban đầu
file_path = r"D:\LAST PROJECT\src_code\audio\ai_voiced_Sora\Sora.mp3"
y, sr = librosa.load(file_path, sr=None)
D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)

# Tái tạo âm thanh từ spectrogram
reconstructed_audio = generate_audio_from_spectrogram(D, sr)
sf.write(r"reconstructed_audio\reconstructed_from_spectrogram.wav", reconstructed_audio, sr)
