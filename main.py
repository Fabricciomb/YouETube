import os
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from pytube import YouTube, Playlist
import re

# Function to create the 'youtube' directory on the desktop if it doesn't exist.
def create_youtube_directory():
    desktop_path = os.path.expanduser("~/Desktop")
    youtube_path = os.path.join(desktop_path, "YouETube By. Fabra")
    if not os.path.exists(youtube_path):
        os.makedirs(youtube_path)
    return youtube_path

# Function to remove invalid characters from the file name
def clean_name(name):
    return re.sub(r'[\/:*?"<>|]', '', name)

# Function to download a YouTube video in the best possible quality.
def download_video(url, destination_folder, format):
    try:
        yt = YouTube(url)
        title = clean_name(yt.title)
        if format == "MP4":
            stream = yt.streams.get_highest_resolution()
        else:
            stream = yt.streams.filter(only_audio=True).first()

        if stream:
            filename = f"{title}.{format.lower()}"
            file_counter = 1
            while os.path.exists(os.path.join(destination_folder, filename)):
                filename = f"{title} ({file_counter}).{format.lower()}"
                file_counter += 1

            print(f"Downloading {format}: {title}")
            stream.download(output_path=destination_folder, filename=filename)
            #messagebox.showinfo("Download Completed", f"{title} downloaded successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
        messagebox.showerror("Error", f"An error occurred: {e}")

def download_button_clicked():
    url = url_entry.get()
    format = format_combobox.get()

    if not destination_folder_label["text"]:
        messagebox.showerror("Error", "Select a destination folder!")
        return

    destination_folder = destination_folder_label["text"]

    if 'playlist' in url.lower():
        download_playlist(url, destination_folder, format)
    else:
        download_video(url, destination_folder, format)

def select_folder():
    destination_folder = filedialog.askdirectory()
    destination_folder_label["text"] = destination_folder

# Create the main window
window = tk.Tk()
window.title("YouETube By. Fabra")

# Set the window icon
icon_path = "logo1.ico"  # Replace with your .ico file path
if os.path.exists(icon_path):
    window.iconbitmap(icon_path)

# Manually configure dark style
window.configure(bg="#000")  # Set the window background color to dark gray

# Set the font size for all elements
font = ("Arial", 14)

# Add margins to elements
margin = 5

# Load an image and resize it to 100x100 pixels
img_path = "logo1.png"
img = tk.PhotoImage(file=img_path)
img = img.subsample(3)  # Resize the image to 100x100 pixels

img_label = tk.Label(window, image=img, bg="#000")  # Set the label background color to dark gray
img_label.pack(pady=margin)

# Label and entry for the URL
url_label = tk.Label(window, text="Video URL:", font=font, bg="#000", fg="white")
url_label.pack(pady=margin)
url_entry = tk.Entry(window, width=20, font=font)
url_entry.pack(pady=margin)

# Button to select the destination folder
select_folder_button = tk.Button(window, text="Destination Folder", command=select_folder, font=font, bg="#363636", fg="white")  # Set the background color to a darker gray and text to white
select_folder_button.pack(pady=margin)

# Label to display the selected destination folder
destination_folder_label = tk.Label(window, text="", font=font, bg="#000", fg="white")  # Set the background color to dark gray and text to white

# Combobox to choose between MP3 and MP4
format_label = tk.Label(window, text="Format:", font=font, bg="#000", fg="white")  # Set the background color to dark gray and text to white
format_label.pack(pady=margin)
formats = ["MP3", "MP4"]
format_combobox = ttk.Combobox(window, values=formats, font=font)
format_combobox.set("MP4")
format_combobox.pack(pady=margin)

# Button to start the download
download_button = tk.Button(window, text="Download", command=download_button_clicked, font=font, bg="#363636", fg="white")  # Set the background color to a darker gray and text to white
download_button.pack(pady=margin)

# Configure spacing and margins
window.geometry("")
window.minsize(300, 390)  # Set the desired minimum size

# Start the GUI
window.mainloop()
