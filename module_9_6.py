def all_variants(text):
    length = len(text)
    for i in range(length):
        yield text[i]

    for start in range(length):
        for end in range(start + 1, length + 1):
            if end - start > 1 and end - start != length:
                yield text[start:end]
    yield text


a = all_variants("abc")
for i in a:
    print(i)
