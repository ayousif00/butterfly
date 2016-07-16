# Butterfly: A Plugin for CFD Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Butterfly.
#
# You should have received a copy of the GNU General Public License
# along with Ladybug; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Load mesh from the case for preview.

-

    Args:
        _case: Butterfly case.
        _load: Load mesh.
        
    Returns:
        mesh: OpenFOAM mesh
"""

ghenv.Component.Name = "Butterfly_Load Mesh"
ghenv.Component.NickName = "loadMesh"
ghenv.Component.Message = 'VER 0.0.01\nJUL_14_2016'
ghenv.Component.Category = "Butterfly"
ghenv.Component.SubCategory = "05::PostProcess"
ghenv.Component.AdditionalHelpFromDocStrings = "1"

if _case and _load:
    _case.copySnappyHexMesh()
    mesh = _case.loadMesh()