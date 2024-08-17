from retinaface import RetinaFace
import matplotlib.pyplot as plt
import cv2

def count_people(img_path):

    img_name = img_path.split('/')[-1]

    faces = RetinaFace.detect_faces(img_path)  # 이미지에서 얼굴 정보 추출
    number_of_people = len(faces)

    img = cv2.imread(img_path)

    # 이미지의 얼굴에 네모 표시하기
    for key in faces.keys():
        face = faces[key]

        facial_area = face['facial_area']

        # 얼굴에 네모 표시
        cv2.rectangle(img=img,
                      pt1=(facial_area[2], facial_area[3]),
                      pt2=(facial_area[0], facial_area[1]),
                      color=(255, 255, 255),
                      thickness=int(2 * img.shape[0] / 1000),
                      lineType=cv2.LINE_AA)
    # 이미지에 인원수 표시하기: 이미지, 문자열, 시작 위치, 폰트 종류, 크기, 색, 두께, 선의 종류
    cv2.putText(img=img,
                text=f"{number_of_people} people",
                org=(10, int(80 * img.shape[0] / 1000)),
                fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                fontScale=3 * img.shape[0] / 1000,
                color=(0, 255, 0),
                thickness=int(4 * img.shape[0] / 1000),
                lineType=cv2.LINE_AA,
                bottomLeftOrigin=False)


    # 다른이름으로 저장하기
    cv2.imwrite(f"static/results/result_of_{img_name}", img)
    return number_of_people
