from main import update_process_list


def print_selection(selection):
    for process in selection:
        print(process)


def start_lookup(selection):
    closer_selection = []
    search = input("\n<search> ")
    if search == 'exit()':
        exit(0)

    for process in selection:
        if search in process['name']:
            closer_selection.append(process)

    return closer_selection


def main():
    closer_selection = update_process_list()
    print_selection(closer_selection)

    while True:
        closer_selection = start_lookup(closer_selection)
        print_selection(closer_selection)


if __name__ == '__main__':
    main()
