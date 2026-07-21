#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_archive_creation.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mny-aro- <mny-aro-@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/19 20:56:32 by mny-aro-            #+#    #+#            #
#   Updated: 2026/07/21 23:13:22 by mny-aro-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys
import typing


def check_arg() -> str | None:
    if len(sys.argv) == 1:
        print("Usage: ft_ancient_text.py <file>\n")
        return None
    else:
        return sys.argv[1]


def open_and_read(file_name: str) -> str | None:
    print(f"Accessing file '{file_name}'")
    try:
        f: typing.IO[str] = open(file_name, "r")
        print("---")
        content = f.read()
        print(f"\n{content}")
        print("\n---")
        f.close()
        print(f"File '{file_name}' closed.")
        return content
    except OSError as err:
        print(f"Error opening file '{file_name}': {err}\n")
        return None


def transform_content(content: str) -> str:
    new_file: list[str] = []
    new_file = content.split("\n")
    cutted_list: list[str] = []
    for file in new_file:
        file += "#"
        cutted_list.append(file)
    final_file = "\n".join(cutted_list)
    return final_file


def save_content(content: str) -> None:
    filename = input("Enter new file name (or empty): ")
    if filename:
        print(f"Saving data to '{filename}'")
        try:
            f: typing.IO[str] = open(filename, "w")
            f.write(content)
            f.close()
            print(f"Data saved in file '{filename}'.")
        except OSError:
            print("Data not saved.")
    else:
        print("Not saving data.")


def main() -> None:
    print("=== Cyber Archives Recovery ===")
    arg = check_arg()
    if arg:
        content = open_and_read(arg)
        if content:
            transformed = transform_content(content)
            print("\nTransform data:")
            print("---")
            print(f"\n{transformed}")
            print("\n---")
            save_content(transformed)
    print()


if __name__ == "__main__":
    main()
