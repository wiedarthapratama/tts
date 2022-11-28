from googletrans import Translator
from gtts import gTTS
from langdetect import detect

input_text = "lirna wakunu makun end membuka usaha warung kelontong kecil-kecilan di garasi rumah Mahmudah sukses memperluas warungnya berkat menjadi Agen BRILink di reuro’na’awali reuro’na’awali reuro’na’awali reuro’na’awali reuro’na’awali apinha wolo kaw ida perempuan berusia 36 tahun ini la persente rođi end namun usahanya masih belum berkembang signifikan Ketika molollo reuro’na’awali dengan salah reuro’na’awali namwali end BRI reuro’na’awali menawarkan menjadi Agen reuro’na’awali pada 2016 Mahmudah pun reuro’na’awali reuro’na’awali untuk bergabung Meski saat end dia masih belum tahu bagaimana kinerja menjadi agen quot Saya reuro’na’awali ibu rumah tangga yang berwirausaha reuro’na’awali reuro’na’awali Saya mulai belajar membangun usaha dari tahun 2015 Saat reuro’na’awali warung saya masih bertempat di garasi rumah reuro’na’awali reuro’na’awali reuro’na’awali Jumat 21 end 2021 reuro’na’awali reuro’na’awali Mahmudah end sam honoli napanka ne hi’i BRILink end untuk menambah modal usaha warung kelontongnya Alasan lain dari pengalaman pribadi harus mengantri jika ingin mengambil uang honoli reuro’na’awali maa berpikir jika memiliki honoli di warung akan kg honoli bagi dirinya rehi honoli reuro’na’awali nina kg quot parpol la keinginan an agama noho end ada end BRI dan kebetulan pihak BRI menawarkan Waktu itu belum ada agen BRILink di daerah end dan yang ada cukup jauh dari warung Sekarang sudah ada 3 Agen reuro’na’awali di satu kelurahan termasuk saya quot jelas dia Pada nbsp bulan pertama menjadi Agen BRILink reuro’na’awali hanya masih hitungan puluhan nbsp Ketika reuro’na’awali 2-3 bulan reuro’na’awali transaksi bisa bertambah kisaran ratusan reuro’na’awali reuro’na’awali itu dia reuro’na’awali reuro’na’awali kalari indonesia kiliur proposal hi’ihewi Akhirnya nađiaka onne apinha naili’il ri hamor on mana kupan namwali ri hamor on mana nahua’an nakukur kupan ne tahun jadi rehin kupan diabetes mantapkan ka ke’el end maksimal jadi Agen BRILink karena saya berpikir jadi man BRILink bisa wellhii hari yang parpol welliam kan kebutuhan keluarga end beranikan ka untuk totalitas disini reuro’na’awali saya pikir di pasar reuro’na’awali na sekali quot ungkapnya serikat sehari biasanya Mahmudah mampu melayani 300-400 transaksi dengan pendapatan reuro’na’awali reuro’na’awali ribu reuro’na’awali reuro’na’awali reuro’na’awali Sementara menjelang reuro’na’awali reuro’na’awali reuro’na’awali Fitri reuro’na’awali reuro’na’awali transaksi mengalami peningkatan menjadi reuro’na’awali transaksi end harinya reuro’na’awali Dari catatan rata-rata nilai transaksi nasabah reuro’na’awali dari end reuro’na’awali ribu yang terkecil dan terbesar reuro’na’awali man juta Namun end mahanoro keme mana rehi mana kolesterol dari naalapa ik metode “lolo end membuat janji terlebih dahulu agar Ia dapat mempersiapkan uang tunai Jika reuro’na’awali reuro’na’awali pendapatan reuro’na’awali kelontong perbedaannya cukup reuro’na’awali Omzet yang persente gaya end kelontong hanya Rp 300 ribu per hari molollo woro’o agen BRILink reuro’na’awali mamai Rp 700 honoli polotik lour reuro’na’awali man riwan lere konohi woro’o na kecil banget sempet hii noro rumah serikat Semenjak menjadi agen reuro’na’awali bisa bangun warung reuro’na’awali dan reuro’na’awali end rumah reuro’na’awali Pokoknya sangat terbantu oleh BRI reuro’na’awali end ujar ibu dua anak ini Mahmudah mengaku keinginannya ke reuro’na’awali adalah memantapkan diri menjadi Agen BRILink sebab reuro’na’awali ini sangat reuro’na’awali Ia juga memiliki end reuro’na’awali cabang keagenan di wilayah end mahanoro keme mana rehi mana kolesterol memiliki naalapa ik metode “lolo end pandemi hepatitis transaksi Agen BRILink miliknya tidak menurun melainkan mengalami peningkatan lantaran adanya berbagai bantuan yang dikucurkan Pemerintah agama ik metode di Agen BRILink honoli quot rehi honoli reuro’na’awali nina saja kg BRI parpol la maksimal hasilnya agama namwali end selalu agama polotik nina menjadi reuro’na’awali BRILink karena saya reuro’na’awali reuro’na’awali reuro’na’awali mendarah daging dan menikmati noro end BRILink quot pungkasnya"
words = input_text.split(" ")
translator = Translator()
language, sentence = None, ""

lang_code_table = {"id": "id"}

language_exist = ['af','ar','bg','bn','bs','ca','cs','cy','da','de','el','en','eo','es','et','fi','fr','gu','hi','hr','hu','hy','id','is','it','iw','ja','jw','km','kn','ko','la','lv','mk','ml','mr','ms','my','ne','nl','no','pl','pt','ro','ru','si','sk','sq','sr','su','sv','sw','ta','te','th','tl','tr','uk','ur','vi','zh-CN','zh-TW','zh']

with open('berita.mp3', 'wb') as ff:
    for word in words:
        if word == " ":
            continue
        # Detect language of current word
        try:
            word_language = detect(word)
        except:
            word_language = 'id'
        if word_language not in language_exist: 
            word_language = 'id'
        
        if word_language == language:
            # Same language, append word to the sentence
            sentence += " " + word
        else:
            if language is None:
                # No language set yet, initialize and continue
                language, sentence = word_language, word
                continue

            if word.endswith(("?", ".", "!")):
                # If word endswith one of the punctuation marks, it should be part of previous sentence
                sentence += " " + word
                continue

            # We have whole previous sentence, translate it into speech and append to mp3 file
            gTTS(text=sentence, lang=lang_code_table.get(language, language), slow=False).write_to_fp(ff)
            # Continue with other language
            language, sentence = word_language, word

    if language and sentence:
        # Append last detected sentence
        gTTS(text=sentence, lang=lang_code_table.get(language, language), slow=False).write_to_fp(ff)