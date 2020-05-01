import daft
from matplotlib import rc


import matplotlib.pyplot as plt
import matplotlib

plt.rc('text', usetex=True)
plt.rc('text.latex', preamble=r'\usepackage{amsmath}\usepackage{amssymb}\usepackage{bm}')

rc("font", family="serif", size=12)
rc("text", usetex=True)

pgm = daft.PGM()

pgm.add_node( "u_0",     r"$\bm{u}_0$",         1, 2, fixed = True )
pgm.add_node( "sigma",   r"$\Sigma$",           3, 2, fixed = True )
pgm.add_node( "z_1",     r"$\mathbf{z}_{1}$",   1, 1 )
pgm.add_node( "z_2",     r"$\mathbf{z}_{2}$",   2, 1 )
pgm.add_node( "z_3",     r"$\mathbf{z}_{3}$",   3, 1 )
pgm.add_node( "z_N-1",   r"$\mathbf{z}_{N-1}$", 4, 1 )
pgm.add_node( "z_N",     r"$\mathbf{z}_{N}$",   5, 1 )

cdots_dic = {}
cdots_dic["linestyle"]=":"
cdots_dic["head_width"]=0
cdots_dic["head_length"]=0

# Edges.
pgm.add_edge( "u_0",    "z_1"   )
pgm.add_edge( "z_1",    "z_2"   )
pgm.add_edge( "z_2",    "z_3"   )
pgm.add_edge( "z_3",    "z_N-1", plot_params=cdots_dic )
pgm.add_edge( "z_N-1",  "z_N"   )

pgm.add_edge( "sigma",  "z_1"   )
pgm.add_edge( "sigma",  "z_2"   )
pgm.add_edge( "sigma",  "z_3"   )
pgm.add_edge( "sigma",  "z_N-1" )
pgm.add_edge( "sigma",  "z_N"   )

# Render and save.
pgm.render()
pgm.savefig("chain_gaussian.pdf")
pgm.savefig("chain_gaussian.png", dpi=400)
