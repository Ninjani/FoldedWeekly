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
cmd.set("ray_texture", 4)
cmd.ray(2000)
filename = f"static/img/{issue}.png"
cmd.png(str(filename), width=2000, height=2000, dpi=300)
cmd.quit()


