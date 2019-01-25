import argparse, re, subprocess

sys_rpms = {}
present_packages = []
absent_packages = []


def main():
    parser = argparse.ArgumentParser(description="Checks versions of mentioned packages on locally machine!")
    parser.add_argument("--input", default="input.txt", help="input file (contains package names)")
    parser.add_argument("--output", help="output file (contains compared packages)")
    args = parser.parse_args()

    command_output = subprocess.check_output(["rpm", "-a", "-q"])
    rpm_list = command_output.strip().split()

    for rpm in rpm_list:
        name = re.split(r"\-\d.*", rpm)[0]
        version = rpm.split(name)[1]
        sys_rpms[name] = version

    with open(args.input, "r") as file_rpms:
        for package in file_rpms:
            _package = package.strip()
            _name = re.split(r"\-\d.*", _package)[0]
            if _name in sys_rpms:
                sys_package = "{package_name}{package_version}".format(package_name=_name,
                                                            package_version=sys_rpms[_name])
                present_packages.append(sys_package)
            else:
                absent_packages.append(_name)

    present_msg = "* Following packages matched in your system - \n"
    absent_msg = "\n* Kindly check following unmatched packages - \n"

    print present_msg
    for pkg in present_packages:
        print pkg
    if absent_packages:
        print "{0}{1}".format("\n", absent_msg)
        for pkg in absent_packages:
            print pkg

    if args.output:
        with open(args.output, "w") as output:
            output.write("{0}{1}".format(present_msg, "\n"))
            for pkg in present_packages:
                output.write("{0}{1}".format(pkg, "\n"))
            if absent_packages:
                output.write("{0}{1}".format(absent_msg, "\n"))
                for pkg in absent_packages:
                    if args.output:
                        output.write("{0}{1}".format(pkg, "\n"))


if __name__ == "__main__":
    main()
