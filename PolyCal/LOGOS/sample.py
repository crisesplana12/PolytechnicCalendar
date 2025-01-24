import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, Toplevel
from tkcalendar import Calendar
import tkinter.messagebox as messagebox
from datetime import datetime
from PIL import Image, ImageTk, ImageOps, ImageDraw
import threading
import time
from datetime import datetime
import sqlite3
from PIL import Image, ImageTk
from tkinter.colorchooser import askcolor
import io
import os

# Geometry of the windows
WIDTH = 1024
HEIGHT = 768

DATABASE_NAME = 'polytechnic.db'

DATABASE_NAME = 'events.db'

# Delete the existing database file if it exists
if os.path.exists(DATABASE_NAME):
    os.remove(DATABASE_NAME)

# Define the init_db function
def init_db():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    # Create events table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY,
            date TEXT NOT NULL,
            title TEXT NOT NULL,
            description TEXT,
            image BLOB,
            highlight_color TEXT
        )
    ''')
    # Create notes table with username
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            title TEXT NOT NULL,
            content TEXT,
            username TEXT NOT NULL,
            highlight_color TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Call init_db to initialize the database
init_db()

# Remaining code
ctk.set_appearance_mode("Light")

STUDENT_INFO = [
    {
        "id": "2024-00253-PQ-0", "PUPid": "2024-00253-PQ-0", "name": "Cristian Esplana", "program": "BSIT 1-2", "image_path": "C:/Users/acer/Desktop/PolyCal/PolyCalendar/Profile/Cristian.png"
    },
    {
        "id": "67891", "PUPid": "2024-00002-PQ-0", "name": "Hannah Canicosa", "program": "BSIT 1-2", "image_path": "C:/Users/acer/Desktop/PolyCal/PolyCalendar/Profile/Hannah.png"
    },
    {
        "id": "2024-00156-PQ-0", "PUPid": "2024-00156-PQ-0", "name": "Cj Acosta", "program": "BSIT 1-2", "image_path": "C:/Users/acer/Desktop/PolyCal/PolyCalendar/Profile/Cj.png"
    },
    {
        "id": "78910", "PUPid": "2024-00118-PQ-0", "name": "Nicole Melican", "program": "BSIT 1-2", "image_path": "C:/Users/acer/Desktop/PolyCal/PolyCalendar/Profile/Nicole.png"
    },
    {
        "id": "2024-00107-PQ-0", "PUPid": "2024-00107-PQ-0", "name": "Edgardo Privaldos Jr", "program": "BSIT 1-2", "image_path": "C:/Users/acer/Desktop/PolyCal/PolyCalendar/Profile/Edgardo.png"
    },
    {
        "id": "89101", "PUPid": "2024-00553-PQ-1", "name": "Jennylyn Vidal", "program": "BSIT Irregular", "image_path": "C:/Users/acer/Desktop/PolyCal/PolyCalendar/Profile/Jennylyn.png"
    }
]

class LoginPage(ctk.CTkFrame):
    def __init__(self, master, on_login_success):
        super().__init__(master)
        self.master = master
        self.on_login_success = on_login_success

        self.create_background()
        self.create_header()
        self.create_login_section()

    def create_background(self):
        try:
            image_path = "C:/Users/acer/Desktop/PolyCal/bgimage.png"
            image = Image.open(image_path)
            resized_image = image.resize((1366, 768))
            tk_image = ImageTk.PhotoImage(resized_image)

            background_label = ctk.CTkLabel(self, image=tk_image, text="")
            background_label.place(x=0, y=0, relwidth=1, relheight=1)
            background_label.image = tk_image
        except FileNotFoundError:
            messagebox.showerror("Error", f"Image not found: {image_path}")

    def create_header(self):
        header_frame = ctk.CTkFrame(self, height=90, fg_color="#A8192E")
        header_frame.pack(fill="x", side="top")

        try:
            image_path = "C:/Users/acer/Desktop/PolyCal/PUPLogo.png"
            image = Image.open(image_path)
            mask = Image.new("L", (60, 60), 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0, 60, 60), fill=255)

            circular_image = ImageOps.fit(image, (60, 60), centering=(0.5, 0.5))
            circular_image.putalpha(mask)

            tk_image = ImageTk.PhotoImage(circular_image)

            image_label = ctk.CTkLabel(header_frame, image=tk_image, text="")
            image_label.image = tk_image
            image_label.pack(side="left", padx=10, pady=10)
        except FileNotFoundError:
            messagebox.showerror("Error", f"Image not found: {image_path}")

        ctk.CTkLabel(
            header_frame,
            text="PolyCal",
            font=("Arial", 30, "bold"),
            text_color="white"
        ).pack(side="left", padx=5)

    def create_login_section(self):
        login_frame = ctk.CTkFrame(self, width=300, fg_color="#FFF8DC", corner_radius=20, border_width=0)
        login_frame.pack(fill="y", padx=20, pady=60, side="right")

        try:
            image_path = "C:/Users/acer/Desktop/PolyCal/PUPLogo.png"
            image = Image.open(image_path)
            mask = Image.new("L", (60, 60), 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0, 60, 60), fill=255)

            circular_image = ImageOps.fit(image, (60, 60), centering=(0.5, 0.5))
            circular_image.putalpha(mask)

            tk_image = ImageTk.PhotoImage(circular_image)

            image_label = ctk.CTkLabel(login_frame, image=tk_image, text="")
            image_label.image = tk_image
            image_label.pack(padx=20, pady=20)
        except FileNotFoundError:
            messagebox.showerror("Error", f"Image not found: {image_path}")

        ctk.CTkLabel(
            login_frame,
            text="Login",
            font=("Arial", 24, "bold"),
            text_color="black"
        ).pack(pady=5)

        ctk.CTkLabel(
            login_frame,
            text="PUP Student ID:",
            font=("Arial", 14),
            text_color="black"
        ).pack(pady=5)

        self.studentid_entry = ctk.CTkEntry(
            login_frame,
            font=("Arial", 14),
            width=200
        )
        self.studentid_entry.pack(padx=10, pady=10)

        login_button = ctk.CTkButton(
            login_frame,
            text="Login",
            font=("Arial", 14, "bold"),
            fg_color="#FFE4C4",
            text_color="red",
            command=self.validate_login
        )
        login_button.pack(padx=20, pady=20)

        # Bind the Enter key to the validate_login method
        self.studentid_entry.bind("<Return>", lambda event: self.validate_login())

    def validate_login(self):
        student_id = self.studentid_entry.get()
        allowed_ids = [student['PUPid'] for student in STUDENT_INFO]

        if student_id.strip() and student_id in allowed_ids:
            student = next((s for s in STUDENT_INFO if s['PUPid'] == student_id), None)
            self.on_login_success(student['PUPid'])
        elif not student_id.strip():
            messagebox.showerror("Login Failed", "Student ID cannot be empty")
        else:
            messagebox.showerror("Login Failed", "Invalid Student ID")

            
def image_to_binary(image_path):
    with open(image_path, "rb") as image_file:
        return image_file.read()

def binary_to_image(binary_data):
    from io import BytesIO
    return Image.open(BytesIO(binary_data))

def insert_event(event_date, event_title, event_description, event_image, highlight_color=None):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO events (date, title, description, image, highlight_color) VALUES (?, ?, ?, ?, ?)
    ''', (event_date, event_title, event_description, event_image, highlight_color))
    conn.commit()
    conn.close()

def insert_note(note_date, note_title, note_content, PUPid, highlight_color=None):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO notes (date, title, content, username, highlight_color) VALUES (?, ?, ?, ?, ?)
    ''', (note_date, note_title, note_content, PUPid, highlight_color))
    conn.commit()
    conn.close()

def update_event_highlight(event_id, highlight_color):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE events SET highlight_color = ? WHERE id = ?
    ''', (highlight_color, event_id))
    conn.commit()
    conn.close()

def update_note_highlight(note_id, highlight_color):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE notes SET highlight_color = ? WHERE id = ?
    ''', (highlight_color, note_id))
    conn.commit()
    conn.close()

def update_event_description(event_id, description):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE events SET description = ? WHERE id = ?
    ''', (description, event_id))
    conn.commit()
    conn.close()

def fetch_event_highlight_color(event_id):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT highlight_color FROM events WHERE id = ?
    ''', (event_id,))
    highlight_color = cursor.fetchone()
    conn.close()
    return highlight_color[0] if highlight_color else None

def fetch_note_highlight_color(note_id):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT highlight_color FROM notes WHERE id = ?
    ''', (note_id,))
    highlight_color = cursor.fetchone()
    conn.close()
    return highlight_color[0] if highlight_color else None

def fetch_event_details(event_title, event_date):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT description, image FROM events WHERE title = ? AND date = ?
    ''', (event_title, event_date))
    event = cursor.fetchone()
    conn.close()
    return event

def fetch_events_by_date(event_date):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT title FROM events WHERE date = ?
    ''', (event_date,))
    events = cursor.fetchall()
    conn.close()
    return events

def fetch_notes_by_date(note_date, PUPid):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT id, title, content FROM notes WHERE date = ? AND username = ?
    ''', (note_date, PUPid))
    notes = cursor.fetchall()
    conn.close()
    return notes

def fetch_note_details(note_title, note_date):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT content FROM notes WHERE title = ? AND date = ?
    ''', (note_title, note_date))
    note = cursor.fetchone()
    conn.close()
    return note

def fetch_event_id(event_title, event_date):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT id FROM events WHERE title = ? AND date = ?
    ''', (event_title, event_date))
    event_id = cursor.fetchone()
    conn.close()
    return event_id[0] if event_id else None

def update_event_highlight(self, event_id, color):
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect('archive.db')
        cursor = conn.cursor()
            
        # Execute a query to update the event highlight color
        cursor.execute("UPDATE events SET highlight_color = ? WHERE id = ?", (color, event_id))
            
        # Commit the changes and close the database connection
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"Database error: {e}")


def fetch_events_by_title(title):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT title, date FROM events WHERE title LIKE ?
    ''', ('%' + title + '%',))
    events = cursor.fetchall()
    conn.close()
    return events

def fetch_notes_by_title(title, PUPid):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT title, date FROM notes WHERE title LIKE ? AND username = ?
    ''', ('%' + title + '%', PUPid))
    notes = cursor.fetchall()
    conn.close()
    return notes

def fetch_upcoming_events(PUPid):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT title, date FROM events WHERE date >= date('now') ORDER BY date ASC
    ''')
    events = cursor.fetchall()
    conn.close()
    return events

def fetch_all_events(self):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT date, title FROM events
    ''')
    events = cursor.fetchall()
    conn.close()
    return events

def add_highlighted_date(date):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO highlighted_dates (date) VALUES (?)
    ''', (date,))
    conn.commit()
    conn.close()

def fetch_highlighted_dates():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT date FROM highlighted_dates
    ''')
    dates = cursor.fetchall()
    conn.close()
    return [date[0] for date in dates]

def delete_highlighted_date(date):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        DELETE FROM highlighted_dates WHERE date = ?
    ''', (date,))
    conn.commit()
    conn.close()

def delete_event(event_id):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        DELETE FROM events WHERE id = ?
    ''', (event_id,))
    conn.commit()
    conn.close()

def delete_note(note_id):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        DELETE FROM notes WHERE id = ?
    ''', (note_id,))
    conn.commit()
    conn.close()

def delete_event_and_refresh(self, event_id, popup):
    delete_event(event_id)
    popup.destroy()
    messagebox.showinfo("Success", "Event deleted successfully.")
    self.update_calendar()
        
class Application(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("PolyCal")
        self.geometry("900x600")
        self.current_date = datetime.now()
        self.show_login_page()

    def show_login_page(self):
        if hasattr(self, 'main_interface'):
            self.main_interface.pack_forget()
        self.login_page = LoginPage(self, self.on_login_success)
        self.login_page.pack(fill="both", expand=True)

    def on_login_success(self, PUPid):
        self.logged_in_PUPid = PUPid
        self.login_page.pack_forget()
        self.show_main_interface(PUPid)

    def show_main_interface(self, PUPid):
        if hasattr(self, 'main_interface'):
            self.main_interface.pack_forget()

        self.main_interface = ctk.CTkFrame(self)
        self.main_interface.pack(fill="both", expand=True)

        self.create_header()
        self.create_footer()
        self.create_sidebar(PUPid)
        self.create_calendar()

    def create_header(self):
        header_frame = ctk.CTkFrame(self.main_interface, height=90, fg_color="#A8192E")
        header_frame.pack(fill="x", side="top")

        try:
            image_path = "C:/Users/acer/Desktop/PolyCal/PUPLogo.png"
            image = Image.open(image_path)
            mask = Image.new("L", (60, 60), 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0, 60, 60), fill=255)

            circular_image = ImageOps.fit(image, (60, 60), centering=(0.5, 0.5))
            circular_image.putalpha(mask)

            tk_image = ImageTk.PhotoImage(circular_image)

            image_label = ctk.CTkLabel(header_frame, image=tk_image, text="")
            image_label.image = tk_image
            image_label.pack(side="left", padx=10, pady=10)
        except FileNotFoundError:
            messagebox.showerror("Error", f"Image not found: {image_path}")
        ctk.CTkLabel(
            header_frame,
            text="PolyCal",
            font=("Arial", 30, "bold"),
            text_color="white"
        ).pack(side="left", padx=5)
    
        self.search_entry = ctk.CTkEntry(header_frame, placeholder_text="Search by Title", width=200)
        self.search_entry.pack(side="left", padx=10, pady=10)
    
        search_button = ctk.CTkButton(
            header_frame,
            text="Search",
            font=("Arial", 14, "bold"),
            fg_color="#FFE4C4",
            text_color="red",
            command=self.search_by_title
        )
        search_button.pack(side="left", padx=10)

        sign_out_button = ctk.CTkButton(
            header_frame,
            text="Sign Out",
            font=("Arial", 14, "bold"),
            fg_color="#FFE4C4",
            text_color="red",
            command=self.sign_out
        )
        sign_out_button.pack(side="right", padx=30)

    def search_by_title(self):
        search_title = self.search_entry.get().strip()
        if not search_title:
            messagebox.showerror("Error", "Search title cannot be empty.")
            return

        events_with_title = fetch_events_by_title(search_title)
        notes_with_title = fetch_notes_by_title(search_title, self.logged_in_username)

        if not events_with_title and not notes_with_title:
            messagebox.showinfo("No Events or Notes", "There are no events or notes with this title.")
            return

        popup = Toplevel(self)
        popup.title("Search Results")
        popup.geometry("400x600")

        if events_with_title:
            for event_data in events_with_title:
                event_title = event_data[0]
                event_date = event_data[1]
                event_details = fetch_event_details(event_title, event_date)

                if event_details:
                    event_description, event_image_data = event_details
                    if event_image_data:
                        if isinstance(event_image_data, str):
                            event_image_data = event_image_data.encode()  # Ensure it's bytes-like
                        event_image = Image.open(io.BytesIO(event_image_data))
                    else:
                        event_image = None
                else:
                    event_description = "No description available."
                    event_image = None

                title_label = ctk.CTkLabel(popup, text=f"Event: {event_title}", font=("Arial", 16))
                title_label.pack(pady=10)

                date_label = ctk.CTkLabel(popup, text=f"Date: {event_date}", font=("Arial", 14))
                date_label.pack(pady=5)

                description_label = ctk.CTkLabel(popup, text="Description:", font=("Arial", 14))
                description_label.pack(pady=5)
                description_text = ctk.CTkTextbox(popup, height=60, width=300)
                description_text.insert("1.0", event_description)
                description_text.pack(pady=5)

                if event_image:
                    img_tk = ImageTk.PhotoImage(event_image)
                    img_label = ctk.CTkLabel(popup, image=img_tk)
                    img_label.image = img_tk
                    img_label.pack(pady=30)

                save_button = ctk.CTkButton(popup, text="Save Description", command=lambda: self.save_description(event_title, event_date, description_text.get("1.0", "end-1c")))
                save_button.pack(pady=10)

                feedback_label = ctk.CTkLabel(popup, text="Feedback:", font=("Arial", 14))
                feedback_label.pack(pady=5)
                feedback_text = ctk.CTkTextbox(popup, height=60, width=300)
                feedback_text.pack(pady=5)

                save_feedback_button = ctk.CTkButton(popup, text="Save Feedback", command=lambda: self.save_feedback(event_title, event_date, feedback_text.get("1.0", "end-1c")))
                save_feedback_button.pack(pady=10)

        if notes_with_title:
            for note_data in notes_with_title:
                note_title = note_data[0]
                note_date = note_data[1]
                note_details = fetch_note_details(note_title, note_date)

                if note_details:
                    note_content = note_details[0]
                else:
                    note_content = "No content available."

                note_title_label = ctk.CTkLabel(popup, text=f"Note: {note_title}", font=("Arial", 16))
                note_title_label.pack(pady=10)

                note_date_label = ctk.CTkLabel(popup, text=f"Date: {note_date}", font=("Arial", 14))
                note_date_label.pack(pady=5)

                note_content_label = ctk.CTkLabel(popup, text="Content:", font=("Arial", 14))
                note_content_label.pack(pady=5)
                note_content_text = ctk.CTkTextbox(popup, height=60, width=300)
                note_content_text.insert("1.0", note_content)
                note_content_text.pack(pady=5)

                save_note_button = ctk.CTkButton(popup, text="Save Content", command=lambda: self.save_note_content(note_title, note_date, note_content_text.get("1.0", "end-1c")))
                save_note_button.pack(pady=10)

        popup.mainloop()


    def create_sidebar(self, PUPid):
        sidebar = ctk.CTkFrame(self.main_interface, width=200, fg_color="#ffe4c4", corner_radius=15, border_width=0)
        sidebar.pack(side="left", padx=40, pady=20)
        student = next((s for s in STUDENT_INFO if s['PUPid'] == PUPid), None)

        if student:
            try:
                image_path = student['image_path']
                image = Image.open(image_path)
                circular_image = ImageOps.fit(image, (100, 100), centering=(0.5, 0.5))
                tk_image = ImageTk.PhotoImage(circular_image)

                image_label = ctk.CTkLabel(sidebar, image=tk_image, text="")
                image_label.image = tk_image
                image_label.pack(pady=5)
            except FileNotFoundError:
                messagebox.showerror("Error", f"Image not found: {image_path}")

            ctk.CTkLabel(
                sidebar,
                text=f"  Welcome, {student['name']}!  ",
                font=("Arial", 18, "bold"),
                text_color="#A8192E"
            ).pack(pady=10, padx=20)

            ctk.CTkLabel(
                sidebar,
                text=f"ID: {student['id']}\nProgram: {student['program']}",
                font=("Arial", 14),
                text_color="#A8192E"
            ).pack(pady=8)

            ctk.CTkButton(
                sidebar,
                text="Add Event",
                font=("Arial", 12, "bold"),
                fg_color="#A8192E",
                text_color="white",
                command=self.option_add
            ).pack(pady=5)

            ctk.CTkButton(
                sidebar,
                text="View Events",
                font=("Arial", 12, "bold"),
                fg_color="#A8192E",
                text_color="white",
                command=self.view_events
            ).pack(pady=5)

            ctk.CTkButton(
                sidebar,
                text="Add Notes",
                font=("Arial", 12, "bold"),
                fg_color="#A8192E",
                text_color="white",
                command=self.add_notes
            ).pack(pady=5)

            ctk.CTkButton(
                sidebar,
                text="View Notes",
                font=("Arial", 12, "bold"),
                fg_color="#A8192E",
                text_color="white",
                command=self.view_notes
            ).pack(pady=5)


    def add_notes(self):
        selected_date = self.calendar_widget.get_date()
        note_title = ctk.CTkInputDialog(text="Enter Note Title", title="Add Note").get_input()

        if not note_title:
            messagebox.showerror("Error", "Note title cannot be empty.")
            return

        note_content = ctk.CTkInputDialog(text="Enter Note Content", title="Add Content").get_input()

        if not note_content:
            messagebox.showerror("Error", "Note content cannot be empty.")
            return

        # Insert the note into the database with the username and default highlight color
        insert_note(selected_date, note_title, note_content, self.logged_in_username)

        messagebox.showinfo("Success", f"Note '{note_title}' added on {selected_date}.")
        self.update_calendar()

    def option_add(self):
        event_date = self.calendar_widget.get_date()
        event_title = ctk.CTkInputDialog(text="Enter Event Title", title="Add Event").get_input()

        if not event_title:
            messagebox.showerror("Error", "Event title cannot be empty.")
            return

        event_description = ctk.CTkInputDialog(text="Enter Event Description", title="Add Description").get_input()

        # Ask for an image (optional)
        image_path = ctk.CTkInputDialog(text="Enter image path for the event (optional)", title="Add Image").get_input()
        event_image = None
        if image_path:
            event_image = image_to_binary(image_path)

        # Insert the event into the database with the default highlight color
        insert_event(event_date, event_title, event_description, event_image)

        messagebox.showinfo("Success", f"Event '{event_title}' added on {event_date}.")
        self.update_calendar()

    def view_events(self):
        selected_date = self.calendar_widget.get_date()
        events_on_date = fetch_events_by_date(selected_date)

        if not events_on_date:
            messagebox.showinfo("No Event", "No event found for this date.")
            return

        # Create popup window
        popup = Toplevel(self)
        popup.title("Event Details")
        popup.geometry("400x600")

        for event_data in events_on_date:
            event_title = event_data[0]
            event_details = fetch_event_details(event_title, selected_date)

            if event_details:
                event_description, event_image_data = event_details
                event_image = Image.open(io.BytesIO(event_image_data)) if event_image_data else None
            else:
                event_description = "No description available."
                event_image = None

            # Display event title
            title_label = ctk.CTkLabel(popup, text=f"Event: {event_title}", font=("Arial", 16))
            title_label.pack(pady=10)

            # Display event date
            date_label = ctk.CTkLabel(popup, text=f"Date: {selected_date}", font=("Arial", 14))
            date_label.pack(pady=5)

            # Display event description
            description_label = ctk.CTkLabel(popup, text="Description:", font=("Arial", 14))
            description_label.pack(pady=5)
            description_text = ctk.CTkTextbox(popup, height=60, width=300)
            description_text.insert("1.5", event_description)
            description_text.pack(pady=5)

            # If there is an image, resize and display it
            if event_image:
                resized_image = event_image.resize((400, 300), Image.LANCZOS)
                img_tk = ImageTk.PhotoImage(resized_image)
                img_label = ctk.CTkLabel(popup, image=img_tk)
                img_label.image = img_tk  # Keep reference to the image
                img_label.pack(pady=30)

            # Add a button to save the description
            save_button = ctk.CTkButton(popup, text="Save Description", command=lambda: self.save_description(event_title, selected_date, description_text.get("1.0", "end-1c")))
            save_button.pack(pady=10)

            # Add a delete button
            delete_button = ctk.CTkButton(popup, text="Delete Event", command=lambda title=event_title, date=selected_date, pop=popup: self.delete_event_and_refresh(fetch_event_id(title, date), pop))
            delete_button.pack(pady=10)

        popup.mainloop()

    def view_notes(self):
        selected_date = self.calendar_widget.get_date()
        notes_on_date = fetch_notes_by_date(selected_date, self.logged_in_username)

        if not notes_on_date:
            messagebox.showinfo("No Notes", "No notes found for this date.")
            return

        # Create popup window
        popup = Toplevel(self)
        popup.title("Notes Details")
        popup.geometry("400x600")

        for note_data in notes_on_date:
            note_id = note_data[0]
            note_title = note_data[1]
            note_content = note_data[2]

            # Display note title
            title_label = ctk.CTkLabel(popup, text=f"Note: {note_title}", font=("Arial", 16))
            title_label.pack(pady=10)

            # Display note date
            date_label = ctk.CTkLabel(popup, text=f"Date: {selected_date}", font=("Arial", 14))
            date_label.pack(pady=5)

            # Display note content
            content_label = ctk.CTkLabel(popup, text="Content:", font=("Arial", 14))
            content_label.pack(pady=5)
            content_text = ctk.CTkTextbox(popup, height=60, width=300)
            content_text.insert("1.5", note_content)
            content_text.pack(pady=5)

            # Add a button to save the content
            save_button = ctk.CTkButton(popup, text="Save Content", command=lambda: self.save_note_content(note_title, selected_date, content_text.get("1.0", "end-1c")))
            save_button.pack(pady=10)

            # Add a delete button
            delete_button = ctk.CTkButton(popup, text="Delete Note", command=lambda note_id=note_id: self.delete_note_and_refresh(note_id, popup))
            delete_button.pack(pady=10)

        popup.mainloop()

    def delete_event(self, event_id):
        try:
            # Connect to the SQLite database
            conn = sqlite3.connect('archive.db')
            cursor = conn.cursor()
            
            # Mark the event as deleted
            cursor.execute("UPDATE events SET deleted = 1 WHERE id = ?", (event_id,))
            
            # Commit the changes and close the database connection
            conn.commit()
            conn.close()
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Database error: {e}")

    def delete_note(self, note_id):
        try:
            # Connect to the SQLite database
            conn = sqlite3.connect('archive.db')
            cursor = conn.cursor()
            
            # Mark the note as deleted
            cursor.execute("UPDATE archive SET deleted = 1 WHERE id = ?", (note_id,))
            
            # Commit the changes and close the database connection
            conn.commit()
            conn.close()
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Database error: {e}")

    def delete_event_and_refresh(self, event_id, popup):
        delete_event(event_id)
        popup.destroy()
        messagebox.showinfo("Success", "Event deleted successfully.")
        self.update_calendar()

    def delete_note_and_refresh(self, note_id, popup):
        delete_note(note_id)
        popup.destroy()
        messagebox.showinfo("Success", "Note deleted successfully.")
        self.update_calendar()
        
    def save_description(self, event_title, event_date, description):
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE events SET description = ? WHERE title = ? AND date = ?
        ''', (description, event_title, event_date))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Description updated successfully.")

    def save_feedback(self, event_title, event_date, feedback):
        # Placeholder function to save feedback in the database
        # Replace this with actual database update logic
        print(f"Event Title: {event_title}")
        print(f"Event Date: {event_date}")
        print(f"Feedback: {feedback}")
        messagebox.showinfo("Success", "Feedback saved successfully.")

    def save_note_content(self, note_title, note_date, content):
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE notes SET content = ? WHERE title = ? AND date = ?
        ''', (content, note_title, note_date))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Content updated successfully.")

    def on_login_success(self, username):
        self.logged_in_username = username
        self.login_page.pack_forget()
        self.show_main_interface(username)
        
    def create_calendar(self):
        calendar_frame = ctk.CTkFrame(self.main_interface, fg_color="#ffe4c4", corner_radius=15, border_width=0, width=600, height=400)
        calendar_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.calendar_widget = Calendar(calendar_frame, selectmode="day",
                                        font = "Arial 12 bold italic",
                                        showweeknumbers=False, 
                                        showothermonthdays=False, 
                                        background='gray', 
                                        foreground='black', 
                                        bordercolor='white', 
                                        borderwidth=5,
                                        headersbackground='white',
                                        selectbackground='lightblue',
                                        normalbackground='#ffe4c4',
                                        weekendbackground='lightgray',
                                        weekendforeground='black',)
        self.calendar_widget.pack(expand=True, fill="both", padx=10, pady=10)

        # Define a tag for event dates
        self.calendar_widget.tag_config('event', background='lightblue', foreground='black')

        self.update_calendar()  # Update the calendar with events loaded from the database

        self.highlight_dates()  # Highlight the dates with events

        # add button to highlight date
        self.highlight_date_button = ctk.CTkButton(self.main_interface, text="Highlight Date", fg_color="#A8192E", command=self.highlight_date)
        self.highlight_date_button.pack(pady=5)

        # Add a button to show upcoming events
        self.upcoming_events_button = ctk.CTkButton(self.main_interface, text="Upcoming Events", fg_color="#A8192E", command=self.show_upcoming_events)
        self.upcoming_events_button.pack(pady=5)

    def highlight_date(self):
        selected_date = self.calendar_widget.get_date()
        add_highlighted_date(selected_date)
        self.highlight_dates()
        messagebox.showinfo("Success", "Date highlighted successfully.")

        

    def show_upcoming_events(self):
        # Fetch all events
        events = self.fetch_all_events()
    
        # Display the events
        events_window = tk.Toplevel(self.main_interface)
        events_window.title("Upcoming Events")
    
        for event in events:
            event_label = tk.Label(events_window, text=f"{event[1]} on {event[0]}")
            event_label.pack()

    def get_events_for_date(self, date):
        # This method should return a list of all events
        # Fetch all events from the database or data source
        events = self.fetch_all_events()
        return [f"{event[1]} on {event[0]}" for event in events]

    def fetch_all_events(self):
        # This method should fetch all events from the database or data source
        # For now, let's return a dummy list of events
        return [
            ("2023-10-01", "Event 1"),
            ("2023-10-02", "Event 2"),
            ("2023-10-03", "Event 3"),
            ("2023-10-04", "Event 4"),
            ("2023-10-05", "Event 5"),
        ]

    def is_date_string_valid(self, date_string, date_format='%Y-%m-%d'):
        """Check if the date_string matches the date_format."""
        try:
            datetime.strptime(date_string, date_format)
            return True
        except ValueError:
            return False

    

    def update_calendar(self):
        self.calendar_widget.calevent_remove('all')  # Remove all previous events
        current_date = self.calendar_widget.get_date()
    
        # Ensure the current_date is in the correct format
        if self.is_date_string_valid(current_date, '%Y-%m-%d'):
            # Get all events and update the calendar
            events = fetch_events_by_date(current_date)
        
            for event in events:
                event_date_str = event[0]
                if self.is_date_string_valid(event_date_str, '%Y-%m-%d'):
                    event_date = datetime.strptime(event_date_str, "%Y-%m-%d").date()
                    event_id = fetch_event_id(event[1], event_date_str)
                    highlight_color = fetch_event_highlight_color(event_id)
                    self.calendar_widget.calevent_create(event_date, event[1], 'event')
                    if highlight_color:
                        self.calendar_widget.tag_config('event', background=highlight_color, foreground='black')
        
            # Get all notes and update the calendar
            notes = fetch_notes_by_date(current_date, self.logged_in_username)
            for note in notes:
                note_date_str = note[0]
                if self.is_date_string_valid(note_date_str, '%Y-%m-%d'):
                    note_date = datetime.strptime(note_date_str, "%Y-%m-%d").date()
                    highlight_color = fetch_note_highlight_color(note[0])
                    self.calendar_widget.calevent_create(note_date, note[1], 'note')
                    if highlight_color:
                        self.calendar_widget.tag_config('note', background=highlight_color, foreground='black')
        
            # Highlight the dates with events
            self.highlight_event_dates(events)

    def highlight_event_dates(self, events):
        selected_date = self.calendar_widget.get_date()
        notes_on_date = fetch_notes_by_date(selected_date, self.logged_in_username)
    
        for event in events:
            event_date_str = event[0]
            if self.is_date_string_valid(event_date_str, '%Y-%m-%d'):
                event_date = datetime.strptime(event_date_str, "%Y-%m-%d").date()
                self.calendar_widget.calevent_create(event_date, 'Event', 'event')
                self.calendar_widget.tag_configure('event', background='lightblue', foreground='black')
                self.calendar_widget.tag_bind('event', "<Enter>", lambda event, date=event_date: self.display_event_details(event, date))
                self.calendar_widget.tag_bind('event', "<Leave>", lambda event: self.hide_event_details())
            
                if notes_on_date:
                    for note_data in notes_on_date:
                        note_title = note_data[0]
                        note_content = fetch_note_details(note_title, selected_date)[0]
                        note_date = datetime.strptime(selected_date, "%Y-%m-%d").date()
                        self.calendar_widget.calevent_create(note_date, note_title, 'note')
                        self.calendar_widget.tag_configure('note', background='lightgreen', foreground='black')

    def show_event_popup(self, event):
        selected_date = self.calendar_widget.get_date()
        events_on_date = fetch_events_by_date(selected_date)
        notes_on_date = fetch_notes_by_date(selected_date)

        if not events_on_date and not notes_on_date:
            messagebox.showinfo("No Events or Notes", "There are no events or notes on this date.")
            return

        popup = Toplevel(self)
        popup.title("Details")
        popup.geometry("400x600")

        if events_on_date:
            for event_data in events_on_date:
                event_title = event_data[0]
                event_details = fetch_event_details(event_title, selected_date)

                if event_details:
                    event_description, event_image_data = event_details
                    event_image = Image.open(io.BytesIO(event_image_data)) if event_image_data else None
                else:
                    event_description = "No description available."
                    event_image = None

                title_label = ctk.CTkLabel(popup, text=f"Event: {event_title}", font=("Arial", 16))
                title_label.pack(pady=10)

                date_label = ctk.CTkLabel(popup, text=f"Date: {selected_date}", font=("Arial", 14))
                date_label.pack(pady=5)

                description_label = ctk.CTkLabel(popup, text="Description:", font=("Arial", 14))
                description_label.pack(pady=5)
                description_text = ctk.CTkTextbox(popup, height=5, width=40)
                description_text.insert("1.0", event_description)
                description_text.pack(pady=5)

                if event_image:
                    img_tk = ImageTk.PhotoImage(event_image)
                    img_label = ctk.CTkLabel(popup, image=img_tk)
                    img_label.image = img_tk  # Keep reference to the image
                    img_label.pack(pady=10)

                save_button = ctk.CTkButton(popup, text="Save Description", command=lambda: self.save_description(event_title, selected_date, description_text.get("1.0", "end-1c")))
                save_button.pack(pady=10)

                feedback_label = ctk.CTkLabel(popup, text="Feedback:", font=("Arial", 14))
                feedback_label.pack(pady=5)
                feedback_text = ctk.CTkTextbox(popup, height=5, width=40)
                feedback_text.pack(pady=5)

                save_feedback_button = ctk.CTkButton(popup, text="Save Feedback", command=lambda: self.save_feedback(event_title, selected_date, feedback_text.get("1.0", "end-1c")))
                save_feedback_button.pack(pady=10)

        if notes_on_date:
            for note_data in notes_on_date:
                note_title = note_data[0]
                note_details = fetch_note_details(note_title, selected_date)

                if note_details:
                    note_content = note_details[0]
                else:
                    note_content = "No content available."

                note_title_label = ctk.CTkLabel(popup, text=f"Note: {note_title}", font=("Arial", 16))
                note_title_label.pack(pady=10)

                note_date_label = ctk.CTkLabel(popup, text=f"Date: {selected_date}", font=("Arial", 14))
                note_date_label.pack(pady=5)

                note_content_label = ctk.CTkLabel(popup, text="Content:", font=("Arial", 14))
                note_content_label.pack(pady=5)
                note_content_text = ctk.CTkTextbox(popup, height=5, width=40)
                note_content_text.insert("1.0", note_content)
                note_content_text.pack(pady=5)

                save_note_button = ctk.CTkButton(popup, text="Save Content", command=lambda: self.save_note_content(note_title, selected_date, note_content_text.get("1.0", "end-1c")))
                save_note_button.pack(pady=10)

        popup.mainloop()
    def create_footer(self):
        footer_frame = ctk.CTkFrame(self.main_interface, height=60, fg_color="#A8192E")
        footer_frame.pack(fill="x", side="bottom")
        ctk.CTkLabel(
            footer_frame,
            text=f"Today's Date: {self.current_date.strftime('%B %d, %Y')}",
            font=("Arial", 12),
            text_color="white"
        ).pack(pady=10)

    def sign_out(self):
        if hasattr(self, 'main_interface'):
            self.main_interface.pack_forget()
        self.show_login_page()

    def loop_login(self, delay=5):
        def loop():
            while True:
                time.sleep(delay)
                self.sign_out()
        threading.Thread(target=loop, daemon=True).start()

def fetch_highlighted_dates():
    # Placeholder function to fetch highlighted dates from the database
    # Replace this with actual database query logic
    return ["2023-10-15", "2023-10-20"]

def highlight_dates():
    highlighted_dates = fetch_highlighted_dates()
    for date in highlighted_dates:
        # Code to highlight the date in the UI
        pass

# Call this function when the application starts or when the user signs in
highlight_dates()

def add_highlighted_date(date):
    # Placeholder function to add a highlighted date to the database
    # Replace this with actual database insert logic
    print(f"Highlighted date added: {date}")

# Example usage of adding a highlighted date
add_highlighted_date('2023-10-15')

def delete_highlighted_date(date):
    # Placeholder function to delete a highlighted date from the database
    # Replace this with actual database delete logic
    print(f"Highlighted date deleted: {date}")

# Example usage of deleting a highlighted date
delete_highlighted_date('2023-10-15')

if __name__ == "__main__": 
    app = Application()
    app.mainloop()
