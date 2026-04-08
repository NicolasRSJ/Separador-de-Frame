import cv2
import os


video_path = 'C:/Users/CONTAUTO/Desktop/Separador de Frame/video/3.mp4'

output_folder = 'frames'
os.makedirs(output_folder, exist_ok=True)

video_name = os.path.splitext(os.path.basename(video_path))[0]

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print(f"Erro ao abrir o arquivo de vídeo. Verifique o caminho: {video_path}")
    exit()

total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

frame_count = 0

while True:
    ret, frame = cap.read()

    if not ret:
        print("\nNão foi possível ler o frame. Fim do vídeo ou erro no arquivo.")
        break

    frame_filename = os.path.join(output_folder, f"frame_{frame_count:04d}_{video_name}.jpg")
    cv2.imwrite(frame_filename, frame)

    frame_count += 1

    if total_frames > 0:
        porcentagem_concluida = (frame_count / total_frames) * 100
        porcentagem_restante = 100 - porcentagem_concluida
        frames_restantes = total_frames - frame_count

        print(
            f"\rGerados: {frame_count}/{total_frames} frames | "
            f"Faltam: {frames_restantes} | "
            f"Restante: {porcentagem_restante:.2f}%",
            end=""
        )

cap.release()

print(f"\nExtração concluída. {frame_count} frames foram extraídos do vídeo {video_name}.")