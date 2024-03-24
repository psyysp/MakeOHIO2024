import cv2 as cv

def find_camera_index():
    index = 1
    while True:
        cap = cv.VideoCapture(index)
        if not cap.isOpened():
            print(f"No camera found at index {index}")
            break
        ret, frame = cap.read()
        if ret:
            cv.imshow(f'Camera at Index {index}', frame)
            print(f"Found camera at index {index}. Press 'q' to close and check next index.")
            if cv.waitKey(1000) & 0xFF == ord('q'):
                break
        cap.release()
        cv.destroyAllWindows()
        

find_camera_index()
