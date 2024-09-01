import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import numpy as np

# Vertex Shader
vertex_shader = """
#version 330 core
in vec4 position;
void main()
{
    gl_Position = position;
}
"""

# Fragment Shader
fragment_shader = """
#version 330 core
out vec4 fragColor;
uniform vec2 iResolution;
uniform float iTime;

// 2D Random Noise
float random(vec2 st) {
    return fract(sin(dot(st.xy, vec2(12.9898,78.233))) * 43758.5453123);
}

// 2D Value Noise
float noise(vec2 st) {
    vec2 i = floor(st);
    vec2 f = fract(st);

    // Four corners in 2D of a tile
    float a = random(i);
    float b = random(i + vec2(1.0, 0.0));
    float c = random(i + vec2(0.0, 1.0));
    float d = random(i + vec2(1.0, 1.0));

    // Smooth Interpolation
    vec2 u = f * f * (3.0 - 2.0 * f);

    // Mix four corners
    return mix(a, b, u.x) + (c - a) * u.y * (1.0 - u.x) + (d - b) * u.x * u.y;
}

// Fractal Brownian Motion
float fbm(vec2 st) {
    float value = 0.0;
    float amplitude = 0.5;
    for (int i = 0; i < 5; i++) {
        value += amplitude * noise(st);
        st *= 2.0;
        amplitude *= 0.5;
    }
    return value;
}

// Color Palette Function
vec3 colorPalette(float t) {
    vec3 a = vec3(0.5, 0.2, 0.7);
    vec3 b = vec3(0.5, 0.2, 0.7);
    vec3 c = vec3(1.0, 1.0, 1.0);
    vec3 d = vec3(0.3, 0.2, 0.8);
    return a + b * cos(6.28318 * (c * t + d));
}

void mainImage(out vec4 fragColor, in vec2 fragCoord) {
    vec2 uv = (fragCoord * 2.0 - iResolution.xy) / iResolution.y;

    // Animate the coordinates
    float time = iTime * 0.1;
    uv *= 2.0 + fbm(uv + time);

    // Generate noise-based pattern
    float n = fbm(uv * 3.0);

    // Color based on the noise
    vec3 color = colorPalette(n);

    // Apply distortion and animation
    vec3 finalColor = color * n * 1.5;

    fragColor = vec4(finalColor, 1.0);
}

void main() {
    mainImage(fragColor, gl_FragCoord.xy);
}

"""

# Class to manage the OpenGL context
class OpenGLApp:
    def __init__(self, width, height, fps_cap, speed):
        self.width = width
        self.height = height
        self.fps_cap = fps_cap
        self.speed = speed
        self.running = True
        self.clock = pygame.time.Clock()

        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height), DOUBLEBUF | OPENGL)
        glViewport(0, 0, self.width, self.height)

        self.shader = self.compile_shaders()
        self.vao, self.vbo, self.ebo = self.create_buffers()

        # Uniform locations
        self.iResolution = glGetUniformLocation(self.shader, 'iResolution')
        self.iTime = glGetUniformLocation(self.shader, 'iTime')

    def compile_shaders(self):
        try:
            shader = compileProgram(
                compileShader(vertex_shader, GL_VERTEX_SHADER),
                compileShader(fragment_shader, GL_FRAGMENT_SHADER)
            )
        except RuntimeError as e:
            print(f"Shader compilation failed: {e}")
            raise SystemExit
        return shader

    def create_buffers(self):
        # Vertex Data
        vertices = np.array([
            -1.0, -1.0, 0.0,
             1.0, -1.0, 0.0,
             1.0,  1.0, 0.0,
            -1.0,  1.0, 0.0
        ], dtype=np.float32)

        # Index Data
        indices = np.array([0, 1, 2, 2, 3, 0], dtype=np.uint32)

        # Create Vertex Array Object (VAO)
        vao = glGenVertexArrays(1)
        glBindVertexArray(vao)

        # Create Vertex Buffer Object (VBO)
        vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, vbo)
        glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

        # Create Element Buffer Object (EBO)
        ebo = glGenBuffers(1)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ebo)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices.nbytes, indices, GL_STATIC_DRAW)

        # Define Position Attribute
        position = glGetAttribLocation(self.shader, 'position')
        glEnableVertexAttribArray(position)
        glVertexAttribPointer(position, 3, GL_FLOAT, GL_FALSE, 0, None)

        return vao, vbo, ebo

    def update_uniforms(self):
        glUniform2f(self.iResolution, self.width, self.height)
        glUniform1f(self.iTime, pygame.time.get_ticks() / (self.speed * 1000))

    def render(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_INT, None)
        pygame.display.flip()

    def run(self):
        glUseProgram(self.shader)
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False

            self.update_uniforms()
            self.render()
            self.clock.tick(self.fps_cap)

        self.cleanup()

    def cleanup(self):
        glDeleteBuffers(1, [self.vbo])
        glDeleteBuffers(1, [self.ebo])
        glDeleteVertexArrays(1, [self.vao])
        glDeleteProgram(self.shader)
        pygame.quit()

# Options
x_W = 1920
y_W = 1080
fps_cap = 120
speed = 1.0  # lower means faster

# Instantiate and run the app
if __name__ == "__main__":
    app = OpenGLApp(x_W, y_W, fps_cap, speed)
    app.run()
