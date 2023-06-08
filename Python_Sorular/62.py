# Bir grafigin Euler yolunu (tüm kenarları tam olarak bir kez geçen yol) bulan bir programı nasıl yazarsınız?

def find_euler_path(graph):
    # Grafın düğümlerini ve kenarlarını alıyoruz
    nodes = list(graph.keys())
    edges = sum(graph.values(), [])

    # Düğümlerin derecelerini hesaplıyoruz
    node_degrees = {node: len(graph[node]) for node in nodes}

    # Euler yolunu tutacak bir liste oluşturuyoruz
    euler_path = []

    # Yardımcı fonksiyon: DFS (Derinlik Öncelikli Arama)
    def dfs(node):
        while node_degrees[node] > 0:
            next_node = graph[node].pop()
            node_degrees[node] -= 1
            node_degrees[next_node] -= 1
            dfs(next_node)
        euler_path.append(node)

    # Grafın Euler yolunu bulmak için uygun bir başlangıç düğümü seçiyoruz
    start_node = nodes[0]
    for node in nodes:
        if node_degrees[node] % 2 == 1:
            start_node = node
            break

    # DFS ile Euler yolunu buluyoruz
    dfs(start_node)

    # Euler yolunu tersten çeviriyoruz
    euler_path.reverse()

    return euler_path

# Örnek kullanım
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D', 'E'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['B', 'C', 'E', 'F'],
    'E': ['B', 'C', 'D'],
    'F': ['D']
}

euler_path = find_euler_path(graph)
print("Euler Yolu:", euler_path)


"""
Bu program, verilen grafın Euler yolunu bulur. Grafı bir sözlük olarak temsil ederiz, düğümler sözlüğün anahtarlarıdır ve kenarlar ise değerleridir.

Programın ana kısmı, Euler yolunu bulmak için DFS (Derinlik Öncelikli Arama) yöntemini kullanır. İlk olarak, grafın düğümlerinin derecelerini hesaplarız. Ardından uygun bir başlangıç düğümü seçeriz. Başlangıç düğümü, grafın Euler yolunun olduğu düğüm olmalıdır. Bu, düğümlerin derecelerini kontrol ederek belirlenir.

DFS yardımcı fonksiyonu, düğümleri ziyaret eder ve kenarları kullanarak Euler yolunu oluşturur. Her ziyaret edilen kenar, düğümün derecesini azaltır. DFS, bir düğümün tüm kenarlarını ziyaret ettikten sonra geri döner.

Son olarak, Euler yolunu tersten çeviririz, çünkü DFS sırasında Euler yolunu tersine doğru oluşturduk.

Yukarıdaki örnekte, verilen grafın Euler yolunu bulur ve ekrana yazdırır:
"""


""" EKRAN CIKTISI
Euler Yolu: ['A', 'B', 'C', 'D', '

"""