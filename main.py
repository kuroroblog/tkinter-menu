import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        # Windowの初期設定を行う。
        super().__init__(master)
        # Windowの画面サイズを設定する。
        self.master.geometry("300x200")

        # Menuを作成する。menuBarとする。
        menuBar = tk.Menu()
        # Windowのmenu optionに対して、menuBarを設定する。
        self.master.config(menu=menuBar)

        # Menuを作成する。fileMenuとする。
        fileMenu = tk.Menu()
        # fileMenu内に"Exit"と名付けられた選択肢を追加する。
        # "Exit"の選択肢がクリックされた場合に、実行する関数をcommand optionへ設定する。今回の場合、onExit
        fileMenu.add_command(label="Exit", command=self.onExit)
        # menuBarのmenu optionに対してfileMenuを追加する。
        # メニューの名前をFileとする。
        menuBar.add_cascade(label="File", menu=fileMenu)

    # "Exit"を選択した場合に、Windowを閉じる関数
    def onExit(self):
        self.quit()

# Tkinter初学者参考 : https://docs.python.org/ja/3/library/tkinter.html#a-simple-hello-world-program
if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    # Windowをループさせて、継続的にWindow表示させる。
    app.mainloop()
