def dodaj_element(wejscie):
    def get_the_maximum_depth(elmt, level=0):

        max_depth = level if isinstance(elmt, list) else -1
        
        if isinstance(elmt, list):
            for x in elmt:
                max_depth = max(max_depth, get_the_maximum_depth(x, level + 1))
        elif isinstance(elmt, tuple):
            for x in elmt:
                max_depth = max(max_depth, get_the_maximum_depth(x, level + 1))
        elif isinstance(elmt, dict):
            for x in elmt.values():
                max_depth = max(max_depth, get_the_maximum_depth(x, level + 1))
        return max_depth

    maximum_depth = get_the_maximum_depth(wejscie)

    def add_element(elmt, level=0):

        if isinstance(elmt, list):
            if level == maximum_depth:
                if len(elmt) > 0:
                    elmt.append(elmt[-1] + 1)
                else:
                    elmt.append(1)
                return

            for x in elmt:
                add_element(x, level + 1)

        elif isinstance(elmt, tuple):
            for x in elmt:
                add_element(x, level + 1)

        elif isinstance(elmt, dict):
            for x in elmt.values():
                add_element(x, level + 1)

    add_element(wejscie)

    return wejscie

if __name__ == '__main__':
    input_list = [
     1, 2, [3, 4, [5, {"klucz": [5, 6], "tekst": [1, 2]}], 5],
     "hello", 3, [4, 5], 5, (6, (1, [7, 8]))
    ]
    output_list = dodaj_element(input_list)
    print(output_list)