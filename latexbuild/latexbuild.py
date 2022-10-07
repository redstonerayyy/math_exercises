import shutil
import subprocess
import os
import pathlib

def convert_file(filepath, buildir, outdir):
    # make build dir
    if not os.path.exists(buildir):
            os.mkdir(buildir)


    # if some files error, continue building the others and print error
    try:
        # start pdflatex executable with arguments and no shell output
        subprocess.call(["pdflatex", "-output-directory", buildir, filepath], stdout=subprocess.DEVNULL)
        # generate filename of new pdf
        pdffilename = os.path.splitext(os.path.basename(filepath))[0] + ".pdf"
        # generate outpath, keep directories from the original path e.g.
        # src/foo/bar.tex become material/foo/bar.pdf
        outpath = outdir
        pathparts = pathlib.PurePath(filepath).parts
        if len(pathparts) > 2:
            middle = pathparts[1:-1]
            for part in middle:
                outpath = os.path.join(outpath, part)

        # create directory for output if not existing
        if not os.path.exists(outpath):
            os.mkdir(outpath)

        # copy from buildfolder to material folder
        shutil.copyfile(
            os.path.join(buildir, pdffilename),
            os.path.join(outpath, pdffilename)
        )
    except:
        print("Error")

# walk folder, get relative paths of al .tex files
def get_filepaths(directory):
    filepaths = []
    for (root,dirs,files) in os.walk('./src', topdown=True):
        for file in files:
            if os.path.splitext(file)[-1] == ".tex":
                filepaths.append(os.path.join(root, file))

    return filepaths

# get files, loop over and build them
if __name__ == "__main__":
    filepaths = get_filepaths("./src")
    fileindex = 0
    for file in filepaths:
        fileindex += 1
        print(f"Converting File {fileindex}/{len(filepaths)}: {os.path.join(file)} ")
        convert_file(file, "./build", "./material")
