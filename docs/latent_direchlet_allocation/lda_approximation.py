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

n = daft.Node( "gamma_m",  r"$\bm{\gamma_m}$", 0, 1 )
n.va = "baseline"
pgm.add_node( n )
pgm.add_node( "theta_m", r"$\bm{\theta_m$",    0, 0 )

pgm.add_node( "phi_mn",  r"$\bm{\phi}_{mn}$",  1, 1 )
pgm.add_node( "z_mn",    r"$\mathbf{z}_{mn}$", 1, 0 )

pgm.add_node( "omega_k", r"$\bm{\omega}_{k}$", 2.3, 1 )
pgm.add_node( "b_k",     r"$\mathbf{b}_{k}$",  2.3, 0 )

# Edges.
pgm.add_edge( "gamma_m", "theta_m" )
pgm.add_edge( "phi_mn",  "z_mn"    )
pgm.add_edge( "omega_k", "b_k"     )

# And a plate.
pgm.add_plate( [ 1.9, -0.5, 0.8, 2.0 ], label = r"$K$",   label_offset = [  33, 0 ] )
pgm.add_plate( [ 0.5, -0.4, 1.0, 1.8 ], label = r"$N_m$", label_offset = [  39, 0 ] )
pgm.add_plate( [-0.8, -0.5, 2.6, 2.0 ], label = r"$M$",   label_offset = [ 133, 0 ] )


# Render and save.
pgm.render()
pgm.savefig("lda_approximation.pdf")
pgm.savefig("lda_approximation.png", dpi=400)
