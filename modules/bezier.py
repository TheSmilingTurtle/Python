import matplotlib.path as mpath
import matplotlib.patches as mpatches

class bezier:
    def __init__(self, type, args, fill_colour="none") -> None:
        self.type = type.lower()
        self.fill_colour = fill_colour
        self.path_type = mpath.Path
        self.points = args

    def build_path(self) -> None:
        types = []
        
        self.path = mpatches.PathPatch(self.path_type(
            self.points,
            self.get_types()),
            fc = self.fill_colour
        )
    
    @property
    def get_types(self):
        if self.type == "c":
            self.types = [self.path_type.CURVE3 for _ in self.points]
            self.types[0] = self.path_type.MOVETO

        return self.types
    
    @property
    def path(self) -> mpatches.PathPatch:
        return self.path
