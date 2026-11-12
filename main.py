# ═══════════════════════════════════════════════════════════════
# main.py — UNFAIR  |  TCP BOT
# UNFAIR TCP — All rights reserved
# ═══════════════════════════════════════════════════════════════

import asyncio
import time
import sys
import os
from pathlib import Path
from cfonts import render

# Verify the distributed source files before importing bot_core.
from integrity_guard import verify_integrity
verify_integrity(Path(__file__).resolve().parent)

import login_engine
import bot_core

from bot_core import (
    TcPOnLine, TcPChaT,
    build_ob55_online_auth, create_auth_token_chat,
    bot_uid, ToKen, region
)
import random


# ═══════════════════════════════════════════════════════════════
# ⚠️ अपनी असली GUEST ID यहाँ डालें
# ═══════════════════════════════════════════════════════════════

BOT_UID      = "8438400627"
BOT_PASSWORD = "5851F76B6D85DB2B234C2C753D911D84BBD8DA8BA408B8BEC41E730BAB04E2BE"
REGION_PREF  = "IND"


def log(level, message):
    icons = {
        "INFO":  ("\033[1;36m", "ℹ"),
        "OK":    ("\033[1;32m", "✔"),
        "WAIT":  ("\033[1;33m", "⏳"),
        "WARN":  ("\033[1;33m", "⚠"),
        "ERROR": ("\033[1;31m", "✘"),
        "BOT":   ("\033[1;35m", "★"),
    }
    color, icon = icons.get(level, ("\033[1;37m", "•"))
    reset = "\033[0m"
    ts = time.strftime("%H:%M:%S")
    print(f"\033[1;90m[{ts}]{reset} {color}{icon} {level:<5}{reset} │ {message}")


def print_banner():
    os.system("clear")

    RED = "\033[1;31m"
    WHITE = "\033[1;37m"
    YELLOW = "\033[1;33m"
    CYAN = "\033[1;36m"
    PURPLE = "\033[1;35m"
    GREEN = "\033[1;32m"
    RESET = "\033[0m"

    print()
    print(f"{RED}╔{'═' * 66}╗{RESET}")
    print(f"{RED}║{WHITE}{'██╗   ██╗███╗   ██╗███████╗ █████╗ ██╗██████╗'.center(66)}{RED}║{RESET}")
    print(f"{RED}║{WHITE}{'██║   ██║████╗  ██║██╔════╝██╔══██╗██║██╔══██╗'.center(66)}{RED}║{RESET}")
    print(f"{RED}║{WHITE}{'██║   ██║██╔██╗ ██║█████╗  ███████║██║██████╔╝'.center(66)}{RED}║{RESET}")
    print(f"{RED}║{WHITE}{'██║   ██║██║╚██╗██║██╔══╝  ██╔══██║██║██╔══██╗'.center(66)}{RED}║{RESET}")
    print(f"{RED}║{WHITE}{'╚██████╔╝██║ ╚████║███████╗██║  ██║██║██║  ██║'.center(66)}{RED}║{RESET}")
    print(f"{RED}║{WHITE}{' ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝'.center(66)}{RED}║{RESET}")
    print(f"{RED}║{YELLOW}{'T C P   P R E M I U M   B O T'.center(66)}{RED}║{RESET}")
    print(f"{RED}╠{'═' * 66}╣{RESET}")
    print(f"{RED}║{CYAN}{'⚡ EVO  •  TEAM  •  MATCH  •  ONLINE ⚡'.center(66)}{RED}║{RESET}")
    print(f"{RED}╠{'═' * 66}╣{RESET}")
    print(f"{RED}║{GREEN}{'● SYSTEM STATUS : READY'.center(66)}{RED}║{RESET}")
    print(f"{RED}║{WHITE}{'● VERSION       : UNFAIR TCP V1.0'.center(66)}{RED}║{RESET}")
    print(f"{RED}║{WHITE}{'● OWNER         : SAHIL BHAI'.center(66)}{RED}║{RESET}")
    print(f"{RED}╠{'═' * 66}╣{RESET}")
    print(f"{RED}║{YELLOW}{'© UNFAIR TCP PREMIUM'.center(66)}{RED}║{RESET}")
    print(f"{RED}╚{'═' * 66}╝{RESET}")
    print()


def print_box(title, lines, color="\033[1;35m"):
    width = 58
    reset = "\033[0m"
    print(f"\n{color}┌{'─' * width}┐{reset}")
    print(f"{color}│{reset} {title.center(width - 1)}{color}│{reset}")
    print(f"{color}├{'─' * width}┤{reset}")
    for line in lines:
        print(f"{color}│{reset} {line:<{width - 1}}{color}│{reset}")
    print(f"{color}└{'─' * width}┘{reset}")


def print_line(title, value, icon="➤"):
    print(f"  {icon} \033[1;36m{title:<14}\033[0m : \033[1;33m{value}\033[0m")


async def MaiiiinE():
    global bot_uid, ToKen, region

    Uid = BOT_UID
    Pw  = BOT_PASSWORD

    if not Uid or not Pw:
        log("ERROR", "UNFAIR_BOT_UID ane UNFAIR_BOT_PASSWORD environment variables set karo.")
        return

    print_banner()
    log("INFO", "लॉगिन प्रक्रिया शुरू हो रही है ...")
    log("INFO", f"लक्ष्य क्षेत्र: {REGION_PREF}")

    try:
        result = await login_engine.do_login(Uid, Pw, REGION_PREF)
    except Exception as e:
        log("ERROR", f"लॉगिन समस्या: {e}")
        return

    if not result:
        log("ERROR", "लॉगिन विफल रहा।")
        await asyncio.sleep(10)
        return

    bot_core.bot_uid = result["bot_uid"]
    bot_core.ToKen = result["token"]
    bot_core.region = result["region"]

    key         = result["key"]
    iv          = result["iv"]
    timestamp   = result["timestamp"]
    online_ip   = result["online_ip"]
    online_port = result["online_port"]
    chat_ip     = result["chat_ip"]
    chat_port   = result["chat_port"]
    acc_name    = result["account_name"]
    clan_id     = result.get("clan_id")
    clan_data   = result.get("clan_data")

    os.system("clear")

    RESET  = "\033[0m"
    CYAN   = "\033[1;36m"
    GREEN  = "\033[1;32m"
    PURPLE = "\033[1;35m"

    # ── बड़े अक्षरों में सिर्फ़ आपका नाम ──
    print()
    print(render("LUCKY", colors=["red", "white"], align="center"))
    print(render("TCP", colors=["yellow", "white"], align="center"))
    print()
    print(f"{PURPLE}{'═' * 60}{RESET}")
    print(f"\033[1;33m{'BOT ONLINE'.center(60)}\033[0m")
    print(f"{PURPLE}{'═' * 60}{RESET}")
    print()

    print_box("ACCOUNT INFORMATION", [
        f"UID          : {result['bot_uid']}",
        f"NAME         : {acc_name}",
        f"REGION       : {result['region']}",
        f"CLAN ID      : {clan_id or 'None'}",
        f"CHAT SERVER  : {chat_ip}:{chat_port}",
        f"GAME SERVER  : {online_ip}:{online_port}",
    ], GREEN)

    print_box("BOT STATUS", [
        "LOGIN SUCCESSFUL",
        "AUTHENTICATION READY",
        "TCP CONNECTION INITIALIZING",
    ], PURPLE)

    log("INFO", "ऑथ टोकन बनाया जा रहा है ...")

    ChatAutH = create_auth_token_chat(
        int(result["bot_uid"]), result["token"],
        int(timestamp), key, iv
    )
    OnlineAutH, _ = build_ob55_online_auth(
        int(result["bot_uid"]), result["token"],
        int(timestamp), key, iv
    )

    log("OK", "ऑथ टोकन तैयार।")
    log("WAIT", "चैट सर्वर से जुड़ रहे हैं ...")

    ready_event = asyncio.Event()
    t1 = asyncio.create_task(
        TcPChaT(
            chat_ip, chat_port, ChatAutH, key, iv,
            ready_event, result["region"],
            clan_id=clan_id,
            clan_data=clan_data,
        )
    )

    await ready_event.wait()
    log("OK", "चैट सर्वर कनेक्शन सफल।")
    await asyncio.sleep(1)

    log("WAIT", "ऑनलाइन सर्वर से जुड़ रहे हैं ...")
    t2 = asyncio.create_task(
        TcPOnLine(online_ip, online_port, key, iv, OnlineAutH)
    )

    print()
    print(f"{PURPLE}{'═' * 70}{RESET}")
    print(render("UNFAIR", colors=["red", "white"], align="center"))
    print(render("T C P", colors=["yellow", "white"], align="center"))
    print(f"{PURPLE}{'═' * 70}{RESET}")

    print(f"\033[1;33m{'⚡ UNFAIR TCP PREMIUM BOT ⚡'.center(70)}\033[0m")
    print(f"{PURPLE}{'═' * 70}{RESET}")

    print_line("OWNER", "SAHIL BHAI")
    print_line("REGION", result['region'])
    print_line("BOT UID", result['bot_uid'])
    print_line("NAME",    acc_name)
    print_line("CLAN",    str(clan_id) if clan_id else "None")
    print_line("STATUS",  "\033[1;32m● RUNNING\033[0m")

    print(f"{PURPLE}{'═' * 70}{RESET}")
    print(f"\033[1;36m{'EVO  •  TEAM  •  MATCH  •  ONLINE'.center(70)}\033[0m")
    print(f"{PURPLE}{'═' * 70}{RESET}")
    print(f"\033[1;35m{'© UNFAIR TCP PREMIUM'.center(70)}\033[0m")
    print()

    await asyncio.gather(t1, t2)


async def StarTinG():
    attempt = 0
    while True:
        attempt += 1
        try:
            log("BOT", f"सेशन #{attempt} शुरू हो रहा है")
            await asyncio.wait_for(MaiiiinE(), timeout=7 * 60 * 60)
        except asyncio.TimeoutError:
            log("WARN", "सेशन खत्म। फिर से चालू हो रहा है ...")
            await asyncio.sleep(3)
        except KeyboardInterrupt:
            log("WARN", "बॉट बंद कर दिया गया।")
            sys.exit(0)
        except Exception as e:
            log("ERROR", f"समस्या: {e}")
            await asyncio.sleep(5)


if __name__ == '__main__':
    try:
        asyncio.run(StarTinG())
    except KeyboardInterrupt:
        print("\nबॉट बंद कर दिया गया।")