import torch
import cv2 as cv
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Load the YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

def main():
    # Initialize the webcam
    cap = cv.VideoCapture(1)  # Assuming USB camera is at index 1
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        # Perform inference
        results = model(frame)

        # Process results to find the largest object
        largest_obj, largest_area = None, 0
        for *box, conf, cls in results.xyxy[0]:  # x1, y1, x2, y2, confidence, class
            area = (box[2] - box[0]) * (box[3] - box[1])  # Width * Height
            if area > largest_area:
                largest_obj = results.names[int(cls)]
                largest_area = area

        # If a largest object is found, speak it out
        if largest_obj:
            print(f"Largest Detected Object: {largest_obj}")
            engine.say(f"{largest_obj}")
            engine.runAndWait()

        # Display the resulting frame
        cv.imshow('Frame', frame)

        if cv.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to quit
            break

    # When everything done, release the capture
    cap.release()
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()
