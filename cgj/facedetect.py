import cv2
import requests
from bs4 import BeautifulSoup

# Function to search Instagram based on a username
def search_instagram(username):
    url = f'https://www.instagram.com/{username}/'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Extract information from the Instagram profile page
        # You might need to inspect the HTML structure of Instagram to find the relevant elements
        # Update the code accordingly
        user_info = soup.find('meta', property='og:description')['content']
        return user_info
    else:
        return None

# Load the pre-trained face cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Open a connection to the camera (usually camera index 0)
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Perform face detection
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        # Perform face-related tasks (e.g., searching Instagram)
        username = 'example_username'
        instagram_info = search_instagram(username)

        if instagram_info:
            print(f"Instagram Information for {username}: {instagram_info}")
        else:
            print(f"Instagram information not found for {username}")

    # Display the resulting frame
    cv2.imshow('Face Detection', frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()
