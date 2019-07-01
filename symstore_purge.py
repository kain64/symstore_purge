import subprocess
from argparse import ArgumentParser

admin_file_name_suffix = "\\000Admin\\server.txt"


def purge(symstore_folders, days):
    for symstore_folder in symstore_folders:
        print("cleaning storage: " + symstore_folder)
        symstore_folder = symstore_folder
        lines = []
        with open(symstore_folder + admin_file_name_suffix) as fp:
            lines = list(reversed(fp.readlines()))

        if len(lines) <= days:
            print("has less than" + str(days) + "days pdb")
            continue
        lines = lines[days:]

        for line in lines:
            sym_id = line.split(",")[0]
            cmd = ['C:\\Program Files (x86)\\Debugging Tools for Windows\\symstore.exe', 'del', '/i', sym_id, "/s",
                   symstore_folder]
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
            (output, err) = process.communicate()
            p_status = process.wait()
            print(output)
            print("Command exit status/return code : " + str(p_status))


def main():
    parser = ArgumentParser()
    parser.add_argument("-d", "--days", dest="days",
                        help="days for purge")
    parser.add_argument("-f", "--folders",
                        dest="folders",
                        help="symstore folders for purge")

    args = parser.parse_args()
    purge(args.folders.split(','), 7)


if __name__ == "__main__":
    main()
