import torch
import cv2
import pyttsx3
import time

# YOLOv5 모델 불러오기
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

# 음성 엔진 초기화
engine = pyttsx3.init()

# 웹캠 설정
cap = cv2.VideoCapture(0)

# 마지막으로 사람이 인식된 시간
last_detection_time = time.time()

# 사람 인식 간격 (예: 5초)
detection_interval = 5

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # YOLOv5 모델로 프레임을 처리하여 결과 얻기
    results = model(frame)

    # 결과 이미지 얻기
    img = results.render()[0]

    # 사람 인식 확인
    person_detected = False
    for detection in results.pred[0]:
        if detection[-1] == 0:  # '0'은 COCO 데이터셋에서 'person' 클래스 ID를 의미합니다.
            person_detected = True
            break

    # 사람이 인식되면 즉시 음성을 출력하고, 이후 감지 간격 시간 동안 대기
    current_time = time.time()
    if person_detected and (current_time - last_detection_time) > detection_interval:
        engine.say("안녕하세요")
        engine.runAndWait()
        last_detection_time = current_time  # 사람 인식 시간 갱신

    # 결과 출력
    cv2.imshow('YOLOv5 Object Detection', img)

    # 'q' 키를 누르거나 창이 닫혔는지 확인하여 종료
    if cv2.waitKey(1) & 0xFF == ord('q') or cv2.getWindowProperty('YOLOv5 Object Detection', cv2.WND_PROP_VISIBLE) < 1:
        break

# 자원 해제
cap.release()
cv2.destroyAllWindows()