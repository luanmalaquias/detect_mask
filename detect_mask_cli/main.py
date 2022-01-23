import os
import platform
import analysisimg

def cleanScreen():
    os.system('cls') if platform.system() == "Windows" else os.system('clear')

cleanScreen()

if __name__ == "__main__":

    # List of images    
    imagens = None
    for _, _, arquivo in os.walk('./img/'):
        imagens = arquivo

    # User choose cam type
    cam_type = int(input("Cam Type:\n[1] Detect Img From File\n[2] Detect Video From Webcam\n>"))
    cleanScreen()

    # From file
    if(cam_type == 1):  
        print("[-1] Back")
        for i,img in enumerate(imagens):
            print(f"[{i}] {img}")
        menu = int(input(">"))
        cleanScreen()
        print("Detecting.. A new window was open, check it. Press Esc to exit.")
        analysisimg.analysisImg(imagens[menu])

    # From webcam
    elif(cam_type == 2):
        print("Detecting.. A new window was open, check it. Press Esc to exit.")
        analysisimg.analysisWebCam()
        
        