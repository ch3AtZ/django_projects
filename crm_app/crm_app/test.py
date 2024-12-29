import tkinter as tk
from tkinter import messagebox
import cv2
from PIL import Image, ImageTk
import threading

class GayGameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Are You Gay Game")

        # Initialize camera
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            messagebox.showerror("Error", "Cannot access the camera")
            root.destroy()
            return

        # Camera feed label
        self.camera_label = tk.Label(root)
        self.camera_label.pack()

        # Question label
        self.question_label = tk.Label(root, text="Are you gay?", font=("Arial", 20))
        self.question_label.pack(pady=10)

        # Buttons frame
        self.buttons_frame = tk.Frame(root)
        self.buttons_frame.pack(pady=20)

        # Yes button
        self.yes_button = tk.Button(self.buttons_frame, text="Yes", font=("Arial", 16), bg="red", fg="white")
        self.yes_button.grid(row=0, column=0, padx=20)

        # No button
        self.no_button = tk.Button(self.buttons_frame, text="No", font=("Arial", 16), bg="green", fg="white", command=self.end_game)
        self.no_button.grid(row=0, column=1, padx=20)

        # Bind hover action to the Yes button
        self.yes_button.bind("<Enter>", self.move_yes_button)

        # Start updating camera feed
        self.update_camera_feed()

    def move_yes_button(self, event):
        """Randomly move the Yes button to a new location."""
        import random
        new_x = random.randint(0, self.buttons_frame.winfo_width() - self.yes_button.winfo_width())
        new_y = random.randint(0, self.buttons_frame.winfo_height() - self.yes_button.winfo_height())
        self.yes_button.place(x=new_x, y=new_y)

    def update_camera_feed(self):
        """Update the camera feed in the Tkinter window."""
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)
            self.camera_label.imgtk = imgtk
            self.camera_label.configure(image=imgtk)
        self.root.after(10, self.update_camera_feed)

    def end_game(self):
        """End the game with a message."""
        messagebox.showinfo("Game Over", "You pressed No. The game is over!")
        self.cap.release()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = GayGameApp(root)
    root.mainloop()