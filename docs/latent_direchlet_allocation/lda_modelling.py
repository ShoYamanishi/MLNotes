import daft
from matplotlib import rc


import matplotlib.pyplot as plt
import matplotlib

plt.rc('text', usetex=True)
plt.rc('text.latex', preamble=r'\usepackage{amsmath}\usepackage{amssymb}\usepackage{bm}')

rc("font", family="serif", size=12)
rc("text", usetex=True)


# Colors.
p_color = {"ec": "#46a546"}
s_color = {"ec": "#f89406"}

pgm = daft.PGM()

n = daft.Node( "alpha",  r"$\bm{\alpha}$",    0, 0 )
n.va = "baseline"
pgm.add_node( n )
pgm.add_node( "theta_m", r"$\bm{\theta_m$",   1, 0 )
pgm.add_node( "z_mn",    r"$\mathbf{z}_{mn}$", 2, 0 )
pgm.add_node( "w_mn",    r"$\mathbf{w}_{mn}$", 3, 0, observed = True )

pgm.add_node( "b_k",     r"$\mathbf{b}_{k}$", 2, 1 )
pgm.add_node( "eta",     r"$\eta$",           1, 1 )

# Edges.
pgm.add_edge( "alpha",   "theta_m" )
pgm.add_edge( "theta_m", "z_mn"    )
pgm.add_edge( "z_mn",    "w_mn"    )
pgm.add_edge( "eta",     "b_k"     )
pgm.add_edge( "b_k",     "w_mn"    )


# And a plate.
pgm.add_plate( [1.5,  0.6, 1.2, 0.8 ], label = r"$K$",   label_offset = [  55, 0 ] )
pgm.add_plate( [1.5, -0.4, 2,   0.8 ], label=r"$N_{m}$", label_offset = [  95, 0 ] )
pgm.add_plate( [0.5, -0.5, 3.3, 1.0 ], label=r"$M$",     label_offset = [ 173, 0 ] )

# Render and save.
pgm.render()
pgm.savefig("lda_modelling.pdf")
pgm.savefig("lda_modelling.png", dpi=400)
