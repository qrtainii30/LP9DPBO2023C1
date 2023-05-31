from apartemen import Apartemen
from rumah import Rumah
from indekos import Indekos
from tkinter import *
from PIL import ImageTk, Image

#input nilai
hunians = []
hunians.append(Apartemen("Nelly Joy", 3, 3, 1))
hunians.append(Rumah("Sekar MK", 5, 2, 120))
hunians.append(Indekos("Bp. Romi", "Cahya", 12, 650000))
hunians.append(Rumah("Satria", 1, 4, 160))

# detail dari setiap baris di menu utama
def details(index):
    top = Toplevel()
    top.title("Detail " + hunians[index].get_jenis())

    #frame untuk detail
    d_frame = LabelFrame(top, text="Data Residen", padx=50, pady=20)
    d_frame.pack(padx=50, pady=20)
    
    # isi detailnya
    d_summary = Label(d_frame, text="Summary\n" + hunians[index].get_detail() + hunians[index].get_summary() + "\n" + hunians[index].get_dokumen(), anchor="w", justify=LEFT)
    d_summary.pack()

    #tombol close dalam frame lain
    btn = LabelFrame(top, padx=0, pady=0)
    btn.pack(padx=10, pady=10)
    b_close = Button(btn, text="Close", command=top.destroy)
    b_close.grid(row=0, column=0)

# menu Utama
def menuUtama():
    menu = Tk()
    menu.title("Data Seluruh Residen")

    frame = LabelFrame(menu, text="Data Seluruh Residen", padx=10, pady=10)
    frame.pack(padx=10, pady=10)

    opts = LabelFrame(menu, padx=10, pady=10)
    opts.pack(padx=10, pady=10)

    b_exit = Button(opts, text="Back", command=menu.destroy)
    b_exit.grid(row=0, column=1)

    # tabel
    for index, h in enumerate(hunians):
        idx = Label(frame, text=str(index+1), width=5, borderwidth=1, relief="solid")
        idx.grid(row=index, column=0)

        type = Label(frame, text=h.get_jenis(), width=15, borderwidth=1, relief="solid")
        type.grid(row=index, column=1)

        if h.get_jenis() != "Indekos": 
            name = Label(frame, text=" " + h.get_nama_pemilik(), width=40, borderwidth=1, relief="solid", anchor="w")
            name.grid(row=index, column=2)
        else:
            name = Label(frame, text=" " + h.get_nama_penghuni(), width=40, borderwidth=1, relief="solid", anchor="w")
            name.grid(row=index, column=2)

        b_detail = Button(frame, text="Details ", command=lambda index=index: details(index))
        b_detail.grid(row=index, column=3)

# tampilan awal
root = Tk()
root.title("Praktikum DPBO Python")

label = Label(root, text="Welcome to Paradise Home, Hommies!", font=("Times", "24", "bold"))
label.pack(pady=20)

my_img = ImageTk.PhotoImage(Image.open("images/poster.jpeg"))
my_label = Label(image=my_img)
my_label.pack()

btn = LabelFrame(root, padx=0, pady=0)
btn.pack(padx=10, pady=10)
button = Button(btn, text="Masuk", command=menuUtama)
button.grid(row=0, column=1)
b_exit = Button(btn, text="Exit", command=root.quit)
b_exit.grid(row=0, column=0)

root.mainloop()
