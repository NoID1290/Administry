import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import numpy as np





fragment_shader_path = "f_gl.noid"
vertex_shader_path = "v_gl.noid"

# Load shader source code
with open(vertex_shader_path, "r") as vs_file:
    vertex_shader = vs_file.read()

with open(fragment_shader_path, "r") as fs_file:
    fragment_shader = fs_file.read()




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
