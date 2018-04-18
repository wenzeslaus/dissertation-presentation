# dissertation-presentation



## Creating one PNG from PDF document

Using ImageMagic (version 6 syntax) in command line (unix-like):

```
mogrify -format png doc.pdf
montage doc-?.png doc-??.png -tile 7x2 -geometry 200 combined.png
```
