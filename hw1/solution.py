def radix_sort(arr):
    max_digits = max([len(str(x[2])) for x in arr])
    base = 10

    bins = [[] for _ in range(base)]

    for i in range(0, max_digits):
        for x in arr:
            digit = (x[2] // base**i) % base
            bins[digit].append(x)

        arr = [x for queue in bins for x in queue]
        bins = [[] for _ in range(base)]

    return arr


if __name__ == "__name__":
    phone_entries = []
    with open("input.txt", "r") as f:
        for line in f.readlines():
            key, value = line.strip().split("\t")
            normalized_number = int("".join(filter(lambda x: x.isdigit(), key)))
            phone_entries.append((key, value, normalized_number))

    phone_entries = radix_sort(phone_entries)

    with open("output.txt", "w") as f:
        for entry in phone_entries:
            print("\t".join(map(str, entry[:2])), file=f)

    # test
    with open("output.txt", "r") as f_output, open("correct.txt", "r") as f_correct:
        for output_line, correct_line in zip(
            f_output.readlines(), f_correct.readlines()
        ):
            assert (
                output_line.strip() == correct_line.strip()
            ), f"Test failed: {correct_line.strip()}"
