# Recognized Coordinate Information of a 1D Code Is Empty

**Problem**

During 1D code recognition, the position information returned upon successful recognition is empty sometimes.

**Solution**

The positions returned are in the same row or column. In the barcode recognition logic, the position information cannot be used to identify the four corners of the recognition rectangle. In this case, you need to handle the problem based on your own service logic.
