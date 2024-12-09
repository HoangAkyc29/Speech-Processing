import librosa
import librosa.display
import soundfile as sf
import numpy as np
import os

def extract_mfcc(file_path, n_mfcc=13):
    """
    Trích xuất MFCCs từ tệp âm thanh.
    """
    # Load audio file
    y, sr = librosa.load(file_path, sr=None)
    
    # Compute MFCCs
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=n_mfcc)
    
    return mfccs, sr

def reconstruct_audio_from_mfcc(mfccs, sr):
    """
    Tái tạo âm thanh từ MFCCs.
    """
    # Apply inverse MFCC to reconstruct approximate audio
    reconstructed_audio = librosa.feature.inverse.mfcc_to_audio(mfccs, sr=sr)
    
    return reconstructed_audio


# Đường dẫn tệp âm thanh đầu vào
file_path = r"D:\LAST PROJECT\src_code\audio\ai_voiced_Sora\Sora.mp3"
    
# Đường dẫn lưu âm thanh tái tạo
output_dir = r"reconstructed_audio"
output_path = os.path.join(output_dir, "reconstructed_from_mfcc.wav")
    
# Tạo thư mục lưu tệp nếu chưa tồn tại
os.makedirs(output_dir, exist_ok=True)
    
# Bước 1: Trích xuất MFCCs từ tệp âm thanh
print("Extracting MFCCs...")
mfccs, sr = extract_mfcc(file_path)
print(f"MFCCs shape: {mfccs.shape}")
    
# Bước 2: Tái tạo âm thanh từ MFCCs
print("Reconstructing audio from MFCCs...")
reconstructed_audio = reconstruct_audio_from_mfcc(mfccs, sr)
    
# Bước 3: Lưu âm thanh tái tạo
print(f"Saving reconstructed audio to {output_path}...")
sf.write(output_path, reconstructed_audio, sr)
print("Audio reconstruction completed!")
