# DataCollector
Use this to capture images and label them same time for deep learning training.

**IMPORTANT:-> **I created this for my weekend project. There is no guarantee of the code or the application. Use at your own risk.****

I have done some basic testing on **Windows 10**,
Required Python modules to compile the source code:- opencv-python, winsound, PyQt6,
Download the Application exe for Windows 10:- https://drive.google.com/file/d/1XQUKkO68bQLG3U-3f-XpTUKYua1I2TO6/view?usp=sharing,
Steps to run the exe:-
1. Download and unzip https://drive.google.com/file/d/1XQUKkO68bQLG3U-3f-XpTUKYua1I2TO6/view?usp=sharing, 
2. Put the camera id in first line of CameraSource.config , if you dont know id try numbers like:- 0, 1 , 2 ... (just any one number)
3. Run the exe application, (It may take some time when you start for first time and when you capture first image)

Second line of CameraSource.config requires float number between 0.1 to 1.0. This is image shown ratio. Sometime camera resolution is very high and full image can not be shown in the capture window. This value downgrades the size of image before showing that in the window, but the original size image is saved on the disk.

Demo Video:- https://drive.google.com/file/d/1xD1afWUUvY31kBbIqtw5oX5cUXjE0S84/view?usp=sharing


Please contribute..


