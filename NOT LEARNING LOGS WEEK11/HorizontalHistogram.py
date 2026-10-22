"""โปรแกรม HorizontalHistogram"""
def main():
    """HorizontalHistogram"""
    s = input()
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for c in chars:
        count = s.count(c)

        if count > 0:
            result = ""

            while count >= 5:
                if result:
                    result += "|"
                result += "-----"
                count -= 5

            if count > 0:
                if result:
                    result += "|"
                result += "-" * count

            print(c, ":", result)
main()
