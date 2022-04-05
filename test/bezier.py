from email.policy import default
import matplotlib.path as mpath
import matplotlib.patches as mpatches

class bezier:
    def __init__(self, type, args, fill_colour="none") -> None:
        self.type = type.lower()
        self.fill_colour = fill_colour
        self.points = args
        self.mat_path = mpath.Path
        self.types = [self.mat_path.MOVETO]
        self.path = None

    def build_path(self) -> None:
        types = []
        
        self.path = mpatches.PathPatch(self.mat_path(
            self.points,
            self.types),
            fc = self.fill_colour
        )

    def add(self, bezier):
        self.points += bezier.points
        self.types += bezier.types
    
    @property
    def get_path(self) -> mpath.Path:
        return self.path
    
    def get_types(self):
        match self.type:
            case "c":
                self.types = [self.mat_path.CURVE3 for _ in self.points]
                self.types[0] = self.mat_path.MOVETO
            case "l":
                self.types = [self.mat_path.LINETO]
            case "h":
                self.types = [self.mat_path.LINETO]