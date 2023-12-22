import tkinter as tk
from tkinter import ttk, messagebox
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class MailApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mail Application by Nikhil")
        self.root.geometry("500x400")

        self.sender_email = "nikhilahirwar16@gmail.com"

        self.create_gui()

    def create_gui(self):
        # Sender Email
        sender_label = ttk.Label(self.root, text="Your Email:")
        sender_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

        self.sender_entry = ttk.Entry(self.root, width=30)
        self.sender_entry.insert(0, self.sender_email)
        self.sender_entry.grid(row=0, column=1, padx=10, pady=10)

        # Recipient Email
        recipient_label = ttk.Label(self.root, text="Recipient Email:")
        recipient_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

        self.recipient_entry = ttk.Entry(self.root, width=30)
        self.recipient_entry.grid(row=1, column=1, padx=10, pady=10)

        # Subject
        subject_label = ttk.Label(self.root, text="Subject:")
        subject_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

        self.subject_entry = ttk.Entry(self.root, width=30)
        self.subject_entry.grid(row=2, column=1, padx=10, pady=10)

        # Message
        message_label = ttk.Label(self.root, text="Message:")
        message_label.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)

        self.message_text = tk.Text(self.root, width=30, height=10)
        self.message_text.grid(row=3, column=1, padx=10, pady=10)

        # Send Button
        send_button = ttk.Button(self.root, text="Send Email", command=self.send_email)
        send_button.grid(row=4, column=1, pady=10)

    def send_email(self):
        recipient_email = self.recipient_entry.get()
        subject = self.subject_entry.get()
        message = self.message_text.get("1.0", tk.END)

        try:
            # Connect to SMTP server
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()

                # Login to the sender's email account
                server.login(self.sender_email, self.sender_password)

                # Create the email message
                email_message = MIMEMultipart()
                email_message["From"] = self.sender_email
                email_message["To"] = recipient_email
                email_message["Subject"] = subject
                email_message.attach(MIMEText(message, "plain"))

                # Send the email
                server.sendmail(self.sender_email, recipient_email, email_message.as_string())

            messagebox.showinfo("Success", "Email sent successfully!")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred:\n{str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = MailApp(root)
    root.mainloop()
