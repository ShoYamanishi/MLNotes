import daft
from matplotlib import rc


import matplotlib.pyplot as plt
import matplotlib

plt.rc( 'text',       usetex   = True )
plt.rc( 'text.latex', preamble = r'\usepackage{amsmath}\usepackage{amssymb}\usepackage{bm}' )

rc( "font", family = "serif", size = 12 )
rc( "text", usetex = True )

pgm = daft.PGM()

pgm.add_node( "x_1",     r"$\mathbf{x}_{1}$",   1, 1 )
pgm.add_node( "x_2",     r"$\mathbf{x}_{2}$",   2, 1 )
pgm.add_node( "x_3",     r"$\mathbf{x}_{3}$",   3, 1 )
pgm.add_node( "x_N-1",   r"$\mathbf{x}_{N-1}$", 4, 1 )
pgm.add_node( "x_N",     r"$\mathbf{x}_{N}$",   5, 1 )

cdots_dic = {}
cdots_dic[ "linestyle"   ] = ":"
cdots_dic[ "head_width"  ] = 0
cdots_dic[ "head_length" ] = 0

undirected_dic = {}
undirected_dic[ "head_width"  ] = 0
undirected_dic[ "head_length" ] = 0

# Edges.
pgm.add_edge( "x_1",    "x_2",   plot_params = undirected_dic )
pgm.add_edge( "x_2",    "x_3",   plot_params = undirected_dic )
pgm.add_edge( "x_3",    "x_N-1", plot_params = cdots_dic      ) 
pgm.add_edge( "x_N-1",  "x_N",   plot_params = undirected_dic )

# Render and save.
pgm.render()
pgm.savefig( "chain_undirected.pdf" )
pgm.savefig( "chain_undirected.png", dpi = 400 )
