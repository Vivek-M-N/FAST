import tkinter as tk
from tkinter import filedialog, messagebox
#from additional_funcs import *
from models import *

def main_gui():
    print("Starting GUI")

    config = None
    model = None
    drive = None
    res = []

    def file_selector():
        nonlocal config 
        nonlocal model
        nonlocal drive
        file_path = filedialog.askopenfilename(title="Select a File")
        if file_path:
            with open(file_path,'r') as file:
                data = file.read().split('\n\n')
            config = list(map(float, data[1].split(',')))
            drive = data[3]
            drive = drive.split('\n')
            model = Bicycle(config)
        else:
            config = None

    def simulation():
        nonlocal res
        res = []
        if config is None:
            messagebox.showwarning("Warning", "No config selected. Please select a file first.")
            return

        for i in range(0, int(config[1]/config[0])):
            print("Timestep: {:.3f}".format(float((i+1)*config[0])))
            
            vx_input = int(drive[i].split(',')[0])
            delta = int(drive[i].split(',')[1])

            #print("Velocity: {}m/s, Steering angle: {}deg".format(vx_input, delta))
            res.append(model.update(vx_input, delta))

    def save_output():
        filename = entry.get() if entry.get() else "test_res"
        with open(filename+'.txt', 'w') as file:
            file.write(str(res))
        print("Simulation result saved to: {}".format(filename))
    
    #main window
    start_screen = tk.Tk()
    start_screen.title("Solver")
    start_screen.geometry("300x200")
    
    #select file button
    input = tk.Button(start_screen, text="Browse", command=file_selector)
    input.pack(pady=5)

    #select file button
    sim = tk.Button(start_screen, text="Simulate", command=simulation)
    sim.pack(pady=5)

    #sim results filename
    label = tk.Label(start_screen, text="Default filename: test_res.txt")
    label.pack(pady=3)
    entry = tk.Entry(start_screen, width=40)
    entry.pack(pady=5)

    #storing sim results
    output = tk.Button(start_screen, text="Save", command=save_output)
    output.pack(pady=5)
    
    start_screen.mainloop()

main_gui()
