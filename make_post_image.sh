pymol -cq draw_protein.py -- $1 $2
convert static/img/$2.png -trim +repage static/img/$2.png
smartcrop --width 1500 --height 300 -s pyramid static/img/$2.png static/img/$2.png
rm $2.cif