import cv2
import random

# Initialize a global list to store points
clicked_points = []

# Function to be called every time the mouse events happen
def mouse_click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        clicked_points.append((x, y))
        print(f"Point added: (x={x}, y={y})")
        cv2.circle(image, (x, y), 5, (255, 0, 0), -1)
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

# Main script starts here
image_path = '0777_2.png'  # Replace with your image path
image = cv2.imread(image_path)
cv2.namedWindow('Image')
cv2.setMouseCallback('Image', mouse_click_event)

cv2.imshow('Image', image)
cv2.waitKey(10000)  # Wait for all points to be clicked

# Choose a random circle within the clicked points area
radius = 50  # Set the radius of the circle
center, radius = choose_random_circle_within(clicked_points, radius)
if center:
    cv2.circle(image, center, radius, (0, 255, 0), 2)  # Draw the circle in green
    cv2.imshow('Image with Random Circle', image)
    cv2.waitKey(0)

cv2.destroyAllWindows()
