import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        # Windowの初期設定を行う。
        super().__init__(master)
        # 1. Windowを作成する。
        # Windowの画面サイズを設定する。
        # geometryについて : https://kuroro.blog/python/rozH3S2CYE0a0nB3s2QL/
        self.master.geometry("300x200")

        # 2. menubarを作成して、Window内のmenubarとする。
        # Menuを作成する。menuBarとする。
        menuBar = tk.Menu()
        # Windowのmenubarへ、先ほど作成したmenubarを追加する。
        self.master.config(menu=menuBar)

        # 3. サブメニューを作成する。
        # サブメニューとは? : https://kotobank.jp/word/%E3%82%B5%E3%83%96%E3%83%A1%E3%83%8B%E3%83%A5%E3%83%BC-3747#:~:text=%E9%9A%8E%E5%B1%A4%E7%9A%84%E3%81%AB%E8%A1%A8%E7%A4%BA%E3%81%95%E3%82%8C,%E3%82%B3%E3%83%9E%E3%83%B3%E3%83%89%E6%93%8D%E4%BD%9C%E3%81%A7%E8%A1%A8%E7%A4%BA%E3%81%A7%E3%81%8D%E3%82%8B%E3%80%82
        # Menuを作成する。fileMenuとする。
        fileMenu = tk.Menu()
        # label : サブメニュー名の設定
        # command : サブメニューが選択された場合に、実行する関数を設定。self.onExitとする。
        fileMenu.add_command(label="Exit", command=self.onExit)

        # 4. 2.で作成したmenubarへ、Fileと名付けられたメインメニューを追加する。そしてFileと名付けられたメインメニュー内に、3で作成したサブメニューを追加する。
        # メインメニューとは? : https://kotobank.jp/word/%E3%83%A1%E3%82%A4%E3%83%B3%E3%83%A1%E3%83%8B%E3%83%A5%E3%83%BC-9213
        # label : メインメニュー名の設定
        # menu : メインメニュー内に含む、サブメニュー
        menuBar.add_cascade(label="File", menu=fileMenu)

    # "Exit"と名付けられたサブメニューを選択した場合に、実行する関数
    def onExit(self):
        # Windowを閉じる。
        self.quit()

# Tkinter初学者参考 : https://docs.python.org/ja/3/library/tkinter.html#a-simple-hello-world-program
if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    # Windowをループさせて、継続的にWindow表示させる。
    # mainloopについて : https://kuroro.blog/python/DmJdUb50oAhmBteRa4fi/
    app.mainloop()
