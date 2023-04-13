import argparse

import utils


parser = argparse.ArgumentParser(description='General info about OS',
                                 epilog='©Amir Hasanov all rights reserved')

# for WebUI
parser.add_argument("-w", "--webui", action='store_true', help="run code with webui (requires Flask)")
parser.add_argument("-p", "--port", type=int, default=8888, help="choose port for webui")

parser.add_argument("-o", "--os_battery_and_time", action='store_true', help="print battery and time")
parser.add_argument("-d", "--ms_defender_status", action='store_true', help="microsoft defender status")
parser.add_argument("-a", "--installed_programs", action='store_true', help="print all installed apps")
parser.add_argument("-s", "--empty_dirs", action='store_true', help="print all empty folder in os")
parser.add_argument("--start", default="C:\\", help="start dir for empty dirs searching")
parser.add_argument("-l", "--languages_list", action='store_true', help="print keyboard layout languages")
parser.add_argument("-i", "--ip_address", action='store_true', help="print OS IP address")
parser.add_argument("-H", "--hostname", action='store_true', help="print OS hostname")
parser.add_argument("-m", "--mac", action='store_true', help="print MAC address")
parser.add_argument("-r", "--rdp", action='store_true', help="check RDP turned on/off")

args = parser.parse_args()


if __name__ == '__main__':
    # getting arguments in python dict format
    d = vars(args)

    if d.get("webui", None):
        # trying to launch server
        try:
            from webui import app
            app.run(host='localhost', port=args.port, debug=False)
        except:
            print("Please install Flask to run webui")
    else:
        # getting only True arguments from utils
        vals = [i for i in d if d[i] is True and i in utils.__all__]

        # setting start dir for empty dirs search
        utils.START_DIR = args.start

        # for non argument code run
        if len(vals) == 0:
            parser.print_help()

        # output per line
        for param in vals:
            result = eval(f"utils.{param}()")
            for line in result:
                print(line)
