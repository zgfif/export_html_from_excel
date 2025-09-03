from app_lib.webpages import Webpages


def main() -> None:
    """
    Run generating html files.
    """

    Webpages(filepath='sources/webpage.xlsx', output_directory='generated_pages').generate()





if __name__ == '__main__':
    main()
