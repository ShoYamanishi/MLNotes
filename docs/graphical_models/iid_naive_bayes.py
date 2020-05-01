import daft
from matplotlib import rc


import matplotlib.pyplot as plt
import matplotlib

plt.rc('text', usetex=True)
plt.rc('text.latex', preamble=r'\usepackage{amsmath}\usepackage{amssymb}\usepackage{bm}')

rc("font", family="serif", size=12)
rc("text", usetex=True)

pgm = daft.PGM()

pgm.add_node( "x_1",     r"$\mathbf{x}_{1}$",   1, 0 )
pgm.add_node( "x_2",     r"$\mathbf{x}_{2}$",   2, 0 )
pgm.add_node( "x_3",     r"$\mathbf{x}_{3}$",   3, 0 )
pgm.add_node( "x_N-1",   r"$\mathbf{x}_{N-1}$", 4, 0 )
pgm.add_node( "x_N",     r"$\mathbf{x}_{N}$",   5, 0 )

pgm.add_node( "mu",      r"$\bm{\mu}$",         3, 1 )

pgm.add_node( "x2_1",     r"$\mathbf{x}_{1}$",   6, 0 )
pgm.add_node( "x2_2",     r"$\mathbf{x}_{2}$",   7, 0 )
pgm.add_node( "x2_3",     r"$\mathbf{x}_{3}$",   8, 0 )
pgm.add_node( "x2_N-1",   r"$\mathbf{x}_{N-1}$", 9, 0 )
pgm.add_node( "x2_N",     r"$\mathbf{x}_{N}$",   10, 0 )

pgm.add_node( "C",        r"$C$",                8, 1 )

cdots_dic = {}
cdots_dic["linestyle"]=":"
cdots_dic["head_width"]=0
cdots_dic["head_length"]=0

# Edges.
pgm.add_edge( "mu",  "x_1"     )
pgm.add_edge( "mu",  "x_2"     )
pgm.add_edge( "mu",  "x_3"     )
pgm.add_edge( "mu",  "x_N-1"   )
pgm.add_edge( "mu",  "x_N"     )
pgm.add_edge( "x_3", "x_N-1", plot_params=cdots_dic )

pgm.add_edge( "C",  "x2_1"     )
pgm.add_edge( "C",  "x2_2"     )
pgm.add_edge( "C",  "x2_3"     )
pgm.add_edge( "C",  "x2_N-1"   )
pgm.add_edge( "C",  "x2_N"     )
pgm.add_edge( "x2_3", "x2_N-1", plot_params=cdots_dic )

# Render and save.
pgm.render()
pgm.savefig("iid_naive_bayes.pdf")
pgm.savefig("iid_naive_bayes.png", dpi=400)
