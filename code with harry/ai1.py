import cv2
import face_recognition

# Load a sample picture and learn how to recognize it
image = face_recognition.load_image_file("WIN_20240609_09_46_43_Pro.jpg")
face_locations = face_recognition.face_locations(image)

# Display the results
print(f"I found {len(face_locations)} face(s) in this photograph.")
for face_location in face_locations:
    top, right, bottom, left = face_location
    print(f"A face is located at pixel location Top: {top}, Left: {left}, Bottom: {bottom}, Right: {right}")

    # Draw a box around the face
    cv2.rectangle(image, (left, top), (right, bottom), (0, 0, 255), 2)

# Display the image with face box
cv2.imshow("Image", cv2.cvtColor(image, cv2.COLOR_RGB2BGR))  
cv2.waitKey(0)
cv2.destroyAllWindows()  
