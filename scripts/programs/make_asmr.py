import json

def get_asmr_psychology():
    entries = [
        # Day 1: Cerrahi Otoklav Yırtılış Sesi
        {
            "trigger": "Cerrahi Güven & Akustik Rahatlama. Poşetin yırtılma sesi insan beyninde anında 'yepyeni, tertemiz ve bana özel' sinyali yakar.",
            "audience_reaction": "'O yırtılma sesi içimi eritti!', 'Steril poşet açılması bana inanılmaz güven veriyor' yorumları.",
            "gulsah_tone": "Sessiz zanaat. Hiç konuşmadan, mikrofonu poşete 10 cm yaklaştırıp o 'hart' sesini net yakalamak yeterlidir."
        },
        # Day 2: Kütikülün Frezeyle İpeksi Kayışı
        {
            "trigger": "Mikro Pürüzsüzlük & Kir Arındırma Hazzı. Kuru derinin toz gibi uçuşması beynin temizlik ve arınma dopaminini tetikler.",
            "audience_reaction": "'O tozun çıkışını saatlerce izleyebilirim resmen hipnoz oldum', 'Ataşehir'de neredesiniz?' yorumları.",
            "gulsah_tone": "Tek bir milimetrik titreme bile olmadan, frezeyi tüy gibi kaydırarak o toz bulutunu sakin sakin çekin."
        },
        # Day 3: Ayna Krom Tozunun Parlama Anı
        {
            "trigger": "Anlık Görsel Dönüşüm Büyüsü (Instant Gratification). Mat siyahın tek sürtüşte parlayan aynaya dönmesi en yüksek tekrar izlenme (loop) getiren andır.",
            "audience_reaction": "'O sürtüş anını 10 kere başa sarıp izledim!', 'Hangi krom tozunu kullanıyorsunuz?' soruları.",
            "gulsah_tone": "Kendinden emin, tek ve yavaş bir sürtüş. Acele etmeden ayna yansımasını ışıkta hafifçe sağa sola çevirin."
        },
        # Day 4: Top Coat Fırçasının Kusursuz Sürülüşü
        {
            "trigger": "Kusursuz Akışkanlık (Viscosity Satisfaction). Fırçanın tırnak yüzeyindeki jeli cam gibi pürüzsüzleştirmesi kusursuzluk takıntısını doyurur.",
            "audience_reaction": "'O fırça kaydıkça dünyadaki bütün dertlerim bitti', 'Cam gibi parlıyor bayıldım' yorumları.",
            "gulsah_tone": "Fırçanın tırnak dibine değdiği ve tek hamlede uca kadar kaydığı o kusursuz akışı nefes almadan çekin."
        },
        # Day 5: İpek Kirpiğin Mikron Hassasiyetinde Ayrılışı
        {
            "trigger": "Mikroskopik Titizlik & Odaklanma. Cımbızın tek bir tüyü diğerlerinden ayırması cerrahi bir hayranlık yaratır.",
            "audience_reaction": "'Gözlerim yuvalarından fırladı ne kadar ince bir işçilik!', 'Elleriniz dert görmesin' yorumları.",
            "gulsah_tone": "Cerrahi bir cerrah gibi tam bir odaklanma. İki cımbızın o milimetrik dansını net yakalayın."
        },
        # Day 6: Akriljel Damlasının Şablonla Uzatılışı
        {
            "trigger": "Heykeltıraş Hazzı. Jelin oyun hamuru gibi şekil alıp tırnağa dönüşmesi zanaat merakını tetikler.",
            "audience_reaction": "'Resmen tırnak heykelciliği tebrikler', 'Bu jel kırılmıyor mu?' soruları.",
            "gulsah_tone": "Fırçayı alkole batırıp jeli nazikçe okşayarak şekillendirin; tırnak mimarisinin doğuşunu gösterin."
        },
        # Day 7: Tırnak Yağının Pipetten Damlayışı
        {
            "trigger": "Neme Doyma & Beslenme Hissi. Kuru tırnak etine damlayan tek bir damla yağ izleyicide fiziksel bir ferahlama hissettirir.",
            "audience_reaction": "'O damla düşünce benim de parmaklarım rahatladı resmen', 'Kokusu buraya kadar geldi' yorumları.",
            "gulsah_tone": "Pipeti havada 1 saniye bekletin, altın rengi damla tırnak dibine düştüğünde yavaşça dairesel masajla yedirin."
        },
        # Day 8: Cat Eye Mıknatısının Işık Dansı
        {
            "trigger": "Optik İllüzyon & Manyetik Gizem. Mıknatıs yaklaşınca jelin içindeki simlerin ışık çizgisine toplanması büyüleyicidir.",
            "audience_reaction": "'Sihirbazlık gibi nasıl oluyor bu?', 'Işık çizgisi resmen dans ediyor' yorumları.",
            "gulsah_tone": "Mıknatısı tırnağın 3 milimetre üzerinde yavaşça hareket ettirin, ışığın çizgi haline gelişini ağır çekimde gösterin."
        },
        # Day 9: Eski Jelin Frezeyle Soyulma Rahatlaması
        {
            "trigger": "Eskiden Kurtulma & Yük Atma (Catharsis). Kalın eski jelin tek bir freze vuruşuyla dökülmesi derin bir psikolojik rahatlama verir.",
            "audience_reaction": "'İçimin bütün stresi o jelle beraber döküldü gitti', 'En tatmin edici tırnak videosu' yorumları.",
            "gulsah_tone": "Karpit frezenin jeli kar gibi sıyırdığı o tok titreşim sesini mikrofona net duyurun."
        },
        # Day 10: Kırmızı Ojenin Kütiküle Sıfır Yanaşması
        {
            "trigger": "Kusursuz Sınır Kontrolü (Border Precision). Kırmızı ojenin ete değmeden 0.1 mm yakınına kadar kusursuz yayılması mükemmeliyetçiliği mest eder.",
            "audience_reaction": "'O ince fırçayla yanaşış anında nefesimi tuttum!', 'Böyle kütikül yanaşması görmedim' yorumları.",
            "gulsah_tone": "İnce detay fırçasıyla kütikül cebine milimetrik yanaşın, fırçanın kavis alışını makro planda sabitleyin."
        },
        # Day 11: Tırnak Törpüleme Ritmi & Akort
        {
            "trigger": "Ritmik Hipnoz & Ses Uyumlanması. Törpünün ritmik sesi insan zihnini meditasyon dalgasına sokar.",
            "audience_reaction": "'Bu sesi saatlerce dinleyebilirim uykum geldi resmen', 'Törpüleme ritmi harika' yorumları.",
            "gulsah_tone": "Törpüyü tek yönde ve sabit bir ritimle çekin; sesin tok ve kesintisiz çıkmasını sağlayın."
        },
        # Day 12: Köpüren Karboksi Maske Cilt ASMR
        {
            "trigger": "Canlanma & Gözenek Arınması. Maskenin çıtır çıtır köpürme sesi izleyicide taze bir cilt nefesi hissettirir.",
            "audience_reaction": "'O çıtırtı sesi resmen cildi arındırıyor hissi verdi', 'Karboksi seansı nerede yapılıyor?' soruları.",
            "gulsah_tone": "Maskeyi cilde nazikçe bastırırken çıkan o mikro kabarcık seslerini mikrofona tam yaklaştırın."
        },
        # Day 13: Fransız Manikürünün (French) Tek Hamlede Çekilişi
        {
            "trigger": "Ustalık Gösterisi (Effortless Mastery). Beyaz French çizgisinin silgi kullanmadan tek bir fırça darbesiyle kusursuz çizilmesi hayranlık uyandırır.",
            "audience_reaction": "'Tek hamlede bunu nasıl çizdiniz şaka gibi!', 'Ben cetvelle çizsem böyle düz olmaz' yorumları.",
            "gulsah_tone": "Nefesinizi tutun, fırçayı tırnağın solundan sağına tek ve akıcı bir hilal hareketiyle çekin."
        },
        # Day 14: Steril Pense ile Kütikül Alınışı
        {
            "trigger": "Pürüzden Kurtulma & Cerrahi Netlik. Ölü kütikül şeridinin tek parça halinde nazikçe koparılması tatmin seviyesini zirveye çıkarır.",
            "audience_reaction": "'O kütikülün tek parça çıkışı beni benden aldı', 'Elleriniz ne kadar narin çalışıyor' yorumları.",
            "gulsah_tone": "Pensenin ucunu sadece ölü deriye oturtun, canlı deriyi çekmeden tek ve temiz bir çıt sesiyle alın."
        },
        # Day 15: İnci Tozunun Süt Beyazı Üzerinde Parlatılması
        {
            "trigger": "Hailey Bieber Glazed Büyüsü. Mat pudranın silikon fırçayla ovuldukça lüks bir inci parıltısına dönüşmesi viral trend gücüdür.",
            "audience_reaction": "'Glazed donut aşkına bayılıyorum bu modele!', 'Fiyat alabilir miyim Ataşehir stüdyonuzdan?' yorumları.",
            "gulsah_tone": "Silikon aplikatörü tırnak ucundan dibine doğru dairesel masajla ovun, sedefli ışıltının doğuşunu ışıkta yakalayın."
        },
        # Day 16: Medikal Pedikür Disk Zımpara Sesi
        {
            "trigger": "Yük Atma & Ağır Kusur Temizliği. Topuktaki sert derinin toz bulutuyla yok oluşu en çok izlenen tatmin kategorisidir.",
            "audience_reaction": "'Bu videodan sonra hemen pedikür randevusu aldım!', 'O kadar rahatlatıcı ki' yorumları.",
            "gulsah_tone": "Diskin düşük devirde topukta nazikçe kaydığı o pürüzsüzleşme anını makro planda çekin."
        },
        # Day 17: Jel Güçlendirme Damlasının Tırnağa Yayılışı
        {
            "trigger": "Kendiliğinden Seviyelenme (Self-Leveling Magic). Jelin tırnağın çukurlarını kendi kendine doldurup ayna gibi düzleşmesi görsel bir tatmin şölenidir.",
            "audience_reaction": "'Jelin kendi kendine düzelmesini izlemek terapi resmen', 'Bunu hangi markayla yapıyorsunuz?' soruları.",
            "gulsah_tone": "Damlayı tırnağın ortasına bırakın, tırnağı 2 saniye ters çevirin, düzeldiğinde ışık çizgisini kameraya yansıtın."
        },
        # Day 18: Kaş Laminasyon Jelinin Taranma Anı
        {
            "trigger": "Kaosun Düzene Girmesi. Dağınık kaş kıllarının tek bir fırça darbesiyle yukarı doğru kusursuz taranması düzen takıntısını doyurur.",
            "audience_reaction": "'O kaşların hizalanışı beni benden aldı', 'Kaş laminasyonu ne kadar kalıcı?' soruları.",
            "gulsah_tone": "Fırçayı dipten uca doğru 45° açıyla tarayın, her kılın aynı hizada parıldadığını gösterin."
        },
        # Day 19: Mikro Taşların Cımbızla Yerleştirilmesi
        {
            "trigger": "Kuyumcu Titizliği & Mücevher İhtişamı. Mikron kristallerin tek tek tırnağa dizilişi zanaatin değerini katlar.",
            "audience_reaction": "'Kuyumcu gibi çalışmışsınız helal olsun', 'Taşlar düşmüyor mu?' soruları.",
            "gulsah_tone": "Cımbızla kristali alın, jel tabanına 'çıt' diye oturtup etrafını sabitleyici jelle kilitleyin."
        },
        # Day 20: Tırnakların Birbirine Tıkırdama Sesi (Tap Test)
        {
            "trigger": "Sağlamlık İspatı & Akustik Tıkırtı. Tırnakların birbirine vurulmasıyla çıkan o tok 'tık tık' sesi kadınlarda 'asla kırılmaz' güveni yaratır.",
            "audience_reaction": "'O ses en sevdiğim tırnak sesi!', 'Cam gibi tok bir ses çıkıyor harika' yorumları.",
            "gulsah_tone": "İki elin tırnaklarını ritmik olarak birbirine tıkırdatın, mikrofonu tırnaklara 5 cm yaklaştırın."
        },
        # Day 21: Linaura Bakım Mumunun Eriyişi ve Masajı
        {
            "trigger": "Sıcak Yağ & Dokunsal Huzur. Eriyen ılık botanik balmın tırnak etlerine masajla dökülmesi saf lüks hazzıdır.",
            "audience_reaction": "'O mumun sıcaklığı ekrandan hissediliyor resmen', 'Linaura mumu satılıyor mu?' soruları.",
            "gulsah_tone": "Mumun porselen kabından ılık yağı elinize dökün, parmak diplerine yavaş ve derin masaj yapın."
        },
        # Day 22: Simli Ombre Geçişinin Fırçayla Dağıtılması
        {
            "trigger": "Renk Gradyanı & Yumuşak Geçiş. Simlerin tırnak ucundan dibine doğru fırçayla tül gibi dağıtılması estetik hazzı tetikler.",
            "audience_reaction": "'Geçiş o kadar yumuşak ki çizgi görünmüyor bile!', 'Yılbaşı tırnağım kesin bu olmalı' yorumları.",
            "gulsah_tone": "Yelpaze fırçayla simleri yukarı doğru hafif vuruşlarla süpürün, kademeli geçişi gösterin."
        },
        # Day 23: İpek Kirpiğin Suyla Test Edilişi
        {
            "trigger": "Suya Dayanıklılık & Güven Testi. Yapılan kirpiğin su damlalarına rağmen dimdik ve tüy gibi kaldığını görmek korkuları siler.",
            "audience_reaction": "'Su değince dökülmüyor mu diyenlere kapak olmuş!', 'Harika bir dayanıklılık' yorumları.",
            "gulsah_tone": "Göz kapağına su spreyi sıkın, kirpik fırçasıyla suyu nazikçe tarayıp kirpiğin kusursuz formunu koruduğunu gösterin."
        },
        # Day 24: Mat Bitişin (Matte Top Coat) Kuruma Büyüsü
        {
            "trigger": "Kadife Dönüşümü. Parlak tırnağın lamba sonrası bir anda kadife matlığa bürünmesi görsel bir sürprizdir.",
            "audience_reaction": "'O kadife dokuyu ellemek istedim resmen!', 'Mat nude inanılmaz asil durmuş' yorumları.",
            "gulsah_tone": "Lambadan çıkan tırnağın üzerindeki alkolü silin, saniyeler içinde kadifeye dönen o matlığı çekin."
        },
        # Day 25: Tırnak Kenarı Temizleme Fırçasının Hareketi
        {
            "trigger": "Sıfır Hata & Kenar Temizliği. Tırnak kenarındaki fazlalığın asetonlu ince fırçayla tek hamlede silinmesi rahatlatır.",
            "audience_reaction": "'O temizleme hamlesi içimi ferahlattı', 'Her detayda ayrı bir titizlik var' yorumları.",
            "gulsah_tone": "Fırçayı tırnak yan oluğuna oturtup tek hamlede kaydırın, geride kalan pürüzsüz çizgiyi gösterin."
        },
        # Day 26: Gül Kurusu Nude Ojenin İki Kat Sürülüşü
        {
            "trigger": "Pigment Doygunluğu & Asalet. Nude rengin tırnak plağını tek katta örtüşü ve ikinci katta derinlik kazanması asil bir zevktir.",
            "audience_reaction": "'Bu gül kurusunun markası ve numarası lütfen!', 'Dünyanın en güzel nude rengi' yorumları.",
            "gulsah_tone": "Fırçayı tırnağa paralel tutarak ojeyi tüy gibi yayın, dalgalanma olmadan pürüzsüzleştiğini gösterin."
        },
        # Day 27: Göz Altı Pedinin Nazikçe Çıkarılışı
        {
            "trigger": "Hassas Dokunuş & Can Yanmaması. Göz altındaki hidrojel pedin sıfır acıyla ve cildi çekmeden ayrılışı güven verir.",
            "audience_reaction": "'O ped çıkarken canım yanacak sanmıştım meğer ne kadar nazikmiş', 'Kirpik seansı çok konforlu görünüyor' yorumları.",
            "gulsah_tone": "Pedi kenarından nazikçe tutup cilde paralel olarak yavaşça çekin, altındaki dinlenmiş göz altını gösterin."
        },
        # Day 28: Tırnak Plakasına Baz Katın Vakumlanışı
        {
            "trigger": "Moleküler Tutunma. Tırnak yüzeyindeki mikro gözeneklere bazın yayılışı ve tırnakla kaynaşması sağlamlık hissi verir.",
            "audience_reaction": "'Bazın sürülüşü bile sanat eseri gibi!', 'Tırnağa zarar vermeden böyle tutunması harika' yorumları.",
            "gulsah_tone": "Fırçayı hafifçe bastırarak bazı tırnak gözeneklerine masaj yaparak yedirin."
        },
        # Day 29: İtalyan Espresso & Manikür Bitiş Senfonisi
        {
            "trigger": "Çifte Zevk Ritüeli. Manikür bittiğinde fincanın masaya konması ve tırnakların fincan üzerinde ışıldaması tam bir lüks yaşam karesidir.",
            "audience_reaction": "'Kahve ve tırnak ikilisi mükemmel!', 'Kendime böyle bir seans hediye edeceğim' yorumları.",
            "gulsah_tone": "Porselen fincanın tabağa 'tık' diye oturuşu ve tırnakların fincanı kavradığı o zarif son kare."
        },
        # Day 30: 30 Günlük ASMR Başyapıt Özeti (Supercut)
        {
            "trigger": "Duyusal Zirve (ASMR Mega-Dopamin). En hipnotik 10 ses ve görüntünün 22 saniyede ardı ardına patlaması en yüksek kaydedilme (Save) oranını getirir.",
            "audience_reaction": "'Bu videoyu kaydedip her gece uyumadan önce izleyeceğim', 'Resmen sanat filmi gibi' yorumları.",
            "gulsah_tone": "Otoklav yırtılışı, freze tozu, krom parıltısı, tırnak tıkırtısı ve kahve sesinin kusursuz ritmik supercut montajı."
        }
    ]
    return entries

print("ASMR psychology generator ready.")
