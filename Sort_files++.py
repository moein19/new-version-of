import os, shutil, customtkinter
from tkinter import Menu
from time import sleep


class Sort_files:
    def __init__(self, s):
        self.s = s

    @property
    def sort_json(self):
        data = os.listdir(self.s)
        if "json files" in data:
            for i in data:
                if i.endswith(".json"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"json files")
                    print(f"file {i} moved to json files")
        elif "json files" not in data:
            os.mkdir(self.s+os.sep+"json files")
        try:
            for i in data:
                if i.endswith(".json"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"json files")
                    print(f"file {i} moved to json files")
        except:
            print("operation wasn`t ok")

    @property
    def sort_python(self):
        data = os.listdir(self.s)
        if "python files" in data:
            for i in data:
                if i.endswith(".py"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"python files")
                    print(f"file {i} moved to python files")
        elif "python files" not in data:
            os.mkdir(self.s+os.sep+"python files")
        try:
            for i in data:
                if i.endswith(".py"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"python files")
                    print(f"file {i} moved to python files")
        except:
            print("operation wasn`t ok")

    @property
    def sort_txt(self):
        data = os.listdir(self.s)
        if "txt files" in data:
            for i in data:
                if i.endswith(".txt"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"txt files")
                    print(f"file {i} moved to txt files")
        elif "txt files" not in data:
            os.mkdir(self.s+os.sep+"txt files")
        try:
            for i in data:
                if i.endswith(".txt"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"txt files")
                    print(f"file {i} moved to txt files")
        except:
            print("operation wasn`t ok")

    @property
    def sort_pickle(self):
        data = os.listdir(self.s)
        if "pickle files" in data:
            for i in data:
                if i.endswith(".pickle"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"pickle files")
                    print(f"file {i} moved to pickle files")
        elif "pickle files" not in data:
            os.mkdir(self.s+os.sep+"pickle files")
        try:
            for i in data:
                if i.endswith(".pickle"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"pickle files")
                    print(f"file {i} moved to pickle files")
        except:
            print("operation wasn`t ok")

    @property
    def sort_csv(self):
        data = os.listdir(self.s)
        if "csv files" in data:
            for i in data:
                if i.endswith(".csv"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"csv files")
                    print(f"file {i} moved to csv files")
        elif "csv files" not in data:
            os.mkdir(self.s+os.sep+"csv files")
        try:
            for i in data:
                if i.endswith(".csv"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"csv files")
                    print(f"file {i} moved to csv files")
        except:
            print("operation wasn`t ok")

    @property
    def sort_html(self):
        data = os.listdir(self.s)
        if "html files" in data:
            for i in data:
                if i.endswith((".html",".htm")):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"html files")
                    print(f"file {i} moved to html files")
        elif "html files" not in data:
            os.mkdir(self.s+os.sep+"html files")
        try:
            for i in data:
                if i.endswith((".html",".htm")):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"html files")
                    print(f"file {i} moved to html files")
        except:
            print("operation wasn`t ok")

    @property
    def sort_xlsx(self):
        data = os.listdir(self.s)
        if "excel files" in data:
            for i in data:
                if i.endswith((".xlsx",".xls")):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"excel files")
                    print(f"file {i} moved to excel files")
        elif "excel files" not in data:
            os.mkdir(self.s+os.sep+"excel files")
        try:
            for i in data:
                if i.endswith((".xlsx",".xls")):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"excel files")
                    print(f"file {i} moved to excel files")
        except:
            print("operation wasn`t ok")

    @property
    def sort_docx(self):
        data = os.listdir(self.s)
        if "word files" in data:
            for i in data:
                if i.endswith(".docx"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"word files")
                    print(f"file {i} moved to word files")
        elif "word files" not in data:
            os.mkdir(self.s+os.sep+"word files")
        try:
            for i in data:
                if i.endswith(".docx"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"word files")
                    print(f"file {i} moved to word files")
        except:
            print("operation wasn`t ok")

    @property
    def sort_pdf(self):
        data = os.listdir(self.s)
        if "pdf files" in data:
            for i in data:
                if i.endswith(".pdf"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"pdf files")
                    print(f"file {i} moved to pdf files")
        elif "pdf files" not in data:
            os.mkdir(self.s+os.sep+"pdf files")
        try:
            for i in data:
                if i.endswith(".pdf"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"pdf files")
                    print(f"file {i} moved to pdf files")
        except:
            print("operation wasn`t ok")

    @property
    def sort_powerPoint(self):
        data = os.listdir(self.s)
        if "powerpoint files" in data:
            for i in data:
                if i.endswith(".pptx"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"powerpoint files")
                    print(f"file {i} moved to powerpoint files")
        elif "powerpoint files" not in data:
            os.mkdir(self.s+os.sep+"powerpoint files")
        try:
            for i in data:
                if i.endswith(".pptx"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"powerpoint files")
                    print(f"file {i} moved to powerpoint files")
        except:
            print("operation wasn`t ok")

    @property
    def sort_photo(self):
        #".jfif",".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".tif", ".webp", ".svg", ".ico", ".heic", ".heif", ".raw"
        data = os.listdir(self.s)
        if "photo files" in data:
            for i in data:
                if i.endswith("jfif"):
                    os.makedirs(self.s+os.sep+"photo files"+os.sep+"jfif files",exist_ok=True)
                if i.endswith("jpg"):
                    os.makedirs(self.s+os.sep+"photo files"+os.sep+"jpg files",exist_ok=True)
                if i.endswith("jpeg"):
                    os.makedirs(self.s+os.sep+"photo files"+os.sep+"jpeg files",exist_ok=True)
                if i.endswith("png"):
                    os.makedirs(self.s+os.sep+"photo files"+os.sep+"png files",exist_ok=True)
                if i.endswith("gif"):
                    os.makedirs(self.s+os.sep+"photo files"+os.sep+"gif files",exist_ok=True)
                if i.endswith("bmp"):
                    os.makedirs(self.s+os.sep+"photo files"+os.sep+"bmp files",exist_ok=True)
                if i.endswith("tiff"):
                    os.makedirs(self.s+os.sep+"photo files"+os.sep+"tiff files",exist_ok=True)
                if i.endswith("tif"):
                    os.makedirs(self.s+os.sep+"photo files"+os.sep+"tif files",exist_ok=True)
                if i.endswith("webp"):
                    os.makedirs(self.s+os.sep+"photo files"+os.sep+"webp files",exist_ok=True)
                if i.endswith("svg"):
                    os.makedirs(self.s+os.sep+"photo files"+os.sep+"svg files",exist_ok=True)
                if i.endswith("ico"):
                    os.makedirs(self.s+os.sep+"photo files"+os.sep+"ico files",exist_ok=True)
                if i.endswith("heic"):
                    os.makedirs(self.s+os.sep+"photo files"+os.sep+"heic files",exist_ok=True)
                if i.endswith("heif"):
                    os.makedirs(self.s+os.sep+"photo files"+os.sep+"heif files",exist_ok=True)
                if i.endswith("raw"):
                    os.makedirs(self.s+os.sep+"photo files"+os.sep+"raw files",exist_ok=True)
            for i in data:
                if i.endswith("jfif"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"photo files"+os.sep+"jfif files")
                if i.endswith("jpg"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"photo files"+os.sep+"jpg files")
                if i.endswith("jpeg"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"photo files"+os.sep+"jpeg files")
                if i.endswith("png"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"photo files"+os.sep+"png files")
                if i.endswith("gif"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"photo files"+os.sep+"gif files")
                if i.endswith("bmp"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"photo files"+os.sep+"bmp files")
                if i.endswith("tiff"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"photo files"+os.sep+"tiff files")
                if i.endswith("tif"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"photo files"+os.sep+"tif files")
                if i.endswith("webp"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"photo files"+os.sep+"webp files")
                if i.endswith("svg"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"photo files"+os.sep+"svg files")
                if i.endswith("ico"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"photo files"+os.sep+"ico files")
                if i.endswith("heic"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"photo files"+os.sep+"heic files")
                if i.endswith("heif"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"photo files"+os.sep+"heif files")
                if i.endswith("raw"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"photo files"+os.sep+"raw files")
        elif "photo files" not in data:
            os.mkdir(self.s+os.sep+"photo files")
        try:
            for i in data:
                if i.endswith("jfif"):
                    os.makedirs(self.s+os.sep+"photo files"+os.sep+"jfif files",exist_ok=True)
                if i.endswith("jpg"):
                    os.makedirs(self.s+os.sep+"photo files"+os.sep+"jpg files",exist_ok=True)
                if i.endswith("jpeg"):
                    os.makedirs(self.s+os.sep+"photo files"+os.sep+"jpeg files",exist_ok=True)
                if i.endswith("png"):
                    os.makedirs(self.s+os.sep+"photo files"+os.sep+"png files",exist_ok=True)
                if i.endswith("gif"):
                    os.makedirs(self.s+os.sep+"photo files"+os.sep+"gif files",exist_ok=True)
                if i.endswith("bmp"):
                    os.makedirs(self.s+os.sep+"photo files"+os.sep+"bmp files",exist_ok=True)
                if i.endswith("tiff"):
                    os.makedirs(self.s+os.sep+"photo files"+os.sep+"tiff files",exist_ok=True)
                if i.endswith("tif"):
                    os.makedirs(self.s+os.sep+"photo files"+os.sep+"tif files",exist_ok=True)
                if i.endswith("webp"):
                    os.makedirs(self.s+os.sep+"photo files"+os.sep+"webp files",exist_ok=True)
                if i.endswith("svg"):
                    os.makedirs(self.s+os.sep+"photo files"+os.sep+"svg files",exist_ok=True)
                if i.endswith("ico"):
                    os.makedirs(self.s+os.sep+"photo files"+os.sep+"ico files",exist_ok=True)
                if i.endswith("heic"):
                    os.makedirs(self.s+os.sep+"photo files"+os.sep+"heic files",exist_ok=True)
                if i.endswith("heif"):
                    os.makedirs(self.s+os.sep+"photo files"+os.sep+"heif files",exist_ok=True)
                if i.endswith("raw"):
                    os.makedirs(self.s+os.sep+"photo files"+os.sep+"raw files",exist_ok=True)
            for i in data:
                if i.endswith("jfif"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"photo files"+os.sep+"jfif files")
                if i.endswith("jpg"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"photo files"+os.sep+"jpg files")
                if i.endswith("jpeg"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"photo files"+os.sep+"jpeg files")
                if i.endswith("png"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"photo files"+os.sep+"png files")
                if i.endswith("gif"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"photo files"+os.sep+"gif files")
                if i.endswith("bmp"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"photo files"+os.sep+"bmp files")
                if i.endswith("tiff"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"photo files"+os.sep+"tiff files")
                if i.endswith("tif"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"photo files"+os.sep+"tif files")
                if i.endswith("webp"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"photo files"+os.sep+"webp files")
                if i.endswith("svg"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"photo files"+os.sep+"svg files")
                if i.endswith("ico"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"photo files"+os.sep+"ico files")
                if i.endswith("heic"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"photo files"+os.sep+"heic files")
                if i.endswith("heif"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"photo files"+os.sep+"heif files")
                if i.endswith("raw"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"photo files"+os.sep+"raw files")
        except:
            print("operation wasn`t ok")

    @property
    def sort_video(self):
        #".mp4", ".mkv", ".mov", ".avi", ".flv", ".wmv", ".webm", ".3gp", ".m4v", ".mpg", ".mpeg", ".ogv", ".ts", ".f4v"
        data = os.listdir(self.s)
        if "video files" in data:
            for i in data:
                if i.endswith("mp4"):
                    os.makedirs(self.s+os.sep+"video files"+os.sep+"mp4 files",exist_ok=True)
                if i.endswith("mkv"):
                    os.makedirs(self.s+os.sep+"video files"+os.sep+"mkv files",exist_ok=True)
                if i.endswith("mov"):
                    os.makedirs(self.s+os.sep+"video files"+os.sep+"mov files",exist_ok=True)
                if i.endswith("avi"):
                    os.makedirs(self.s+os.sep+"video files"+os.sep+"avi files",exist_ok=True)
                if i.endswith("flv"):
                    os.makedirs(self.s+os.sep+"video files"+os.sep+"flv files",exist_ok=True)
                if i.endswith("wmv"):
                    os.makedirs(self.s+os.sep+"video files"+os.sep+"wmv files",exist_ok=True)
                if i.endswith("webm"):
                    os.makedirs(self.s+os.sep+"video files"+os.sep+"webm files",exist_ok=True)
                if i.endswith("3gp"):
                    os.makedirs(self.s+os.sep+"video files"+os.sep+"3gp files",exist_ok=True)
                if i.endswith("m4v"):
                    os.makedirs(self.s+os.sep+"video files"+os.sep+"m4v files",exist_ok=True)
                if i.endswith("mpg"):
                    os.makedirs(self.s+os.sep+"video files"+os.sep+"mpg files",exist_ok=True)
                if i.endswith("mpeg"):
                    os.makedirs(self.s+os.sep+"video files"+os.sep+"mpeg files",exist_ok=True)
                if i.endswith("ogv"):
                    os.makedirs(self.s+os.sep+"video files"+os.sep+"ogv files",exist_ok=True)
                if i.endswith("ts"):
                    os.makedirs(self.s+os.sep+"video files"+os.sep+"ts files",exist_ok=True)
                if i.endswith("f4v"):
                    os.makedirs(self.s+os.sep+"video files"+os.sep+"f4v files",exist_ok=True)
            for i in data:
                if i.endswith("mp4"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"video files"+os.sep+"mp4 files")
                if i.endswith("mkv"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"video files"+os.sep+"mkv files")
                if i.endswith("mov"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"video files"+os.sep+"mov files")
                if i.endswith("avi"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"video files"+os.sep+"avi files")
                if i.endswith("flv"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"video files"+os.sep+"flv files")
                if i.endswith("wmv"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"video files"+os.sep+"wmv files")
                if i.endswith("webm"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"video files"+os.sep+"webm files")
                if i.endswith("3gp"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"video files"+os.sep+"3gp files")
                if i.endswith("m4v"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"video files"+os.sep+"m4v files")
                if i.endswith("mpg"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"video files"+os.sep+"mpg files")
                if i.endswith("mpeg"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"video files"+os.sep+"mpeg files")
                if i.endswith("ovg"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"video files"+os.sep+"ovg files")
                if i.endswith("ts"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"video files"+os.sep+"ts files")
                if i.endswith("f4v"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"video files"+os.sep+"f4v files")
        elif "video files" not in data:
            os.mkdir(self.s+os.sep+"video files")
        try:
            for i in data:
                if i.endswith("mp4"):
                    os.makedirs(self.s+os.sep+"video files"+os.sep+"mp4 files",exist_ok=True)
                if i.endswith("mkv"):
                    os.makedirs(self.s+os.sep+"video files"+os.sep+"mkv files",exist_ok=True)
                if i.endswith("mov"):
                    os.makedirs(self.s+os.sep+"video files"+os.sep+"mov files",exist_ok=True)
                if i.endswith("avi"):
                    os.makedirs(self.s+os.sep+"video files"+os.sep+"avi files",exist_ok=True)
                if i.endswith("flv"):
                    os.makedirs(self.s+os.sep+"video files"+os.sep+"flv files",exist_ok=True)
                if i.endswith("wmv"):
                    os.makedirs(self.s+os.sep+"video files"+os.sep+"wmv files",exist_ok=True)
                if i.endswith("webm"):
                    os.makedirs(self.s+os.sep+"video files"+os.sep+"webm files",exist_ok=True)
                if i.endswith("3gp"):
                    os.makedirs(self.s+os.sep+"video files"+os.sep+"3gp files",exist_ok=True)
                if i.endswith("m4v"):
                    os.makedirs(self.s+os.sep+"video files"+os.sep+"m4v files",exist_ok=True)
                if i.endswith("mpg"):
                    os.makedirs(self.s+os.sep+"video files"+os.sep+"mpg files",exist_ok=True)
                if i.endswith("mpeg"):
                    os.makedirs(self.s+os.sep+"video files"+os.sep+"mpeg files",exist_ok=True)
                if i.endswith("ogv"):
                    os.makedirs(self.s+os.sep+"video files"+os.sep+"ogv files",exist_ok=True)
                if i.endswith("ts"):
                    os.makedirs(self.s+os.sep+"video files"+os.sep+"ts files",exist_ok=True)
                if i.endswith("f4v"):
                    os.makedirs(self.s+os.sep+"video files"+os.sep+"f4v files",exist_ok=True)
            for i in data:
                if i.endswith("mp4"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"video files"+os.sep+"mp4 files")
                if i.endswith("mkv"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"video files"+os.sep+"mkv files")
                if i.endswith("mov"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"video files"+os.sep+"mov files")
                if i.endswith("avi"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"video files"+os.sep+"avi files")
                if i.endswith("flv"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"video files"+os.sep+"flv files")
                if i.endswith("wmv"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"video files"+os.sep+"wmv files")
                if i.endswith("webm"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"video files"+os.sep+"webm files")
                if i.endswith("3gp"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"video files"+os.sep+"3gp files")
                if i.endswith("m4v"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"video files"+os.sep+"m4v files")
                if i.endswith("mpg"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"video files"+os.sep+"mpg files")
                if i.endswith("mpeg"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"video files"+os.sep+"mpeg files")
                if i.endswith("ovg"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"video files"+os.sep+"ovg files")
                if i.endswith("ts"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"video files"+os.sep+"ts files")
                if i.endswith("f4v"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"video files"+os.sep+"f4v files")
        except:
            print("operation wasn`t ok")

    @property
    def sort_music(self):
        #".mp3", ".wav", ".aac", ".flac", ".ogg", ".wma", ".m4a", ".alac", ".aiff", ".amr", ".opus"
        data = os.listdir(self.s)
        if "music files" in data:
            for i in data:
                if i.endswith("mp3"):
                    os.makedirs(self.s+os.sep+"music files"+os.sep+"mp3 files",exist_ok=True)
                if i.endswith("wav"):
                    os.makedirs(self.s+os.sep+"music files"+os.sep+"wav files",exist_ok=True)
                if i.endswith("aac"):
                    os.makedirs(self.s+os.sep+"music files"+os.sep+"aac files",exist_ok=True)
                if i.endswith("flac"):
                    os.makedirs(self.s+os.sep+"music files"+os.sep+"flac files",exist_ok=True)
                if i.endswith("ogg"):
                    os.makedirs(self.s+os.sep+"music files"+os.sep+"ogg files",exist_ok=True)
                if i.endswith("wma"):
                    os.makedirs(self.s+os.sep+"music files"+os.sep+"wma files",exist_ok=True)
                if i.endswith("m4a"):
                    os.makedirs(self.s+os.sep+"music files"+os.sep+"m4a files",exist_ok=True)
                if i.endswith("alac"):
                    os.makedirs(self.s+os.sep+"music files"+os.sep+"alac files",exist_ok=True)
                if i.endswith("aiff"):
                    os.makedirs(self.s+os.sep+"music files"+os.sep+"aiff files",exist_ok=True)
                if i.endswith("amr"):
                    os.makedirs(self.s+os.sep+"music files"+os.sep+"amr files",exist_ok=True)
                if i.endswith("opus"):
                    os.makedirs(self.s+os.sep+"music files"+os.sep+"opus files",exist_ok=True)
            for i in data:
                if i.endswith("mp3"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"music files"+os.sep+"mp3 files")
                if i.endswith("wav"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"music files"+os.sep+"wav files")
                if i.endswith("aac"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"music files"+os.sep+"aac files")
                if i.endswith("flac"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"music files"+os.sep+"flac files")
                if i.endswith("ogg"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"music files"+os.sep+"ogg files")
                if i.endswith("wma"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"music files"+os.sep+"wma files")
                if i.endswith("m4a"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"music files"+os.sep+"m4a files")
                if i.endswith("alac"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"music files"+os.sep+"alac files")
                if i.endswith("aiff"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"music files"+os.sep+"aiff files")
                if i.endswith("amr"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"music files"+os.sep+"amr files")
                if i.endswith("opus"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"music files"+os.sep+"opus files")
        elif "music files" not in data:
            os.mkdir(self.s+os.sep+"music files")
        try:

            for i in data:
                if i.endswith("mp3"):
                    os.makedirs(self.s+os.sep+"music files"+os.sep+"mp3 files",exist_ok=True)
                if i.endswith("wav"):
                    os.makedirs(self.s+os.sep+"music files"+os.sep+"wav files",exist_ok=True)
                if i.endswith("aac"):
                    os.makedirs(self.s+os.sep+"music files"+os.sep+"aac files",exist_ok=True)
                if i.endswith("flac"):
                    os.makedirs(self.s+os.sep+"music files"+os.sep+"flac files",exist_ok=True)
                if i.endswith("ogg"):
                    os.makedirs(self.s+os.sep+"music files"+os.sep+"ogg files",exist_ok=True)
                if i.endswith("wma"):
                    os.makedirs(self.s+os.sep+"music files"+os.sep+"wma files",exist_ok=True)
                if i.endswith("m4a"):
                    os.makedirs(self.s+os.sep+"music files"+os.sep+"m4a files",exist_ok=True)
                if i.endswith("alac"):
                    os.makedirs(self.s+os.sep+"music files"+os.sep+"alac files",exist_ok=True)
                if i.endswith("aiff"):
                    os.makedirs(self.s+os.sep+"music files"+os.sep+"aiff files",exist_ok=True)
                if i.endswith("amr"):
                    os.makedirs(self.s+os.sep+"music files"+os.sep+"amr files",exist_ok=True)
                if i.endswith("opus"):
                    os.makedirs(self.s+os.sep+"music files"+os.sep+"opus files",exist_ok=True)
            for i in data:
                if i.endswith("mp3"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"music files"+os.sep+"mp3 files")
                if i.endswith("wav"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"music files"+os.sep+"wav files")
                if i.endswith("aac"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"music files"+os.sep+"aac files")
                if i.endswith("flac"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"music files"+os.sep+"flac files")
                if i.endswith("ogg"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"music files"+os.sep+"ogg files")
                if i.endswith("wma"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"music files"+os.sep+"wma files")
                if i.endswith("m4a"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"music files"+os.sep+"m4a files")
                if i.endswith("alac"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"music files"+os.sep+"alac files")
                if i.endswith("aiff"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"music files"+os.sep+"aiff files")
                if i.endswith("amr"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"music files"+os.sep+"amr files")
                if i.endswith("opus"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"music files"+os.sep+"opus files")

        except:
            print("operation wasn`t ok")

    @property
    def sort_exe(self):
        data = os.listdir(self.s)
        if "exe files" in data:
            for i in data:
                if i.endswith(".exe"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"exe files")
                    print(f"file {i} moved to exe files")
        elif "exe files" not in data:
            os.mkdir(self.s+os.sep+"exe files")
        try:
            for i in data:
                if i.endswith(".exe"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"exe files")
                    print(f"file {i} moved to exe files")
        except:
            print("operation wasn`t ok")

    @property
    def sort_rar(self):
        data = os.listdir(self.s)
        if "rar files" in data:
            for i in data:
                if i.endswith(".rar"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"rar files")
                    print(f"file {i} moved to rar files")
        elif "rar files" not in data:
            os.mkdir(self.s+os.sep+"rar files")
        try:
            for i in data:
                if i.endswith(".rar"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"rar files")
                    print(f"file {i} moved to rar files")
        except:
            print("operation wasn`t ok")


    @property
    def sort_apk(self):
        data = os.listdir(self.s)
        if "apk files" in data:
            for i in data:
                if i.endswith(".apk"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"apk files")
                    print(f"file {i} moved to apk files")
        elif "apk files" not in data:
            os.mkdir(self.s+os.sep+"apk files")
        try:
            for i in data:
                if i.endswith(".apk"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"apk files")
                    print(f"file {i} moved to apk files")
        except:
            print("operation wasn`t ok")
    @property
    def sort_zip(self):
        data = os.listdir(self.s)
        if "zip files" in data:
            for i in data:
                if i.endswith(".zip"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"zip files")
                    print(f"file {i} moved to zip files")
        elif "zip files" not in data:
            os.mkdir(self.s+os.sep+"zip files")
        try:
            for i in data:
                if i.endswith(".zip"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"zip files")
                    print(f"file {i} moved to zip files")
        except:
            print("operation wasn`t ok")

    @property
    def sort_access(self):
        data = os.listdir(self.s)
        if "access files" in data:
            for i in data:
                if i.endswith(".accdb"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"access files")
                    print(f"file {i} moved to access files")
        elif "access files" not in data:
            os.mkdir(self.s+os.sep+"access files")
        try:
            for i in data:
                if i.endswith(".accdb"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"access files")
                    print(f"file {i} moved to access files")
        except:
            print("operation wasn`t ok")

class Window(customtkinter.CTk):

    def setting(self):
        setting = customtkinter.CTk()

        setting.geometry(f"{setting.winfo_screenwidth()}x{setting.winfo_screenheight()}+0+0")
        setting.title("Settings")

        def ForegroundColorButton(ch):
            btn_sort_access.configure(hover_color=ch)
            btn_sort_apk.configure(hover_color=ch)
            btn_sort_all.configure(hover_color=ch)
            btn_sort_csv.configure(hover_color=ch)
            btn_sort_exe.configure(hover_color=ch)
            btn_sort_html.configure(hover_color=ch)
            btn_sort_json.configure(hover_color=ch)
            btn_sort_music.configure(hover_color=ch)
            btn_sort_pdf.configure(hover_color=ch)
            btn_sort_photo.configure(hover_color=ch)
            btn_sort_pickle.configure(hover_color=ch)
            btn_sort_powerpoint.configure(hover_color=ch)
            btn_sort_python.configure(hover_color=ch)
            btn_sort_rar.configure(hover_color=ch)
            btn_sort_txt.configure(hover_color=ch)
            btn_sort_video.configure(hover_color=ch)
            btn_sort_word.configure(hover_color=ch)
            btn_sort_excel.configure(hover_color=ch)
            btn_sort_zip.configure(hover_color=ch)

        def BackgroundColorButton(ch):
            btn_sort_access.configure(fg_color=ch)
            btn_sort_apk.configure(fg_color=ch)
            btn_sort_all.configure(fg_color=ch)
            btn_sort_csv.configure(fg_color=ch)
            btn_sort_exe.configure(fg_color=ch)
            btn_sort_html.configure(fg_color=ch)
            btn_sort_json.configure(fg_color=ch)
            btn_sort_music.configure(fg_color=ch)
            btn_sort_pdf.configure(fg_color=ch)
            btn_sort_photo.configure(fg_color=ch)
            btn_sort_pickle.configure(fg_color=ch)
            btn_sort_powerpoint.configure(fg_color=ch)
            btn_sort_python.configure(fg_color=ch)
            btn_sort_rar.configure(fg_color=ch)
            btn_sort_txt.configure(fg_color=ch)
            btn_sort_video.configure(fg_color=ch)
            btn_sort_word.configure(fg_color=ch)
            btn_sort_excel.configure(fg_color=ch)
            btn_sort_zip.configure(fg_color=ch)
        
        def get_home():
            setting.destroy()

        def TextColorButtons(ch):
            btn_sort_access.configure(text_color=ch)
            btn_sort_apk.configure(text_color=ch)
            btn_sort_all.configure(text_color=ch)
            btn_sort_csv.configure(text_color=ch)
            btn_sort_exe.configure(text_color=ch)
            btn_sort_html.configure(text_color=ch)
            btn_sort_json.configure(text_color=ch)
            btn_sort_music.configure(text_color=ch)
            btn_sort_pdf.configure(text_color=ch)
            btn_sort_photo.configure(text_color=ch)
            btn_sort_pickle.configure(text_color=ch)
            btn_sort_powerpoint.configure(text_color=ch)
            btn_sort_python.configure(text_color=ch)
            btn_sort_rar.configure(text_color=ch)
            btn_sort_txt.configure(text_color=ch)
            btn_sort_video.configure(text_color=ch)
            btn_sort_word.configure(text_color=ch)
            btn_sort_excel.configure(text_color=ch)
            btn_sort_zip.configure(text_color=ch)

        MenuBar = Menu(setting)
        setting.config(menu=MenuBar)

        HomeMenu = Menu(setting,tearoff=0,font=5,activebackground="black",activeforeground="red",fg="Blue",bg="white")
        HomeMenu.add_command(label="Home",command=get_home)
        MenuBar.add_cascade(label="Home",menu=HomeMenu)

        lbl = customtkinter.CTkLabel(setting,text="BackGroundColorsButtons")
        lbl.pack(pady=10)

        color = ["black","white"]

        colors = ["red","green","blue","silver","purple","yellow","black","white"]

        colors2 = ["blue","green","red","silver","purple","yellow","black","white"]


        combo = customtkinter.CTkComboBox(setting,values=colors,command=BackgroundColorButton)
        combo.pack(pady=10)

        lbl2 = customtkinter.CTkLabel(setting,text="ForeGroundColorsButtons")
        lbl2.pack(pady=10)

        combo2 = customtkinter.CTkComboBox(setting,values=colors2,command=ForegroundColorButton)
        combo2.pack(pady=10)

        lbl3 = customtkinter.CTkLabel(setting,text="TextColorButtons")
        lbl3.pack(pady=10)

        combo3 = customtkinter.CTkComboBox(setting,values=color,command=TextColorButtons)
        combo3.pack(pady=10)

        setting.mainloop()
    def help(self):
        help = customtkinter.CTk()

        help.geometry(f"{help.winfo_screenwidth()}x{help.winfo_screenheight()}+0+0")
        help.title("Help")

        def dest():
            help.destroy()

        def help_del():
            Description.configure(state="normal")
            Description.delete(0.0,'end')
            Description.configure(state="disabled")

        def help_():
            Description.configure(state="normal")
            Description.insert(0.0,text=

                """

Description:

To use this program, you must first enter an address in the relevant field

Note: The address must belong to a folder of files, not the address of a file

The exit button is for closing the program.

You can delete the folder address with the delete address button and then enter a new address so that you do not need to close and reopen the program

After entering the address, click the desired button to sort the files so that all the relevant files go to the folder created by the program

For example, when you click the sort_exe button, all the exe files of the address go to the folder that is automatically created and the folder name is exe_files

If you click a button and there is no file of that type, the program creates an empty folder for you

This program is able to sort 18 different types including photos, videos, music, ...


Note: Because the photo file has many types, 
the program, in addition to automatically creating a folder in that folder, 
also creates another folder. 
This time, the name of the second automatic folder is the name of the photo type that the file follows.
For example, if you have a photo file with the extension jpg, when the program creates the photo_files folder,
it creates another folder called jpg_files inside it, 
and all your photo files that have this extension go into that folder.
Music and video files are like photo files.

If you click the sort_all button, it will sort all 18 types for you

Note: Suppose you used this program and, for example, sorted Python files, now you have added another Python file to your folder. When you press the sort_python button, the program will no longer create a folder, but will move all Python files back to the folder that was previously created for the first time.

From the color_them section, you can choose the theme you want, which is white or black.

This section also has a system option, which will be the background color of your system, which is ultimately white or black.

Trans_late to persian language

ترجمه به زبان فارسی


توضیحات:

برای استفاده از این برنامه ابتدا باید یک آدرس در قسمت مربوطه وارد کنید

توجه: آدرس باید متعلق به پوشه ای از فایل ها باشد، نه آدرس یک فایل

دکمه خروج از برنامه برای بستن برنامه است

می توانید آدرس پوشه را با دکمه حذف آدرس حذف کنید و سپس یک آدرس جدید وارد کنید تا نیازی به بستن و باز کردن مجدد برنامه نباشد.

پس از وارد کردن آدرس، روی دکمه مورد نظر کلیک کنید تا فایل ها مرتب شوند تا تمام فایل های مربوطه به پوشه ایجاد شده توسط برنامه بروند.

به عنوان مثال، وقتی دکمه sort_exe را کلیک می کنید، تمام فایل های exe آدرس به پوشه ای می روند که به طور خودکار ایجاد می شود و نام پوشه exe_files است.

اگر روی دکمه ای کلیک کنید و فایلی از آن نوع وجود نداشته باشد، برنامه یک پوشه خالی برای شما ایجاد می کند

این برنامه قادر است 18 نوع مختلف از جمله عکس، فیلم، موزیک و ... را مرتب کند.


توجه: از آنجا که فایل عکس دارای انواع مختلفی است،
این برنامه علاوه بر ایجاد خودکار یک پوشه در آن پوشه،
همچنین یک پوشه دیگر ایجاد می کند.
این بار نام پوشه دوم خودکار نام نوع عکسی است که فایل دنبال می کند.
به عنوان مثال، اگر یک فایل عکس با پسوند jpg دارید، زمانی که برنامه پوشه photo_files را ایجاد می کند،
پوشه دیگری به نام jpg_files در داخل آن ایجاد می کند،
و تمام فایل های عکس شما که دارای این پسوند هستند به آن پوشه می روند.
فایل های موسیقی و ویدئو مانند فایل های عکس هستند.

اگر روی دکمه sort_all کلیک کنید، همه 18 نوع را برای شما مرتب می کند

نکته: فرض کنید از این برنامه استفاده کرده اید و مثلا فایل های پایتون را مرتب کرده اید، حالا یک فایل پایتون دیگر را به پوشه خود اضافه کرده اید. هنگامی که دکمه sort_python را فشار می دهید، برنامه دیگر پوشه ای ایجاد نمی کند، بلکه تمام فایل های پایتون را به پوشه ای که قبلا برای اولین بار ایجاد شده بود، برمی گرداند.

از قسمت color_them می توانید تم مورد نظر خود را انتخاب کنید که سفید یا مشکی است.

این قسمت یک گزینه سیستم نیز دارد که رنگ پس زمینه سیستم شما خواهد بود که در نهایت سفید یا سیاه است.





            
        

        """
            )
            Description.configure(state="disabled")

        MenuBar = Menu(help)
        help.config(menu=MenuBar)

        HomeMenu = Menu(MenuBar,tearoff=0,font=5,activebackground="black",activeforeground="red",fg="Blue",bg="white")
        HomeMenu.add_command(label="Home",command=dest)
        MenuBar.add_cascade(label="Home",menu=HomeMenu)

        Description = customtkinter.CTkTextbox(help,state="disabled",font=customtkinter.CTkFont(size=25),wrap="word",width=500,height=500)
        Description.pack(pady=10)

        btn_help = customtkinter.CTkButton(help,text_color="black",text="Description",fg_color="red",hover_color="blue",corner_radius=50,command=help_)
        btn_help.pack(pady=10)

        btn_help_del = customtkinter.CTkButton(help,text_color="black",text="Delete-Description",fg_color="red",hover_color="blue",corner_radius=50,command=help_del)
        btn_help_del.pack(pady=10)

        help.mainloop()


    def info(self):
        help = customtkinter.CTk()

        help.geometry(f"{help.winfo_screenwidth()}x{help.winfo_screenheight()}+0+0")
        help.title("info")

        def dest():
            help.destroy()

        def help_del():
            Description.configure(state="normal")
            Description.delete(0.0,'end')
            Description.configure(state="disabled")

        def help_():
            Description.configure(state="normal")
            Description.insert(0.0,text=

                """
                Program specifications:

Program name: Sort _Files++
Program function: Sort files in a folder
Programmer: mohammad Moein Hosseinzadeh
designer : Amir Mohammad RajabAlian
Author_email = moein191013895@gmail.com
Programming language : Python
Year of manufacture : 2024
Number of program lines: 1515
Duration of creation: 5 months

Warning : The program can be run on a 64-bit system.

مشخصات برنامه:

نام برنامه: Sort _Files++
عملکرد برنامه: مرتب سازی فایل ها در یک پوشه
برنامه نویس : محمد معین حسین زاده
طراح:امیر محمد رجبعلیان
نویسنده_ایمیل : moein191013895@gmail.com
زبان برنامه نویسی: پایتون
سال ساخت: 2024
تعداد خطوط برنامه: 1515
مدت زمان ایجاد: 5 ماه

هشدار: برنامه را می توان بر روی یک سیستم 64 بیتی اجرا کرد.

        

        """
            )
            Description.configure(state="disabled")

        MenuBar = Menu(help)
        help.config(menu=MenuBar)

        HomeMenu = Menu(MenuBar,tearoff=0,font=5,activebackground="black",activeforeground="red",fg="Blue",bg="white")
        HomeMenu.add_command(label="Home",command=dest)
        MenuBar.add_cascade(label="Home",menu=HomeMenu)

        Description = customtkinter.CTkTextbox(help,state="disabled",font=customtkinter.CTkFont(size=25),wrap="word",width=500,height=500)
        Description.pack(pady=10)

        btn_help = customtkinter.CTkButton(help,text_color="black",text="Description",fg_color="red",hover_color="blue",corner_radius=50,command=help_)
        btn_help.pack(pady=10)

        btn_help_del = customtkinter.CTkButton(help,text_color="black",text="Delete-Description",fg_color="red",hover_color="blue",corner_radius=50,command=help_del)
        btn_help_del.pack(pady=10)

        help.mainloop()


    def them(self,ch):
        customtkinter.set_appearance_mode(ch)

    def delete(self):
        entry.delete(0,"end")

    def prev(self):
        input_.deiconify()

    def access(self):
        address = Sort_files(entry.get())
        print(address.sort_access)
        ok.remove("sort files ok")
        ok.append("sort-access was ok")
        combo.configure(values=ok)
        

    def apk(self):
        address = Sort_files(entry.get())
        print(address.sort_apk)
        ok.remove("sort files ok")
        ok.append("sort-apk was ok")
        combo.configure(values=ok)

    def csv(self):
        address = Sort_files(entry.get())
        print(address.sort_csv)
        ok.remove("sort files ok")
        ok.append("sort-csv was ok")
        combo.configure(values=ok)

    def exe(self):
        address = Sort_files(entry.get())
        print(address.sort_exe)
        ok.remove("sort files ok")
        ok.append("sort-exe was ok")
        combo.configure(values=ok)

    def html(self):
        address = Sort_files(entry.get())
        print(address.sort_html)
        ok.remove("sort files ok")
        ok.append("sort-html was ok")
        combo.configure(values=ok)

    def json(self):
        address = Sort_files(entry.get())
        print(address.sort_json)
        ok.remove("sort files ok")
        ok.append("sort-json was ok")
        combo.configure(values=ok)

    def music(self):
        address = Sort_files(entry.get())
        print(address.sort_music)
        ok.remove("sort files ok")
        ok.append("sort-music was ok")
        combo.configure(values=ok)

    def pdf(self):
        address = Sort_files(entry.get())
        print(address.sort_pdf)
        ok.remove("sort files ok")
        ok.append("sort-pdf was ok")
        combo.configure(values=ok)

    def photo(self):
        address = Sort_files(entry.get())
        print(address.sort_photo)
        ok.remove("sort files ok")
        ok.append("sort-photo was ok")
        combo.configure(values=ok)

    def pickle(self):
        address = Sort_files(entry.get())
        print(address.sort_pickle)
        ok.remove("sort files ok")
        ok.append("sort-pickle was ok")
        combo.configure(values=ok)
    def powerpoint(self):
        address = Sort_files(entry.get())
        print(address.sort_powerPoint)
        ok.remove("sort files ok")
        ok.append("sort-powerpoint was ok")
        combo.configure(values=ok)
    def python(self):
        address = Sort_files(entry.get())
        print(address.sort_python)
        ok.remove("sort files ok")
        ok.append("sort-python was ok")
        combo.configure(values=ok)

    def rar(self):
        address = Sort_files(entry.get())
        print(address.sort_rar)
        ok.remove("sort files ok")
        ok.append("sort-rar was ok")
        combo.configure(values=ok)
    def txt(self):
        address = Sort_files(entry.get())
        print(address.sort_txt)
        ok.remove("sort files ok")
        ok.append("sort-txt was ok")
        combo.configure(values=ok)
    def video(self):
        address = Sort_files(entry.get())
        print(address.sort_video)
        ok.remove("sort files ok")
        ok.append("sort-video was ok")
        combo.configure(values=ok)

    def word(self):
        address = Sort_files(entry.get())
        print(address.sort_docx)
        ok.remove("sort files ok")
        ok.append("sort-word was ok")
        combo.configure(values=ok)
    def excel(self):
        address = Sort_files(entry.get())
        print(address.sort_xlsx)
        ok.remove("sort files ok")
        ok.append("sort-excel was ok")
        combo.configure(values=ok)

    def zip(self):
        address = Sort_files(entry.get())
        print(address.sort_zip)
        ok.remove("sort files ok")
        ok.append("sort-zip was ok")
        combo.configure(values=ok)

    def all(self):
        address = Sort_files(entry.get())
        print(address.sort_access)
        print(address.sort_apk)
        print(address.sort_csv)
        print(address.sort_docx)
        print(address.sort_exe)
        print(address.sort_html)
        print(address.sort_json)
        print(address.sort_music)
        print(address.sort_pdf)
        print(address.sort_photo)
        print(address.sort_pickle)
        print(address.sort_powerPoint)
        print(address.sort_python)
        print(address.sort_rar)
        print(address.sort_video)
        print(address.sort_txt)
        print(address.sort_zip)
        print(address.sort_xlsx)
        ok.remove("sort files ok")
        ok.append("sort-all was ok")
        combo.configure(values=ok)
    def __init__(self):
        super().__init__()
        
        MenuBar = Menu(self)
        self.config(menu=MenuBar)
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        self.geometry(f"{width}x{height}+0+0")
        self.title("Sort_Files++")
        self.grid_columnconfigure(0,weight=1)
        self.grid_columnconfigure(1,weight=1)
        self.grid_rowconfigure(0,weight=1)
        self.grid_rowconfigure(1,weight=7)
        customtkinter.set_appearance_mode("light")
        frame1 = customtkinter.CTkFrame(self)
        frame1.grid(row=0,column=1,sticky="nsew")
        frame1.grid_columnconfigure(5,weight=5)
        frame1.grid_rowconfigure(5,weight=5)

        global ok
        ok = ["sort files ok"]
        global combo
        combo = customtkinter.CTkComboBox(frame1,values=ok)
        combo.grid(row=5,column=5,sticky="ew")

        frame1.grid_columnconfigure(0,weight=1)

        ExitMenu = Menu(self,tearoff=0,font=5,activebackground="black",activeforeground="red",fg="Blue",bg="white")
        ExitMenu.add_command(label="Exit",command=self.quit)
        MenuBar.add_cascade(label="Exit",menu=ExitMenu)

        frame2 = customtkinter.CTkFrame(self)
        frame2.grid(row=1,column=0,sticky="nsew")

        frame3 = customtkinter.CTkFrame(self)
        frame3.grid(row=0, column=0, sticky="nsew")
        frame3.grid_rowconfigure(6,weight=5)


        global btn_sort_access
        btn_sort_access = customtkinter.CTkButton(frame3, fg_color="red", hover_color="blue", text="sort_access",command=self.access,text_color="black")
        btn_sort_access.grid(row=0, column=0, sticky="nsew",pady=5,padx=5)

        global btn_sort_apk
        btn_sort_apk = customtkinter.CTkButton(frame3, fg_color="red", hover_color="blue", text="sort_android",command=self.apk,text_color="black")
        btn_sort_apk.grid(row=1, column=0, sticky="nsew",pady=5,padx=5)

        global btn_sort_csv
        btn_sort_csv = customtkinter.CTkButton(frame3,fg_color="red",hover_color="blue",text="sort_csv",command=self.csv,text_color="black")
        btn_sort_csv.grid(row=2,column=0,sticky="nsew",pady=5,padx=5)


        global btn_sort_exe
        btn_sort_exe = customtkinter.CTkButton(frame3,fg_color="red",hover_color="blue",text="sort_exe",command=self.exe,text_color="black")
        btn_sort_exe.grid(row=3,column=0,sticky="nsew",pady=5,padx=5)


        global btn_sort_html
        btn_sort_html = customtkinter.CTkButton(frame3,fg_color="red",hover_color="blue",text="sort_html",command=self.html,text_color="black")
        btn_sort_html.grid(sticky="nsew",pady=5,padx=5,row=5,column=2)


        global btn_sort_json
        btn_sort_json = customtkinter.CTkButton(frame3, fg_color="red", hover_color="blue", text="sort_json",command=self.json,text_color="black")
        btn_sort_json.grid(row=4, column=0, sticky="nsew", pady=5, padx=5)

        global btn_sort_music
        btn_sort_music = customtkinter.CTkButton(frame3, fg_color="red", hover_color="blue", text="sort_music",command=self.music,text_color="black")
        btn_sort_music.grid(row=5, column=0, sticky="nsew", pady=5, padx=5)

        global btn_sort_pdf
        btn_sort_pdf = customtkinter.CTkButton(frame3, fg_color="red", hover_color="blue", text="sort_pdf",command=self.pdf, text_color="black")
        btn_sort_pdf.grid(row=0, column=1, sticky="nsew", pady=5, padx=5)


        global btn_sort_photo
        btn_sort_photo = customtkinter.CTkButton(frame3, fg_color="red", hover_color="blue", text="sort_photo",command=self.photo, text_color="black")
        btn_sort_photo.grid(row=1, column=1, sticky="nsew", pady=5, padx=5)


        global btn_sort_pickle
        btn_sort_pickle = customtkinter.CTkButton(frame3, fg_color="red", hover_color="blue", text="sort_pickle",command=self.pickle, text_color="black")
        btn_sort_pickle.grid(row=2, column=1, sticky="nsew", pady=5, padx=5)

        global btn_sort_powerpoint
        btn_sort_powerpoint = customtkinter.CTkButton(frame3, fg_color="red", hover_color="blue", text="sort_powerpoint",command=self.powerpoint, text_color="black")
        btn_sort_powerpoint.grid(row=3, column=1, sticky="nsew", pady=5, padx=5)


        global btn_sort_python
        btn_sort_python = customtkinter.CTkButton(frame3, fg_color="red", hover_color="blue", text="sort_python",command=self.python, text_color="black")
        btn_sort_python.grid(row=4, column=1, sticky="nsew", pady=5, padx=5)


        global btn_sort_rar
        btn_sort_rar = customtkinter.CTkButton(frame3, fg_color="red", hover_color="blue", text="sort_rar",command=self.rar, text_color="black")
        btn_sort_rar.grid(row=5, column=1, sticky="nsew", pady=5, padx=5)


        global btn_sort_txt
        btn_sort_txt = customtkinter.CTkButton(frame3, fg_color="red", hover_color="blue", text="sort_txt",command=self.txt, text_color="black")
        btn_sort_txt.grid(row=0, column=2, sticky="nsew", pady=5, padx=5)


        global btn_sort_video
        btn_sort_video = customtkinter.CTkButton(frame3, fg_color="red", hover_color="blue", text="sort_video",command=self.video, text_color="black")
        btn_sort_video.grid(row=1, column=2, sticky="nsew", pady=5, padx=5)


        global btn_sort_word
        btn_sort_word = customtkinter.CTkButton(frame3, fg_color="red", hover_color="blue", text="sort_word",command=self.word, text_color="black")
        btn_sort_word.grid(row=2, column=2, sticky="nsew", pady=5, padx=5)


        global btn_sort_excel
        btn_sort_excel = customtkinter.CTkButton(frame3, fg_color="red", hover_color="blue", text="sort_excel",command=self.excel, text_color="black")
        btn_sort_excel.grid(row=3, column=2, sticky="nsew", pady=5, padx=5)


        global btn_sort_zip
        btn_sort_zip = customtkinter.CTkButton(frame3, fg_color="red", hover_color="blue", text="sort_zip",command=self.zip, text_color="black")
        btn_sort_zip.grid(row=4, column=2, sticky="nsew", pady=5, padx=5)

        btn_Previous_page = customtkinter.CTkButton(frame3,fg_color="green",hover_color="blue",text_color="black",text="Input Page",command=self.prev)
        btn_Previous_page.grid(row=3,column=5,sticky="ew",padx=50)

        global btn_sort_all
        btn_sort_all = customtkinter.CTkButton(frame3,fg_color="red",hover_color="blue",text="sort_all",command=self.all,text_color="black")
        btn_sort_all.grid(row=6,column=0,sticky="ew",columnspan=3,padx=5,pady=5)

        frame4 = customtkinter.CTkFrame(self)
        frame4.grid(row=1, column=1, sticky="nsew",rowspan=2)
        frame4.grid_columnconfigure(0,weight=1)
        frame4.grid_rowconfigure(1,weight=2)
        frame4.grid_columnconfigure(1,weight=0)

        HelpMenu = Menu(MenuBar,tearoff=0,font=5,activebackground="black",activeforeground="red",fg="Blue",bg="white")
        HelpMenu.add_command(label="Help",command=self.help)
        HelpMenu.add_command(label="info",command=self.info)
        MenuBar.add_cascade(label="Help",menu = HelpMenu)

        SettingMenu = Menu(self,tearoff=0,font=5,activebackground="black",activeforeground="red",fg="Blue",bg="white")
        SettingMenu.add_command(label="Settings",command=self.setting)
        MenuBar.add_cascade(label="Settings",menu=SettingMenu)


class Input(customtkinter.CTk):
        
    def help(self):
        help = customtkinter.CTk()

        help.geometry(f"{help.winfo_screenwidth()}x{help.winfo_screenheight()}+0+0")
        help.title("Help")

        def dest():
            help.destroy()

        def help_del():
            Description.configure(state="normal")
            Description.delete(0.0,'end')
            Description.configure(state="disabled")

        def help_():
            Description.configure(state="normal")
            Description.insert(0.0,text=

                """

Description:

To use this program, you must first enter an address in the relevant field

Note: The address must belong to a folder of files, not the address of a file

The exit button is for closing the program.

You can delete the folder address with the delete address button and then enter a new address so that you do not need to close and reopen the program

After entering the address, click the desired button to sort the files so that all the relevant files go to the folder created by the program

For example, when you click the sort_exe button, all the exe files of the address go to the folder that is automatically created and the folder name is exe_files

If you click a button and there is no file of that type, the program creates an empty folder for you

This program is able to sort 18 different types including photos, videos, music, ...


Note: Because the photo file has many types, 
the program, in addition to automatically creating a folder in that folder, 
also creates another folder. 
This time, the name of the second automatic folder is the name of the photo type that the file follows.
For example, if you have a photo file with the extension jpg, when the program creates the photo_files folder,
it creates another folder called jpg_files inside it, 
and all your photo files that have this extension go into that folder.
Music and video files are like photo files.

If you click the sort_all button, it will sort all 18 types for you

Note: Suppose you used this program and, for example, sorted Python files, now you have added another Python file to your folder. When you press the sort_python button, the program will no longer create a folder, but will move all Python files back to the folder that was previously created for the first time.

From the color_them section, you can choose the theme you want, which is white or black.

This section also has a system option, which will be the background color of your system, which is ultimately white or black.

Trans_late to persian language

ترجمه به زبان فارسی


توضیحات:

برای استفاده از این برنامه ابتدا باید یک آدرس در قسمت مربوطه وارد کنید

توجه: آدرس باید متعلق به پوشه ای از فایل ها باشد، نه آدرس یک فایل

دکمه خروج از برنامه برای بستن برنامه است

می توانید آدرس پوشه را با دکمه حذف آدرس حذف کنید و سپس یک آدرس جدید وارد کنید تا نیازی به بستن و باز کردن مجدد برنامه نباشد.

پس از وارد کردن آدرس، روی دکمه مورد نظر کلیک کنید تا فایل ها مرتب شوند تا تمام فایل های مربوطه به پوشه ایجاد شده توسط برنامه بروند.

به عنوان مثال، وقتی دکمه sort_exe را کلیک می کنید، تمام فایل های exe آدرس به پوشه ای می روند که به طور خودکار ایجاد می شود و نام پوشه exe_files است.

اگر روی دکمه ای کلیک کنید و فایلی از آن نوع وجود نداشته باشد، برنامه یک پوشه خالی برای شما ایجاد می کند

این برنامه قادر است 18 نوع مختلف از جمله عکس، فیلم، موزیک و ... را مرتب کند.


توجه: از آنجا که فایل عکس دارای انواع مختلفی است،
این برنامه علاوه بر ایجاد خودکار یک پوشه در آن پوشه،
همچنین یک پوشه دیگر ایجاد می کند.
این بار نام پوشه دوم خودکار نام نوع عکسی است که فایل دنبال می کند.
به عنوان مثال، اگر یک فایل عکس با پسوند jpg دارید، زمانی که برنامه پوشه photo_files را ایجاد می کند،
پوشه دیگری به نام jpg_files در داخل آن ایجاد می کند،
و تمام فایل های عکس شما که دارای این پسوند هستند به آن پوشه می روند.
فایل های موسیقی و ویدئو مانند فایل های عکس هستند.

اگر روی دکمه sort_all کلیک کنید، همه 18 نوع را برای شما مرتب می کند

نکته: فرض کنید از این برنامه استفاده کرده اید و مثلا فایل های پایتون را مرتب کرده اید، حالا یک فایل پایتون دیگر را به پوشه خود اضافه کرده اید. هنگامی که دکمه sort_python را فشار می دهید، برنامه دیگر پوشه ای ایجاد نمی کند، بلکه تمام فایل های پایتون را به پوشه ای که قبلا برای اولین بار ایجاد شده بود، برمی گرداند.

از قسمت color_them می توانید تم مورد نظر خود را انتخاب کنید که سفید یا مشکی است.

این قسمت یک گزینه سیستم نیز دارد که رنگ پس زمینه سیستم شما خواهد بود که در نهایت سفید یا سیاه است.





            
        

        """
            )
            Description.configure(state="disabled")

        MenuBar = Menu(help)
        help.config(menu=MenuBar)

        HomeMenu = Menu(MenuBar,tearoff=0,font=5,activebackground="black",activeforeground="red",fg="Blue",bg="white")
        HomeMenu.add_command(label="Input",command=dest)
        MenuBar.add_cascade(label="Input",menu=HomeMenu)

        global Description

        Description = customtkinter.CTkTextbox(help,state="disabled",font=customtkinter.CTkFont(size=25),wrap="word",width=500,height=500)
        Description.pack(pady=10)

        btn_help = customtkinter.CTkButton(help,text_color="black",text="Description",fg_color="red",hover_color="blue",corner_radius=50,command=help_)
        btn_help.pack(pady=10)

        btn_help_del = customtkinter.CTkButton(help,text_color="black",text="Delete-Description",fg_color="red",hover_color="blue",corner_radius=50,command=help_del)
        btn_help_del.pack(pady=10)

        help.mainloop()


    def info(self):
        help = customtkinter.CTk()

        help.geometry(f"{help.winfo_screenwidth()}x{help.winfo_screenheight()}+0+0")
        help.title("info")

        def dest():
            help.destroy()

        def help_del():
            Description.configure(state="normal")
            Description.delete(0.0,'end')
            Description.configure(state="disabled")

        def help_():
            Description.configure(state="normal")
            Description.insert(0.0,text=

                """

                            
Program specifications:

Program name: Sort _Files++
Program function: Sort files in a folder
Programmer: mohammad Moein Hosseinzadeh
designer : Amir Mohammad RajabAlian
Author_email = moein191013895@gmail.com
Programming language : Python
Year of manufacture : 2024
Number of program lines: 1515
Duration of creation: 5 months

Warning : The program can be run on a 64-bit system.

مشخصات برنامه:

نام برنامه: Sort _Files++
عملکرد برنامه: مرتب سازی فایل ها در یک پوشه
برنامه نویس : محمد معین حسین زاده
طراح:امیر محمد رجبعلیان
نویسنده_ایمیل : moein191013895@gmail.com
زبان برنامه نویسی: پایتون
سال ساخت: 2024
تعداد خطوط برنامه: 1515
مدت زمان ایجاد: 5 ماه

هشدار: برنامه را می توان بر روی یک سیستم 64 بیتی اجرا کرد.
            
        

        """
            )
            Description.configure(state="disabled")

        MenuBar = Menu(help)
        help.config(menu=MenuBar)

        HomeMenu = Menu(MenuBar,tearoff=0,font=5,activebackground="black",activeforeground="red",fg="Blue",bg="white")
        HomeMenu.add_command(label="Input",command=dest)
        MenuBar.add_cascade(label="Input",menu=HomeMenu)

        global Description

        Description = customtkinter.CTkTextbox(help,state="disabled",font=customtkinter.CTkFont(size=25),wrap="word",width=500,height=500)
        Description.pack(pady=10)

        btn_help = customtkinter.CTkButton(help,text_color="black",text="Description",fg_color="red",hover_color="blue",corner_radius=50,command=help_)
        btn_help.pack(pady=10)

        btn_help_del = customtkinter.CTkButton(help,text_color="black",text="Delete-Description",fg_color="red",hover_color="blue",corner_radius=50,command=help_del)
        btn_help_del.pack(pady=10)

        help.mainloop()


    def delete(self):
        entry.delete(0,'end')

    def __init__(self):
        super().__init__()
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}+0+0")
        self.title("Input")
        customtkinter.set_appearance_mode("light")

        MenuBar = Menu(self)
        self.config(menu=MenuBar)
        ExitMenu = Menu(MenuBar,tearoff=0,font=5,activebackground="black",activeforeground="red",fg="Blue",bg="white")
        ExitMenu.add_command(label="Exit",command=self.quit)
        MenuBar.add_cascade(label="Exit",menu=ExitMenu)

        HelpMenu = Menu(MenuBar,tearoff=0,font=5,activebackground="black",activeforeground="red",fg="Blue",bg="white")
        HelpMenu.add_command(label="Help",command=self.help)
        HelpMenu.add_command(label="info",command=self.info)
        MenuBar.add_cascade(label="Help",menu = HelpMenu)

        global entry
        entry = customtkinter.CTkEntry(self,placeholder_text="Enter your address in this PC for sort files : ",width=500,corner_radius=50,fg_color="blue",text_color="black",border_color="silver")
        entry.pack(pady=10)

        btn_delete = customtkinter.CTkButton(self,text="Delete_address",hover_color="yellow",text_color="black",fg_color="green",corner_radius=50,command=self.delete)
        btn_delete.pack(pady=10)

        btn_nextPage = customtkinter.CTkButton(self,text="Home Page",hover_color="yellow",text_color="black",fg_color="green",corner_radius=50,command=self.next)
        btn_nextPage.pack(pady=10)
    
    def next(self):
        if __name__ == "__main__":
            window2 = Window()
            window2.mainloop()
        self.destroy()

        if window2.destroy():
            self.destroy()


class Welcome(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}+0+0")
        self.title("Welcome")
        customtkinter.set_appearance_mode("light")

        lbl = customtkinter.CTkLabel(self,text="Welcome",font=customtkinter.CTkFont(size=25))
        lbl.pack(pady=10)

        start_app = customtkinter.CTkButton(self,text="StartApp",text_color="black",fg_color="green",hover_color="blue",corner_radius=50,command=self.get_entry)
        start_app.pack(pady=10)

    def get_entry(self):

        self.destroy()
        if __name__ == "__main__":
            global input_
            input_ = Input()
            input_.mainloop()

if __name__ == "__main__":
    window = Welcome()
    window.mainloop()