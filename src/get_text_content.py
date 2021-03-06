from textwrap import fill

characterLimit = 32  # characters per line

# "./src/files/test.txt"


def get_text_content(filepath):
    file = open(filepath)
    content = file.read()
    paragraphList = content.split("\n")

    def wrapText(string):
        return fill(string, characterLimit)

    mappedList = []
    for text in map(wrapText, paragraphList):
        mappedList.append(text)

    result = "\n".join(mappedList)

    return result
