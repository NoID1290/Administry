import numpy as np
import matplotlib.pyplot as plt

w = 1280
h = 720
samples = 1  # Number of samples 

def normalize(x):
    return x / np.linalg.norm(x)

def intersect_plane(O, D, P, N):
    denom = np.dot(D, N)
    if np.abs(denom) < 1e-6:
        return np.inf
    d = np.dot(P - O, N) / denom
    if d < 0:
        return np.inf
    return d

def intersect_sphere(O, D, S, R):
    a = np.dot(D, D)
    OS = O - S
    b = 2 * np.dot(D, OS)
    c = np.dot(OS, OS) - R * R
    disc = b * b - 4 * a * c
    if disc > 0:
        distSqrt = np.sqrt(disc)
        q = (-b - distSqrt) / 2.0 if b < 0 else (-b + distSqrt) / 2.0
        t0 = q / a
        t1 = c / q
        t0, t1 = min(t0, t1), max(t0, t1)
        if t1 >= 0:
            return t1 if t0 < 0 else t0
    return np.inf

def intersect(O, D, obj):
    if obj['type'] == 'plane':
        return intersect_plane(O, D, obj['position'], obj['normal'])
    elif obj['type'] == 'sphere':
        return intersect_sphere(O, D, obj['position'], obj['radius'])

def get_normal(obj, M):
    if obj['type'] == 'sphere':
        N = normalize(M - obj['position'])
    elif obj['type'] == 'plane':
        N = obj['normal']
    return N
    
def get_color(obj, M):
    color = obj['color']
    if not hasattr(color, '__len__'):
        color = color(M)
    return color

def trace_ray(rayO, rayD, depth):
    t = np.inf
    for i, obj in enumerate(scene):
        t_obj = intersect(rayO, rayD, obj)
        if t_obj < t:
            t, obj_idx = t_obj, i
    if t == np.inf:
        return np.zeros(3)  # Background color
    obj = scene[obj_idx]
    M = rayO + rayD * t
    N = get_normal(obj, M)
    color = get_color(obj, M)
    toL = normalize(L - M)
    toO = normalize(O - M)
    
    # Shadow check
    shadow_intensity = 1.0
    for k, obj_sh in enumerate(scene):
        if k != obj_idx:
            l = intersect(M + N * .0001, toL, obj_sh)
            if l < np.inf:
                shadow_intensity *= 0.5
    
    # Ambient, Diffuse, Specular
    col_ray = ambient
    col_ray += shadow_intensity * obj.get('diffuse_c', diffuse_c) * max(np.dot(N, toL), 0) * color
    col_ray += obj.get('specular_c', specular_c) * shadow_intensity * max(np.dot(N, normalize(toL + toO)), 0) ** specular_k * color_light
    
    # Reflection
    if depth < depth_max and 'reflection' in obj:
        rayO_reflect = M + N * .0001
        rayD_reflect = normalize(rayD - 2 * np.dot(rayD, N) * N)
        col_ray += obj['reflection'] * trace_ray(rayO_reflect, rayD_reflect, depth + 1)
    
    # Refraction (for dielectric materials like glass)
    if obj.get('material', '') == 'dielectric' and depth < depth_max:
        eta = obj.get('ior', 1.5)  # Index of refraction
        cosi = -np.dot(N, rayD)
        etai = 1
        etat = eta
        if cosi < 0:
            cosi = -cosi
            etai, etat = etat, etai
            N = -N
        eta_ratio = etai / etat
        k = 1 - eta_ratio ** 2 * (1 - cosi ** 2)
        if k >= 0:
            refractD = normalize(eta_ratio * rayD + (eta_ratio * cosi - np.sqrt(k)) * N)
            col_ray += trace_ray(M - N * .0001, refractD, depth + 1)

    return col_ray

def add_sphere(position, radius, color, reflection=0.5, material='diffuse', ior=1.5):
    return dict(type='sphere', position=np.array(position), 
                radius=np.array(radius), color=np.array(color), 
                reflection=reflection, material=material, ior=ior)

def add_plane(position, normal):
    return dict(type='plane', position=np.array(position), 
                normal=np.array(normal),
                color=lambda M: (color_plane0 
                    if (int(M[0] * 2) % 2) == (int(M[2] * 2) % 2) else color_plane1),
                diffuse_c=.75, specular_c=.5, reflection=.25)

color_plane0 = 1. * np.ones(3)
color_plane1 = 0. * np.ones(3)
scene = [
    add_sphere([.75, .1, 1.], .6, [0., 0., 1.]),
    add_sphere([-.75, .1, 2.25], .6, [.5, .223, .5], reflection=0.7, material='dielectric'),
    add_sphere([-2.75, .1, 3.5], .6, [1., .572, .184], reflection=0.9, material='metallic'),
    add_plane([0., -.5, 0.], [0., 1., 0.]),
]

L = np.array([5., 5., -10.])
color_light = np.ones(3)

ambient = .05
diffuse_c = 1.
specular_c = 1.
specular_k = 50

depth_max = 5
O = np.array([0., 0.35, -1.])
Q = np.array([0., 0., 0.])
img = np.zeros((h, w, 3))

r = float(w) / h
S = (-1., -1. / r + .25, 1., 1. / r + .25)

for i, x in enumerate(np.linspace(S[0], S[2], w)):
    if i % 10 == 0:
        print(f"{i / float(w) * 100:.2f}%")
    for j, y in enumerate(np.linspace(S[1], S[3], h)):
        col = np.zeros(3)
        for s in range(samples):
            Q[:2] = (x + (np.random.random() - 0.5) / w, y + (np.random.random() - 0.5) / h)
            D = normalize(Q - O)
            col += trace_ray(O, D, 0)
        img[h - j - 1, i, :] = np.clip(col / samples, 0, 1)

plt.imsave('raytest1.png', img)
