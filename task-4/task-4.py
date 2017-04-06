import sys
import argparse


def get_paragraphs(filename_in):
    paragraphs = []
    new_paragraph = []

    if filename_in is not None:
        file_in = open(filename_in, "r")
        for line in file_in:
            new_words = line.split()
            if line != '\n':
                new_paragraph.extend(new_words)
            else:
                if new_paragraph:
                    paragraphs.append(new_paragraph)
                new_paragraph = []
        if new_paragraph:
            paragraphs.append(new_paragraph)
        file_in.close()

    else:
        for line in sys.stdin.readlines():
            new_words = line.split()
            if line != '\n':
                new_paragraph.extend(new_words)
            else:
                if new_paragraph:
                    paragraphs.append(new_paragraph)
                new_paragraph = []
        if new_paragraph:
            paragraphs.append(new_paragraph)

    return paragraphs


def format_words_in_paragraph(paragraph):
    special_symbols = [44, 46, 63, 33, 45, 58, 39]
    result = []
    new_word = ''
    flag_special_symbols = False
    for word in paragraph:
        if not flag_special_symbols and new_word:
            result.append(new_word)
            new_word = ''

        for char in word:
            if ord(char) in special_symbols:
                flag_special_symbols = True
            elif flag_special_symbols:
                result.append(new_word)
                new_word = ''
                flag_special_symbols = False

            new_word += char

    if new_word:
        result.append(new_word)

    return result


def format_paragraph(paragraph, line_length, paragraph_spaces):
    assert line_length > 0, \
        "Line length cannot be non-positive."
    assert paragraph_spaces >= 0, \
        "Paragraph spaces cannot be negative."
    assert line_length >= paragraph_spaces, \
        "Line length cannot be less than paragraph spaces."

    lines = []
    new_line = ' ' * paragraph_spaces
    fixed_paragraph = format_words_in_paragraph(paragraph)
    need_space = 0

    for word in fixed_paragraph:
        assert line_length >= len(word), \
            "Line length cannot be less than word length."
        if len(new_line) + need_space + len(word) > line_length:
            lines.append(new_line)
            new_line = word
        else:
            new_line += ' ' + word

    if new_line:
        lines.append(new_line)

    return lines


def process(filename_in, filename_out,
            line_length, paragraph_spaces):
    paragraphs = get_paragraphs(filename_in)
    if filename_out is not None:
        file_out = open(filename_out, "w")
        for paragraph in paragraphs:
            for line in format_paragraph(paragraph,
                                         line_length,
                                         paragraph_spaces):
                file_out.write(line + '\n')
        file_out.close()

    else:
        for paragraph in paragraphs:
            for line in format_paragraph(paragraph,
                                         line_length,
                                         paragraph_spaces):
                print(line)


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-i', '--input', type=str, default=None)
    parser.add_argument('-o', '--output', type=str, default=None)
    parser.add_argument('-l', '--line-length', type=int)
    parser.add_argument('-p', '--paragraph-spaces', type=int)

    args = parser.parse_args()
    process(args.input, args.output, args.line_length,
            args.paragraph_spaces)

if __name__ == '__main__':
    main()
