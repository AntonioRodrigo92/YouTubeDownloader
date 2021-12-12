import Utils


def main():
    input_location = input("select the input file: ")
    output_location = input("select the output location: ")
    f = open(input_location, 'r')
    lines = f.readlines()

    for line in lines:
        if Utils.is_valid_youtube_url(line):
            Utils.download_audio(line, output_location)
    f.close()


if __name__ == "__main__":
    main()
