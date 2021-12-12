import tkinter as tk
from tkinter import filedialog

root = tk.Tk()

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)

#variables
folder_path = tk.StringVar()

# input window

# instructions
instructions = tk.Label(root, text="Paste the youtube URLs into the main window. Select the output directory")
instructions.grid(columns=3, column=0, row=0)

# browse button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, command=lambda: select_output_folder(), height=2, width=20)
browse_text.set("Browse output directory")
browse_btn.grid(column=0, row=2)


# output dir label
# download_path_text = tk.StringVar()
# download_path_text.set("Select the output directory")
download_path_label = tk.Label(root, text="Select the output directory", height=2, width=45)
#download_path_label.grid(columns=2, column=1, row=2)
download_path_label.grid(column=1, row=2, columnspan=2)


# download button
download_text = tk.StringVar()
download_text.set("Download")
download_btn = tk.Button(root, textvariable=download_text, command=lambda: download_logic(), bg="#FF0000", fg="white", height=2, width=15)
#download_btn.grid(columns=3, column=0, row=3)
download_btn.grid(column=0, row=3, columnspan=3)


#functions
def select_output_folder():
    global folder_path
    path = filedialog.askdirectory()
    folder_path.set(path)
    download_path_label.config(text=path)


def download_logic():
    download_text.set("Downloading . . .")
    print(folder_path.get())


root.mainloop()
