import matplotlib.path as mpath
import matplotlib.patches as mpatches


class bezier:
    def __init__(self, type, *args, style="none") -> None:
        self.type = type.lower()
        self.style = style
        self.path_type = mpath.Path
        self.points = [x for x in args]

    def build_path(self) -> None:
        types = []
        match self.type:
            case "c":
                types = [self.path_type.CURVE3 for _ in self.points]
                types[0] = self.path_type.MOVETO
        self.path = mpatches.PathPatch(
            [self.points],
            types,
            fc=self.style
        )

    @property
    def path(self) -> mpatches.PathPatch:
        return self.path
