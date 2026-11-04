import json

def get_luxury_cues_and_psychology():
    entries = [
        # Day 1: Ataşehir Uphill Towers'ta Sakin Bir Güzellik Molası
        {
            "tripod": "Girişten masaya doğru sinematik yavaş gimbal kaydırması, göz hizasında.",
            "focus": "1x Lens, -0.3 EV. Mermer zemin üzerindeki altın yansımalara ve taze çekilmiş kahve buharına odak kilidi.",
            "hands": "Danışanın elleri keten koltuğun kolçağında dinlenir, Gülşah porselen fincanda ikram sunar.",
            "action": "Uphill Towers'ın ferah mermer lobisinden stüdyonun sakin loş atmosferine 2 saniyelik geçiş, ardından cam bardakta eriyen Linaura mumu ve dinginliğin 6 saniyelik görseli.",
            "trigger": "Sessiz Lüks & Şehir Kaosundan Kaçış. Ataşehir'in yoğun plazasından çıkıp kendini şımartacak vaha arayan elit kadınları çeker.",
            "audience_reaction": "'İşte huzur tam olarak bu!', 'Ataşehir'de böyle sakin bir yer olduğunu bilmiyordum' yorumları.",
            "gulsah_tone": "Dingin ve asil: 'Gününüz ne kadar hızlı akarsa aksın, bu kapıdan içeri girdiğinizde saatler yavaşlar. Burası tamamen sizin dinlenme alanınız' fısıltısı."
        },
        # Day 2: VIP Odada Aynı Anda 3 İşlem: Zamanınızı Geri Alın
        {
            "tripod": "VIP odanın köşesinden geniş sinematik açı.",
            "focus": "1x Lens, -0.2 EV. Üç uzmanın eldivenli senkronize ellerine odak kilidi.",
            "hands": "Biri manikürde jeli fırçalarken, diğeri pedikür diskini kaydırır, kirpik uzmanı baş ucunda çalışır.",
            "action": "Danışanın koltuğa uzanıp gözlerini kapattığı 2 saniye, ardından 1.5 saat içinde sıfır bekleme ile biten komple bakımın 6 saniyelik senkronize büyüsü.",
            "trigger": "Zaman Fakirliği & Ultra Verimlilik. Zamanı paradan değerli olan üst düzey yöneticiler ve anneler için en yüksek biletli teklif.",
            "audience_reaction": "'Aynı anda 3 işlem benim hayatımı kurtarır!', 'VIP oda fiyatı nedir randevu almak istiyorum' yorumları.",
            "gulsah_tone": "Net ve profesyonel: 'Bütün gününüzü güzellik merkezlerinde parça parça harcamayın. VIP odamızda zamanınızı size geri veriyoruz' de."
        },
        # Day 3: Park Çilesi Yok: Vale ve Kapalı Otopark Ayrıcalığı
        {
            "tripod": "Rezidans kapalı otopark girişinden asansöre doğru takip açısı.",
            "focus": "1x Lens, asansörün B Blok 14. kat tuşuna ve konforlu çıkışa odak kilidi.",
            "hands": "Danışan araba anahtarını valeye teslim eder veya kapalı otoparktan doğrudan asansöre biner.",
            "action": "Ataşehir trafiğindeki park çilesi 2 saniye, ardından kapalı otoparktan asansörle 30 saniyede stüdyo kapısına ulaşılan 6 saniyelik sürtünmesiz konfor.",
            "trigger": "Lojistik Sürtünmeyi Sıfırlama (Frictionless Luxury). Kadınların en büyük kabusu olan 'park yeri bulamama' stresini tamamen ortadan kaldırır.",
            "audience_reaction": "'Ataşehir'de park yeri olmaması gitmeme sebebiydi, kapalı otopark olması muazzam!', 'Vale hizmeti ücretsiz mi?' soruları.",
            "gulsah_tone": "Çözüm odaklı ve rahat: 'Ataşehir'de 20 dakika park yeri arayıp randevunuza stresli girmeyin. Kapalı otoparkımızdan asansöre binin, 1 dakikada masamızdasınız' de."
        },
        # Day 4: Şehir Gürültüsünden İzole: Kişiye Özel Dingin Kabin
        {
            "tripod": "Kabin içinde 45° açıda, ses yalıtımlı kapının kapanışına odaklı.",
            "focus": "1x Lens, -0.3 EV. Akustik lofi müziğin hoparlöründen süzülen dinginliğe odak kilidi.",
            "hands": "Gülşah kapıyı nazikçe kapatır, stüdyodaki tüm dış sesler anında kesilir.",
            "action": "Kapı kapandığı an dışarıdaki telefon ve koridor seslerinin sıfırlandığı ve sadece su sesi ve rahatlatıcı müziğin kaldığı 6 saniye.",
            "trigger": "Duyusal Detoks (Sensory Sanctuary). Gün boyu gürültüye maruz kalmış zihinlerin aradığı mutlak sessizlik.",
            "audience_reaction": "'O kapı kapandığında gelen sessizlik resmen terapi gibi', 'Böyle bir izole kabin harika' yorumları.",
            "gulsah_tone": "Yumuşak ve huzurlu: 'Burası dedikodunun, yüksek sesli telefon konuşmalarının olmadığı bir sığınaktır. Sadece siz, kahveniz ve bakımınız' de."
        },
        # Day 5: İtalyan Espressosu Eşliğinde Tırnak Seansı
        {
            "tripod": "Masada 45° açıda, porselen espresso fincanı ve tırnak paletine odaklı.",
            "focus": "1x Lens, espresso üzerindeki altın rengi kremaya ve mermer masaya odak kilidi.",
            "hands": "Danışan fincanı iki eliyle tutar, yeni yapılmış fildişi French tırnaklar fincan üzerinde ışıldar.",
            "action": "Taze çekilen İtalyan kahvesinin bardağa akışı 2 saniye, ardından kahve eşliğinde yapılan zarif manikürün 6 saniyelik keyif karesi.",
            "trigger": "Gastronomik Lüks & Keyif Ritüeli. Bir seansı rutin bir işlemden çıkarıp lüks bir kafede geçirilen keyifli bir molaya dönüştürür.",
            "audience_reaction": "'O kahvenin kreması bile kalite kokuyor!', 'Kahvemi alıp gelmek için sabırsızlanıyorum' yorumları.",
            "gulsah_tone": "Samimi bir ev sahibi gibi: 'Bizim masamızda kahve aceleye gelmez. Taze çekilmiş espressonuz hazır, gerisini bize bırakın' gülümsemesi."
        },
        # Day 6: Zamanı Değerli Plaza Kadınlarına Özel Hızlı Bakım
        {
            "tripod": "Masa seviyesinde 30° dinamik açıda, saat kadranı ve ellere odaklı.",
            "focus": "1x Lens, kol saatindeki dakikalar ile frezenin milimetrik hızına odak kilidi.",
            "hands": "Hızlı, kusursuz ve titreşimsiz el hareketleri.",
            "action": "Saatin 12:00'yi vuruşu 2 saniye, ardından tam 45 dakikada tek bir milimetrik hata olmadan tamamlanan Rus manikürünün 6 saniyelik profesyonel gücü.",
            "trigger": "Hız & Tavizsiz Kalite Dengesi. 'Hızlı yapan kalitesiz yapar' mitini yıkarak profesyonel hızı kanıtlar.",
            "audience_reaction": "'Öğle aramda gelip yaptırabilirim muazzam bir hız!', 'Ataşehir Varyap'tan yürüyerek geleceğim' yorumları.",
            "gulsah_tone": "Tempolu ve güven veren: 'Hızlı olmak baştan savma yapmak değildir; her hareketin ezbere bilinmesidir. 45 dakikada çıkıp toplantınıza yetişebilirsiniz' de."
        },
        # Day 7: Tek Kullanımlık Medikal Uçlar ve Cerrahi Hijyen
        {
            "tripod": "45° makro açıda, otoklav cihazının dijital ekranı ve steril paketlere odaklı.",
            "focus": "2x Makro, poşet üzerindeki pembeden kahverengiye dönen sterilizasyon indikatörüne odak kilidi.",
            "hands": "Eldivenli eller paketi danışanın gözü önünde tek hamlede açar.",
            "action": "İndikatörün renginin değiştiğini gösteren 2 saniyelik güvenlik karesi, ardından metal tepsiye bırakılan elmas uçların 6 saniyelik güven sesi.",
            "trigger": "Kusursuz Hijyen Güvencesi (Medical-Grade Disgust Defense). Mantar veya enfeksiyon korkusu olan kadınların tek vazgeçilmezi.",
            "audience_reaction": "'Otoklav poşetinin rengini göstermeniz ne kadar profesyonel olduğunuzun kanıtı', 'Gözüm kapalı gelebileceğim tek yer' yorumları.",
            "gulsah_tone": "Tavizsiz bir ciddiyetle: 'Güzellik hijyenden sonra gelir. Masamızda kullanılan her metal alet hastane ameliyathanelerindeki otoklav standardıyla sterilize edilir' de."
        },
        # Day 8: Rezidans Konforunda Özel Randevu Sistemi
        {
            "tripod": "Stüdyo girişindeki karşılama alanında 45° açıda.",
            "focus": "1x Lens, -0.2 EV. Randevu defterindeki seyrek, kişiye özel saat bloklarına odak kilidi.",
            "hands": "Gülşah kapıyı açıp misafiri ismiyle karşılar.",
            "action": "Kapı zili çaldığında Gülşah'ın kapıyı tebessümle açışı 2 saniye, arkada bekleyen başka hiçbir müşterinin olmadığı tamamen kişiye özel 6 saniyelik mahremiyet.",
            "trigger": "Mahremiyet & Seçkinlik (Exclusivity). Sıra beklemeden, kalabalık kuaför keşmekeşi yaşamadan hizmet alma arzusu.",
            "audience_reaction": "'Sıra beklememek en büyük lüks!', 'Kendimi prenses gibi hissederim bu ortamda' yorumları.",
            "gulsah_tone": "Zarifçe: 'Bizde kapıda sıra beklemek, dip dibe oturmak yoktur. Randevu saatiniz sadece size aittir; stüdyomuz o saatte sizin evinizdir' de."
        },
        # Day 9: El, Ayak ve Kirpik: 1.5 Saatte Baştan Aşağı Yenilenme
        {
            "tripod": "Geniş açıda, bakım sonrası müşterinin aynadaki komple yenilenmiş haline odaklı.",
            "focus": "1x Lens, -0.3 EV. Tırnaklar, pedikür ve kirpiklerin kusursuz uyumuna odak kilidi.",
            "hands": "Danışan parmaklarını saçlarına götürür, kirpiklerini aynada kontrol eder.",
            "action": "Yorgun gelip 1.5 saat sonra gözleri parlayan, elleri ve ayakları ışıldayan danışanın 6 saniyelik dönüşüm ışıltısı.",
            "trigger": "Komple Yenilenme & Yüksek Dopamin. Tek seferde baştan aşağı yenilenmenin verdiği muazzam enerji.",
            "audience_reaction": "'1.5 saatte yeni bir insan olmak resmen!', 'Paket içeriği nedir hemen randevu almak istiyorum' yorumları.",
            "gulsah_tone": "Coşkuyla: 'Günün sonunda aynaya baktığınızda 'iyi ki kendime bu zamanı ayırmışım' diyeceksiniz. El, ayak ve kirpik aynı anda tamam' de."
        },
        # Day 10: Gözlerinizi Kapatıp Dinlenebileceğiniz Dingin Alan
        {
            "tripod": "Yumuşak pedikür koltuğunun yanından 30° dinlenme açısı.",
            "focus": "1x Lens, -0.4 EV. Loş sarı aydınlatmaya ve ayak masajındaki ılık köpüklere odak kilidi.",
            "hands": "Uzman nazikçe ayak bileğini kavrar, deniz tuzu peelingiyle masaj yapar.",
            "action": "Danışanın arkasına yaslanıp göz maskesini taktığı 2 saniye, ardından aromaterapi eşliğindeki 6 saniyelik spa huzuru.",
            "trigger": "Ruhsal Detoks & Fiziksel Gevşeme. Sadece estetik değil, derin bir dinlenme arayan tükenmiş zihinler için.",
            "audience_reaction": "'Şu koltukta 1 saat uyumak için her şeyimi verirdim', 'Ataşehir'de böyle bir spa manikürü var mıydı!' yorumları.",
            "gulsah_tone": "Fısıldayarak: 'Telefonunuzu sessize alın, gözlerinizi kapatın. Dünyayı 1 saatliğine dışarıda bırakın' de."
        },
        # Day 11: Ataşehir'in Kalbinde Gürültüden İzole Bir Vaha
        {
            "tripod": "Uphill Towers balkonundan Ataşehir gökdelen silüetine doğru kaydırma.",
            "focus": "1x Lens, pencere camındaki yağmur damlaları ve içerideki sıcak kahveye odak kilidi.",
            "hands": "Danışan pencere kenarında kahvesini yudumlar, elleri bakımlı ve sıcacıktır.",
            "action": "Dışarıdaki şehir trafiği 2 saniye, ardından pencere kapandığında içeride başlayan sıcacık Linaura masajının 6 saniyelik huzuru.",
            "trigger": "Lokasyon Prestiji & Yüksek Standart. Uphill Towers'ın bilinen güvenli ve prestijli konumunu vurgular.",
            "audience_reaction": "'Uphill Towers'ta olması çok iyi lokasyon harika!', 'Hemen komşuyuz mutlaka uğrayacağım' yorumları.",
            "gulsah_tone": "Sakin ve güvenli: 'Ataşehir'in tam merkezindeyiz ama şehrin tüm karmaşasından 14 kat yukarıda, sessiz bir bulutun üzerindeyiz' de."
        },
        # Day 12: Masada Sadece Siz ve Sanatçınız: Sıfır Bekleme
        {
            "tripod": "Masada 45° açıda, boş ve tertemiz hazırlanmış çalışma alanına odaklı.",
            "focus": "1x Lens, masadaki taze porselen fincan ve steril metal tepsiye odak kilidi.",
            "hands": "Gülşah sandalyeyi nazikçe çeker, misafiri buyur eder.",
            "action": "Masanın dakikası dakikasına hazır oluşu 2 saniye, ardından randevu saatinde masaya oturulup sıfır saniye beklemeyle başlayan 6 saniyelik disiplin.",
            "trigger": "Dakiklik & Zamana Saygı. Kuaförlerde '10 dakikaya alıyoruz' denilip 40 dakika bekletilen kadınların en büyük kurtuluşudur.",
            "audience_reaction": "'Kuaförlerde beklemekten nefret eden biri olarak bayıldım!', 'İşte profesyonellik bu' yorumları.",
            "gulsah_tone": "Net bir disiplinle: 'Bizim kapımızdan girdiğinizde 'biraz bekleyin' cümlesini duymazsınız. Saat 14:00 randevunuz varsa masanız 13:55'te hazırdır' de."
        },
        # Day 13: Kişiye Özel İkramlar ve Premium Deneyim
        {
            "tripod": "45° açıda, şık mermer sunum tepsisindeki ikramlara odaklı.",
            "focus": "1x Lens, porselen fincandaki taze çekilmiş kahve ve özel bitter çikolataya odak kilidi.",
            "hands": "Danışan ikram tepsisinden çikolatasını alır, tırnaklar ışıldar.",
            "action": "Kişiye özel sunulan şık ikram anı 2 saniye, ardından bakım sırasında kahvenin sıcaklığını koruyan porselen zarafetinin 6 saniyesi.",
            "trigger": "Şımartılma & Butik Ağırlanma. Kendini değerli hissetmek isteyen her kadının hoşuna giden ince detaylar.",
            "audience_reaction": "'Sunum bile ne kadar zarif!', 'Kendime böyle bir gün hediye etmeliyim' yorumları.",
            "gulsah_tone": "Tatlı bir tebessümle: 'Güzellik sadece tırnakta bitmez; ruhunuzun nasıl ağırlandığıyla tamamlanır. Afiyet olsun' de."
        },
        # Day 14: Kapıda Başlayan Lüks: Uphill Towers B Blok
        {
            "tripod": "Uphill Towers B Blok giriş kapısından asansöre doğru geniş sinematik takip.",
            "focus": "1x Lens, rezidans güvenliğinin nazik selamlamasına ve şık lobisine odak kilidi.",
            "hands": "Danışan lobiden geçer, asansöre biner.",
            "action": "Güvenlikli, nezih ve elit rezidans girişinin 2 saniyesi, ardından stüdyonun kapısındaki Linail altın amblemine varışın 6 saniyelik güvencesi.",
            "trigger": "Güvenlik & Sosyal Statü Doğrulaması. Rastgele bir apartman dairesi değil, Ataşehir'in en bilinen rezidansında olduğunu bilmenin verdiği huzur.",
            "audience_reaction": "'Rezidans içinde olması çok güvenli ve nezih', 'Adres tarifi çok net teşekkürler' yorumları.",
            "gulsah_tone": "Asil ve net: 'Uphill Towers B Blok Daire 14. Güvenlikten geçip asansörle doğrudan bize geliyorsunuz; tamamen konforlu ve güvenli' de."
        },
        # Day 15: Yoğun İş Temposunda Kendinize Ayırdığınız En Değerli Saat
        {
            "tripod": "45° açıda, dinlenen eller ve fildişi French tırnaklara odaklı.",
            "focus": "1x Lens, -0.3 EV. Mermer üzerindeki ellerin sakin duruşuna odak kilidi.",
            "hands": "Gülşah nazikçe tırnak yağı damlatır, parmak uçlarına hafif masaj yapar.",
            "action": "Gözlerini dinlendiren danışanın yüzündeki yorgunluğun yerini dinginliğe bıraktığı o 6 saniyelik huzur karesi.",
            "trigger": "Kendine Zaman Ayırma Suçluluğunu Yok Etme. Sürekli koşturan kadınlara 'kendine bu saati ayırmak senin hakkın' mesajı verir.",
            "audience_reaction": "'Gerçekten kendime ayırdığım tek saat bu seanslar', 'Ellerinize sağlık harika bir ortam' yorumları.",
            "gulsah_tone": "Şefkatle: 'Bütün gün iş, ev, sorumluluklar... Bu 1 saat sadece ve sadece sizin. Kendinize iyi bakın' de."
        },
        # Day 16: Lüks Bir Spa Hissiyatında Medikal Pedikür Seansı
        {
            "tripod": "Medikal pedikür alanında 45° açıda, disk zımparanın yumuşak dönüşüne odaklı.",
            "focus": "2x Makro, topuktaki ölü derinin bebek tenine dönüştüğü ana odaklı.",
            "hands": "Eldivenli eller tek kullanımlık steril disk zımparayla topuğu parlatır.",
            "action": "Sertleşmiş topuk derisinin mikron mikron toza dönüşüp altından ipeksi tenin çıktığı ve sıcak havluyla sarıldığı 6 saniyelik spa anı.",
            "trigger": "Ayak Kusurunu Gizleme Çilesine Son. Sertleşmiş topuklardan utanan kadınların yaz-kış özgürce açık ayakkabı giymesini sağlar.",
            "audience_reaction": "'O topuğun ipek gibi oluşu beni benden aldı!', 'Pedikür seansı ne kadar sürüyor?' soruları.",
            "gulsah_tone": "Podolojik uzmanlıkla: 'Ayaklar vücudun bütün yükünü taşır. Jiletle kesmeden, sadece medikal disk zımparayla bebek teni yumuşaklığına kavuşturuyoruz' de."
        },
        # Day 17: Tasarım Detaylarında Saklı Sessiz Zarafet
        {
            "tripod": "Masada 45° makro açıda, tırnak üzerindeki mikro fırça hareketine odaklı.",
            "focus": "2x Makro, Hailey Bieber tarzı glazed donut ayna yansımasına odak kilidi.",
            "hands": "Işık altında tırnaklar sağa sola hafifçe döner, inci tozu parıldar.",
            "action": "Abartısız, bağırmayan ama 'nerede yaptırdın?' dedirten o sessiz lüks tırnak ışıltısının 6 saniyelik makro videosu.",
            "trigger": "Sessiz Lüks (Quiet Luxury / Old Money Estetiği). Gösterişli taşlardan ve neonlardan kaçınan, zarafeti detayda arayan kitleye hitap eder.",
            "audience_reaction": "'İşte gerçek zarafet! Asla avam durmuyor', 'Glazed donut modelinin yapılışı nedir?' soruları.",
            "gulsah_tone": "Zarafetle: 'Lüks bağırmaz; sessizce parıldar. Tırnakta öyle bir inci dokunuşu bırakıyoruz ki, herkes zarafetinize hayran kalıyor' de."
        },
        # Day 18: Günün Stresini Unutturan Aromatik Sıcak Havlu Masajı
        {
            "tripod": "45° açıda, sıcak havlu kazanından çıkan buharlı pamuk havluya odaklı.",
            "focus": "1x Lens, havludan yükselen aromatik okaliptüs ve lavanta buharına odak kilidi.",
            "hands": "Gülşah sıcak havluyu danışanın ellerine sarar, nazikçe baskı masajı uygular.",
            "action": "Sıcak havlunun parmakları sarıp kasları gevşettiği o 6 saniyelik derin rahatlama karesi.",
            "trigger": "Dokunsal Zevk (Tactile Pleasure). Sıcak havlu seansları kadın beyninde anında gevşeme hormonu salgılar.",
            "audience_reaction": "'O sıcak havlu anı için bile gelinir!', 'Ataşehir'de böyle spa detayı yapan yer yok' yorumları.",
            "gulsah_tone": "Huzur veren bir fısıltıyla: 'İşlem bittiğinde ellerinizi aromatik sıcak havluyla sarıyoruz; tüm günün yorgunluğu o buharla uçup gidiyor' de."
        },
        # Day 19: Gözlerinizi Yormayan Dinlendirici Aydınlatma
        {
            "tripod": "Stüdyo tavanından mermer masaya inen sıcak altın aydınlatmaya odaklı.",
            "focus": "1x Lens, -0.3 EV. Yumuşak amber tonlu dinlendirici ışığa odak kilidi.",
            "hands": "Masanın üzerindeki aydınlatma sadece tırnağa odaklanır, danışanın yüzüne doğrudan vurmaz.",
            "action": "Gözü yoran beyaz floresan ışıkların olmadığı, sıcak porselen ve altın ışıltılı 6 saniyelik dinlendirici ortam karesi.",
            "trigger": "Göz ve Baş Ağrısı Yaşamama. Kuaförlerdeki kör edici beyaz ışıklardan bunalan kadınlar için dinlendirici bir atmosfer.",
            "audience_reaction": "'O beyaz hastane ışıklarından nefret ediyordum burası çok dinlendirici', 'Ambiyans 10 numara' yorumları.",
            "gulsah_tone": "Işık mimarı gibi: 'Gözlerinizi yoran sert ışıklar burada yok. Sadece işimize odaklanan çalışma ışığımız ve ruhunuzu dinlendiren sıcak amber tonlarımız var' de."
        },
        # Day 20: Ataşehir'de Güvenle Gelebileceğiniz Butik Bir Rezidans
        {
            "tripod": "Stüdyo salonunun geniş sinematik açısı, mermer ve keten detaylarla.",
            "focus": "1x Lens, -0.2 EV. Doğal gün ışığının ferahlığına odak kilidi.",
            "hands": "Gülşah tebessümle masasında oturur, misafirini bekler.",
            "action": "Gürültülü cadde dükkanları yerine, tamamen butik ve huzurlu bir rezidans dairesinde olmanın getirdiği 6 saniyelik güven duygusu.",
            "trigger": "Elit Sınıf Aidiyeti. Cadde üstü kalabalık dükkanlar yerine rezidans içi butik stüdyoları tercih eden kitleye seslenir.",
            "audience_reaction": "'Butik stüdyolar her zaman çok daha kaliteli oluyor', 'Randevu oluşturmak istiyorum' yorumları.",
            "gulsah_tone": "Güvenle: 'Fabrikasyon kuaför düzenine inanmıyoruz. Biz butik kalmayı, her misafirimizle tek tek ilgilenmeyi ve o güven bağını korumayı seçtik' de."
        },
        # Day 21: Toplantı Öncesi Kusursuz Görünüm Garantisi
        {
            "tripod": "45° açıda, tırnak uçlarının milimetrik netliğine odaklı.",
            "focus": "2x Makro, top coat'un cam gibi kuruduğu ana odaklı.",
            "hands": "Danışan arabasının direksiyonunu tutar, tırnaklar ışıldar.",
            "action": "Masadan kalkıp doğrudan önemli bir görüşmeye giden ve ellerinin kusursuzluğundan güç alan kadının 6 saniyelik karizması.",
            "trigger": "Özgüven & Başarı Psikolojisi. Bakımlı tırnakların bir kadının beden dilini nasıl değiştirdiğini kanıtlar.",
            "audience_reaction": "'Tırnaklarım bakımlı olunca kendimi çok daha güçlü hissediyorum kesinlikle!', 'Harika bir işçilik' yorumları.",
            "gulsah_tone": "Motive edici: 'Elleriniz kusursuz olduğunda masaya evrak bırakırken bile beden diliniz değişir. O özgüven her toplantıyı kazandırır' de."
        },
        # Day 22: Sıradanlığa Yer Yok: Sadece Birinci Sınıf Malzemeler
        {
            "tripod": "90° dik açıda, masaya dizilmiş birinci sınıf Avrupa jelleri ve elmas uçlara odaklı.",
            "focus": "1x Lens, -0.3 EV. Şişelerin şık lüks ambalajlarına odak kilidi.",
            "hands": "Gülşah eldivenli elleriyle sadece sertifikalı, asitsiz ürünleri seçer.",
            "action": "Ucuza kaçılmamış, tırnağı sarartmayan ve kokusuz çalışan birinci sınıf malzemelerin 6 saniyelik lüks geçişi.",
            "trigger": "Kalite Ayrımı & Sağlık Bilinci. Ucuz kimyasalların tırnağı mahvettiğini bilen bilinçli tüketiciyi yakalar.",
            "audience_reaction": "'Kullandığınız ürünlerin kalitesi ekrandan bile belli oluyor', 'Tırnağıma asla ucuz malzeme sürdürmem' yorumları.",
            "gulsah_tone": "Dürüstlükle: 'Bizim masamızda kaliteden ödün vermek yoktur. Tırnağınıza değen her damla jel, Avrupa standartlarında ve hipoalerjeniktir' de."
        },
        # Day 23: Kendi Evinizin Konforunda Bir Bakım Deneyimi
        {
            "tripod": "45° açıda, rahat keten koltukta ayaklarını uzatmış danışana odaklı.",
            "focus": "1x Lens, danışanın yüzündeki rahatlamış tebessüme odak kilidi.",
            "hands": "Danışan fincanını yudumlar, uzmanlar sessizce bakımını tamamlar.",
            "action": "Kendi evinde gibi terliklerini giyip kahvesini yudumlayan ve kendini tamamen güvende hisseden kadının 6 saniyelik huzuru.",
            "trigger": "Ev Konforu & Yargısız Samimiyet. Kasılmadan, gerilmeden tamamen rahat hissedebileceği bir alan arayışı.",
            "audience_reaction": "'Tam olarak aradığım ortam! Kuaförlerin o gergin havası yok', 'Çok sıcak bir stüdyo' yorumları.",
            "gulsah_tone": "Sıcak bir karşılama: 'Buraya geldiğinizde misafir değil, evin kızı gibi hissedersiniz. Ayakkabılarınızı çıkarın, kahvenizi alın, gerisi bizde' de."
        },
        # Day 24: Hafta Sonu Yoğunluğu Olmadan Hafta İçi Sakinliği
        {
            "tripod": "Geniş açıda, stüdyonun gün ortası güneş alan aydınlık salonuna odaklı.",
            "focus": "1x Lens, -0.2 EV. Güneş ışığının mermer zemindeki oyununa odak kilidi.",
            "hands": "Danışan ellerini masada dinlendirir, dışarıda kuş sesleri duyulur.",
            "action": "Hafta içi saat 14:00'te tamamen sakin, kimsenin acele etmediği ve vaktin genişlediği 6 saniyelik dingin seans.",
            "trigger": "Ayrıcalıklı Zaman Dilimi. Hafta sonu kalabalığından kaçabilen kadınları hafta içi boş saatlere çeken akıllı randevu kurgusu.",
            "audience_reaction": "'Hafta içi gitmek kesinlikle en güzeli', 'Çarşamba günü için randevu alabilir miyim?' soruları.",
            "gulsah_tone": "Tatlı bir tüyo gibi: 'Hafta sonunun kalabalığı yerine hafta içi sakin bir kahve molası vermek kendinize yapacağınız en büyük iyiliktir' de."
        },
        # Day 25: Rezidans Penceresinden Ataşehir Manzarası
        {
            "tripod": "14. kat penceresinden Ataşehir manzarasına doğru sinematik açı.",
            "focus": "1x Lens, camdaki hafif yansıma ve masadaki parlak tırnaklara odak kilidi.",
            "hands": "Danışan ellerini pencereye doğru uzatır, tırnaklar gökyüzünün ışığında parlar.",
            "action": "Gökdelenlerin üzerinden süzülen doğal ışık altında yeni yapılmış tırnakların 6 saniyelik ışıltısı.",
            "trigger": "Yüksek İrtifa & Perspektif Rahatlaması. Rezidans manzarasının getirdiği elit tatmin.",
            "audience_reaction": "'Manzara da tırnaklar da muhteşem!', 'Uphill Towers B Blok kaçıncı kattasınız?' soruları.",
            "gulsah_tone": "Huzurla: '14. kattan Ataşehir'i izlerken bakımınızı tamamlamak... Günün stresini geride bırakmanın en güzel manzarası' de."
        },
        # Day 26: Zaman Fakiri Kadınların Gizli Kurtarıcısı
        {
            "tripod": "45° açıda, stüdyodan çıkış anı ve kapının zarifçe açılışına odaklı.",
            "focus": "1x Lens, danışanın yüzündeki dinamik ve enerjik gülümsemeye odak kilidi.",
            "hands": "Danışan çantasını omzuna takar, bakımlı elleriyle kapıyı açar.",
            "action": "1 saat önce yorgun girip 1 saat sonra kusursuz tırnaklarla işine dönen kadının 6 saniyelik asil yürüyüşü.",
            "trigger": "Zaman Kurtarma Başarısı. İş ve aile dengesi arasında sıkışan kadınlara pratik bir can simidi olur.",
            "audience_reaction": "'Zamanımı almayan yerleri seviyorum, Linail tam bana göre', 'Haftaya pazartesi geleceğim' yorumları.",
            "gulsah_tone": "Kutlayarak: 'Zamanınız altın kadar değerli. Masamızda tek bir dakikanız bile boşa harcanmaz; tam vaktinde girer, tam vaktinde çıkarsınız' de."
        },
        # Day 27: Her Seans Arasında 30 Dakikalık Tam Havalandırma
        {
            "tripod": "Pencereden giren taze temiz hava akımına ve açık pencerelere odaklı.",
            "focus": "1x Lens, -0.3 EV. Havalandırılan ferah kabine ve temizlenen yüzeylere odak kilidi.",
            "hands": "Gülşah her misafirden sonra masayı tıbbi dezenfektanla siler, pencereleri ardına kadar açar.",
            "action": "İki misafir arasında taze havanın stüdyoyu doldurduğu ve masanın sıfırdan sterilize edildiği 6 saniyelik hijyen molası.",
            "trigger": "Taze Hava & Kalabalık/Koku Tiksintisi Olmaması. Kuaförlerdeki ağır kimyasal oje kokusundan nefret eden kadınların sığınağı.",
            "audience_reaction": "'Kuaförlerdeki o ağır oje kokusu bende migren yapıyordu, havalandırma detayı harika!', 'İşte gerçek titizlik' yorumları.",
            "gulsah_tone": "Ferah bir nefesle: 'Masamızda üst üste yığılan randevular yoktur. Her seans arasında 30 dakika stüdyomuz tamamen havalandırılır; içeri girdiğinizde sadece taze hava ve botanik kokular karşılarsınız' de."
        },
        # Day 28: VIP Odada Arkadaşınızla veya Tek Başınıza Özel Seans
        {
            "tripod": "Geniş sinematik açıda, VIP odanın iki kişilik konforlu koltuklarına odaklı.",
            "focus": "1x Lens, -0.2 EV. İki koltuğun arasındaki mermer sehpa ve kahvelere odak kilidi.",
            "hands": "İki arkadaş karşılıklı kahvelerini tokuşturur, uzmanlar eşzamanlı çalışır.",
            "action": "En yakın arkadaşınızla kapıyı kapatıp hem dertleşip hem güzelleştiğiniz 6 saniyelik VIP özel seans.",
            "trigger": "Arkadaşla Kaliteli Vakit Geçirme (Social Luxury). Sosyalleşmeyi bakımla birleştiren yüksek biletli randevu.",
            "audience_reaction": "'Kankamla hemen geliyoruz bu oda tam bizlik!', 'İki kişilik VIP randevu için nasıl iletişime geçebilirim?' yorumları.",
            "gulsah_tone": "Neşeyle: 'En yakın arkadaşınızı alın, VIP odanın kapısını kapatın. Hem sohbetinizi edin hem kahvenizi için, tırnaklarınız aynı anda tamamlansın' de."
        },
        # Day 29: Sessiz Lüksün Tanımı: Çaba Harcanmamış Doğal Asalet
        {
            "tripod": "45° makro açıda, kusursuz nude jel sürülmüş tırnaklara odaklı.",
            "focus": "2x Makro, tırnak plağının kendi doğal pembeliğiyle kaynaşan pudra tona odak kilidi.",
            "hands": "Zarifçe kıvrılan parmaklar, kaşmir kazağın kolunu hafifçe geriye çeker.",
            "action": "Abartıdan uzak, 10 metreden 'ben buradayım' diye bağırmayan ama yakınına gelindiğinde nefes kesen sessiz lüks tırnağın 6 saniyesi.",
            "trigger": "Old Money / Çabasız Zarafet. Zenginliğini veya statüsünü bağırmadan, asil detaylarla göstermek isteyen elit kadın profili.",
            "audience_reaction": "'İşte zengin tırnağı tam olarak budur!', 'Çok asil duruyor renk kodu nedir?' yorumları.",
            "gulsah_tone": "Zarafet dersi gibi: 'Gerçek lüks çaba harcanmamış gibi görünendir. Tırnaklarınıza baktıklarında protez değil, doğuştan kusursuz elleriniz var sansınlar' de."
        },
        # Day 30: Ay Sonu Lüks Özeti: Ataşehir'de Kendini Özel Hisseden Kadınlar
        {
            "tripod": "Masanın 45° açısında, stüdyonun genel lüks mermer ve altın detaylarına odaklı.",
            "focus": "1x Lens, -0.3 EV. Masadaki yanan Linaura mumuna ve gün batımı manzarasına odak kilidi.",
            "hands": "Gülşah masada dinlenir, kameraya sıcacık gülümser.",
            "action": "Bu ay Uphill Towers'ta ağırlanan yüzlerce kadının ellerindeki asil tasarımların sinematik 6 saniyelik şöleni.",
            "trigger": "Kapanış & Yeni Ayın VIP Randevu Aciliyeti (Scarcity). Takipçilere yeni ayda yer kalmayacağı korkusunu (FOMO) vererek randevu kapattırır.",
            "audience_reaction": "'Yeni ay için yerinizi hemen ayırtıyorum!', 'Ataşehir'in en güzel stüdyosu' yorumları.",
            "gulsah_tone": "Teşekkür ve davet: 'Bu ay da masamızı paylaşan, ellerini bize emanet eden tüm kadınlara teşekkürler. Yeni ayın VIP randevuları açıldı, siz de masamızda yerinizi alın' de."
        }
    ]
    return entries

print("Luxury cues & psychology generator ready.")
