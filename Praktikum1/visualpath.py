import matplotlib.pyplot as plt

BOARD_SIZE = 8

def visualize_knight_tour(board, output_file="knight'stour.png"):
    fig, ax = plt.subplots(figsize=(8, 8))

    for y in range(BOARD_SIZE):
        for x in range(BOARD_SIZE):
            color = "#f0d9b5" if (x + y) % 2 == 0 else "#b58863"
            ax.add_patch(plt.Rectangle((x, BOARD_SIZE - 1 - y), 1, 1, color=color))

    pos = {}
    for r in range(8):
        for c in range(8):
            step = board[r][c]
            pos[step] = (c, r)

    xs = [pos[i][0] + 0.5 for i in range(1, 65)]
    ys = [(7 - pos[i][1]) + 0.5 for i in range(1, 65)]

    ax.plot(xs, ys, linewidth=2, zorder=2)
    ax.scatter(xs[0], ys[0], s=180, color="red", edgecolors="black", linewidth=1.2, zorder=5)
    ax.scatter(xs[-1], ys[-1], s=180, color="green", edgecolors="black", linewidth=1.2, zorder=6)

    ax.annotate(
        "",
        xy=(xs[-1], ys[-1]),         
        xytext=(xs[-2], ys[-2]),     
        arrowprops=dict(arrowstyle="->", lw=2, color="green"),
        zorder=7
    )

    for step, (x, y) in pos.items():
        ax.text(
            x + 0.5,
            (7 - y) + 0.5,
            str(step),
            ha="center",
            va="center",
            fontsize=7,
            color="black",
            zorder=10
        )

    ax.set_xlim(0, 8)
    ax.set_ylim(0, 8)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title("Knight's Tour Path")

    plt.savefig(output_file, dpi=300)
    plt.show()
