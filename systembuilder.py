import random
from bodies import Star

spectral_class = ""
while spectral_class not in ['O', 'B', 'A', 'F', 'G', 'K', 'M']:
  spectral_class = input('Choose stellar class [O, B, A, F, G, K, M]: ').upper()
print('\nLuminosity classes')
print('0  - Hypergiant')
print('Ia, Iab, Ib - Supergiants in decreasing order of luminosity')
print('II - Bright giants')
print('III - Normal giants')
print('IV - Subgiants')
print('V - Main sequence stars (dwarfs)')
print('VI - Subdwarfs')
print('D - White dwarfs')
print();
luminosity_class = ""
while luminosity_class not in ['V']:
    luminosity_class = input('Choose luminosity class (only main sequence implemented for now): ').upper()
mass_table = {
    'V': {
        'O': (16.0, 200.0),
        'B': (2.1, 16.0),
        'A': (1.4, 2.1),
        'F': (1.04, 1.4),
        'G': (0.8, 1.04),
        'K': (0.45, 0.8),
        'M': (0.08, 0.45)
    }
}
(min_mass, max_mass) = mass_table[luminosity_class][spectral_class]
stellar_mass = random.uniform(min_mass, max_mass)
chosen_mass = 0
while chosen_mass < min_mass or chosen_mass > max_mass:
    s = input('Choose a stellar mass from {} to {} (or hit return for {:.2f}): '.format(min_mass, max_mass, stellar_mass))
    if s == "":
        chosen_mass = stellar_mass
stellar_mass = chosen_mass
star = Star()
star.spectral_type = spectral_class
star.luminosity_class = luminosity_class
star.mass = stellar_mass

f = open('out/system.html', 'wt', encoding="utf8")
f.write('<html><head><meta charset="UTF-8"></head>\n')
f.write('<body>')
f.write('<h1>System Overview</h1>\n')
f.write('<h2>Star</h2>\n')
f.write('<table border=0>\n')
f.write('<tr><th>Spectral type<td>{}</tr>\n'.format(star.spectral_type))
f.write('<tr><th>Luminosity class<td>{}</tr>\n'.format(star.luminosity_class))
f.write('<tr><th>Mass (M<sub>☉</sub>)<td>{:.2f}</tr>\n'.format(star.mass))
f.write('<tr><th>Luminosity (☉ = 1)<td>{:.2f}</tr>\n'.format(star.luminosity()))
f.write('<tr><th>Diameter (☉ = 1, km)<td>{:.2f}<td>{:.0f}</tr>\n'.format(star.diameter(), star.diameter() * 1391016.0))
f.write('<tr><th>Surface temperature (☉ = 1, K)<td>{:.2f}<td>{:.0f}</tr>\n'.format(star.surface_temperature(), star.diameter() * 5778.0))
f.write('<tr><th>Lifetime (☉ = 1, M years)<td>{:.2f}</tr>\n'.format(star.lifetime(), star.lifetime() * 9000.0))
f.write('</table>\n')
f.write('<h2>System parameters</h2>\n')
f.write('<table border=0>\n')
f.write('<tr><th>&nbsp;<th>Distance<th>Minimum<th>Maximum</tr>\n')
f.write('<tr><th>Planet zone (AU)<td>&nbsp;<td>{:.2f}<td>{:.2f}</tr>\n'.format(star.planets_zone()[0], star.planets_zone()[1]))
f.write('<tr><th>Goldilocks zone (AU)<td>&nbsp;<td>{:.2f}<td>{:.2f}</tr>\n'.format(star.goldilocks_zone()[0], star.goldilocks_zone()[1]))
f.write('<tr><th>Frost line (AU)<td>{:.2f}<td>&nbsp;<td>&nbsp;</tr>\n'.format(star.frost_line()))
f.write('</table>\n')





f.write('</body></html>')
f.close()
