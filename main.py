import os

dirs = ["New folder"]

for dir in dirs:
    # os.system(f'py -m manga_translator -v --mode batch --use-cuda --detector ctd --inpainter default --translator=sugoi --font-path "LDFComicSans.ttf" --font-size-offset 2 -f jpg -l ENG -i "E:\VSC\manga-image-translator\{dir}"')
    os.system(f'py -m manga_translator -v --mode batch --use-cuda --detector ctd --inpainter default --font-path "LDFComicSans.ttf" -f jpg -l ENG -i "E:\VSC\manga-image-translator\{dir}"')