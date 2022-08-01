#include <iostream>
#include <opencv2/highgui.hpp>
#include <opencv2/core.hpp>
#include <opencv2/imgcodecs.hpp>

using namespace cv;
using namespace std;



int main()
{
    
    Mat image;
    image = imread("D:\\pics\\003.jpg");

    if (image.empty()) {
        cout << "Could not open or find the image" << endl;
        return -1;
    }

    namedWindow("Display window", WINDOW_AUTOSIZE);
    imshow("Display window", image);

    waitKey(0);

    //return 0;
}

