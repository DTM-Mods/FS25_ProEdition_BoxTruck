"""Rebuild the flatbed body's width-dependent geometry to the Krone ProfiLiner load width (2.44 m clear, was 2.38).
Real geometry, no object scaling: box edges move out D each side (bevels unchanged), the 15 planks are re-spaced,
the tailgate diamond tread is regenerated, side parts move out D. Underrun, light bar, lamps, subframe unchanged.
Run: blender -b previews/flatbed_tailgate_v3/flatbed_tailgate_proposal_v3.blend -P widen_body.py
Writes source/flatbed_runtime/build/flatbed_body_wide_source.blend (input for build_body.py)."""
import bpy, math
from pathlib import Path
from mathutils import Vector
ROOT = Path(__file__).resolve().parents[2]
D = 0.03
O = bpy.data.objects

def widen_box(ob):            # push every vertex away from the centre line by D (world X)
    mw = ob.matrix_world; inv = mw.inverted()
    for v in ob.data.vertices:
        w = mw @ v.co
        assert abs(w.x) > 0.3, ob.name
        w.x += D if w.x > 0 else -D
        v.co = inv @ w

def move_out(ob):
    x = ob.matrix_world.translation.x
    if abs(x) < 0.05:
        x = sum((ob.matrix_world @ v.co).x for v in ob.data.vertices) / len(ob.data.vertices)
    mw = ob.matrix_world.copy(); mw.translation.x += D if x > 0 else -D; ob.matrix_world = mw

stretch = ['Structural deck', 'Headboard top', 'Headboard lower protection', 'Tailgate stainless panel', 'Tailgate upper folded lip']
stretch += [o.name for o in O if o.name.startswith(('Deck crossmember', 'Headboard horizontal rail'))]
moves = [o.name for o in O if o.name.startswith(('Board fixed post', 'Board hinge ', 'Deck edge aluminum rail', 'Headboard upright',
                                               'Amber side marker', 'Tailgate latch'))]
moves += [o.name for o in O if o.name.startswith('Stake ') and o.type == 'EMPTY']
for n in stretch: widen_box(O[n])
bpy.context.view_layer.update()
for n in moves:
    if O[n].parent and O[n].parent.name in moves: continue
    move_out(O[n]); bpy.context.view_layer.update()

# 15 deck planks, evenly re-spaced across the wider deck (6 mm gaps as before)
half = 1.21 + D; pw = 2 * half / 15
for i in range(15):
    ob = O['Deck plank %02d' % i]; mw = ob.matrix_world; inv = mw.inverted()
    xs = [(mw @ v.co).x for v in ob.data.vertices]; lo, hi = min(xs), max(xs)
    x0 = -half + i * pw; x1 = x0 + pw - .006
    for v in ob.data.vertices:
        w = mw @ v.co; w.x = x0 if abs(w.x - lo) < abs(w.x - hi) else x1; v.co = inv @ w

# Tailgate diamond tread: same pattern as tailgate_v3.py, one more column for the wider panel
tread = O['Tailgate diamond pattern']; cols = 40; x_start = -0.06 * (cols - 1) / 2
verts = []; faces = []
for row in range(6):
    y = 1.662 + row * .043
    for col in range(cols):
        x = x_start + col * .060
        a = math.radians(45 if (row + col) % 2 == 0 else -45)
        u = Vector((math.cos(a), math.sin(a))); v = Vector((-math.sin(a), math.cos(a)))
        corners = [u * .018, v * .0045, -u * .018, -v * .0045]
        s = len(verts)
        for depth, sc in [(5.3833, 1), (5.386, 0.55)]:
            for c in corners: verts.append((x + c.x * sc, depth, y + c.y * sc))
        faces.append((s + 4, s + 7, s + 6, s + 5))
        for j in range(4): faces.append((s + j, s + (j + 1) % 4, s + 4 + (j + 1) % 4, s + 4 + j))
inv = tread.matrix_world.inverted()
old = tread.data; mesh = bpy.data.meshes.new(old.name)
mesh.from_pydata([tuple(inv @ Vector(p)) for p in verts], [], faces)
for m in old.materials: mesh.materials.append(m)
tread.data = mesh; bpy.data.meshes.remove(old)
bpy.context.view_layer.update()

def span(n):
    xs = [(O[n].matrix_world @ v.co).x for v in O[n].data.vertices]; return min(xs), max(xs)
def close(a, b): return abs(a - b) < 1e-4
assert close(span('Structural deck')[1], 1.305) and close(span('Tailgate stainless panel')[1], 1.215)
assert close(span('Deck plank 00')[0], -1.24) and close(span('Deck plank 14')[1], 1.24 - .006)
assert close(span('Stake steel upright')[1], -1.225)          # stake inner face: 2.45 m between stakes
assert close(span('Board fixed post')[1], -1.22)          # post inner face: 2.44 m clear (UAL width)
assert close(span('Drop side panel')[1], -1.255) and close(O['Board hinge -1 0'].matrix_world.translation.x, -1.305)
assert all(o.scale[:] == (1, 1, 1) for o in O if o.type == 'MESH' and not o.name.startswith('VOLVO'))
out = ROOT / 'source/flatbed_runtime/build/flatbed_body_wide_source.blend'
bpy.ops.wm.save_as_mainfile(filepath=str(out))
print('WIDE_BODY_READY', len(stretch), 'boxes widened,', len(moves), 'parts moved, 15 planks, tread', cols, 'cols ->', out)
