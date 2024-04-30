
from math import sqrt, cos, radians

class S_coords:
    def __init__(self, node = None) -> None:
        if node:
            self.lat = dict(node)["lat"]
            self.lon = dict(node)["lat"]
        else:
            self.lat = 0
            self.lon = 0

    def dist2(self, another, scale = None):
        if scale:
            print(self.scale(scale))
            print(another.scale(scale))
            tmp = self.scale(scale) - another.scale(scale)
        else:
            tmp = self - another

        print(tmp)

        return tmp * tmp
        
    def dist(self, another, scale = None):
        return sqrt(self.dist2(another, scale))
    
    def scale(self, scale):
        return S_coords({"lat": scale * self.lat, "lon": 2 * scale * self.lon * cos(radians(self.lat))})
    
    def __mul__(self, another):
        return self.lon * another.lon + self.lat * another.lat
    
    def __neg__(self):
        return S_coords({"lat": - self.lat, "lon": - self.lon})
    
    def __sub__(self, another):
        return self + (-another)

    def __add__(self, another):
        return S_coords({"lat": another.lat + self.lat, "lon": another.lon + self.lon})
    
    def __repr__(self):
        return f"<Scoords lat:{self.lat} lon:{self.lon}>"

n1 = S_coords({"lat": 47.3833749, "lon": 8.5431961 })
n2 = S_coords({"lat": 47.3834387, "lon": 8.5434747 })

s = 40_075/2 #earth circumference in km

print(n1.dist2(n2, s))
print(n1.dist(n2, s))