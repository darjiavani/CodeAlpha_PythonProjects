from tkinter import *

def send():
    user_msg = entry.get().lower()

    chat.insert(END, "You: " + user_msg + "\n")

    if user_msg == "hello":
        bot_reply = "Hi!"
    elif user_msg == "how are you":
        bot_reply = "I'm fine, thanks!"
    elif user_msg == "what is your name":
        bot_reply = "I am a Basic ChatBot."
    elif user_msg == "bye":
        bot_reply = "Goodbye!"
    else:
        bot_reply = "Sorry, I don't understand."

    chat.insert(END, "Bot: " + bot_reply + "\n\n")

    entry.delete(0, END)

root = Tk()
root.title("Basic ChatBot")
root.geometry("600x400")

chat = Text(root, font=("Arial", 12))
chat.pack(padx=10, pady=10, fill=BOTH, expand=True)

frame = Frame(root)
frame.pack(fill=X, padx=10, pady=5)

entry = Entry(frame, font=("Arial", 12))
entry.pack(side=LEFT, fill=X, expand=True)

btn = Button(
    frame,
    text="Send",
    command=send,
    bg="green",
    fg="white"
)
btn.pack(side=RIGHT)

root.mainloop()