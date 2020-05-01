import daft
from matplotlib import rc


import matplotlib.pyplot as plt
import matplotlib

plt.rc( 'text',       usetex   = True )
plt.rc( 'text.latex', preamble = r'\usepackage{amsmath}\usepackage{amssymb}\usepackage{bm}' )

rc( "font", family = "serif", size = 12 )
rc( "text", usetex = True )

pgm = daft.PGM()

pgm.add_node( "x_1",     r"$\mathbf{x}_{1}$",    1,   0, observed=True )
pgm.add_node( "x_2",     r"$\mathbf{x}_{2}$",    2,   0, observed=True )
pgm.add_node( "x_3",     r"$\mathbf{x}_{3}$",    3,   0, observed=True )
pgm.add_node( "x_4",     r"$\mathbf{x}_{3}$",    4,   0, observed=True )

pgm.add_node( "x_5",     r"$\mathbf{x}_{5}$",    1.3, 1, observed=True )
pgm.add_node( "x_6",     r"$\mathbf{x}_{6}$",    2.3, 1, observed=True )
pgm.add_node( "x_7",     r"$\mathbf{x}_{7}$",    3.3, 1, observed=True )
pgm.add_node( "x_8",     r"$\mathbf{x}_{8}$",    4.3, 1, observed=True )

pgm.add_node( "x_9",     r"$\mathbf{x}_{9}$",    1.6, 2, observed=True )
pgm.add_node( "x_10",    r"$\mathbf{x}_{10}$",   2.6, 2, observed=True )
pgm.add_node( "x_11",    r"$\mathbf{x}_{11}$",   3.6, 2, observed=True )
pgm.add_node( "x_12",    r"$\mathbf{x}_{12}$",   4.6, 2, observed=True )


pgm.add_node( "w_1",     r"$\mathbf{z}_{1}$",    1,   1.5 )
pgm.add_node( "w_2",     r"$\mathbf{z}_{2}$",    2,   1.5 )
pgm.add_node( "w_3",     r"$\mathbf{z}_{3}$",    3,   1.5 )
pgm.add_node( "w_4",     r"$\mathbf{z}_{4}$",    4,   1.5 )

pgm.add_node( "w_5",     r"$\mathbf{z}_{5}$",    1.3, 2.5 )
pgm.add_node( "w_6",     r"$\mathbf{z}_{6}$",    2.3, 2.5 )
pgm.add_node( "w_7",     r"$\mathbf{z}_{7}$",    3.3, 2.5 )
pgm.add_node( "w_8",     r"$\mathbf{z}_{8}$",    4.3, 2.5 )

pgm.add_node( "w_9",     r"$\mathbf{z}_{9}$",    1.6, 3.5 )
pgm.add_node( "w_10",    r"$\mathbf{z}_{10}$",   2.6, 3.5 )
pgm.add_node( "w_11",    r"$\mathbf{z}_{11}$",   3.6, 3.5 )
pgm.add_node( "w_12",    r"$\mathbf{z}_{12}$",   4.6, 3.5 )


cdots_dic = {}
cdots_dic[ "linestyle"   ] = ":"
cdots_dic[ "head_width"  ] = 0
cdots_dic[ "head_length" ] = 0

undirected_dic = {}
undirected_dic[ "head_width"  ] = 0
undirected_dic[ "head_length" ] = 0

# Edges.
pgm.add_edge( "w_1",    "x_1" ,   plot_params = undirected_dic )
pgm.add_edge( "w_2",    "x_2" ,   plot_params = undirected_dic )
pgm.add_edge( "w_3",    "x_3" ,   plot_params = undirected_dic )
pgm.add_edge( "w_4",    "x_4" ,   plot_params = undirected_dic )
pgm.add_edge( "w_5",    "x_5" ,   plot_params = undirected_dic )
pgm.add_edge( "w_6",    "x_6" ,   plot_params = undirected_dic )
pgm.add_edge( "w_7",    "x_7" ,   plot_params = undirected_dic )
pgm.add_edge( "w_8",    "x_8" ,   plot_params = undirected_dic )
pgm.add_edge( "w_9",    "x_9" ,   plot_params = undirected_dic )
pgm.add_edge( "w_10",   "x_10",   plot_params = undirected_dic )
pgm.add_edge( "w_11",   "x_11",   plot_params = undirected_dic )
pgm.add_edge( "w_12",   "x_12",   plot_params = undirected_dic )

pgm.add_edge( "w_1",    "w_2",   plot_params = undirected_dic )
pgm.add_edge( "w_2",    "w_3",   plot_params = undirected_dic )
pgm.add_edge( "w_3",    "w_4",   plot_params = undirected_dic )

pgm.add_edge( "w_5",    "w_6",   plot_params = undirected_dic )
pgm.add_edge( "w_6",    "w_7",   plot_params = undirected_dic )
pgm.add_edge( "w_7",    "w_8",   plot_params = undirected_dic )

pgm.add_edge( "w_9",    "w_10",  plot_params = undirected_dic )
pgm.add_edge( "w_10",   "w_11",  plot_params = undirected_dic )
pgm.add_edge( "w_11",   "w_12",  plot_params = undirected_dic )

pgm.add_edge( "w_1",    "w_5",  plot_params = undirected_dic )
pgm.add_edge( "w_5",    "w_9",  plot_params = undirected_dic )

pgm.add_edge( "w_2",    "w_6",  plot_params = undirected_dic )
pgm.add_edge( "w_6",    "w_10", plot_params = undirected_dic )

pgm.add_edge( "w_3",    "w_7",  plot_params = undirected_dic )
pgm.add_edge( "w_7",    "w_11", plot_params = undirected_dic )

pgm.add_edge( "w_4",    "w_8",  plot_params = undirected_dic )
pgm.add_edge( "w_8",    "w_12", plot_params = undirected_dic )

# Render and save.
pgm.render()
pgm.savefig( "grid_crf.pdf" )
pgm.savefig( "grid_crf.png", dpi = 400 )
