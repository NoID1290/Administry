import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import numpy as np

# Vertex Shader
vertex_shader = """
#version 330
in vec4 position;
void main()
{
    gl_Position = position;
}
"""

# Fragment Shader
fragment_shader = """
#version 330
out vec4 fragColor;
uniform vec2 iResolution;
uniform float iTime;

vec3 palette(float t) {
    vec3 a = vec3(0.5, 0.5, 0.5);
    vec3 b = vec3(0.5, 0.5, 0.5);
    vec3 c = vec3(1.0, 1.0, 1.0);
    vec3 d = vec3(0.263, 0.416, 0.557);
    return a + b * cos(6.28318 * (c * t + d));
}

void mainImage(out vec4 fragColor, in vec2 fragCoord) {
    vec2 uv = (fragCoord * 2.0 - iResolution.xy) / iResolution.y;
    vec2 uv0 = uv;
    vec3 finalColor = vec3(0.0);
    
    for (float i = 0.0; i < 4.0; i++) {
        uv = fract(uv * 1.5) - 0.5;

        float d = length(uv) * exp(-length(uv0));

        vec3 col = palette(length(uv0) + i * 0.4 + iTime * 0.4);

        d = sin(d * 8.0 + iTime) / 8.0;
        d = abs(d);

        d = pow(0.01 / d, 1.2);

        finalColor += col * d;
    }
    
    fragColor = vec4(finalColor, 1.0);
}

void main() {
    mainImage(fragColor, gl_FragCoord.xy);
}
"""

# Initialize Pygame and OpenGL
pygame.init()
screen = pygame.display.set_mode((800, 600), DOUBLEBUF | OPENGL)
glViewport(0, 0, 800, 600)

# Compile Shaders
shader = compileProgram(
    compileShader(vertex_shader, GL_VERTEX_SHADER),
    compileShader(fragment_shader, GL_FRAGMENT_SHADER)
)

# Vertex Data
vertices = [
    -1.0, -1.0, 0.0,
     1.0, -1.0, 0.0,
     1.0,  1.0, 0.0,
    -1.0,  1.0, 0.0
]

# Index Data
indices = [
    0, 1, 2,
    2, 3, 0
]

# Convert to GLfloat arrays
vertices = np.array(vertices, dtype=np.float32)
indices = np.array(indices, dtype=np.uint32)

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
position = glGetAttribLocation(shader, 'position')
glEnableVertexAttribArray(position)
glVertexAttribPointer(position, 3, GL_FLOAT, GL_FALSE, 0, None)

# Use the Shader Program
glUseProgram(shader)

# Uniform locations
iResolution = glGetUniformLocation(shader, 'iResolution')
iTime = glGetUniformLocation(shader, 'iTime')

# Main Loop
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Update uniforms
    glUniform2f(iResolution, 800, 600)
    glUniform1f(iTime, pygame.time.get_ticks() / 1000.0)

    glClear(GL_COLOR_BUFFER_BIT)
    glDrawElements(GL_TRIANGLES, len(indices), GL_UNSIGNED_INT, None)
    pygame.display.flip()
    clock.tick(60)

# Cleanup
glDeleteBuffers(1, [vbo])
glDeleteBuffers(1, [ebo])
glDeleteVertexArrays(1, [vao])
glDeleteProgram(shader)
pygame.quit()
