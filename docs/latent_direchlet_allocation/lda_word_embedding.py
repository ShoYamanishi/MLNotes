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

n = daft.Node( "theta_new", r"$\bm{\theta\!=\!\frac{1}{K}\bm{1}$", 1, 0, scale=1.5, observed = True )
n.va = "baseline"
pgm.add_node( n )
pgm.add_node( "z",      r"$\mathbf{z}$",     2, 0 )
pgm.add_node( "w",      r"$\mathbf{w}$",     3, 0, observed = True )
pgm.add_node( "b_k",    r"$\mathbf{b}_{k}$", 2, 1, observed = True )

pgm.add_node( "z2",     r"$\mathbf{z}$",     4, 0 )
pgm.add_node( "phi",    r"$\bm{\phi$",       4, 1 )

# Edges.
pgm.add_edge( "theta_new", "z"  )
pgm.add_edge( "z",         "w"  )
pgm.add_edge( "b_k",       "w"  )

pgm.add_edge( "phi",       "z2" )


# And a plate.
pgm.add_plate( [1.5,  0.6, 1.2, 0.8 ], label = r"$K$",   label_offset = [  55, 0 ] )

# Render and save.
pgm.render()
pgm.savefig( "lda_word_embedding.pdf" )
pgm.savefig( "lda_word_embedding.png", dpi=400 )
