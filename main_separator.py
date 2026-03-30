import cv2
import os

# Caminho do vídeo
video_path = 'C:/Users/CONTAUTO/Desktop/Separador de Frame/video/6.mp4'

# Crie uma pasta para salvar os frames
output_folder = 'frames'
os.makedirs(output_folder, exist_ok=True)

# Abra o vídeo
cap = cv2.VideoCapture(video_path)

# Verificar se o vídeo foi carregado corretamente
if not cap.isOpened():
    print(f"Erro ao abrir o arquivo de vídeo. Verifique o caminho: {video_path}")
    exit()

# Inicialize um contador de frames
frame_count = 0

while True:
    # Leia um frame do vídeo
    ret, frame = cap.read()
    
    # Se não for possível ler o frame (fim do vídeo), pare
    if not ret:
        print("Não foi possível ler o frame. Fim do vídeo ou erro no arquivo.")
        break
    
    # Salve o frame como uma imagem
    frame_filename = os.path.join(output_folder, f"frame_{frame_count:04d}.jpg")
    cv2.imwrite(frame_filename, frame)
    
    # Incrementar o contador de frames
    frame_count += 1

# Libere o objeto de captura de vídeo
cap.release()

print(f"Extração concluída. {frame_count} frames foram extraídos.")
