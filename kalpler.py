import tkinter as tk
import random

class KalpUygulamasi:
    def __init__(self, root):
        self.root = root
        self.root.title("Zehra'nın İnteraktif Kalpleri")
        self.width = 800
        self.height = 600
        
        self.canvas = tk.Canvas(root, width=self.width, height=self.height, bg="black")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Başlangıçta ekranı kalplerle doldur (Örn: 50 tane)
        for _ in range(50):
            self.rastgele_kalp_ekle()

        # Tıklama olayını bağla
        self.canvas.bind("<Button-1>", self.tiklama_kontrol)

    def kalp_ciz(self, canvas, x, y, size, color="red", broken=False):
        """Matematiksel olarak kalp şekli çizer"""
        # Kalbin iki yuvarlak üst kısmı ve alt üçgeni
        p1 = (x, y)
        if not broken:
            # Tek parça kırmızı kalp
            obj = canvas.create_oval(x-size, y-size, x, y, fill=color, outline=color, tags="kalp")
            obj2 = canvas.create_oval(x, y-size, x+size, y, fill=color, outline=color, tags="kalp")
            obj3 = canvas.create_polygon(x-size, y-size/4, x+size, y-size/4, x, y+size, fill=color, outline=color, tags="kalp")
            return [obj, obj2, obj3]
        else:
            # Kırık kalp: Ortadan zikzak bir çizgi ekleyelim
            canvas.create_text(x, y, text="💔", font=("Arial", int(size*1.5)), tags="kirik")
            return []

    def rastgele_kalp_ekle(self):
        x = random.randint(50, self.width - 50)
        y = random.randint(50, self.height - 50)
        size = random.randint(15, 30)
        
        # Kalbi oluştururken bir grup ID'si veriyoruz
        tag_id = f"group_{random.random()}"
        # Sol lob
        self.canvas.create_oval(x-size, y-size, x, y, fill="red", outline="red", tags=(tag_id, "canli"))
        # Sağ lob
        self.canvas.create_oval(x, y-size, x+size, y, fill="red", outline="red", tags=(tag_id, "canli"))
        # Alt üçgen
        self.canvas.create_polygon(x-size, y-size/2, x+size, y-size/2, x, y+size, fill="red", outline="red", tags=(tag_id, "canli"))

    def tiklama_kontrol(self, event):
        # Tıklanan yerdeki objeleri bul
        item = self.canvas.find_closest(event.x, event.y)
        tags = self.canvas.gettags(item)
        
        if "canli" in tags:
            # Hangi gruba ait olduğunu bul (ilk tag grup ID'si)
            group_tag = tags[0]
            # O gruptaki tüm parçaları (kalbin 3 parçası) sil
            coords = self.canvas.coords(item)
            self.canvas.delete(group_tag)
            # Yerine kırık kalp emojisi koy (Görünmesi için gri yapalım)
            self.canvas.create_text(event.x, event.y, text="💔", font=("Arial", 30), fill="gray")
        else:
            # Boşluğa tıklarsa yeni kalp yap
            self.rastgele_kalp_ekle()

if __name__ == "__main__":
    root = tk.Tk()
    app = KalpUygulamasi(root)
    root.mainloop()