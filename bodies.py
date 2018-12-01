class Star:

    spectral_type = 'G' # O, B, A, F, G, K, M
    luminosity_class = 'V' # 0, Ia, Iab, Ib, II, III, IV, V, VI, D
    mass = 1.0 # in Sun masses

    def luminosity(self):
        return pow(self.mass, 4)

    def diameter(self):
        return pow(self.mass, 0.74)

    def surface_temperature(self):
        return pow(self.mass, 0.505)

    def lifetime(self):
        return pow(self.mass, -2.5)

    def goldilocks_zone(self): # (min, max) in AU
        distance = pow(self.luminosity(), 0.5)
        return (0.95 * distance, 1.37 * distance)

    def planets_zone(self): # (min, max) in AU
        return (0.1 * self.mass, 40.0 * self.mass)

    def frost_line(self): # in AU
        return 4.85 * pow(self.luminosity(), 0.5)
