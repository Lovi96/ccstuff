def excluding():
    list_of_items = ["kutya", "cica", "mérési hiba", "kutya", "cica", "kolbász"]
    item = ""
    list_without_dupes = []
    for i in list_of_items:
        item = i
        if item not in list_without_dupes:
            list_without_dupes.append(i)
    return list_without_dupes


def main():
    print(excluding())

main()
