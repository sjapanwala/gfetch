import os
import platform
import getpass
import subprocess
import math
import psutil
if os.name == "posix":
    import distro
import re
import time
import datetime
DISTROS_SUPPORTED = ["Ubuntu","Debian","Gentoo","Arch","Fedora","Manjaro","Linux Mint"]
COLORLINE1 ="\033[90m███\033[91m███\033[92m███\033[93m███\033[94m███\033[95m███\033[96m███\033[97m███"
COLORLINE2 ="\033[30m███\033[31m███\033[32m███\033[33m███\033[34m███\033[35m███\033[36m███\033[37m███"
def get_logos(userstring,underline,kernal,osinfo,uptime,shell,terminal,memory,battery):
    logos = {
        'Ubuntu':[
            '\n'
            f'                    \033[38;5;88m██\033[38;5;124m██\033[38;5;88m██              \033[91m\033[0m{userstring}\n'
            f'            \033[38;5;88m██\033[38;5;130m██\033[38;5;130m██\033[38;5;52m██\033[38;5;124m██\033[38;5;124m██\033[38;5;124m██              \033[91m\033[0m{underline}\n'
            f'        \033[38;5;94m██  \033[38;5;166m██\033[38;5;202m██\033[38;5;202m██\033[38;5;166m██\033[38;5;52m██\033[38;5;88m██\033[38;5;52m██              \033[91m   \033[0m{osinfo}\n'
            f'      \033[38;5;94m██\033[38;5;178m██\033[38;5;94m██\033[38;5;52m██\033[38;5;130m██\033[38;5;130m██\033[38;5;166m██\033[38;5;166m██\033[38;5;130m██\033[38;5;130m██              \033[91m   \033[0m{kernal}\n'
            f'      \033[38;5;178m██\033[38;5;214m██\033[38;5;136m██        \033[38;5;94m██\033[38;5;166m██\033[38;5;202m██\033[38;5;88m██            \033[91m   \033[0m{uptime}\n'
            f'  \033[38;5;52m██\033[38;5;52m██\033[38;5;178m██\033[38;5;178m██            \033[38;5;130m██\033[38;5;202m██\033[38;5;166m██            \033[0m{shell}\n'
            f'\033[38;5;166m██\033[38;5;202m██\033[38;5;130m██\033[38;5;136m██\033[38;5;136m██            \033[38;5;52m██\033[38;5;94m██\033[38;5;94m██\033[38;5;88m██          \033[91m   \033[0m{terminal}\n'
            f'\033[38;5;166m██\033[38;5;202m██\033[38;5;130m██\033[38;5;136m██\033[38;5;136m██              \033[38;5;88m██\033[38;5;88m██\033[38;5;52m██          \033[0m{battery}\n'
            f'  \033[38;5;52m██\033[38;5;52m██\033[38;5;178m██\033[38;5;178m██            \033[38;5;88m██\033[38;5;124m██\033[38;5;124m██            \033[91m󰍛   \033[0m{memory}\n'
            f'      \033[38;5;178m██\033[38;5;214m██\033[38;5;136m██        \033[38;5;88m██\033[38;5;124m██\033[38;5;124m██\033[38;5;88m██\n'
            f'      \033[38;5;94m██\033[38;5;178m██\033[38;5;94m██\033[38;5;52m██\033[38;5;88m██\033[38;5;88m██\033[38;5;124m██\033[38;5;124m██\033[38;5;88m██\033[38;5;88m██\n'
            f'        \033[38;5;94m██  \033[38;5;124m██\033[38;5;124m██\033[38;5;124m██\033[38;5;124m██\033[38;5;52m██\033[38;5;136m██\033[38;5;58m██\n'
            f'            \033[38;5;52m██\033[38;5;88m██\033[38;5;88m██\033[38;5;52m██\033[38;5;178m██\033[38;5;214m██\033[38;5;178m██\n'
            f'                    \033[38;5;94m██\033[38;5;178m██\033[38;5;136m██              {COLORLINE1}\n'
            f'                      \033[38;5;94m██                {COLORLINE2}\n'
            ],
        'Debian':[
            '\n'
            '          \033[38;5;52m██\033[38;5;88m██\033[38;5;52m██\033[38;5;52m██\n'
            '      \033[38;5;88m██\033[38;5;161m██\033[38;5;161m██\033[38;5;125m██\033[38;5;89m██\033[38;5;89m██\033[38;5;125m██\033[38;5;125m██\033[38;5;88m██\n'
            ''
            '    \033[38;5;125m██\033[38;5;125m██\033[38;5;52m██          \033[38;5;52m██\033[38;5;161m██\033[38;5;125m██\n'
            '  \033[38;5;88m██\033[38;5;125m██                \033[38;5;52m██\033[38;5;125m██\033[38;5;52m██\n'
            '\033[38;5;52m██\033[38;5;125m██        \033[38;5;52m██\033[38;5;52m██\033[38;5;52m██      \033[38;5;161m██\n'
            '\033[38;5;88m██\033[38;5;88m██      \033[38;5;52m██            \033[38;5;125m██\033[38;5;52m██\n'
            '\033[38;5;88m██\033[38;5;52m██      \033[38;5;88m██            \033[38;5;125m██\n'
            '\033[38;5;88m██\033[38;5;52m██      \033[38;5;52m██\033[38;5;52m██        \033[38;5;88m██\033[38;5;52m██\n'
            '\033[38;5;52m██\033[38;5;88m██        \033[38;5;52m██\033[38;5;88m██\033[38;5;52m██\033[38;5;52m██\033[38;5;88m██\n'
            '  \033[38;5;125m██\033[38;5;52m██\n'
            '  \033[38;5;52m██\033[38;5;125m██\n'
            '    \033[38;5;88m██\033[38;5;88m██\n'
            '      \033[38;5;52m██\033[38;5;89m██\n'
            '          \033[38;5;52m██\033[38;5;52m██\n'
            ],
        'Gentoo':[
            '\n'
            '      \033[38;5;60m██\033[38;5;145m██\033[38;5;188m██\033[38;5;146m██\033[38;5;103m██\033[38;5;17m██\n'
            '    \033[38;5;146m██\033[38;5;188m██\033[38;5;231m██\033[38;5;231m██\033[38;5;188m██\033[38;5;188m██\033[38;5;146m██\033[38;5;103m██\n'
            '  \033[38;5;146m██\033[38;5;231m██\033[38;5;231m██\033[38;5;231m██\033[38;5;231m██\033[38;5;188m██\033[38;5;188m██\033[38;5;188m██\033[38;5;146m██\033[38;5;146m██\033[38;5;17m██\n'
            '\033[38;5;60m██\033[38;5;188m██\033[38;5;231m██\033[38;5;231m██\033[38;5;231m██\033[38;5;188m██\033[38;5;146m██\033[38;5;140m██\033[38;5;145m██\033[38;5;146m██\033[38;5;146m██\033[38;5;146m██\033[38;5;59m██\n'
            '\033[38;5;103m██\033[38;5;188m██\033[38;5;188m██\033[38;5;231m██\033[38;5;231m██\033[38;5;188m██\033[38;5;103m██\033[38;5;103m██\033[38;5;103m██\033[38;5;146m██\033[38;5;146m██\033[38;5;146m██\033[38;5;146m██\033[38;5;59m██\n'
            '\033[38;5;17m██\033[38;5;140m██\033[38;5;188m██\033[38;5;188m██\033[38;5;188m██\033[38;5;231m██\033[38;5;188m██\033[38;5;188m██\033[38;5;188m██\033[38;5;146m██\033[38;5;146m██\033[38;5;146m██\033[38;5;146m██\033[38;5;188m██\n'
            '    \033[38;5;103m██\033[38;5;146m██\033[38;5;188m██\033[38;5;188m██\033[38;5;188m██\033[38;5;188m██\033[38;5;188m██\033[38;5;146m██\033[38;5;146m██\033[38;5;146m██\033[38;5;146m██\033[38;5;188m██\033[38;5;103m██\n'
            '      \033[38;5;188m██\033[38;5;188m██\033[38;5;188m██\033[38;5;188m██\033[38;5;188m██\033[38;5;146m██\033[38;5;146m██\033[38;5;146m██\033[38;5;146m██\033[38;5;188m██\033[38;5;102m██\n'
            '  \033[38;5;59m██\033[38;5;188m██\033[38;5;231m██\033[38;5;188m██\033[38;5;188m██\033[38;5;188m██\033[38;5;188m██\033[38;5;146m██\033[38;5;146m██\033[38;5;188m██\033[38;5;188m██\033[38;5;103m██\n'
            '  \033[38;5;188m██\033[38;5;231m██\033[38;5;188m██\033[38;5;188m██\033[38;5;188m██\033[38;5;188m██\033[38;5;146m██\033[38;5;146m██\033[38;5;188m██\033[38;5;146m██\033[38;5;96m██\n'
            '\033[38;5;145m██\033[38;5;188m██\033[38;5;188m██\033[38;5;188m██\033[38;5;188m██\033[38;5;188m██\033[38;5;188m██\033[38;5;188m██\033[38;5;188m██\033[38;5;139m██\033[38;5;59m██\n'
            '\033[38;5;188m██\033[38;5;188m██\033[38;5;188m██\033[38;5;188m██\033[38;5;188m██\033[38;5;188m██\033[38;5;188m██\033[38;5;145m██\033[38;5;96m██\n'
            ''
            '\033[38;5;102m██\033[38;5;188m██\033[38;5;188m██\033[38;5;188m██\033[38;5;182m██\033[38;5;145m██\033[38;5;96m██\033[38;5;53m██\n'
            '  \033[38;5;60m██\033[38;5;60m██\033[38;5;60m██\033[38;5;60m██\033[38;5;17m██\n'
            '    \033[38;5;59m██\033[38;5;17m██\n'
        ],
        'Arch':[
            '\n'
            '              \033[38;5;17m██\n'
            '            \033[38;5;24m██\033[38;5;24m██\n'
            '            \033[38;5;31m██\033[38;5;32m██\n'
            '          \033[38;5;23m██\033[38;5;32m██\033[38;5;32m██\033[38;5;24m██\n'
            '          \033[38;5;24m██\033[38;5;31m██\033[38;5;32m██\033[38;5;31m██\n'
            '        \033[38;5;23m██\033[38;5;32m██\033[38;5;31m██\033[38;5;32m██\033[38;5;32m██\033[38;5;24m██\n'
            '        \033[38;5;31m██\033[38;5;32m██\033[38;5;32m██\033[38;5;32m██\033[38;5;32m██\033[38;5;31m██\n'
            '      \033[38;5;23m██\033[38;5;32m██\033[38;5;32m██\033[38;5;32m██\033[38;5;32m██\033[38;5;32m██\033[38;5;32m██\033[38;5;24m██\n'
            '      \033[38;5;31m██\033[38;5;32m██\033[38;5;32m██\033[38;5;23m██\033[38;5;23m██\033[38;5;32m██\033[38;5;32m██\033[38;5;31m██\n'
            '    \033[38;5;24m██\033[38;5;32m██\033[38;5;32m██\033[38;5;30m██    \033[38;5;24m██\033[38;5;32m██\033[38;5;32m██\033[38;5;24m██\n'
            '    \033[38;5;31m██\033[38;5;32m██\033[38;5;32m██\033[38;5;24m██    \033[38;5;23m██\033[38;5;32m██\033[38;5;31m██\033[38;5;31m██\n'
            '  \033[38;5;24m██\033[38;5;32m██\033[38;5;32m██\033[38;5;31m██\033[38;5;23m██    \033[38;5;17m██\033[38;5;31m██\033[38;5;32m██\033[38;5;32m██\033[38;5;23m██\n'
            '  \033[38;5;32m██\033[38;5;31m██\033[38;5;17m██            \033[38;5;17m██\033[38;5;30m██\033[38;5;32m██\n'
            '\033[38;5;24m██\033[38;5;17m██                      \033[38;5;24m██\n'
            ],
        'Fedora':[
            '\n'
            '        \033[38;5;17m██\033[38;5;23m██\033[38;5;24m██\033[38;5;24m██\033[38;5;23m██\033[38;5;17m██\n'
            '      \033[38;5;24m██\033[38;5;24m██\033[38;5;24m██\033[38;5;24m██\033[38;5;24m██\033[38;5;66m██\033[38;5;67m██\033[38;5;24m██\n'
            '    \033[38;5;24m██\033[38;5;24m██\033[38;5;24m██\033[38;5;24m██\033[38;5;60m██\033[38;5;188m██\033[38;5;231m██\033[38;5;231m██\033[38;5;110m██\033[38;5;24m██\n'
            '  \033[38;5;24m██\033[38;5;24m██\033[38;5;24m██\033[38;5;24m██\033[38;5;24m██\033[38;5;188m██\033[38;5;188m██\033[38;5;103m██\033[38;5;67m██\033[38;5;67m██\033[38;5;67m██\033[38;5;24m██\n'
            '\033[38;5;17m██\033[38;5;24m██\033[38;5;24m██\033[38;5;24m██\033[38;5;24m██\033[38;5;60m██\033[38;5;231m██\033[38;5;103m██\033[38;5;24m██\033[38;5;24m██\033[38;5;24m██\033[38;5;67m██\033[38;5;24m██\033[38;5;17m██\n'
            '\033[38;5;23m██\033[38;5;24m██\033[38;5;24m██\033[38;5;24m██\033[38;5;24m██\033[38;5;60m██\033[38;5;231m██\033[38;5;103m██\033[38;5;24m██\033[38;5;24m██\033[38;5;24m██\033[38;5;67m██\033[38;5;24m██\033[38;5;23m██\n'
            '\033[38;5;24m██\033[38;5;24m██\033[38;5;24m██\033[38;5;24m██\033[38;5;67m██\033[38;5;103m██\033[38;5;231m██\033[38;5;145m██\033[38;5;67m██\033[38;5;60m██\033[38;5;67m██\033[38;5;67m██\033[38;5;24m██\033[38;5;24m██\n'
            '\033[38;5;24m██\033[38;5;24m██\033[38;5;67m██\033[38;5;109m██\033[38;5;231m██\033[38;5;231m██\033[38;5;231m██\033[38;5;231m██\033[38;5;231m██\033[38;5;110m██\033[38;5;67m██\033[38;5;24m██\033[38;5;24m██\033[38;5;24m██\033[38;5;17m██\n'
            '\033[38;5;24m██\033[38;5;67m██\033[38;5;67m██\033[38;5;24m██\033[38;5;66m██\033[38;5;103m██\033[38;5;231m██\033[38;5;109m██\033[38;5;66m██\033[38;5;24m██\033[38;5;24m██\033[38;5;24m██\033[38;5;24m██\033[38;5;24m██\n'
            '\033[38;5;24m██\033[38;5;67m██\033[38;5;24m██\033[38;5;24m██\033[38;5;24m██\033[38;5;60m██\033[38;5;231m██\033[38;5;103m██\033[38;5;24m██\033[38;5;24m██\033[38;5;24m██\033[38;5;24m██\033[38;5;24m██\033[38;5;17m██\n'
            '\033[38;5;24m██\033[38;5;67m██\033[38;5;24m██\033[38;5;24m██\033[38;5;24m██\033[38;5;103m██\033[38;5;231m██\033[38;5;103m██\033[38;5;24m██\033[38;5;24m██\033[38;5;24m██\033[38;5;24m██\033[38;5;24m██\n'
            '\033[38;5;24m██\033[38;5;67m██\033[38;5;67m██\033[38;5;67m██\033[38;5;103m██\033[38;5;188m██\033[38;5;188m██\033[38;5;24m██\033[38;5;24m██\033[38;5;24m██\033[38;5;24m██\033[38;5;24m██\n'
            '\033[38;5;24m██\033[38;5;24m██\033[38;5;103m██\033[38;5;231m██\033[38;5;231m██\033[38;5;188m██\033[38;5;66m██\033[38;5;24m██\033[38;5;24m██\033[38;5;24m██\033[38;5;24m██\n'
            '\033[38;5;17m██\033[38;5;24m██\033[38;5;24m██\033[38;5;66m██\033[38;5;66m██\033[38;5;24m██\033[38;5;24m██\033[38;5;24m██\033[38;5;24m██\033[38;5;17m██\n'
            '\033[38;5;17m██\033[38;5;17m██\033[38;5;17m██\033[38;5;17m██\033[38;5;17m██\033[38;5;17m██\033[38;5;17m██\n'
        ],
        'Manjaro':[
            '\n'
            '\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;16m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\n'
            '\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;16m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\n'
            '\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;16m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\n'
            '\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;16m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\n'
            '\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;16m██\033[38;5;16m██\033[38;5;16m██\033[38;5;16m██\033[38;5;16m██\033[38;5;16m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\n'
            '\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;16m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;16m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\n'
            '\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;16m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;16m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\n'
            '\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;16m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;16m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\n'
            '\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;16m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;16m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\n'
            '\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;16m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;16m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\n'
            '\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;16m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;16m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\n'
            '\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;16m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;16m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\n'
            '\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;16m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;16m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\n'
            '\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;16m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;16m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\n'
            '\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;16m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;16m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\033[38;5;35m██\n'
        ],
        'Mint':[
            '\n'
            '        \033[38;5;102m██\033[38;5;188m██\033[38;5;188m██\033[38;5;188m██\033[38;5;188m██\033[38;5;102m██\n'
            '    \033[38;5;59m██\033[38;5;188m██\033[38;5;187m██\033[38;5;114m██\033[38;5;107m██\033[38;5;107m██\033[38;5;108m██\033[38;5;151m██\033[38;5;188m██\033[38;5;59m██\n'
            '  \033[38;5;59m██\033[38;5;188m██\033[38;5;108m██\033[38;5;107m██\033[38;5;107m██\033[38;5;107m██\033[38;5;107m██\033[38;5;107m██\033[38;5;107m██\033[38;5;108m██\033[38;5;188m██\033[38;5;102m██\n'
            '  \033[38;5;188m██\033[38;5;108m██\033[38;5;150m██\033[38;5;107m██\033[38;5;107m██\033[38;5;107m██\033[38;5;107m██\033[38;5;107m██\033[38;5;107m██\033[38;5;107m██\033[38;5;108m██\033[38;5;188m██\n'
            '\033[38;5;102m██\033[38;5;187m██\033[38;5;107m██\033[38;5;188m██\033[38;5;108m██\033[38;5;107m██\033[38;5;188m██\033[38;5;188m██\033[38;5;188m██\033[38;5;188m██\033[38;5;150m██\033[38;5;107m██\033[38;5;151m██\033[38;5;102m██\n'
            '\033[38;5;188m██\033[38;5;114m██\033[38;5;107m██\033[38;5;188m██\033[38;5;108m██\033[38;5;151m██\033[38;5;151m██\033[38;5;151m██\033[38;5;188m██\033[38;5;150m██\033[38;5;188m██\033[38;5;107m██\033[38;5;108m██\033[38;5;188m██\n'
            '\033[38;5;188m██\033[38;5;107m██\033[38;5;107m██\033[38;5;188m██\033[38;5;108m██\033[38;5;151m██\033[38;5;150m██\033[38;5;150m██\033[38;5;151m██\033[38;5;107m██\033[38;5;188m██\033[38;5;107m██\033[38;5;107m██\033[38;5;231m██\033[38;5;145m██\n'
            '\033[38;5;188m██\033[38;5;107m██\033[38;5;107m██\033[38;5;188m██\033[38;5;108m██\033[38;5;151m██\033[38;5;150m██\033[38;5;150m██\033[38;5;151m██\033[38;5;107m██\033[38;5;188m██\033[38;5;107m██\033[38;5;107m██\033[38;5;231m██\033[38;5;145m██\n'
            '\033[38;5;188m██\033[38;5;108m██\033[38;5;107m██\033[38;5;188m██\033[38;5;108m██\033[38;5;108m██\033[38;5;107m██\033[38;5;107m██\033[38;5;108m██\033[38;5;108m██\033[38;5;188m██\033[38;5;107m██\033[38;5;108m██\033[38;5;188m██\n'
            '\033[38;5;102m██\033[38;5;151m██\033[38;5;107m██\033[38;5;150m██\033[38;5;188m██\033[38;5;151m██\033[38;5;151m██\033[38;5;151m██\033[38;5;151m██\033[38;5;188m██\033[38;5;151m██\033[38;5;107m██\033[38;5;151m██\033[38;5;145m██\n'
            '\033[38;5;188m██\033[38;5;108m██\033[38;5;107m██\033[38;5;150m██\033[38;5;151m██\033[38;5;151m██\033[38;5;151m██\033[38;5;151m██\033[38;5;150m██\033[38;5;107m██\033[38;5;107m██\033[38;5;188m██\n'
            '\033[38;5;59m██\033[38;5;188m██\033[38;5;108m██\033[38;5;107m██\033[38;5;107m██\033[38;5;107m██\033[38;5;107m██\033[38;5;107m██\033[38;5;107m██\033[38;5;107m██\033[38;5;188m██\033[38;5;102m██\n'
            '  \033[38;5;102m██\033[38;5;188m██\033[38;5;151m██\033[38;5;108m██\033[38;5;107m██\033[38;5;107m██\033[38;5;108m██\033[38;5;151m██\033[38;5;188m██\033[38;5;102m██\n'
            '      \033[38;5;102m██\033[38;5;188m██\033[38;5;231m██\033[38;5;231m██\033[38;5;188m██\033[38;5;145m██\n'
            '          \033[38;5;145m██\033[38;5;145m██\n'
        ],
        'Windows':[
            '\n'
            f'      \033[38;5;130m██\033[38;5;166m██\033[38;5;166m██\033[38;5;130m██\033[38;5;52m██                          \033[91m\033[0m{userstring}\n'
            f'    \033[38;5;52m██\033[38;5;172m██\033[38;5;172m██\033[38;5;172m██\033[38;5;172m██\033[38;5;130m██                          \033[91m\033[0m{underline}\n'
            f'    \033[38;5;130m██\033[38;5;172m██\033[38;5;172m██\033[38;5;172m██\033[38;5;172m██\033[38;5;94m██\033[38;5;64m██\033[38;5;106m██\033[38;5;106m██\033[38;5;100m██\033[38;5;106m██\033[38;5;64m██              \033[91m   \033[0m{osinfo}\n'
            f'    \033[38;5;166m██\033[38;5;172m██\033[38;5;172m██\033[38;5;172m██\033[38;5;172m██\033[38;5;52m██\033[38;5;106m██\033[38;5;106m██\033[38;5;106m██\033[38;5;106m██\033[38;5;106m██\033[38;5;22m█               \033[91m   \033[0m{kernal}\n'
            f'  \033[38;5;52m██\033[38;5;166m██\033[38;5;130m██\033[38;5;94m██\033[38;5;166m██\033[38;5;166m██  \033[38;5;106m██\033[38;5;106m██\033[38;5;106m██\033[38;5;106m██\033[38;5;106m██                \033[91m   \033[0m{uptime}\n'
            f'    \033[38;5;23m██\033[38;5;30m██\033[38;5;24m██\033[38;5;17m██\033[38;5;52m██\033[38;5;64m██\033[38;5;106m██\033[38;5;106m██\033[38;5;106m██\033[38;5;106m██\033[38;5;64m██                \033[0m{shell}\n'
            f'  \033[38;5;31m██\033[38;5;38m██\033[38;5;38m██\033[38;5;38m██\033[38;5;38m██\033[38;5;23m██  \033[38;5;64m██\033[38;5;106m██\033[38;5;106m██\033[38;5;64m██                  \033[91m   \033[0m{terminal}\n'
            f'  \033[38;5;38m██\033[38;5;38m██\033[38;5;38m██\033[38;5;38m██\033[38;5;38m██  \033[38;5;178m██\033[38;5;100m██\033[38;5;94m██\033[38;5;94m██\033[38;5;136m██                  \033[0m{battery}\n'
            f'\033[38;5;23m██\033[38;5;38m██\033[38;5;38m██\033[38;5;38m██\033[38;5;38m██\033[38;5;31m██\033[38;5;58m██\033[38;5;214m██\033[38;5;214m██\033[38;5;214m██\033[38;5;214m██\033[38;5;178m██                  \033[91m󰍛   \033[0m{memory}\n'
            '\033[38;5;31m██\033[38;5;38m██\033[38;5;38m██\033[38;5;38m██\033[38;5;38m██\033[38;5;24m██\033[38;5;136m██\033[38;5;214m██\033[38;5;214m██\033[38;5;214m██\033[38;5;214m██\033[38;5;100m██\n'
            f'            \033[38;5;178m██\033[38;5;214m██\033[38;5;214m██\033[38;5;214m██\033[38;5;214m██\033[38;5;52m██                  {COLORLINE1}\n'
            f'            \033[38;5;136m██\033[38;5;178m██\033[38;5;214m██\033[38;5;178m██\033[38;5;136m██                    {COLORLINE2}\n'
        ],
        'Default':[
            '\n'
            '          \033[38;5;17m██\033[38;5;17m██\n'
            '      \033[38;5;23m██\033[38;5;109m██\033[38;5;67m██\033[38;5;67m██\033[38;5;67m██\033[38;5;23m██\n'
            '      \033[38;5;23m██\033[38;5;67m██\033[38;5;67m██\033[38;5;67m██\033[38;5;67m██\033[38;5;24m██\n'
            '  \033[38;5;17m██\033[38;5;23m██\033[38;5;24m██\033[38;5;24m██\033[38;5;24m██\033[38;5;67m██\033[38;5;67m██\033[38;5;24m██\033[38;5;100m██\033[38;5;58m██\n'
            '  \033[38;5;67m██\033[38;5;67m██\033[38;5;67m██\033[38;5;67m██\033[38;5;67m██\033[38;5;67m██\033[38;5;67m██\033[38;5;23m██\033[38;5;221m██\033[38;5;185m██\033[38;5;52m██\n'
            '\033[38;5;17m██\033[38;5;67m██\033[38;5;67m██\033[38;5;67m██\033[38;5;24m██\033[38;5;24m██\033[38;5;24m██\033[38;5;24m██\033[38;5;58m██\033[38;5;221m██\033[38;5;221m██\033[38;5;94m██\n'
            '\033[38;5;17m██\033[38;5;67m██\033[38;5;67m██\033[38;5;59m██\033[38;5;136m██\033[38;5;143m██\033[38;5;143m██\033[38;5;143m██\033[38;5;179m██\033[38;5;221m██\033[38;5;221m██\033[38;5;94m██\n'
            ' \033[38;5;67m██\033[38;5;67m██\033[38;5;100m██\033[38;5;221m██\033[38;5;221m██\033[38;5;221m██\033[38;5;221m██\033[38;5;221m██\033[38;5;221m██\033[38;5;221m██\033[38;5;58m██\n'
            ' \033[38;5;17m██\033[38;5;24m██\033[38;5;100m██\033[38;5;221m██\033[38;5;221m██\033[38;5;136m██\033[38;5;136m██\033[38;5;136m██\033[38;5;136m██\033[38;5;94m██\n'
            '     \033[38;5;100m██\033[38;5;221m██\033[38;5;221m██\033[38;5;185m██\033[38;5;186m██\033[38;5;136m██\n'
            '     \033[38;5;94m██\033[38;5;221m██\033[38;5;221m██\033[38;5;221m██\033[38;5;222m██\033[38;5;100m██\n'
            '       \033[38;5;58m██\033[38;5;94m██\033[38;5;94m██\033[38;5;58m██\n'
        ]
    }
    if os.name == "nt":
        return logos['Windows']
    elif os.name != "posix":
        print("Sorry, This System Is Not Supported!")
        exit
    else:
        if distro.name() in DISTROS_SUPPORTED:
            return logos[distro.name()]
        else:
            return logos['Default']
def bytes_to_mib(bytes):
    return bytes / (1024 ** 2)  # Convert bytes to MiB
    
def user_info():
     userstring = f"{getpass.getuser()}\033[91m@\033[0m{platform.node()}"
     underline = len(userstring) * "-"
     return userstring,underline

def get_osinfo():
    if os.name == "nt":
        return "Windows (NT)"
    elif os.name == "dariwn":
        return MacOS
    else:
        return f"{distro.name()} {distro.version()}"
    
def secs_to_other(seconds):
    if seconds >= 3600:
        return f"{seconds / 3600:.2f} hours"
    elif seconds >= 60:
        return f"{seconds / 60:.2f} minutes"
    else:
        return f"{seconds:.2f} seconds"

def get_uptime_from_proc():
    try:
        with open('/proc/uptime', 'r') as file:
            uptime_seconds = float(file.read().split()[0])
            return secs_to_other(uptime_seconds)
    except Exception as e:
        return f"Failed to retrieve uptime: {e}"

def get_windows_uptime():

    # Get the system uptime in seconds
    uptime_seconds = time.time() - psutil.boot_time()

    # Convert to a more readable format (hours, minutes, seconds)
    uptime_str = time.strftime("%H:%M:%S", time.gmtime(uptime_seconds))

    return uptime_str

def get_default_shell():
    os_type = platform.system()

    if os_type == "Linux" or os_type == "Darwin":  # Darwin is macOS
        # For Unix-like systems
        shell = os.getenv('SHELL', '/bin/sh')  # Default to /bin/sh if SHELL is not set
        shell = f"\033[91m   \033[0m{shell}"
    elif os_type == "Windows":
        # For Windows, default to cmd.exe
        shell = "\033[91m   \033[0mCMD"
    else:
        shell = "Unknown shell"

    return shell

def get_terminal_info():
    os_type = platform.system()

    if os_type in ["Linux", "Darwin"]:  # Darwin is macOS
        shell = os.getenv('SHELL', 'Unknown')
        term_program = os.getenv('TERM_PROGRAM', 'Unknown')
        return term_program
    
    elif os_type == "Windows":
        comspec = os.getenv('ComSpec', 'Unknown')
        return f"{comspec}"
    
    else:
        return "Unknown operating system"
    
def batteryinfo():
    battery = int(psutil.sensors_battery().percent)
    if psutil.sensors_battery().power_plugged:
        return f'\033[92m   \033[0m{battery}%'
    elif battery > 90:
        return f'\033[91m   \033[0m{battery}%'
    elif battery > 70:
        return f'\033[91m   \033[0m{battery}%'
    elif battery > 45:
        return f'\033[91m   \033[0m{battery}%'
    elif battery > 20:
        return f'\033[91m   \033[0m{battery}%'
    else:
        return f'\033[91m   \033[0m{battery}%'

osinfo = get_osinfo()   
shell = get_default_shell() 
userstring,underline = user_info()
terminal = get_terminal_info()
if os.name == "nt":
    uptime = get_windows_uptime()
else:
    uptime = get_uptime_from_proc()
mem_info = psutil.virtual_memory()
memory = f"{int(bytes_to_mib(mem_info.used))}MiB \ {int(bytes_to_mib(mem_info.total))}MiB"
battery = batteryinfo()
kernal = platform.release()



logos = get_logos(userstring,underline,kernal,osinfo,uptime,shell,terminal,memory,battery)
for logo in logos:
        print(f"\033[0m", logo)
