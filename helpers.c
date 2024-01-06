#include "helpers.h"
#include <stdio.h>
#include <stdlib.h>

void colorize(int height, int width, RGBTRIPLE image[height][width])
{
        for (int row=0; row< height; row++)
    {
        for (int unit=0; unit< width; unit++)
        {
            if (image[row][unit].rgbtBlue== 0 && image[row][unit].rgbtRed== 0 && image[row][unit].rgbtGreen== 0)
            {
                image[row][unit].rgbtBlue= rand() %256;
                image[row][unit].rgbtRed= rand() %256;
                image[row][unit].rgbtGreen= rand() %256;
                if (image[row][unit].rgbtBlue== 255 && image[row][unit].rgbtRed== 255 && image[row][unit].rgbtGreen== 255)
                {
                    image[row][unit].rgbtBlue= 0;
                }
            }
        }
    }

    // Change all black pixels to a color of your choosing
}
