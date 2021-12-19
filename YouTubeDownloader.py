import tempfile
import tkinter as tk
from tkinter import filedialog
from Downloader import Downloader


def main():
    root = tk.Tk()
    root.title('YouTube Downloader')

    canvas = tk.Canvas(root, width=600, height=300)
    canvas.grid(columnspan=3, rowspan=3)

    # variables
    global folder_path
    folder_path = tk.StringVar()
    global temp_directory
    temp_directory = tempfile.TemporaryDirectory()

    # input window
    input_links = tk.Text(root)
    input_links.grid(column=0, row=0, columnspan=3, rowspan=2, padx=10, pady=10)

    # instructions
    # instructions = tk.Label(root, text="Paste the youtube URLs into the main window. Select the output directory")
    # instructions.grid(columns=3, column=0, row=0)

    # browse button
    browse_text = tk.StringVar()
    browse_btn = tk.Button(root, textvariable=browse_text, command=lambda: select_output_folder(), height=2, width=20)
    browse_text.set("Browse output directory")
    browse_btn.grid(column=0, row=2, padx=10, pady=10)

    # output dir label
    download_path_label = tk.Label(root, text="Select the output directory", height=2, width=45)
    download_path_label.grid(column=1, row=2, columnspan=2, padx=10, pady=10)

    # download button
    download_text = tk.StringVar()
    download_text.set("Download")
    download_btn = tk.Button(root, textvariable=download_text, command=lambda: download_logic(), bg="#FF0000",
                             fg="white", height=2, width=15)
    # download_btn.grid(columns=3, column=0, row=3)
    download_btn.grid(column=0, row=3, columnspan=3, padx=10, pady=10)

    # functions
    def select_output_folder():
        path = filedialog.askdirectory()
        folder_path.set(path)
        download_path_label.config(text=path)

    def read_input_text():
        lines = input_links.get("1.0", "end-1c")
        links = lines.split('\n')
        return links

    # download logic
    def download_logic():
        links = read_input_text()
        output_dir = folder_path.get()
        downloader = Downloader(links, temp_directory, output_dir, download_text, download_path_label)
        downloader.download()

    root.mainloop()


if __name__ == "__main__":
    main()
