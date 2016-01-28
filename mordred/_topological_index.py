from ._base import Descriptor
from ._common import Diameter as CDiameter
from ._common import Radius as CRadius


class TopologicalIndexBase(Descriptor):
    explicit_hydrogens = False

    @classmethod
    def preset(cls):
        yield cls()

    def __reduce_ex__(self, version):
        return self.__class__, ()


class Radius(TopologicalIndexBase):
    r"""radius descriptor."""

    __slots__ = ()

    def __str__(self):
        return 'Radius'

    def dependencies(self):
        return dict(
            R=CRadius(self.explicit_hydrogens)
        )

    def calculate(self, mol, R):
        return int(R)

    rtype = int


class Diameter(TopologicalIndexBase):
    r"""diameter descriptor."""

    __slots__ = ()

    def __str__(self):
        return 'Diameter'

    def dependencies(self):
        return dict(
            D=CDiameter(self.explicit_hydrogens)
        )

    def calculate(self, mol, D):
        return int(D)

    rtype = int


class TopologicalShapeIndex(TopologicalIndexBase):
    r"""topological shape index descriptor.

    .. math::

        I_{\rm topo} = \frac{D - R}{R}

    where
    :math:`R` is graph radius,
    :math:`D` is graph diameter.

    :returns: NaN when :math:`R = 0`
    """

    __slots__ = ()

    def __str__(self):
        return 'TopoShapeIndex'

    def dependencies(self):
        return dict(
            R=CRadius(self.explicit_hydrogens),
            D=CDiameter(self.explicit_hydrogens),
        )

    def calculate(self, mol, R, D):
        if R == 0:
            return float('nan')

        return float(D - R) / float(R)

    rtype = float


class PetitjeanIndex(TopologicalIndexBase):
    r"""Petitjean index descriptor.

    .. math::

        I_{\rm Petitjean} = \frac{D - R}{D}

    where
    :math:`R` is graph radius,
    :math:`D` is graph diameter.

    :returns: NaN when :math:`D = 0`
    """

    __slots__ = ()

    def __str__(self):
        return 'PetitjeanIndex'

    def dependencies(self):
        return dict(
            R=CRadius(self.explicit_hydrogens),
            D=CDiameter(self.explicit_hydrogens),
        )

    def calculate(self, mol, R, D):
        if D == 0:
            return float('nan')

        return float(D - R) / float(D)

    rtype = float
