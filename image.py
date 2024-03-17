import cv2
import random
import numpy as np

# Initialize a global list to store points
clicked_points = []

# Create an empty (white) image instead of reading from a path

# image = np.ones((height, width, 3), np.uint8) * 255  # White background
image_path = './images/0777_1.png'  # Replace with your image path
image = cv2.imread(image_path)
height, width, _ = image.shape
print(f"Image Width: {width}, Image Height: {height}")
# Function to be called every time the mouse events happen
def mouse_click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        clicked_points.append((x, y))
        print(f"Point added: (x={x}, y={y})")
        cv2.circle(image, (x, y), 5, (0, 0, 0), -1)  # Change circle color to black
        cv2.imshow('Image', image)

# Find the bounding box for the clicked points
def find_bounding_box(points):
    x_coords = [p[0] for p in points]
    y_coords = [p[1] for p in points]
    return min(x_coords), min(y_coords), max(x_coords), max(y_coords)

# Choose a random circle within the bounding box
def choose_random_circle_within(points, radius):
    xmin, ymin, xmax, ymax = find_bounding_box(points)
    # Adjust the min and max to ensure the circle stays within bounds
    xmin += radius
    xmax -= radius
    ymin += radius
    ymax -= radius
    
    if xmin >= xmax or ymin >= ymax:
        print("Bounding box too small for the given radius.")
        return None, None
    
    x = random.randint(xmin, xmax)
    y = random.randint(ymin, ymax)
    return (x, y), radius

cv2.namedWindow('Image')
cv2.setMouseCallback('Image', mouse_click_event)

cv2.imshow('Image', image)
cv2.waitKey(10000)  # Change to 0 to wait indefinitely until a key is pressed

# Choose a random circle within the clicked points area
radius = 50  # Set the radius of the circle
center, radius = choose_random_circle_within(clicked_points, radius)
if center:
    # Draw the final circle in black on a new white background image
    final_image = np.ones((height, width, 3), np.uint8) * 255  # White background
    cv2.circle(final_image, center, radius, (0, 0, 0), -1)  # Draw the circle in black
    cv2.imshow('Image with Random Circle', final_image)
    cv2.imwrite('final_image.png', final_image)  # Save the image to the current directory
    cv2.waitKey(0)

cv2.destroyAllWindows()
