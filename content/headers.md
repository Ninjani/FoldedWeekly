
## Pymol script
`draw_protein.py`

``` python
from pymol import cmd
import sys

_, pdb_id, issue = sys.argv
cmd.fetch(pdb_id)
cmd.bg_color("white")
cmd.remove("solvent")
cmd.zoom()
cmd.orient()
cmd.set("cartoon_fancy_helices", 1)
cmd.set("ambient", 0.5)
cmd.set("antialias", 2)
cmd.set("cartoon_sampling", 30)
cmd.set("ray_trace_mode", 2)
cmd.set("ray_trace_color", "0x775abf")
cmd.set("ray_opaque_background", "off")
cmd.set("ray_trace_gain", 2)
cmd.set("ray_trace_disco_factor", 1.)
cmd.ray(2000)
filename = f"{issue}_pymol.png"
cmd.png(str(filename), width=2000, height=2000, dpi=300)
cmd.quit()
```


## Cropping
Uses ImageMagick and [smartcrop](http://www.fmwconcepts.com/imagemagick/smartcrop/index.php)

`./make_post_image <pdb_id> <issue_num>`

```bash
pymol -cq draw_protein.py -- $1 $2
convert $2_pymol.png -trim +repage $2.png
./smartcrop -w 1500 -h 300 -s pyramid $2.png $2.png
mv $2.png FoldedWeekly/static/img
```

## PDB IDs
| Issue | PDB ID |
|---|---|	
| 1 | 7lc2 | 
| 2 | 7rxv |
| 3 | 7rwz |
| 4 | 7dit |
| 5 | 7r6z |
| 6 | 7ptx |
| 7 | 7p12 |
| 8 | 7dsd |
| 9 | 7nma |