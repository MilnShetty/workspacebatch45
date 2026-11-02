
from datetime import datetime
import tkinter as tk
from tkinter import messagebox
import winsound


def main():
    root = tk.Tk()
    root.title("Digital Clock & Alarm")
    root.geometry("400x300")
    root.resizable(False, False)
    root.configure(bg="#151525")

    # Digital clock
    clock = tk.Label(
        root,
        font=("Arial", 42, "bold"),
        fg="#00ffcc",
        bg="#151525"
    )
    clock.pack(pady=20)

    # Alarm input
    tk.Label(
        root,
        text="Set Alarm (HH:MM:SS)",
        font=("Arial", 14),
        fg="white",
        bg="#151525"
    ).pack()

    alarm_entry = tk.Entry(
        root,
        font=("Arial", 18),
        justify="center"
    )
    alarm_entry.pack(pady=10)

    alarm_time = None
    alarm_triggered = False

    def set_alarm():
        nonlocal alarm_time, alarm_triggered

        alarm_time = alarm_entry.get().strip()
        try:
            datetime.strptime(alarm_time, "%H:%M:%S")
            alarm_triggered = False
            status.config(text="Alarm set for " + alarm_time,
                          fg="#00ffcc")
        except ValueError:
            messagebox.showerror(
                "Invalid Time",
                "Enter time in HH:MM:SS format"
            )

    def stop_alarm():
        nonlocal alarm_time
        alarm_time = None
        status.config(text="Alarm stopped", fg="orange")

    tk.Button(
        root,
        text="Set Alarm",
        command=set_alarm,
        font=("Arial", 12),
        bg="#00aa88",
        fg="white"
    ).pack(pady=5)

    tk.Button(
        root,
        text="Stop Alarm",
        command=stop_alarm,
        font=("Arial", 12),
        bg="#cc3333",
        fg="white"
    ).pack(pady=5)

    status = tk.Label(
        root,
        text="No alarm set",
        font=("Arial", 12),
        fg="white",
        bg="#151525"
    )
    status.pack(pady=10)

    def update():
        nonlocal alarm_triggered

        now = datetime.now()
        clock.config(text=now.strftime("%H:%M:%S"))

        if (alarm_time == now.strftime("%H:%M:%S")
                and not alarm_triggered):
            alarm_triggered = True
            status.config(text="⏰ ALARM RINGING!",
                          fg="red")

            # Play alarm sound
            winsound.PlaySound(
                "SystemExclamation",
                winsound.SND_ALIAS | winsound.SND_ASYNC |
                winsound.SND_LOOP
            )

        root.after(200, update)

    update()
    root.mainloop()


if __name__ == "__main__":
    main()
