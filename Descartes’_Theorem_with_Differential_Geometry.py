import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

# ---------------------------------------------------
# DARK SCIENTIFIC STYLE
# ---------------------------------------------------
plt.style.use('dark_background')

# ---------------------------------------------------
# GENERATE SPHERE FUNCTION
# ---------------------------------------------------
def generate_sphere(r):

    theta = np.linspace(0, 2 * np.pi, 100)
    phi = np.linspace(0, np.pi, 100)

    theta, phi = np.meshgrid(theta, phi)

    x = r * np.sin(phi) * np.cos(theta)
    y = r * np.sin(phi) * np.sin(theta)
    z = r * np.cos(phi)

    return x, y, z

# ---------------------------------------------------
# MAIN PROGRAM
# ---------------------------------------------------
def main():

    # Sphere radii
    radii = [1, 2, 3, 4]

    # Neon scientific colors
    colors = ['cyan', 'magenta', 'lime', 'orange']

    # Curvature calculation
    curvatures = [1 / r for r in radii]
    total_curvature = sum(curvatures)

    # ---------------------------------------------------
    # CREATE FIGURE
    # ---------------------------------------------------
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111, projection='3d')

    # Dark background
    fig.patch.set_facecolor('black')
    ax.set_facecolor('black')

    # ---------------------------------------------------
    # PLOT SPHERES
    # ---------------------------------------------------
    for r, c in zip(radii, colors):

        x, y, z = generate_sphere(r)

        # Transparent glowing surface
        ax.plot_surface(
            x, y, z,
            color=c,
            alpha=0.25,
            edgecolor='white',
            linewidth=0.2,
            rstride=4,
            cstride=4
        )

        # Wireframe overlay
        ax.plot_wireframe(
            x, y, z,
            color='white',
            alpha=0.08
        )

        # Curvature labels
        ax.text(
            r,
            0,
            0,
            f"k={1/r:.2f}",
            color='white',
            fontsize=10
        )

    # ---------------------------------------------------
    # AXIS SETTINGS
    # ---------------------------------------------------
    ax.set_title(
        "Descartes' Theorem Visualization",
        fontsize=16,
        color='cyan',
        pad=20
    )

    ax.set_xlabel('X-axis', color='white')
    ax.set_ylabel('Y-axis', color='white')
    ax.set_zlabel('Z-axis', color='white')

    ax.grid(color='cyan', alpha=0.2)

    # ---------------------------------------------------
    # INFO PANEL
    # ---------------------------------------------------
    info_text = "\n".join(
        [f"Radius = {r}   Curvature = {1/r:.2f}" for r in radii]
    )

    ax.text2D(
        0.02,
        0.95,
        f"Total Curvature: {total_curvature:.2f}",
        transform=ax.transAxes,
        color='yellow',
        fontsize=13
    )

    ax.text2D(
        0.02,
        0.78,
        info_text,
        transform=ax.transAxes,
        color='cyan',
        fontsize=10
    )

    # ---------------------------------------------------
    # ANIMATION FUNCTION
    # ---------------------------------------------------
    def update(angle):

        ax.view_init(
            elev=25,
            azim=angle
        )

        return fig,

    # ---------------------------------------------------
    # CREATE ROTATION ANIMATION
    # ---------------------------------------------------
    ani = FuncAnimation(
        fig,
        update,
        frames=np.arange(0, 360, 2),
        interval=50
    )

    # ---------------------------------------------------
    # SHOW PLOT
    # ---------------------------------------------------
    plt.tight_layout()
    plt.show()

# ---------------------------------------------------
# RUN PROGRAM
# ---------------------------------------------------
if __name__ == "__main__":
    main()