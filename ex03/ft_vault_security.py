#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_vault_security.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mny-aro- <mny-aro-@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/22 14:49:49 by mny-aro-            #+#    #+#            #
#   Updated: 2026/07/22 17:20:22 by mny-aro-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def secure_archive(filename: str,
                   action: str = "r", content: str = "") -> tuple[bool, str]:
    if action == "r":
        try:
            with open(filename, action) as file:
                data = file.read()
            return True, data
        except OSError as err:
            return False, str(err)
    elif action == "w":
        try:
            with open(filename, action) as file:
                data = file.write(content)
            return True, "Content successfully written to file"
        except OSError as err:
            return False, str(err)
    else:
        return False, "Invalid action"


def main() -> None:
    print("=== Cyber Archives Security ===")
    print("\nUsing 'secure_archive' to read from a nonexistent file:")
    test_access = secure_archive("/not/existing/file", "r")
    print(test_access)
    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    test_read = secure_archive("/etc/shadow", "r")
    print(test_read)
    print("\nUsing 'secure_archive' to read from a regular file:")
    test_regular = secure_archive("ancient_fragment.txt", "r")
    print(test_regular)
    print("\nUsing 'secure_archive' to write previous content to a new file:")
    test_write = secure_archive("new_file.txt", "w", test_regular[1])
    print(test_write)


if __name__ == "__main__":
    main()
