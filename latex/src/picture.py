from colors import *
class Picture:
  def __init__(self, img):
    self.img = img;

  def __eq__(self, other):
    return self.img == other.img

  def _invColor(self, color):
    if color not in inverter:
      return color
    return inverter[color]

  def verticalMirror(self):
    """Devuelve el espejo vertical de la imagen"""
    vertical = []
    for value in self.img:
    	vertical.append(value[::-1])
    return Picture(vertical)

  def horizontalMirror(self):
    """ Devuelve el espejo horizontal de la imagen """
    return Picture(self.img[::-1])

  def negative(self):
    """ Devuelve un negativo de la imagen """
    invertString = lambda s: "".join([self._invColor(s[i]) for i in range(len(s))])
    return Picture([invertString(self.img[i]) for i in range(len(self.img))])

  def join(self, p):
    """ Devuelve una nueva figura poniendo la figura del argumento 
        al lado derecho de la figura actual """
    return Picture([self.img[i] + p.img[i] for i in range(len(self.img))])

  def up(self, p):
    return Picture(self.img + p.img)

  def under(self, p):
    """ Devuelve una nueva figura poniendo la figura p sobre la
        figura actual """
    if self.__eq__(p):
      return p
    mtx = []
    for i in range(len(self.img)):
      mtx.append([])
      for j in range(len(self.img[i])):
        mtx[i].append(p.img[i][j] if p.img[i][j] != " " else self.img[i][j])

    return Picture(["".join(mtx[i]) for i in range(len(mtx))])
  
  def horizontalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual al costado
        la cantidad de veces que indique el valor de n """
    repeatStr = lambda n, s: "".join([s for i in range(n)])
    return Picture([repeatStr(n+1, self.img[i]) for i in range(len(self.img))])

  def verticalRepeat(self, n):
    return Picture(self.img*(n+1))

  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    mtx = []
    for i in range(len(self.img[0])):
      mtx.append([])
      for j in range(len(self.img)):
        mtx[i].append("")
    
    for i in range(len(self.img)):
      for j in range(len(self.img[0])):
        mtx[j][len(self.img) - i - 1] = self.img[i][j]

    return Picture(["".join(mtx[i]) for i in range(len(mtx))])

