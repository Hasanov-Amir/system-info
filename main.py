import utils
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='General info about OS',
                                     epilog='©Amir Hasanov all rights reserved')

    parser.add_argument("-a", "--installed_programs", action='store_true', help="print all installed apps")
    parser.add_argument("-i", "--ip_address", action='store_true', help="print OS IP address")
    parser.add_argument("-r", "--rdp", action='store_true', help="check RDP turned on/off")
    parser.add_argument("-o", "--os_battery_and_time", action='store_true', help="print battery and time")
    parser.add_argument("-d", "--ms_defender_status", action='store_true', help="microsoft defender status")
    parser.add_argument("-s", "--search_empty_dirs", action='store_true', help="print all empty folder in os")
    parser.add_argument("-l", "--languages_list", action='store_true', help="print keyboard layout languages")
    parser.add_argument("-m", "--mac", action='store_true', help="print MAC address")
    parser.add_argument("-H", "--hostname", action='store_true', help="print OS hostname")
    args = parser.parse_args()

    d = vars(args)
    vals = [i for i in d if d[i] is True]

    if len(vals) == 0:
        parser.print_help()

    for param in vals:
        result = eval(f"utils.{param}()")
        if isinstance(result, str):
            print(result)
        else:
            for i in result:
                print(i)
