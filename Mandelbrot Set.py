import numpy as np
import matplotlib.pyplot as plt

# iterate Z until confirm it will go to the infinity or not and count the interate times for each pixel
def Mandelbrot_Set_Iterate(Re, Im, Max_Iter):
    
    # define Z and C where Z_n = (Z_n-1)^2 + C
    C = complex(real = Re, imag = Im)
    Z = 0.0j
    
    # find out the edege and outbound pixels and mark with gradient color values (i_iter value)
    for i_iter in range (Max_Iter):
        Z = Z**2 + C
        # judge if stop iterating: absolute value of Z must be <= 2 (or Z squre must be <= 4)
        if Z.real * Z.real + Z.imag * Z.imag > 4:
            # specify gradient colors of outbound pixels according to the iterate values
            return i_iter
    
    # specify the color of inbound pixels to Max_Iter
    return Max_Iter

# define iteration density - rows X cols
cols = 768
rows = 1024

# mark all the pixels in the figure with "0" backgroud
draw_pixel_pointer = np.zeros([rows, cols])

# define the max iteration - more iterate times more clear edge of the figure
Iter_times = 50

# mark the Mandelbrot Set pixels with the pointer
for row_index, Re in enumerate(np.linspace(-2, 0.5, num=rows)):
    for col_index, Im in enumerate(np.linspace(-1, 1, num=cols)):
        draw_pixel_pointer[row_index, col_index] = Mandelbrot_Set_Iterate(Re, Im, Iter_times)

# define figure resolution
plt.figure(dpi=200, figsize=(3,3))
# draw the figure - anti-aliased: bilinear and .T flipping the rows and columns in 2D
plt.imshow(draw_pixel_pointer.T, cmap='RdBu', interpolation='bilinear', extent=[-2, 0.5, -1, 1])
plt.xlabel("Re")
plt.ylabel('Im')

plt.show()
