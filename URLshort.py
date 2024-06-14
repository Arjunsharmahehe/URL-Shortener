import pyshorteners
import pyperclip as clip

def shortenURL(original_url):
    """
    Shortens URL
    :return: Shortened URL -> string
    """
    s = pyshorteners.Shortener()
    short_url = s.tinyurl.short(original_url)
    print(short_url)
    clip.copy(short_url)
    print('URL copied to clipboard!')

def main():
    original_url = input("Enter the URL: ")
    shortenURL(original_url)

if __name__ == '__main__':
    main()
