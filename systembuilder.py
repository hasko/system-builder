import random
import os

from bodies import Star

star = Star()

spectral_type = ''
while spectral_type not in ['O', 'B', 'A', 'F', 'G', 'K', 'M']:
  spectral_type = input('Choose stellar class [O, B, A, F, G, K, M] (or hit return for G): ').upper()
  if spectral_type == '':
      spectral_type = 'G'
star.spectral_type = spectral_type

lum_classes = {
    '0': { 'name': 'Hypergiants' },
    'Ia': { 'name': 'Luminous supergiants' },
    'Iab': { 'name': 'Intermediate supergiants' },
    'Ib': { 'name': 'Less luminous supergiants' },
    'II': { 'name': 'Bright giants' },
    'III': { 'name': 'Normal giants' },
    'IV': { 'name': 'Subgiants' },
    'V': { 'name': 'Main-sequence stars (dwarfs)' },
    'VI': { 'name': 'Subdwarfs' },
    'D': { 'name': 'White dwarfs' }
}

print('\nLuminosity classes')
print('0 - Hypergiant')
print('Ia, Iab, Ib - Supergiants in decreasing order of luminosity')
print('II - Bright giants')
print('III - Normal giants')
print('IV - Subgiants')
print('V - Main sequence stars (dwarfs)')
print('VI - Subdwarfs')
print('D - White dwarfs')
print();
luminosity_class = ''
while luminosity_class not in ['V']:
    luminosity_class = input('Choose luminosity class (only main sequence implemented for now): ').upper()
    if luminosity_class == '':
        luminosity_class = 'V'
star.luminosity_class = luminosity_class

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
(min_mass, max_mass) = mass_table[star.luminosity_class][star.spectral_type]
random_mass = random.uniform(min_mass, max_mass)
chosen_mass = 0
while chosen_mass < min_mass or chosen_mass > max_mass:
    s = input('Choose a stellar mass from {} to {} (or hit return for {:.2f}): '.format(min_mass, max_mass, random_mass))
    if s == "":
        chosen_mass = random_mass
    else:
        chosen_mass = float(s)
star.mass = chosen_mass

if not os.path.exists('out'):
    os.mkdir('out')

f = open('out/system.html', 'wt', encoding="utf8")
f.write('<html><head><meta charset="UTF-8">')
f.write('<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">\n')
f.write('<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">\n')
f.write('</head>\n')
f.write('<body>')
f.write('<div class="container">')
f.write('<h1>System Overview</h1>\n')
f.write('<h2>Star</h2>\n')
f.write('<table class="table">\n')
f.write('<tr><th scope="row">Spectral type<td>{}<td>&nbsp;</tr>\n'.format(star.spectral_type))
f.write('<tr><th scope="row">Luminosity class<td>{}<td>{}</tr>\n'.format(star.luminosity_class, lum_classes[star.luminosity_class]['name']))
f.write('<tr><th scope="row">Mass<td>{:.2f} M<sub>☉</sub><td>{:.2e} kg</tr>\n'.format(star.mass, star.mass * 1.98847e30))
f.write('<tr><th scope="row">Luminosity<td>{:.5f} L<sub>☉</sub><td>{:0.2e} W</tr>\n'.format(star.luminosity(), star.luminosity() * 3.828e26))
f.write('<tr><th scope="row">Diameter<td>{:.2f} D<sub>☉</sub><td>{:.0f} km</tr>\n'.format(star.diameter(), star.diameter() * 1391016.0))
f.write('<tr><th scope="row">Surface temperature<td>{:.2f} T<sub>☉</sub><td>{:.0f} K</tr>\n'.format(star.surface_temperature(), star.diameter() * 5778.0))
f.write('<tr><th scope="row">Lifetime<td>{:.2f}<td>{:.0f} My</tr>\n'.format(star.lifetime(), star.lifetime() * 9000.0))
f.write('</table>\n')
f.write('<h2>System parameters</h2>\n')
f.write('<table class="table">\n')
f.write('<tr><th>&nbsp;<th scope="col">Distance<th scope="col">Minimum<th scope="col">Maximum</tr>\n')
f.write('<tr><th scope="row">Planet zone<td>&nbsp;<td>{:.2f} AU<td>{:.2f} AU</tr>\n'.format(star.planets_zone()[0], star.planets_zone()[1]))
f.write('<tr><th scope="row">Goldilocks zone<td>&nbsp;<td>{:.2f} AU<td>{:.2f} AU</tr>\n'.format(star.goldilocks_zone()[0], star.goldilocks_zone()[1]))
f.write('<tr><th scope="row">Frost line<td>{:.2f} AU<td>&nbsp;<td>&nbsp;</tr>\n'.format(star.frost_line()))
f.write('</table>\n')


f.write('</div>')
f.write('<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>\n')
f.write('<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>\n')
f.write('<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>\n')
f.write('</table>\n')





f.write('</body></html>')
f.close()
