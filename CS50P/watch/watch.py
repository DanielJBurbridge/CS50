import re

def main():

    # tests = [
    #     ['<iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>', 'xvFZjo5PgG0'],
    #     ['<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>', 'xvFZjo5PgG0'],
    #     ['<iframe width="560" height="315" src="https://cs50.harvard.edu/python"></iframe>', None]
    # ]

    # for test in tests:
    #     result = parse(test[0])
    #     if result == None:
    #         print(f"{result}, {'PASSED' if result == test[1] else 'FAILED'}")
    #     else:
    #         print(f"{result}, {'PASSED' if result.split('/')[-1] == test[1] else 'FAILED'}")

    html_to_parse = input("HTML: ")
    print(parse(html_to_parse))

def parse(s):

    pattern = construct_pattern()

    match = re.search(pattern, s)
    if match == None:
        return match
    else:
        return format(match.groups()[-1])

def format(s):
    return f"https://youtu.be/{s.split('/')[-1]}"


def construct_pattern():
    pattern = re.compile(r'src="https?://(www\.)?youtube\.com(.*?)"')
    return pattern

if __name__ == "__main__":
    main()