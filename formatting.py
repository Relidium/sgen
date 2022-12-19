#██████╗ ██╗   ██╗    ██████╗ ███████╗██╗     ██╗██████╗ ██╗██╗   ██╗███╗   ███╗
#██╔══██╗╚██╗ ██╔╝    ██╔══██╗██╔════╝██║     ██║██╔══██╗██║██║   ██║████╗ ████║
#██████╔╝ ╚████╔╝     ██████╔╝█████╗  ██║     ██║██║  ██║██║██║   ██║██╔████╔██║
#██╔══██╗  ╚██╔╝      ██╔══██╗██╔══╝  ██║     ██║██║  ██║██║██║   ██║██║╚██╔╝██║
#██████╔╝   ██║       ██║  ██║███████╗███████╗██║██████╔╝██║╚██████╔╝██║ ╚═╝ ██║
#╚═════╝    ╚═╝       ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝╚═════╝ ╚═╝ ╚═════╝ ╚═╝     ╚═╝
#                                 @curd#9782
from string import digits, ascii_lowercase as letters, punctuation as symbols
from random import SystemRandom as srnd, uniform as decimal

def formatCharacter(translateString: str, mode: str):
    match mode:
        case "upper":
            return translateString.upper()
        case "lower":
            return translateString.lower()
        case "none" | "mixedcase":
            #50%/50% for upper/lower
            if decimal(0, 1) < .5:
                return translateString.upper()
            else:
                return translateString.lower()
        case _:
            return translateString

def formatRandom(translateString: str, extrasetting:str="none"):
    translateString = list(translateString)
    for shift in range(len(translateString)):
        match translateString[shift]:
            case "X":
                translateString[shift] = formatCharacter(''.join(srnd().choice(
                    letters + digits) for _ in range(1)), extrasetting)
            case "R":
                translateString[shift] = formatCharacter(''.join(srnd().choice(
                    letters + symbols) for _ in range(1)), extrasetting)
            case "L":
                translateString[shift] = formatCharacter(''.join(srnd().choice(
                    digits + symbols) for _ in range(1)), extrasetting)
            case "T":
                translateString[shift] = formatCharacter(''.join(srnd().choice(
                    letters + symbols + digits) for _ in range(1)), extrasetting)
            case "E":
                translateString[shift] = formatCharacter(''.join(srnd().choice(
                    digits) for _ in range(1)), extrasetting)
            case "B":
                translateString[shift] = formatCharacter(''.join(srnd().choice(
                    letters) for _ in range(1)), extrasetting)
            case "N":
                translateString[shift] = formatCharacter(''.join(srnd().choice(
                    symbols) for _ in range(1)), extrasetting)
    return ''.join(translateString)
