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

n = daft.Node( "alpha",  r"$\bm{\alpha}$",    0, 0, observed = True )
n.va = "baseline"
pgm.add_node( n )
pgm.add_node( "theta_new", r"$\bm{\theta_{new}$", 1, 0 )
pgm.add_node( "z_mn",      r"$\mathbf{z}_{mn}$",  2, 0 )
pgm.add_node( "w_mn",      r"$\mathbf{w}_{mn}$",  3, 0, observed = True )
pgm.add_node( "b_k",       r"$\mathbf{b}_{k}$",   2, 1, observed = True )


pgm.add_node( "theta_new2", r"$\bm{\theta_{new}$", 5, 0 )
pgm.add_node( "gamma_new", r"$\bm{\gamma_{new}$",  5, 1 )

# Edges.
pgm.add_edge( "alpha",     "theta_new" )
pgm.add_edge( "theta_new", "z_mn"      )
pgm.add_edge( "z_mn",      "w_mn"      )
pgm.add_edge( "b_k",       "w_mn"      )

pgm.add_edge( "gamma_new", "theta_new2" )

# And a plate.
pgm.add_plate( [1.5,  0.6, 1.2, 0.8 ], label = r"$K$",   label_offset = [  55, 0 ] )
pgm.add_plate( [1.5, -0.4, 2,   0.8 ], label=r"$N_{m}$", label_offset = [  95, 0 ] )

# Render and save.
pgm.render()
pgm.savefig("lda_inference.pdf")
pgm.savefig("lda_inference.png", dpi=400)
