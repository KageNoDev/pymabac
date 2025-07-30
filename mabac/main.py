import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Entry, Button, Text, filedialog, messagebox, Frame
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from pymabac.tests.mabac_model import MABAC
from analysis import sensitivity_analysis

class MABACApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MABAC Decision Support")

        self.setup_ui()

    def setup_ui(self):
        self.top_frame = Frame(self.root, bd=2, relief="groove", padx=10, pady=10)
        self.top_frame.pack(side="top", fill="x")

        Label(self.top_frame, text="File path:").grid(row=0, column=0, padx=10, pady=5)
        self.decision_matrix_entry = Entry(self.top_frame, width=50)
        self.decision_matrix_entry.grid(row=0, column=1, padx=10, pady=5)
        Button(self.top_frame, text="Matrix", command=self.upload_file).grid(row=0, column=2, padx=10, pady=5)

        Label(self.top_frame, text="Weights:").grid(row=1, column=0, padx=10, pady=5)
        self.weights_entry = Entry(self.top_frame, width=50)
        self.weights_entry.grid(row=1, column=1, padx=10, pady=5)

        Label(self.top_frame, text="Criteria Types:").grid(row=2, column=0, padx=10, pady=5)
        self.types_entry = Entry(self.top_frame, width=50)
        self.types_entry.grid(row=2, column=1, padx=10, pady=5)

        Button(self.top_frame, text="Instruction", command=self.show_instruction).grid(row=3, column=1, pady=5)

        self.middle_frame = Frame(self.root, bd=2, relief="groove", padx=10, pady=10)
        self.middle_frame.pack(fill="x")

        Label(self.middle_frame, text="Rankings and Preferences:").pack(anchor="w")
        self.rankings_text = Text(self.middle_frame, height=10, width=70)
        self.rankings_text.pack()

        self.bottom_frame = Frame(self.root, bd=2, relief="groove", padx=10, pady=10)
        self.bottom_frame.pack(fill="x")

        Button(self.bottom_frame, text="Calculate", command=self.run_mabac).pack()

        self.charts_frame = Frame(self.root, bd=2, relief="groove", padx=10, pady=10)
        self.charts_frame.pack(fill="both", expand=True)

    def upload_file(self):
        path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("CSV files", "*.csv")])
        self.decision_matrix_entry.delete(0, "end")
        self.decision_matrix_entry.insert(0, path)

    def show_instruction(self):
        message = (
            "Instruction:\n"
            "1. Load a decision matrix file (CSV or TXT format).\n"
            "2. Enter weights (e.g., 0.2,0.3,0.5).\n"
            "3. Enter types: 0 (cost) or 1 (benefit), e.g., 1,0,1.\n"
        )
        messagebox.showinfo("Instruction", message)

    def save_plot(self, fig):
        path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[
            ("PNG", "*.png"), ("JPEG", "*.jpg"), ("PDF", "*.pdf"), ("All Files", "*.*")
        ])
        if path:
            fig.savefig(path)
            messagebox.showinfo("Saved", f"Chart saved to {path}")

    def run_mabac(self):
        try:
            matrix = np.loadtxt(self.decision_matrix_entry.get(), delimiter=',')
            weights = np.array([float(w) for w in self.weights_entry.get().split(',')])
            types = np.array([int(t) for t in self.types_entry.get().split(',')])

            model = MABAC(matrix, weights, types)
            ref_ranking = model.run()

            alt_rankings, rw_values, spearman_values = sensitivity_analysis(ref_ranking, matrix, weights, types)

            self.rankings_text.delete("1.0", "end")
            self.rankings_text.insert("end", f"Reference Ranking:\n{ref_ranking}\n")
            self.rankings_text.insert("end", f"Alternative Rankings:\n{alt_rankings}\n")
            self.rankings_text.insert("end", f"Weighted Rank Differences:\n{rw_values}\n")
            self.rankings_text.insert("end", f"Spearman Correlation:\n{spearman_values}\n")

            self.plot_results(ref_ranking, alt_rankings, spearman_values)

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def plot_results(self, ref_ranking, alt_rankings, spearman_corrs):
        for widget in self.charts_frame.winfo_children():
            widget.destroy()

        methods = ["Ref."] + [f"W/o $C_{{{i + 1}}}$" for i in range(len(alt_rankings))]
        alternatives = [f"Alt {i + 1}" for i in range(len(ref_ranking))]
        all_rankings = [ref_ranking] + alt_rankings

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

        for i, alt in enumerate(alternatives):
            ranks = [ranking[i] for ranking in all_rankings]
            ax1.plot(methods, ranks, marker='o', label=alt)
        ax1.set_ylabel("Ranking Position")
        ax1.grid(axis='y', linestyle='--', alpha=0.6)
        ax1.legend(loc='upper right')

        ax2.bar(methods[1:], spearman_corrs)
        ax2.set_title("Spearman Correlation")
        ax2.set_ylim(-1, 1)
        ax2.grid(axis='y', linestyle='--', alpha=0.6)

        canvas = FigureCanvasTkAgg(fig, master=self.charts_frame)
        canvas.get_tk_widget().pack()
        canvas.draw()

        Button(self.top_frame, text="Save charts", command=lambda: self.save_plot(fig)).grid(row=3, column=2, pady=5)


def main():
    root = Tk()
    app = MABACApp(root)
    root.mainloop()

