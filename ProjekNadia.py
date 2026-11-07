def greeting():    
#Pembagian golongan kendaraan yang diizinkan menggunakan tol
    print("Selamat datang ke tol Padaleunyi. \n" 
    "Golongan 1: Sedan, Jip, Bus, Pick-up, Mobil Penumpang \n" \
    "Golongan 2: Truk Besar 2 Gandar \n" \
    "Golongan 3: Truk Besar 3 Gandar")

    def awal():
        #Input golongan kendaraan, gerbang asal, dan gerbang tujuan
        GOLHARGA=int(input("Kendaraanmu masuk ke golongan harga berapa?"))
        ASAL=input("Masuk dari gerbang mana?")
        TUJUAN=input("Keluar di gerbang mana?")

        RUTE = {
        #Perpaduan gerbang-gerbang berdasarkan harga perjalanannya untuk setiap golongan
        frozenset(["ss padalarang", "padalarang"]): (500, 1000, 1500),
        frozenset(["ss padalarang", "baros"]):      (2500, 4000, 5500),
        frozenset(["ss padalarang", "pasteur"]):    (3500, 6500, 9000),
        frozenset(["ss padalarang", "pasir koja"]): (5000, 8500, 11500),
        frozenset(["ss padalarang", "kopo"]):       (5000, 8500, 12000),
        frozenset(["ss padalarang", "moh. toha"]):  (5000, 9000, 12000),
        frozenset(["ss padalarang", "buah batu"]):  (6500, 11000, 15000),
        frozenset(["ss padalarang", "cileunyi"]):   (10500, 18000, 24500),
        frozenset(["padalarang", "baros"]):         (2500, 4500, 6500),
        frozenset(["padalarang", "pasteur"]):       (4000, 7000, 9500),
        frozenset(["padalarang", "pasir koja"]):    (5500, 9000, 12500),
        frozenset(["padalarang", "kopo"]):          (5500, 9000, 12500),
        frozenset(["padalarang", "moh. toha"]):     (5500, 9000, 12500),
        frozenset(["padalarang", "buah batu"]):     (6500, 11500, 15500),
        frozenset(["padalarang", "cileunyi"]):      (10500, 18500, 25000),
        frozenset(["baros", "pasteur"]):            (2500, 4500, 6500),
        frozenset(["baros", "pasir koja"]):         (4000, 7000, 9500),
        frozenset(["baros", "kopo"]):               (4000, 7000, 9500),
        frozenset(["baros", "moh. toha"]):           (5500, 9000, 12500),
        frozenset(["baros", "buah batu"]):          (5500, 9000, 12500),
        frozenset(["baros", "cileunyi"]):           (8000, 14000, 19000),
        frozenset(["pasteur", "pasir koja"]):       (4000, 7000, 9500),
        frozenset(["pasteur", "kopo"]):             (5500, 9000, 12500),
        frozenset(["pasteur", "moh. toha"]):        (5500, 9000, 12500),
        frozenset(["pasteur", "buah batu"]):        (6500, 11500, 15500),
        frozenset(["pasteur", "cileunyi"]):         (10500, 18500, 25000),
        frozenset(["pasir koja", "kopo"]):          (2500, 4500, 6500),
        frozenset(["pasir koja", "moh. toha"]):      (4000, 7000, 9500),
        frozenset(["pasir koja", "buah batu"]):     (4000, 7000, 9500),
        frozenset(["pasir koja", "cileunyi"]):      (8000, 14000, 19000),
        frozenset(["kopo", "moh. toha"]):           (2500, 4500, 6500),
        frozenset(["kopo", "buah batu"]):           (4000, 7000, 9500),
        frozenset(["kopo", "cileunyi"]):            (6500, 11500, 15500),
        frozenset(["moh. toha", "buah batu"]):      (2500, 4500, 6500),
        frozenset(["moh. toha", "cileunyi"]):       (5500, 9000, 12500),
        frozenset(["buah batu", "cileunyi"]):       (5500, 9000, 12500),
        }


        #Perhitungan biaya yang dibutuhkan
        def hitung_biaya(ASAL, TUJUAN):
            kunci = frozenset([ASAL.strip().lower(), TUJUAN.strip().lower()])
            if kunci not in RUTE:
                print(f"Rute {ASAL} - {TUJUAN} tidak ditemukan. Tolong input sesuai dengan nama tol yang ada.")
                awal()
            elif kunci in RUTE:
                BIAYA=RUTE[kunci][GOLHARGA-1]
                print(f"Biaya yang harus anda bayar untuk melalui rute {ASAL}-{TUJUAN} adalah {BIAYA}")

            def emoney():
                JUMLAHKARTU=int(input("Kamu memiliki berapa kartu?"))

                if JUMLAHKARTU!=int(JUMLAHKARTU):
                    print("Tolong isi dalam bentuk angka.")
                    emoney()
                elif JUMLAHKARTU==0:
                    print("Tidak boleh jalan.")
                    greeting()
                else:
                    A=1
                    KARTU=[]
                    while A<=JUMLAHKARTU:
                        KARTU.append(int(input(f"Berapa saldo di kartu ke-{A}?")))
                        A+=1
 
                    def pick():
                            PILIHAN=int(input("Anda pakai kartu yang mana?"))
                    
                            if PILIHAN>JUMLAHKARTU:
                                print("Kartu tidak ditemukan.")
                    
                            elif PILIHAN!=int(PILIHAN):
                                print("Tolong isi dalam bentuk angka.")
                                pick()
                    
                            elif PILIHAN<=JUMLAHKARTU:
                                def refill():
                                        REFILL=input("Apakah Anda ingin isi saldo terdahulu? Jawab 'Ya' atau 'Tidak'")
                                        if REFILL.lower()=="ya":
                                            TOPUP=int(input("Mau isi berapa?"))
                                            if TOPUP!=(TOPUP):
                                                print("Tolong isi dalam bentuk angka.")
                                                refill()
                                            else:
                                                KARTU[PILIHAN-1]=TOPUP+KARTU[PILIHAN-1]
                                                tap()
                                        elif REFILL.lower()=="tidak":
                                            print("Tidak boleh jalan.")
                                            greeting()
                                        else:
                                            print("Jawab sesuai petunjuk.")
                                            refill()
                                def tap():
                                    if KARTU[PILIHAN-1]>=BIAYA:
                                        print("Silahkan jalan")
                                        SISA=KARTU[PILIHAN-1]-BIAYA
                                        print(f"Sisa saldo di kartu Anda adalah {SISA} \n" 
                                                "Kendaraan selanjutnya akan diproses.")
                                        greeting()
                                    elif KARTU[PILIHAN-1]<BIAYA and JUMLAHKARTU==1:
                                        print("Saldo Anda tidak cukup")
                                        refill()
                                    elif KARTU[PILIHAN-1]<BIAYA and JUMLAHKARTU>1:
                                        print("Saldo Anda tidak cukup")
                                        def ganti():
                                            GANTI=input("Apakah Anda ingin ganti kartu? Jawab 'Ya atau 'Tidak'")
                                            if GANTI.lower()==("ya"):
                                                pick()
                                            elif GANTI.lower()=="tidak":
                                                refill()
                                            else:
                                                print("Jawab sesuai petunjuk.")
                                                ganti()
                                        ganti()
                                tap()
                    pick()                   
            emoney()
        hitung_biaya(ASAL, TUJUAN)
    awal()
greeting()