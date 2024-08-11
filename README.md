
1. Contour Approximation :
This script approximates the contours in an image by reducing the number of points in each contour, making the curves more regular and saving the corrected image.

2. Align Borders : 
This script reads an image, detects contours, and aligns the bounding boxes of detected shapes to the nearest axis-aligned rectangle, enhancing the symmetry of shapes.

3. Detect and Count Shapes :
This code detects various geometric shapes (like triangles, squares, circles) in an image, counts the occurrences of each shape, and labels them on the output image.

4. Detect and Count Straight Lines :
This code detects straight lines in an image using the Hough Line Transform, counts the number of detected lines, and draws them on the original image.

5. Regularize Curves :
The script detects contours and approximates them with polygons, optionally smoothing the curves using polynomial fitting, and draws the regularized curves on a new image.

6. Detect Symmetric Curves :
This script identifies and counts symmetric curves in an image by comparing the original curve with its flipped versions (horizontally and vertically), highlighting symmetric contours.

7. Complete Incomplete Curves :
The script detects edges and contours in an image, then uses inpainting to fill in and complete incomplete curves based on the contour information.

8. Fit Bézier Curve :
This code fits a Bézier curve to the largest contour in an image, using control points to approximate the shape and plot it alongside the original contour.









9. Fit Ellipses to Contours :
The code detects edges, finds contours, and fits ellipses to the contours with more than 5 points, completing and visualizing incomplete curves by drawing the ellipses on the image.
