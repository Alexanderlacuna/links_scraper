import subprocess


def run_subprocess(command):

    subprocess.Popen([command], shell=True)


run_subprocess("python3  genelinks.py")
