import daft
from matplotlib import rc


import matplotlib.pyplot as plt
import matplotlib

plt.rc('text', usetex=True)
plt.rc('text.latex', preamble=r'\usepackage{amsmath}\usepackage{amssymb}\usepackage{bm}')

rc("font", family="serif", size=12)
rc("text", usetex=True)

pgm = daft.PGM()

pgm.add_node( "x_1",     r"$\mathbf{x}_{1}$",   1, 1 )
pgm.add_node( "x_2",     r"$\mathbf{x}_{2}$",   2, 1 )
pgm.add_node( "x_3",     r"$\mathbf{x}_{3}$",   3, 1 )
pgm.add_node( "x_N-1",   r"$\mathbf{x}_{N-1}$", 4, 1 )
pgm.add_node( "x_N",     r"$\mathbf{x}_{N}$",   5, 1 )

pgm.add_node( "y",       r"$\bm{y}$",           3, 0 )

cdots_dic = {}
cdots_dic["linestyle"]=":"
cdots_dic["head_width"]=0
cdots_dic["head_length"]=0

# Edges.
pgm.add_edge( "x_1",    "y"   )
pgm.add_edge( "x_2",    "y"   )
pgm.add_edge( "x_3",    "y"   )
pgm.add_edge( "x_N-1",  "y"   )
pgm.add_edge( "x_N",    "y"   )
pgm.add_edge( "x_3",    "x_N-1", plot_params=cdots_dic )


# Render and save.
pgm.render()
pgm.savefig("param_reduction.pdf")
pgm.savefig("param_reduction.png", dpi=400)
