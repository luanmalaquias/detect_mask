from tkinter import IntVar, Tk, Radiobutton, Button, Label
from tkinter.filedialog import askopenfilename
from analysisimg import analysisImg, analysisWebCam


main = Tk()
main.title("Detect Mask")
main.geometry(f"300x200+{(main.winfo_screenwidth()-300)//2}+{(main.winfo_screenheight()-200)//2}")

var = IntVar()

rb_file = Radiobutton(main, text="Arquivo", variable=var, value=1, command=lambda: change_widget_visibility(var))
rb_file.place(x=50, y=30)

btn_search = Button(main, text="Abrir", command=lambda:select_file())
filename = None

rb_webcam = Radiobutton(main, text="Webcam", variable=var, value=2, command=lambda: change_widget_visibility(var))
rb_webcam.place(x=50, y=70)

btn_start = Button(main, text="Iniciar detecção", command=lambda: start_detection(filename, var))
btn_start.place(x=100, y=130)

lbl_path = Label(main, text="")

def change_widget_visibility(option):
    if option.get()==1:
        btn_search.place(x=130, y=30)
        lbl_path.place(x=10, y=170)
    else:
        btn_search.place_forget()
        lbl_path.place_forget()

def select_file():
    global filename
    filename = askopenfilename()
    lbl_path.config(text=filename)

def start_detection(file, option):
    if option.get()==1:
        if file!=None and file!="":
            analysisImg(file)
        else:
            lbl_path.config(text="Caminho não selecionado")
    elif option.get()==2:
        analysisWebCam()

if __name__ == "__main__":
    while True:
        main.update_idletasks()
        main.update()