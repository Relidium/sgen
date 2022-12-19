#██████╗ ██╗   ██╗    ██████╗ ███████╗██╗     ██╗██████╗ ██╗██╗   ██╗███╗   ███╗
#██╔══██╗╚██╗ ██╔╝    ██╔══██╗██╔════╝██║     ██║██╔══██╗██║██║   ██║████╗ ████║
#██████╔╝ ╚████╔╝     ██████╔╝█████╗  ██║     ██║██║  ██║██║██║   ██║██╔████╔██║
#██╔══██╗  ╚██╔╝      ██╔══██╗██╔══╝  ██║     ██║██║  ██║██║██║   ██║██║╚██╔╝██║
#██████╔╝   ██║       ██║  ██║███████╗███████╗██║██████╔╝██║╚██████╔╝██║ ╚═╝ ██║
#╚═════╝    ╚═╝       ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝╚═════╝ ╚═╝ ╚═════╝ ╚═╝     ╚═╝
#                                 @curd#9782
from os import path, makedirs, remove
from random import SystemRandom as srnd
from threading import Thread
from datetime import date
import customtkinter as ctk
from formatting import formatRandom

class metadata:
    #Generation data
    genCount = 100
    fileCount = 1
    #Format data
    custom_formats = []
    generation_format = "none"
    generation_extra = "none"

if not path.exists('settings.cfg'):
    with open('settings.cfg', 'w', encoding="utf-8") as newSettingFile:
        newSettingFile.write(
            'generationcount=100\nfilecount=1')
        newSettingFile.close()

if not path.exists('custom.txt'):
    with open('custom.txt', 'w', encoding="utf-8") as newCustomFile:
        newCustomFile.write(
            'MyCustomGeneration:XXXX-XXXX-XXXX-XXXX Passcode-EEEE:lower')
        newCustomFile.close()

if not path.exists('Generations/'):
    makedirs('Generations/')

with open("settings.cfg", 'r', encoding='utf-8') as settingsRead:
    conts = settingsRead.readlines()
    try:
        metadata.genCount = int(conts[0][16:])
        metadata.fileCount = int(conts[1][10:])
        settingsRead.close()
    except ValueError:
        settingsRead.close()
        remove("settings.cfg")
        with open('settings.cfg', 'w', encoding="utf-8") as newSettingFile:
            newSettingFile.write('generationcount=100\nfilecount=1')
            newSettingFile.close()

def log(self, text):
    self.Output.configure(state="normal")
    self.Output.insert("insert", f"{text}\n")
    self.Output.configure(state="disabled")

def setup(gentype):
    #Prepare settings and I/O for generation
    if not path.exists('Generations/'):
        makedirs('Generations/')
    #Checks, limits, minimums and reformats
    if isinstance(metadata.genCount, int) is False or isinstance(metadata.fileCount, int) is False:
        metadata.genCount = 100
        metadata.fileCount = 1
    else:
        if metadata.genCount > 20_000: metadata.genCount = 20_000
        if metadata.genCount < 1: metadata.genCount = 1

        if metadata.fileCount > 750: metadata.fileCount = 100
        if metadata.fileCount < 1: metadata.fileCount = 1
    for selection in metadata.custom_formats:
        if selection[0] == gentype: metadata.generation_format = selection[1]; metadata.generation_extra = selection[2]

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("545x360")
        self._set_appearance_mode("Dark")
        self.title("SGen by Relidium")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0, 1), weight=1)

        self.Output = ctk.CTkTextbox(master=self)
        self.Output.grid(row=0, column=0, rowspan=1,columnspan=3, padx=10, pady=(10, 0), sticky="nsew")

        self.select_gen_type = ctk.CTkComboBox( master=self, values=["Select generation type"])
        self.select_gen_type.grid( row=1, column=0, padx=10, pady=10, sticky="ew")

        self.generateButton = ctk.CTkButton(master=self, command=self.generate, text="Generate")
        self.generateButton.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

        with open('custom.txt', 'r', encoding='utf-8') as readCustom:
            formats = readCustom.readlines()
            if len(formats) < 1: pass
            for line in formats:
                instance = line.split(':')
                instance[1] = instance[1].strip()
                instance = tuple(instance)
                metadata.custom_formats.append(instance)
            readCustom.close()

        for line in metadata.custom_formats: self.select_gen_type.configure(values=self.select_gen_type._values+[line[0]])
        log(self, "Welcome to SGen by Relidium")
        log(self, "VIEW THE 'README.txt' FILE BEFORE USING THIS PROGRAM!\nAfter adding new generations, restart this program.")

    def generate(self):
        setup(self.select_gen_type.get())
        if self.select_gen_type.get() == "Select generation type": log(self, "Please select a generation method."); return
        def Generate_Formatted_File(file_name_appendix: str):
            #Allocate memory for generations
            generations = [""]*metadata.genCount

            for index in range(metadata.genCount):
                try: generations[index] = f"{formatRandom(metadata.generation_format, metadata.generation_extra)}\n"
                except TypeError: log(self, "There was an error reading your generation format. Check the typing in your custom.txt file to fix this error."); break

            #Write to file post generation
            with open(f"Generations/{''.join(srnd().choice('QWERTYUIOPASDFGHJKLZXCVBNM246819') for _ in range(6))}-{file_name_appendix}.txt", 'w', encoding='utf-8') as newfile:
                generations = ''.join(str(x) for x in generations)[:-1]
                newfile.write(f"This file was created on {date.today()} ({metadata.genCount} generations):\n{generations}")
                newfile.close()
            del generations

        for _ in range(metadata.fileCount):
            Thread(target=Generate_Formatted_File, daemon=True, args=[self.select_gen_type.get()]).start()

if __name__ == "__main__":
    app = App()
    app.mainloop()
