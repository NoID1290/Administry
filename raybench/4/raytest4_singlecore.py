import numpy as np
import matplotlib.pyplot as plt

# Constants
w = 800
h = 600
max_depth = 5
samples_per_pixel = 4  # Number of samples for anti-aliasing

# Helper functions
def normalize(v):
    return v / np.linalg.norm(v)

def reflect(I, N):
    return I - 2 * np.dot(I, N) * N

def refract(I, N, refractive_index):
    cosi = -max(-1, min(1, np.dot(I, N)))
    etai = 1
    etat = refractive_index
    n = N
    if cosi < 0:  # Outside the surface
        cosi = -cosi
    else:  # Inside the surface
        etai, etat = etat, etai
        n = -N
    eta = etai / etat
    k = 1 - eta * eta * (1 - cosi * cosi)
    if k < 0:
        return None
    return eta * I + (eta * cosi - np.sqrt(k)) * n

# Ray class
class Ray:
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = normalize(direction)

# Object classes
class Object:
    def __init__(self, color, reflection=0.5, refraction=0.0, diffuse_c=1.0, specular_c=1.0, specular_k=50):
        self.color = np.array(color)
        self.reflection = reflection
        self.refraction = refraction
        self.diffuse_c = diffuse_c
        self.specular_c = specular_c
        self.specular_k = specular_k

    def intersect(self, ray):
        raise NotImplementedError("Intersect method not implemented!")

    def normal(self, point):
        raise NotImplementedError("Normal method not implemented!")

    def bounding_box(self):
        raise NotImplementedError("Bounding box method not implemented!")

class Sphere(Object):
    def __init__(self, position, radius, **kwargs):
        super().__init__(**kwargs)
        self.position = np.array(position)
        self.radius = radius

    def intersect(self, ray):
        L = self.position - ray.origin
        tca = np.dot(L, ray.direction)
        d2 = np.dot(L, L) - tca * tca
        if d2 > self.radius ** 2:
            return np.inf
        thc = np.sqrt(self.radius ** 2 - d2)
        t0 = tca - thc
        t1 = tca + thc
        if t0 < 0:
            t0 = t1
        if t0 < 0:
            return np.inf
        return t0

    def normal(self, point):
        return normalize(point - self.position)

    def bounding_box(self):
        min_corner = self.position - self.radius
        max_corner = self.position + self.radius
        return min_corner, max_corner

class Plane(Object):
    def __init__(self, position, normal, **kwargs):
        super().__init__(**kwargs)
        self.position = np.array(position)
        self.normal_vec = normalize(normal)

    def intersect(self, ray):
        denom = np.dot(ray.direction, self.normal_vec)
        if np.abs(denom) < 1e-6:
            return np.inf
        t = np.dot(self.position - ray.origin, self.normal_vec) / denom
        return t if t >= 0 else np.inf

    def normal(self, point):
        return self.normal_vec

    def bounding_box(self):
        # Planes do not have a bounded box, but we return a large box for BVH intersection testing
        return (np.array([-np.inf, -np.inf, -np.inf]), np.array([np.inf, np.inf, np.inf]))

# Bounding Volume Hierarchy (BVH) class
class BVHNode:
    def __init__(self, objects):
        self.objects = objects
        self.left = None
        self.right = None
        self.bounding_box = self.calculate_bounding_box()

    def calculate_bounding_box(self):
        min_corner = np.min([obj.bounding_box()[0] for obj in self.objects], axis=0)
        max_corner = np.max([obj.bounding_box()[1] for obj in self.objects], axis=0)
        return min_corner, max_corner

    def intersect(self, ray):
        min_corner, max_corner = self.bounding_box
        tmin = (min_corner - ray.origin) / ray.direction
        tmax = (max_corner - ray.origin) / ray.direction
        t1 = np.minimum(tmin, tmax)
        t2 = np.maximum(tmin, tmax)
        t_near = np.max(t1)
        t_far = np.min(t2)
        return t_near <= t_far and t_far >= 0

# Ray tracing functions
def trace_ray(ray, depth):
    if depth >= max_depth:
        return np.zeros(3)

    t_min = np.inf
    hit_obj = None
    hit_point = None
    normal = None

    for obj in scene:
        if bvh.intersect(ray):
            t = obj.intersect(ray)
            if t < t_min:
                t_min = t
                hit_obj = obj
                hit_point = ray.origin + ray.direction * t
                normal = obj.normal(hit_point)

    if hit_obj is None:
        return np.zeros(3)

    color = hit_obj.color * ambient

    # Lighting calculations
    light_dir = normalize(L - hit_point)
    light_ray = Ray(hit_point + normal * 1e-5, light_dir)
    shadow = any(obj.intersect(light_ray) < np.linalg.norm(L - hit_point) for obj in scene)

    if not shadow:
        # Diffuse reflection
        diffuse_intensity = max(np.dot(light_dir, normal), 0)
        color += hit_obj.color * hit_obj.diffuse_c * diffuse_intensity

        # Specular reflection
        view_dir = normalize(O - hit_point)
        reflection_dir = reflect(-light_dir, normal)
        specular_intensity = max(np.dot(reflection_dir, view_dir), 0) ** hit_obj.specular_k
        color += color_light * hit_obj.specular_c * specular_intensity

    # Reflection
    reflected_ray = Ray(hit_point + normal * 1e-5, reflect(ray.direction, normal))
    reflection_color = trace_ray(reflected_ray, depth + 1)
    color += reflection_color * hit_obj.reflection

    # Refraction
    if hit_obj.refraction > 0:
        refracted_dir = refract(ray.direction, normal, hit_obj.refraction)
        if refracted_dir is not None:
            refracted_ray = Ray(hit_point - normal * 1e-5, refracted_dir)
            refraction_color = trace_ray(refracted_ray, depth + 1)
            color += refraction_color * hit_obj.refraction

    return np.clip(color, 0, 1)

# Scene setup
scene = [
    Sphere(position=[0.75, 0.1, 1.], radius=0.6, color=[0., 0., 1.], reflection=0.5, refraction=0.1),
    Sphere(position=[-0.75, 0.1, 2.25], radius=0.6, color=[0.5, 0.223, 0.5], reflection=0.5),
    Sphere(position=[-2.75, 0.1, 3.5], radius=0.6, color=[1., 0.572, 0.184], reflection=0.5),
    Plane(position=[0., -0.5, 0.], normal=[0., 1., 0.], color=[1., 1., 1.], reflection=0.25)
]

# Create BVH
bvh = BVHNode(scene)

L = np.array([5., 5., -10.])
color_light = np.ones(3)
ambient = 0.05
O = np.array([0., 0.35, -1.])

# Image rendering with anti-aliasing
r = float(w) / h
S = (-1., -1. / r + 0.25, 1., 1. / r + 0.25)
img = np.zeros((h, w, 3))

for i, x in enumerate(np.linspace(S[0], S[2], w)):
    if i % 10 == 0:
        print(f"{i / float(w) * 100:.2f}%")
    for j, y in enumerate(np.linspace(S[1], S[3], h)):
        col = np.zeros(3)
        for _ in range(samples_per_pixel):
            offset_x = np.random.uniform(-0.5, 0.5) / w
            offset_y = np.random.uniform(-0.5, 0.5) / h
            Q = np.array([x + offset_x, y + offset_y, 0])
            ray = Ray(O, Q - O)
            col += trace_ray(ray, 0)
        img[h - j - 1, i, :] = np.clip(col / samples_per_pixel, 0, 1)

plt.imsave('4_singlecore.png', img)
