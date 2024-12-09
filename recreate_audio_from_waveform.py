import librosa
import soundfile as sf

# Load audio
file_path = r"D:\LAST PROJECT\src_code\audio\ai_voiced_Sora\Sora.mp3"
y, sr = librosa.load(file_path, sr=None)

# Adjust pitch (n_steps > 0: tăng pitch, n_steps < 0: giảm pitch)
# Đảm bảo `n_steps` được truyền chính xác
try:
    y_pitch = librosa.effects.pitch_shift(y=y, sr=sr, n_steps=4)
except Exception as e:
    print(f"Error in pitch shifting: {e}")
    y_pitch = y  # Dùng âm thanh gốc nếu lỗi xảy ra

# Adjust speed (speed_factor > 1: tăng tốc, speed_factor < 1: giảm tốc)
speed_factor = 1.2  # Tăng tốc 20%
try:
    y_speed = librosa.effects.time_stretch(y_pitch, rate=speed_factor)
except Exception as e:
    print(f"Error in speed adjustment: {e}")
    y_speed = y_pitch  # Dùng âm thanh sau khi điều chỉnh pitch nếu lỗi xảy ra

# Save adjusted audio
output_path = r"reconstructed_audio\reconstructed_from_waveform.wav"
sf.write(output_path, y_speed, sr)
print(f"Processed audio saved to: {output_path}")
