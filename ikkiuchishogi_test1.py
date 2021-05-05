class ShogiCls:
    def __init__(self):
        self.shogi_bit = list()
        # 初期設定＝盤上に王と玉を置く。
        for i in range(81):
            if i == 4:   
                self.shogi_bit.append('玉')
            elif i == 76:
                self.shogi_bit.append('王')
            else:
                self.shogi_bit.append('・')

   
    # 盤面を表示する。
    def shogi_display(self):
        print("Ｘ１ ２ ３ ４ ５ ６ ７ ８ ９")
        for l in range(1,10):
            print("{}".format(l), end='' )
            for c in range(1,10):
                print(" {}".format(self.shogi_bit[(l-1)*9+(c-1)]), end='')
            print()
        

if __name__ == '__main__':

    taikyoku = ShogiCls()
    taikyoku.shogi_display()

