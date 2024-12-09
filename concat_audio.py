import os
from pydub import AudioSegment

# AudioSegment.ffmpeg = "other_lib\ffmpeg-7.1"

def concatenate_audio_in_folder(folder_path, output_file, gap_duration=300):
    """
    Nối tất cả các file âm thanh trong một thư mục với khoảng nghỉ giữa mỗi file.

    :param folder_path: Đường dẫn thư mục chứa các file âm thanh
    :param output_file: Đường dẫn file xuất ra
    :param gap_duration: Thời lượng khoảng nghỉ giữa mỗi file (ms)
    """
    # Tạo đoạn âm thanh rỗng làm khoảng nghỉ
    gap = AudioSegment.silent(duration=gap_duration)

    # Tạo audio đầu ra ban đầu là rỗng
    combined_audio = AudioSegment.empty()

    # Lấy danh sách file âm thanh trong thư mục
    audio_files = [f for f in os.listdir(folder_path) if f.endswith('.ogg')]

    # Sắp xếp danh sách file theo tên (nếu cần)
    audio_files.sort()

    if not audio_files:
        print("Không có file .ogg nào trong thư mục.")
        return

    # Nối các file âm thanh
    for audio_file in audio_files:
        file_path = os.path.join(folder_path, audio_file)
        print(f"Đang xử lý: {file_path}")
        audio = AudioSegment.from_file(file_path, format="ogg")
        combined_audio += audio + gap

    # Lưu file âm thanh đã ghép
    combined_audio.export(output_file, format="ogg")
    print(f"File đã được lưu tại: {output_file}")

# Đường dẫn thư mục chứa các file âm thanh
input_folder = "audio\Sora\sr"

# Tên file xuất ra
output = "combined_audio.ogg"

# Gọi hàm nối file
concatenate_audio_in_folder(input_folder, output)
