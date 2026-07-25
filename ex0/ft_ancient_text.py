#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_ancient_text.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mny-aro- <mny-aro-@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/19 14:01:45 by mny-aro-            #+#    #+#            #
#   Updated: 2026/07/26 01:10:04 by mny-aro-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys
import typing


def check_arg() -> str | None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>\n")
        return None
    else:
        return sys.argv[1]


def open_and_read(file_name: str) -> None:
    print(f"Accessing file '{file_name}'")
    f: typing.IO[str] | None = None
    try:
        f = open(file_name, "r")
        print("---")
        print(f"\n{f.read()}")
        print("\n---")
    except OSError as err:
        print(f"Error opening file '{file_name}': {err}\n")
    finally:
        if f is not None:
            f.close()
            print(f"File '{file_name}' closed.")

def main() -> None:
    print("=== Cyber Archives Recovery ===")
    arg = check_arg()
    if arg:
        open_and_read(arg)


if __name__ == "__main__":
    main()
