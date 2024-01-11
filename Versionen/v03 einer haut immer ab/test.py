import numpy as np
from decimal import Decimal, getcontext

# Werte initialisieren
alt_winner = np.array([Decimal(1)])
alt_looser = np.array([Decimal(1)])
exponent = Decimal(0.005)

# Berechnung durchführen
pointsjs1 = np.round(alt_winner + np.power(2, (alt_winner - alt_looser) * exponent), 3)
pointsjs = np.round(alt_looser - np.power(2, (alt_looser - alt_winner) * exponent), 3)

