import shutil
import subprocess
import os

def convert_file(filepath, outdir):
    try:
        subprocess.call(["pdflatex", "-output-directory", outdir, filepath], stdout=subprocess.DEVNULL)
        pdffilename = os.path.splitext(os.path.basename(filepath))[0] + ".pdf"
        shutil.copyfile(
            os.path.join(outdir, pdffilename),
            os.path.join("./material", pdffilename)
        )
    except:
        print("Error")


if __name__ == "__main__":
    files = os.listdir("./src")
    fileindex = 0
    for file in files:
        fileindex += 1
        print(f"Converting File {fileindex}/{len(files)}: {os.path.join('./src', file)} ")
        convert_file(os.path.join("./src", file), "./build")
