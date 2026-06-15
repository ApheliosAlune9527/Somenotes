import sys, os, subprocess, shutil

bat_args = sys.argv[1:]
src_file = None

for arg in bat_args:
    if arg.endswith('.c'):
        src_file = arg
        break

if not src_file:
    sys.stderr.write("Error: no .c file found in args\n")
    sys.exit(1)

if not os.path.exists(src_file):
    sys.stderr.write(f"Error: source file not found: {src_file}\n")
    sys.exit(1)

temp_dir = r"C:\temp_src"
os.makedirs(temp_dir, exist_ok=True)
dest = os.path.join(temp_dir, "temp.c")
exe_path = os.path.join(temp_dir, "temp.exe")
shutil.copy(src_file, dest)

try:
    compile_result = subprocess.run(
        ["gcc", "-finput-charset=UTF-8", "-fexec-charset=GBK", dest, "-o", exe_path],
        capture_output=True, text=True
    )
    if compile_result.returncode != 0:
        sys.stderr.write(compile_result.stderr)
        sys.exit(compile_result.returncode)

    proc = subprocess.Popen(
        [exe_path],
        stdin=None,
        stdout=None,
        stderr=None
    )
    proc.wait()
    sys.exit(proc.returncode)

finally:
    for f in [dest, exe_path]:
        if os.path.exists(f):
            try:
                os.remove(f)
            except:
                pass
