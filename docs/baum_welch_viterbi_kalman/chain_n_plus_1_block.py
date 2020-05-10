import daft
from matplotlib import rc


import matplotlib.pyplot as plt
import matplotlib

plt.rc('text', usetex=True)
plt.rc('text.latex', preamble=r'\usepackage{amsmath}\usepackage{amssymb}\usepackage{bm}')

rc("font", family="serif", size=12)
rc("text", usetex=True)

pgm = daft.PGM()

pgm.add_node( "z_1",     r"$\mathbf{z}_{1}$",   1, 1 )
pgm.add_node( "z_2",     r"$\mathbf{z}_{2}$",   2, 1 )
pgm.add_node( "z_3",     r"$\mathbf{z}_{3}$",   3, 1 )
pgm.add_node( "z_n-1",   r"$\mathbf{z}_{n-1}$", 4, 1 )
pgm.add_node( "z_n",     r"$\mathbf{z}_{n}$",   5, 1 )
pgm.add_node( "z_n+1",   r"$\mathbf{z}_{n+1}$", 6, 1, observed=True )
pgm.add_node( "z_N-1",   r"$\mathbf{z}_{N-1}$", 7, 1 )
pgm.add_node( "z_N",     r"$\mathbf{z}_{N}$",   8, 1 )

pgm.add_node( "x_1",     r"$\mathbf{x}_{1}$",   1, 0, observed=True )
pgm.add_node( "x_2",     r"$\mathbf{x}_{2}$",   2, 0, observed=True )
pgm.add_node( "x_3",     r"$\mathbf{x}_{3}$",   3, 0, observed=True )
pgm.add_node( "x_n-1",   r"$\mathbf{x}_{n-1}$", 4, 0, observed=True )
pgm.add_node( "x_n",     r"$\mathbf{x}_{n}$",   5, 0, observed=True )
pgm.add_node( "x_n+1",   r"$\mathbf{x}_{n+1}$", 6, 0, observed=True )
pgm.add_node( "x_N-1",   r"$\mathbf{x}_{N-1}$", 7, 0, observed=True )
pgm.add_node( "x_N",     r"$\mathbf{x}_{N}$",   8, 0, observed=True )

cdots_dic = {}
cdots_dic["linestyle"]=":"
cdots_dic["head_width"]=0
cdots_dic["head_length"]=0

# Edges.
pgm.add_edge( "z_1",    "z_2"   )
pgm.add_edge( "z_2",    "z_3"   )
pgm.add_edge( "z_3",    "z_n-1", plot_params=cdots_dic )
pgm.add_edge( "z_n-1",  "z_n"   )
pgm.add_edge( "z_n",    "z_n+1" )
pgm.add_edge( "z_n+1",  "z_N-1", plot_params=cdots_dic )
pgm.add_edge( "z_N-1",  "z_N"   )
pgm.add_edge( "z_1",    "x_1"   )
pgm.add_edge( "z_2",    "x_2"   )
pgm.add_edge( "z_3",    "x_3"   )
pgm.add_edge( "z_n-1",  "x_n-1" )
pgm.add_edge( "z_n",    "x_n"   )
pgm.add_edge( "z_n+1",  "x_n+1" )
pgm.add_edge( "z_N-1",  "x_N-1" )
pgm.add_edge( "z_N",    "x_N"   )


# Render and save.
pgm.render()
pgm.savefig("chain_n_plus_1_block.pdf")
pgm.savefig("chain_n_plus_1_block.png", dpi=400)
