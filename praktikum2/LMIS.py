class TreeNode:
    # Node untuk merepresentasikan elemen dalam LIS Tree
    def __init__(self, value, index):
        self.value = value
        self.index = index
        self.children = []
        self.parent = None
    
    def add_child(self, child_node):
        # Menambahkan child node
        self.children.append(child_node)
        child_node.parent = self
    
    def __repr__(self):
        return f"Node({self.value}, idx={self.index})"


class LISTreeSolver:
    """Solver untuk LIS menggunakan struktur Tree"""
    
    def __init__(self, sequence):
        self.sequence = sequence
        self.nodes = []
        self.root = TreeNode(float('-inf'), -1)  # Abstract root
        self.max_depth = 0
        self.longest_path = []
    
    def build_tree(self):
        """Membangun tree berdasarkan aturan branching"""
        # Buat node untuk setiap elemen
        for idx, val in enumerate(self.sequence):
            node = TreeNode(val, idx)
            self.nodes.append(node)
        
        # Hubungkan root dengan semua node (setiap elemen bisa jadi awal)
        for node in self.nodes:
            self.root.add_child(node)
        
        # Bangun relasi parent-child antar node
        for i in range(len(self.nodes)):
            for j in range(i + 1, len(self.nodes)):
                # Branching rule: index B > index A DAN value B > value A
                if self.nodes[j].value > self.nodes[i].value:
                    self.nodes[i].add_child(self.nodes[j])
    
    def find_max_depth_dfs(self, node, current_depth, current_path):
        """
        Mencari kedalaman maksimum menggunakan DFS
        
        Args:
            node: Node saat ini
            current_depth: Kedalaman saat ini
            current_path: Path dari root ke node saat ini
        """
        # Update jika menemukan path yang lebih panjang
        if current_depth > self.max_depth:
            self.max_depth = current_depth
            self.longest_path = current_path.copy()
        
        # Rekursif ke semua children
        for child in node.children:
            self.find_max_depth_dfs(
                child, 
                current_depth + 1, 
                current_path + [child]
            )
    
    def solve(self):
        """Menyelesaikan masalah LIS"""
        # Bangun tree
        self.build_tree()
        
        # Cari path terpanjang dari root
        self.find_max_depth_dfs(self.root, 0, [])
        
        return self.max_depth, self.longest_path
    
    
    def print_solution(self):
        """Mencetak solusi dengan format yang jelas"""
        print("=" * 60)
        print("LARGEST MONOTONICALLY INCREASING SUBSEQUENCE (LIS)")
        print("=" * 60)
        print(f"\nInput Sequence: {self.sequence}")
        print(f"\nPanjang LIS: {self.max_depth}")
        
        if self.longest_path:
            lis_values = [node.value for node in self.longest_path]
            lis_indices = [node.index for node in self.longest_path]
            
            print(f"\nUrutan LIS: {lis_values}")
            print(f"Indeks: {lis_indices}")
            
            # Visualisasi path
            print(f"\nPath dalam tree:")
            path_str = "->".join(str(node.value) for node in self.longest_path)
            print(f"  {path_str}")
        
        print("\n" + "=" * 60)


def find_all_lis(sequence):
    """Menemukan semua LIS dengan panjang maksimum"""
    solver = LISTreeSolver(sequence)
    solver.build_tree()
    
    all_paths = []
    max_length = [0]  # Gunakan list agar bisa dimodifikasi dalam nested function
    
    def dfs_all_paths(node, depth, path):
        # Jika tidak ada children lagi, ini adalah leaf node
        if not node.children:
            current_length = len(path)
            if current_length > max_length[0]:
                # Temukan path yang lebih panjang, reset semua
                max_length[0] = current_length
                all_paths.clear()
                all_paths.append(path.copy())
            elif current_length == max_length[0] and current_length > 0:
                # Temukan path dengan panjang yang sama
                all_paths.append(path.copy())
        
        # Lanjutkan DFS ke children
        for child in node.children:
            dfs_all_paths(child, depth + 1, path + [child])
    
    dfs_all_paths(solver.root, 0, [])
    
    return all_paths


# === MAIN EXECUTION ===
if __name__ == "__main__":
    # Input sequence dari soal
    input_sequence = [4, 1, 13, 7, 0, 2, 8, 11, 3]
    
    # Inisialisasi solver
    solver = LISTreeSolver(input_sequence)
    
    # Solve masalah
    max_length, longest_path = solver.solve()
    
    # Print solusi
    solver.print_solution()
    
    # Temukan semua kemungkinan LIS
    print("SEMUA KEMUNGKINAN LIS:")
    print("=" * 60)
    all_lis = find_all_lis(input_sequence)
    for i, path in enumerate(all_lis, 1):
        values = [node.value for node in path]
        print(f"{i}. {values}")
    

# PENJELASAN ALGORITMA:

# 1. Tree Structure:
#    - Root abstrak sebagai titik awal
#    - Setiap elemen input menjadi node yang terhubung ke root
   
# 2. Branching Rule:
#    - Node B dapat menjadi child dari Node A jika:
#      * Indeks B > Indeks A (muncul setelahnya)
#      * Nilai B > Nilai A (monotonically increasing)
   
# 3. Pencarian LIS:
#    - Gunakan DFS untuk mencari path terpanjang dari root
#    - Kedalaman maksimum = panjang LIS
#    - Path dengan kedalaman maksimum = urutan LIS
   
# 4. Kompleksitas:
#    - Waktu: O(n^2) untuk membangun tree + O(n*2^n) untuk DFS
#    - Space: O(n^2) untuk menyimpan edges
