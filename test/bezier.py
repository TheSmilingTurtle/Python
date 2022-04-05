import matplotlib.path as mpath
import matplotlib.patches as mpatches

class bezier:
    def __init__(self, type, args, fill_colour="none") -> None:
        self.type = type.lower()
        self.fill_colour = fill_colour
        self.points = args
        self.mat_path = mpath.Path
        self.path = None

    def build_path(self) -> None:
        types = []
        
        self.path = mpatches.PathPatch(self.mat_path(
            self.points,
            self.get_types),
            fc = self.fill_colour
        )
    
    @property
    def get_path(self) -> mpath.Path:
        return self.path
    
    @property
    def get_types(self):
        match self.type:
            case "c":
                self.types = [self.mat_path.CURVE3 for _ in self.points]
                self.types[0] = self.mat_path.MOVETO

        return self.types
