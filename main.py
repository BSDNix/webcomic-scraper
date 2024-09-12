from comic_collection import ComicCollection
import datetime
import config as cfg
import argparse

date = datetime.datetime.today()
year = date.strftime("%Y")
UPDATED_ON = date.strftime("%d-%m-%Y %H:%M:%S")
LASTUPDATED=f"<center><h3>Last update: {UPDATED_ON}</h3></center>"

###
### HTML HEADER
###
HTMLHEAD=f"""
<!DOCTYPE html>
<html>
<head>
    <title>Comics</title>
    <link rel="stylesheet" href="dark-theme.css">
    <link rel="icon" type="image/png" href="comics.png" />
</head>
<body>
{LASTUPDATED}
<div class="ex1">
<center>
<hr style='width:70%;text-align:left;margin-left:0'>
"""

###
### HTML FOOTER
###
HTMLFOOT=f"""
{LASTUPDATED}
</center>
</div>
</body>
</html>
"""

def main():
    parser = argparse.ArgumentParser(description="Fetch comics.")
    parser.add_argument('--one', type=str, help="Fetch one comic by title.")
    args = parser.parse_args()

    # Assume comics is a list of comic objects.
    mycomics = ComicCollection('comics')  
    fetcher = ComicFetcher(comics)

    if args.one:
        # Fetch one comic based on the provided title
        result = fetcher.get_one_comic(args.one)
        if result:
            print(result)
    else:
        my_comics = ComicCollection('comics')
        comics=my_comics.get_all_comics()

    f = open(f"{cfg.OUTPUT_DIR}/{cfg.OUTPUT_FILE}", "w")
    f.write(HTMLHEAD + comics + HTMLFOOT)
    f.close()

if __name__ == '__main__':
    main()
