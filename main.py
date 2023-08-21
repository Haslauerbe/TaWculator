import tkinter as tk
from tkinter import simpledialog, scrolledtext, messagebox


# Funktion zur Berechnung der Einschränkungsfunktion
def restriction_function(d, t):
    if d < t:
        return 0
    else:
        return d - t


# Funktion zur Berechnung der Summe der Einschränkungsfunktionen
def total_restriction(d1, d2, d3, t1, t2, t3):
    return restriction_function(d1, t1) + restriction_function(d2, t2) + restriction_function(d3, t3)


def auto(d1, d2, d3, hit):
    count = 0
    if d1 == hit:
        count += 1
    if d2 == hit:
        count += 1
    if d3 == hit:
        count += 1
    return True if count >= 2 else False


def auto_misserfolg(d1, d2, d3):
    return auto(d1, d2, d3, 20)


def auto_erfolg(d1, d2, d3):
    return auto(d1, d2, d3, 1)


def erfolg(d1, d2, d3, t1, t2, t3, schwellenwert):
    if auto_misserfolg(d1, d2, d3):
        return 0
    if auto_erfolg(d1, d2, d3):
        return 1
    if total_restriction(d1, d2, d3, t1, t2, t3) <= schwellenwert:
        return 1
    return 0


def show_results(t1, t2, t3):
    # Error-Handling: Überprüfe, ob die Werte streng größer als 0 sind
    if t1 <= 0 or t2 <= 0 or t3 <= 0:
        messagebox.showerror("Fehler", "Die Werte der Eigenschaften müssen größer als 0 sein.")
        return

    results_text.delete(1.0, tk.END)  # Clear previous results
    results_text.insert(tk.END, "Talentwert\tErfolgs-Wahrscheinlichkeit\n")

    results = []

    for schwellenwert in range(21):
        anzahl_erfolge = 0
        for x in range(1, 21):
            for y in range(1, 21):
                for z in range(1, 21):
                    anzahl_erfolge += erfolg(x, y, z, t1, t2, t3, schwellenwert)
        erfolgs_wahrscheinlichkeit = anzahl_erfolge / (20 * 20 * 20)
        results.append([schwellenwert, 100*erfolgs_wahrscheinlichkeit])

    for result in results:
        results_text.insert(tk.END, f"{result[0]}\t\t{result[1]:.6f}\n")


def main():
    # Create a Tkinter root window
    root = tk.Tk()

    root.title("TaWculator")
    t1_label = tk.Label(root, text="Eigenschaft 1:")
    t1_entry = tk.Entry(root)
    t1_label.pack()
    t1_entry.pack()

    t2_label = tk.Label(root, text="Eigenschaft 2:")
    t2_entry = tk.Entry(root)
    t2_label.pack()
    t2_entry.pack()

    t3_label = tk.Label(root, text="Eigenschaft 3:")
    t3_entry = tk.Entry(root)
    t3_label.pack()
    t3_entry.pack()

    ok_button = tk.Button(root, text="Berechnen", command=lambda: show_results(get_float_value(t1_entry), get_float_value(t2_entry), get_float_value(t3_entry)))
    ok_button.pack()

    # Bind the Return key to the Berechnen button
    root.bind("<Return>", lambda event: ok_button.invoke())

    global results_text
    results_text = scrolledtext.ScrolledText(root, wrap=tk.WORD)
    results_text.pack()

    root.mainloop()


def get_float_value(entry):
    value = entry.get()
    return float(value) if value else 0.0


if __name__ == "__main__":
    main()
