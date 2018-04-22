# Slides for Dissertation Defense Presentation

## Cite This Work as

### Papers

Petras, V., Petrasova, A., Jeziorska, J. & Mitasova, H. “Processing UAV and lidar point clouds in
GRASS GIS”. ISPRS-International Archives of the Photogrammetry, Remote Sensing and Spatial
Information Sciences. 2016, pp. 945–952.

Petras, V., Petrasova, A., Harmon, B., Meentemeyer, R. K. & Mitasova, H. “Integrating Free and
Open Source Solutions into Geospatial Science Education”. ISPRS International Journal of
Geo-Information 4.2 (1, 2015), pp. 942–956. DOI : 10.3390/ijgi4020942 .

Petras, V., Mitasova, H. & Petrasova, A. “Mapping gradient fields of landform migration”. Geomor-
phometry for Geosciences (2015). Ed. by Jasiewicz, J., Zwolinski, Z., Mitasova, H. & Hengl, T.

Petras, V., Newcomb, D. J. & Mitasova, H. “Generalized 3D fragmentation index derived from lidar
point clouds”. Open Geospatial Data, Software and Standards 2.1 (2017), p. 9.

## Creating one PNG from PDF document

Using ImageMagic (version 6 syntax) in command line (unix-like):

```
mogrify -format png doc.pdf
montage doc-?.png doc-??.png -tile 7x2 -geometry 200 combined.png
```
