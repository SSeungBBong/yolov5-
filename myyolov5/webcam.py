import cv2

# 웹캠을 연결 (기본적으로 0번 카메라 사용)
cap = cv2.VideoCapture(0)

# 카메라가 열리지 않았으면 종료
if not cap.isOpened():
    print("웹캠을 열 수 없습니다.")
    exit()

while True:
    # 웹캠으로부터 프레임 읽기
    ret, frame = cap.read()
    
    # 프레임이 잘 읽히지 않으면 종료
    if not ret:
        print("프레임을 읽을 수 없습니다.")
        break
    
    # 프레임을 화면에 출력
    cv2.imshow('Webcam', frame)

     # 'q' 키를 누르거나 창이 닫혔는지 확인
    if cv2.waitKey(1) & 0xFF == ord('q') or cv2.getWindowProperty('Webcam', cv2.WND_PROP_VISIBLE) < 1:
        break

# 웹캠 리소스 해제 및 윈도우 종료
cap.release()
cv2.destroyAllWindows()
