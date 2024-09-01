from rt_utils import *
from objects import *
from random_utils import *
from camera import Camera
import matplotlib.pyplot as plt
import time

# Define engine constants
SAMPLES_PER_RAY = 20   # default 100
MAX_RAY_BOUNCE = 50     # default 50
MAX_RAY_LENGTH = 1e20   # default 1e20

# User constants config
u_screen_W = 400    # default 1200
u_screen_H = 200    # default 675
u_user_gamma = 2    # default 2
u_aperture = 0.1    # default 0.1
u_fov = 6           # default 6
u_distfocus = 10    # default 10




def create_random_scene(N):
    """Create a random scene with spheres."""
    scene = [Sphere(np.float32([0, -1000, 0]), 1000, 
                    albedo=np.float32([0.5, 0.5, 0.5]),
                    material=Material.LAMBERTIAN)]

    for a in range(-N, N):
        for b in range(-N, N):
            choose_mat = np.random.random()
            center = np.float32([a + 0.9 * np.random.random(), 0.2, b + 0.9 * np.random.random()])

            if np.linalg.norm(center - np.float32([4, 0.2, 0])) > 0.9:
                if choose_mat < 0.8:
                    # Diffuse material
                    albedo = np.float32(np.random.random(3)**2)
                    scene.append(Sphere(center, 0.2, albedo=albedo, material=Material.LAMBERTIAN))
                elif choose_mat < 0.95:
                    # Metal material
                    albedo = np.float32(np.random.random(3) * 0.5 + 0.5)
                    roughness = np.random.random() * 0.5
                    scene.append(Sphere(center, 0.2, albedo=albedo, material=Material.METAL, roughness=roughness))
                else:
                    # Glass material
                    scene.append(Sphere(center, 0.2, material=Material.DIELECTRICS, ref_idx=1.5))

    # Add additional spheres
    scene.append(Sphere(np.float32([0, 1, 0]), 1.0, material=Material.DIELECTRICS, ref_idx=1.5))
    scene.append(Sphere(np.float32([-4, 1, 0]), 1.0, albedo=np.float32([0.4, 0.2, 0.1]), material=Material.LAMBERTIAN))
    scene.append(Sphere(np.float32([4, 1, 0]), 1.0, albedo=np.float32([0.7, 0.6, 0.5]), material=Material.METAL, roughness=0.0))

    return scene

def prepare_buffers(scene):
    """Prepare buffers for scene data."""
    centers = []
    radii = []
    albedos = []
    materials = []
    roughnesses = []
    ref_idxs = []
    obj_idxs = []

    for obj_idx, obj in enumerate(scene):
        centers.append(obj.center)
        radii.append(obj.radius)
        albedos.append(obj.albedo)
        materials.append(obj.material.value)
        roughnesses.append(obj.roughness)
        ref_idxs.append(obj.ref_idx)
        obj_idxs.append(obj_idx)

    # Convert to contiguous arrays
    return (np.ascontiguousarray(centers, dtype=np.float32),
            np.ascontiguousarray(radii, dtype=np.float32),
            np.ascontiguousarray(albedos, dtype=np.float32),
            np.ascontiguousarray(materials, dtype=np.int32),
            np.ascontiguousarray(roughnesses, dtype=np.float32),
            np.ascontiguousarray(ref_idxs, dtype=np.float32),
            np.ascontiguousarray(obj_idxs, dtype=np.int32))

def main():
    # Define camera parameters
    img_wh, fov = (u_screen_W, u_screen_H), np.pi/u_fov
    lookfrom = np.float32([13, 2, 3])
    lookat = np.float32([0, 0, -1])
    vup = np.float32([0, 1, 0])
    focus_dist = u_distfocus
    aperture = u_aperture
    camera = Camera(lookfrom, lookat, vup, img_wh, fov, focus_dist, aperture)

    # CUDA block size
    tpb = 32 * 16
    blocks = 64 * 64
    chunk = int(2**20)

    # Construct the scene
    tscene = time.time()
    scene = create_random_scene(11)
    (centers, radii, albedos, materials, roughnesses, ref_idxs, obj_idxs) = prepare_buffers(scene)
    print(f'Scene has {len(scene)} objects, took {time.time() - tscene:.4f} s to construct')

    # Create random vectors
    rand_vec3 = random_unit_vector(int(1e6))

    # Start ray tracing
    start_time = time.time()

    # Create initial rays
    rays_o, rays_d = camera.get_rays(SAMPLES_PER_RAY)
    rays_o = np.ascontiguousarray(rays_o, dtype=np.float32)
    rays_d = np.ascontiguousarray(rays_d, dtype=np.float32)
    rays_idx = np.arange(len(rays_o))
    rays_color = np.ones_like(rays_o)

    bounce = 0
    while len(rays_o) > 1:
        N = len(rays_o)
        hit_record = np.zeros((N, 16), dtype=np.float32)
        hit_record[:, 0] += MAX_RAY_LENGTH  # index 0 stores hit t
        hit_record[:, 1] += -1  # index 1 stores hit object
        # indices 2~4 store hit position
        # indices 5~7 store hit normal (normalized vec3)
        hit_record[:, 8] += 1  # index 8 stores if front face or not
        # indices 9~11 store scatter direction
        # indices 12~14 store albedo
        # index 15 stores scatter or not

        rand_vec3_ = rand_vec3[np.random.randint(rand_vec3.shape[0], size=len(rays_o)), :]

        for i in range(0, N, chunk):  # Process rays by chunk to avoid CUDA OOM
            ray_sphere_intersect[blocks, tpb](
                rays_o[i:i + chunk], rays_d[i:i + chunk], 1e-4, 
                centers, radii, albedos, materials, 
                roughnesses, ref_idxs, obj_idxs, 
                hit_record[i:i + chunk], rand_vec3_[i:i + chunk]
            )

        # Find hits or no hits
        rays_valid = hit_record[:, 0] < MAX_RAY_LENGTH
        rays_idx_hit = rays_idx[rays_valid]
        rays_idx_nohit = rays_idx[~rays_valid]

        # Set background color for rays that didn't hit anything
        t = normalize(rays_d[~rays_valid])[:, 1:2] * 0.5 + 0.5
        rays_color[rays_idx_nohit] *= (1.0 - t) * np.array([1.0, 1.0, 1.0]) + t * np.array([0.5, 0.7, 1.0])

        bounce += 1
        if bounce >= MAX_RAY_BOUNCE:
            rays_color[rays_idx_hit] = 0.0  # Black for rays that didn't stop
            break

        # Update rays for the next bounce
        hit_record_ = hit_record[rays_valid]
        scatter = hit_record_[:, 15] > 0

        # If it didn't scatter (the ray is absorbed), set color to black
        rays_idx_nohit = rays_idx_hit[~scatter]
        rays_color[rays_idx_nohit] = 0

        # Otherwise, continue tracing the ray
        hit_record_ = hit_record_[scatter]
        rays_o = np.ascontiguousarray(hit_record_[:, 2:5])
        rays_d = np.ascontiguousarray(hit_record_[:, 9:12])
        attenuation = hit_record_[:, 12:15]

        rays_idx_hit = rays_idx_hit[scatter]
        rays_color[rays_idx_hit] *= attenuation

        rays_idx = rays_idx_hit

    # Average the color and apply gamma correction
    rays_color = rays_color.reshape(-1, SAMPLES_PER_RAY, 3).mean(1)
    GAMMA = u_user_gamma
    rays_color = rays_color**(1 / GAMMA)

    end_time = time.time()
    print(f'Rendering time: {end_time - start_time:.4f} s')
    print('Saving to raybench_CUDA.png ...')
    plt.imsave('raybench_CUDA.png', rays_color.reshape(img_wh[1], img_wh[0], 3))

if __name__ == '__main__':
    main()
