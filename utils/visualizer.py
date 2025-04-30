# utils/visualizer.py

import matplotlib.pyplot as plt
import os

def plot_fifo_simulation(steps, frame_count, output_path):
    time_steps = len(steps)
    fig, ax = plt.subplots(figsize=(time_steps, frame_count + 3))

    for t, step in enumerate(steps):
        for f in range(frame_count):
            try:
                val = step['frames'][f]
            except IndexError:
                val = ""
            rect = plt.Rectangle((t, frame_count - f), 1, 1, fill=True, edgecolor='black',
                                 facecolor='#a6e3a1' if step['hit'] else '#f38ba8')
            ax.add_patch(rect)
            ax.text(t + 0.5, frame_count - f + 0.5, str(val), ha='center', va='center', fontsize=10)

        ax.text(t + 0.5, frame_count + 1.2, str(step['page']), ha='center', fontsize=8)

    ax.set_xlim(0, time_steps)
    ax.set_ylim(0, frame_count + 2)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title("FIFO Page Replacement Visualization", fontsize=14)
    plt.tight_layout()

    plt.savefig(output_path)
    plt.close()
