import json

def get_storytelling_cues_and_psychology():
    entries = [
        # Day 1: Uçuşuna 2 Saat Kala Gelen Misafirimiz
        {
            "tripod": "45° açıda, stüdyo kapısı ve masaya doğru geniş kadraj.",
            "focus": "1x Lens, -0.2 EV. Masadaki valiz detayı ve hızlı çalışan ellere odak kilidi.",
            "hands": "İki uzmanın aynı anda sağ ve sol ele hızlı ve senkronize dokunuşu.",
            "action": "Danışanın nefes nefese masaya oturuşu 2 saniye, ardından iki uzmanın 40 dakikada kusursuz nude jeli bitirip danışanın bavulunu alıp taksiye koştuğu 6 saniyelik film gibi an.",
            "trigger": "Zaman Krizi & Güvenilir Kurtarıcı. Acil durumlarda profesyonel bir ekibin hayat kurtardığını görmek yoğun kadınlar için büyük bir rahatlamadır.",
            "audience_reaction": "'İki uzmanın aynı anda girmesi inanılmaz bir lüks!', 'Haftaya benim de uçuşum var tam böyle bir yer arıyordum' yorumları.",
            "gulsah_tone": "Gülerek ve tempolu: 'Valiz kapıda, uçak 2 saat sonra... İşte bizim masada en sevdiğimiz adrenalin dolu seanslar :)' samimiyeti."
        },
        # Day 2: Gelinimiz Nikaha 3 Saat Kala Tırnağını Kırmıştı...
        {
            "tripod": "45° açıda, gelinlik detayları ve yüzük parmağına odaklı.",
            "focus": "2x Makro, yüzük parmağındaki şablon jel mimarisine odak kilidi.",
            "hands": "Gülşah danışanın elini şefkatle tutar, kahve fincanını uzatır.",
            "action": "Ağlamak üzere olan gelinin kahvesini yudumlayıp rahatlaması 2 saniye, ardından 30 dakikada inşa edilen kusursuz French tırnağın 6 saniyelik ışıltısı.",
            "trigger": "Duygusal Dayanışma & Krizden Zafer Çıkarma. Düğün stresi yaşayan tüm gelin adaylarının kalbine dokunur.",
            "audience_reaction": "'Gözlerim doldu resmen hayatını kurtarmışsınız!', 'Benim de düğünüm Ataşehir'de kesin geleceğim' yorumları.",
            "gulsah_tone": "Abla şefkatiyle: 'Düğün günü hiçbir gelinimizin ağlamasına izin vermeyiz; o yüzük masamızdan kusursuz parlayarak çıkar' de."
        },
        # Day 3: Benden 'Pinterest'te Gördüğü Çılgın Modeli İstedi
        {
            "tripod": "90° dik açıda, masadaki telefon ekranı ve Gülşah'ın çizim fırçasına odaklı.",
            "focus": "1x Lens, telefondaki aşırı abartılı görsel ile masadaki zarif tırnağa odak kilidi.",
            "hands": "Danışan telefonu gösterir, Gülşah gülümseyerek kendi fırçasını seçer.",
            "action": "Telefondaki 3D zincirli kaba modelin gösterilmesi 2 saniye, ardından danışanın ofis stiline uyarlanan asil süt beyazı krom tasarımın 6 saniyelik parıltısı.",
            "trigger": "Dürüst Zevk Danışmanlığı. Müşteriye körü körüne 'yaparız' demek yerine, ona gerçekten yakışanı ve hayatını zorlaştırmayacak olanı öneren usta saygısı.",
            "audience_reaction": "'İyi ki vazgeçirmişsiniz bu yeni model bin kat daha asil!', 'Bana da böyle dürüst bir uzman lazım' yorumları.",
            "gulsah_tone": "Mizahi ve samimi: 'Pinterest'teki her model günlük hayata uymaz kızlar :) Klavyede yazı yazamayacağınız tırnağı masamdan çıkaramam' gülümsemesi."
        },
        # Day 4: 4 Yıldır Masamızı Şenlendiren Sadık Danışanımızın Hikayesi
        {
            "tripod": "45° açıda, iki kişinin karşılıklı sohbet anını arkadan yakalayan sinematik açı.",
            "focus": "1x Lens, -0.3 EV. Kahve fincanlarının buharına ve gülen yüzlere odak kilidi.",
            "hands": "Gülşah elmas frezeyi zahmetsizce kullanırken danışan kahvesinden bir yudum alır.",
            "action": "Karşılıklı kahkaha atılan o doğal dostluk anı 2 saniye, ardından 4 yıldır korunan doğal tırnakların 6 saniyelik kusursuz uzama videosu.",
            "trigger": "Aidiyet & Yıllara Dayanan Güven. Müşteri-uzman ilişkisinin ötesinde bir dostluk alanı olduğunu görmek yeni gelenlere güven verir.",
            "audience_reaction": "'Böyle bir tırnakçım olsun başka hiçbir şey istemem', '4 yıl aynı yere gitmek büyük sadakat tebrikler' yorumları.",
            "gulsah_tone": "İçten ve vefalı: 'Ezgi'yle masamızda 4 koca yıl geçti; aşklar, iş değişiklikleri, tatiller... Tırnaklar sadece bahane, sohbet paha biçilmez' de."
        },
        # Day 5: İlk Defa Protez Yaptıracak Olan Misafirimizin Korkusu
        {
            "tripod": "45° makro açı, ilk kez frezeyi gören tedirgin parmaklara odaklı.",
            "focus": "2x Makro, frezenin tırnağa değdiği ilk tüy hafifliğindeki ana odak kilidi.",
            "hands": "Danışanın hafif gergin eli, Gülşah'ın eli danışanın elini rahatlatmak için okşar.",
            "action": "Danışanın 'acıtır mı?' tedirginliğiyle frezeyi izlemesi 2 saniye, ardından freze değer değmez 'aa hiç hissetmiyorum bile!' diyerek rahatladığı 6 saniyelik gülümseme.",
            "trigger": "Acı Korkusunu Kırma (Fear Eraser). Hayatında hiç tırnak yaptırmamış ve korkan binlerce kadının kapıyı çalmasını sağlar.",
            "audience_reaction": "'Ben de acıyacak diye çok korkuyordum!', 'İlk kez yaptıracağım Ataşehir'de randevu alabilir miyim?' soruları.",
            "gulsah_tone": "Rahatlatıcı ve nazik: 'Korktuğunuz şey işlem değil, kötü anlatanlar :) Bakın, gıdıklanmaktan başka hiçbir şey hissetmeyeceksiniz' de."
        },
        # Day 6: Eşiyle Yıl Dönümü Yemeği İçin Sürpriz Bakım Seansı
        {
            "tripod": "45° açıda, masadaki zarif kırmızı gül buketi ve ellerin detayına odaklı.",
            "focus": "1x Lens, -0.2 EV. Yüzükteki taşın ve klasik Fransız manikürünün parıltısına odak kilidi.",
            "hands": "Danışan ellerini mermer masada dinlendirir, porselen fincanla uyum içindedir.",
            "action": "Çantadan çıkarılan akşam yemeği elbisesi fotoğrafı 2 saniye, ardından o elbiseye özel yapılan kusursuz kırmızı klasik manikürün 6 saniyelik asil duruşu.",
            "trigger": "Romantizm & Özel Hissetme Arzusu. Kadınların en özel günlerinde kendilerini baştan yaratma heyecanına ortak olur.",
            "audience_reaction": "'Kırmızının tonu tam bir afet!', 'Yıl dönümü için ben de böyle bir tırnak istiyorum' yorumları.",
            "gulsah_tone": "Heyecan ortaklığıyla: 'Akşam çok özel bir masa var, o masada kadeh kalktığında eller kusursuz konuşmalıydı. Kırmızının en asil tonunu seçtik' de."
        },
        # Day 7: Bana 'Bana Bırak, Sen Tasarla' Dediğinde Yaptığım Tasarım
        {
            "tripod": "90° dik tepe açısında, mermer masa ve fırça hareketlerine odaklı.",
            "focus": "2x Makro, fırçanın beyaz zemin üzerine çektiği soyut altın çizgiye odak kilidi.",
            "hands": "Gülşah'ın kendinden emin eli ince fırçayla serbest stil nail art çizer.",
            "action": "Gülşah'ın fırçayı eline alıp 'en sevdiğim cümle' tebessümü 2 saniye, ardından ortaya çıkan haute-couture minimalist altın varak tasarımının 6 saniyelik parıltısı.",
            "trigger": "Yaratıcı Deha & Sanatçı Özgürlüğü. Uzmana teslim olmanın getirdiği eşsiz lüks hissi.",
            "audience_reaction": "'Bana bırak diyen uzman candır!', 'Bu tasarıma bayıldım haftaya aynısını yapalım' yorumları.",
            "gulsah_tone": "Sanatçı coşkusuyla: 'Bir kadının masaya oturup 'Gülşah sana bırakıyorum' demesi benim için tuvalin başına geçmektir. İşte ortaya çıkan o zarif başyapıt' de."
        },
        # Day 8: Toplantı Arasında 1 Saatte Gelen CEO Danışanımız
        {
            "tripod": "45° açıda, masanın köşesindeki kapalı MacBook ve çalışan ellere odaklı.",
            "focus": "1x Lens, -0.3 EV. Mat siyah laptop ile pudra nude tırnakların kontrastına odak kilidi.",
            "hands": "Senkronize çalışan iki uzmanın hızlı ve sessiz manikür hareketi.",
            "action": "Masaya bırakılan araba anahtarı ve telefon 2 saniye, ardından 50 dakikada sıfır gecikmeyle bitirilen kusursuz yönetici tırnağının 6 saniyelik tok duruşu.",
            "trigger": "Güçlü Kadın / Kariyer Statüsü. Yoğun iş kadınlarına zaman kaybettirmeden en üst düzey protokol sunduğunu kanıtlar.",
            "audience_reaction": "'Tam bir iş kadını tırnağı bayıldım!', 'Toplantı arasına böyle sığması harika bir sistem' yorumları.",
            "gulsah_tone": "Kibar ve profesyonel: 'Saat 14:00'te yönetim kurulu toplantısı vardı. Masaya 13:00'te oturdu, 13:50'de kapıdan uğurladık. Zamanı yöneten kadınlara saygımız sonsuz' de."
        },
        # Day 9: Tırnaklarını Masada Saklayan Bir Misafirimizin Zaferi
        {
            "tripod": "45° açıda, danışanın ilk oturduğu andaki çekingen el hareketine odaklı.",
            "focus": "1x Lens, ellerin yumruk halinden gevşeme anına odak kilidi.",
            "hands": "Danışanın elleri başlangıçta masanın altında saklanır, Gülşah elleri nazikçe masanın üstüne alır.",
            "action": "Ellerin çekinerek masaya konduğu 2 saniye, ardından işlem bittiğinde danışanın aynaya bakıp 'artık ellerimi saklamayacağım' dediği 6 saniyelik gurur karesi.",
            "trigger": "İçsel Özgürleşme & Derin Rahatlama. Kusuru yüzünden utanan kadınların Linail'de güvende olduğunu gösterir.",
            "audience_reaction": "'Tüylerim diken diken oldu resmen bir kadına özgüven vermişsiniz', 'Ben de ellerimi saklıyorum randevu almak istiyorum' yorumları.",
            "gulsah_tone": "Duygusal ve kucaklayıcı: 'Buraya adım atan hiçbir kadın ellerinden utanmayacak. Burası kusurların saklandığı değil, zarafete dönüştüğü yerdir' de."
        },
        # Day 10: Başka Şehirden Uphill Towers'a Sırf Manikür İçin Gelen Misafir
        {
            "tripod": "45° açıda, stüdyonun ferah salonu ve Uphill manzarasını kadraja alarak.",
            "focus": "1x Lens, -0.2 EV. Pencereden süzülen doğal ışığa odak kilidi.",
            "hands": "Gülşah kahve ikram ederken danışanın elleri incelenir.",
            "action": "Danışanın 'Bursa'dan sırf senin için geldim' dediği an 2 saniye, ardından yapılan 4 haftalık garantili jel mimarisinin 6 saniyelik video kanıtı.",
            "trigger": "Yüksek Otorite & Uzaklardan Gelinmeye Değer Kalite (Magnetism). Ataşehir dışından da talep olduğunu görerek yerel kitleyi aciliyete sokar.",
            "audience_reaction": "'Şehirlerarası gelinecek kadar iyi gerçekten!', 'Ben Ataşehir'de oturup hala gelemedim hemen yazıyorum' yorumları.",
            "gulsah_tone": "Mahcup ama gururlu: 'Bursa'dan, Ankara'dan masamıza gelen danışanlarımızı görünce işimize olan aşkımız katlanıyor. Hoş geldin sefalar getirdin' de."
        },
        # Day 11: Düğün Sonrası Balayı Tırnakları: Kum ve Denize Meydan Okuma
        {
            "tripod": "45° makro açı, parlak deniz kabuğu yansıması veren inci tozuna odaklı.",
            "focus": "2x Makro, tırnak ucundaki sedefli ışıltıya odak kilidi.",
            "hands": "Sol el tırnakları çevirir, sağ el mikron fırçayla ekstra dayanıklı deniz kalkanı top coat sürer.",
            "action": "Bavul ve hasır şapka detayı 2 saniye, ardından kum, tuzlu su ve güneşe 3 hafta boyunca bana mısın demeyecek sedefli balayı tırnağının 6 saniyelik ışıltısı.",
            "trigger": "Tatil Heyecanı & Dayanıklılık İhtiyacı. Balayında tırnağı kırılmasın isteyen her gelinin hayalidir.",
            "audience_reaction": "'Balayında tırnağım kırılacak diye korkuyordum bu model tam aradığım şey!', 'Renk kodu nedir?' soruları.",
            "gulsah_tone": "Neşeli ve tatil havasında: 'Maldivler yolcusu gelinimize öyle bir top coat mühürledik ki, deniz tuzu bile parlaklığına dokunamaz :) İyi tatiller!' de."
        },
        # Day 12: Anne-Kız Günü: Birlikte Geçirilen 2 Saatlik Huzur Seansı
        {
            "tripod": "Geniş açıda, iki yan yana manikür masasını ve kahveleri kadraja alarak.",
            "focus": "1x Lens, -0.2 EV. İki kadının yan yana kahkahasına odak kilidi.",
            "hands": "Anne klasik zarif gül kurusu, kızı modern glazed donut tasarımını seçmiş eller yan yana.",
            "action": "Annenin kızının tırnağına bakıp gülümsemesi 2 saniye, ardından iki neslin masada buluştuğu zarafet dolu ellerin 6 saniyelik karesi.",
            "trigger": "Aile Sıcaklığı & Hediyeleşme Ritüeli. Anneler gününde veya hafta sonu anne-kız kaliteli vakit geçirme isteğini tetikler.",
            "audience_reaction": "'Annemi alıp hemen geleceğim çok tatlı bir ortam!', 'Anne-kız seansı için paketiniz var mı?' yorumları.",
            "gulsah_tone": "Sıcak ve nostaljik: 'Bugün masamızda en tatlı anne-kız sohbeti vardı. Biri zamansız klasik, diğeri modern trend... Güzellik nesilden nesile geçer' de."
        },
        # Day 13: Yıllardır Tırnak Yiyen Danışanımızın İlk Kırmızı Ojesi
        {
            "tripod": "45° açıda, kırmızı oje fırçasının tırnağa ilk değdiği ana odaklı.",
            "focus": "2x Makro, tırnak dibine sıfır yanaşan kırmızının pürüzsüz çizgisine odak kilidi.",
            "hands": "Gülşah nefesini tutarak kırmızı fırçayı çeker, danışan heyecanla izler.",
            "action": "Yıllarca kırmızı sürmeye cesaret edememiş danışanın oje sürülürken gözlerinin parladığı ve aynaya baktığı 6 saniyelik tarihi an.",
            "trigger": "Cesaret & Kadınsı Gücün Uyanışı. Kırmızı oje kadın psikolojisinde özgüvenin simgesidir.",
            "audience_reaction": "'Kırmızı oje bir kadının zaferidir tebrikler!', 'Eller resmen konuşuyor muazzam' yorumları.",
            "gulsah_tone": "Tüyleri diken diken eden bir samimiyetle: 'Yıllarca tırnaklarını saklayan bir kadına ilk kırmızı ojesini sürmek bu mesleğin en büyük ödülüdür' de."
        },
        # Day 14: Çok Önemli Bir İş Görüşmesine Gidecek Danışanımızın Güçlü Elleri
        {
            "tripod": "45° açıda, şık deri evrak çantası ve masadaki ellere odaklı.",
            "focus": "1x Lens, -0.3 EV. Minimalist fildişi French tırnakların tok duruşuna odak kilidi.",
            "hands": "Danışan ellerini güvenle kavuşturur, tırnaklar kusursuz bir profesyonellik yayar.",
            "action": "Danışanın 'Yarın hayatımın en önemli sunumu var' cümlesi 2 saniye, ardından tokalaşırken muazzam bir ilk izlenim bırakacak asil tırnakların 6 saniyelik gücü.",
            "trigger": "Profesyonel Statü & İlk İzlenim Psikolojisi. İş dünyasında bakımlı ellerin imza niteliğinde olduğunu hatırlatır.",
            "audience_reaction": "'Eller kesinlikle ilk izlenimdir çok doğru!', 'O fildişi tonun kodunu alabilir miyim?' yorumları.",
            "gulsah_tone": "Güç veren bir koç gibi: 'İş görüşmesinde dosyanızı uzatırken ilk görünen şey ellerinizdir. Ona öyle bir tırnak yaptık ki, o masadan ret cevabı çıkamaz' de."
        },
        # Day 15: Masada Kahve İçerken Uyuya Kalan Yorgun Misafirimiz
        {
            "tripod": "45° açıda, loş stüdyo ışığı ve dinlenen danışana odaklı.",
            "focus": "1x Lens, -0.3 EV. Müşterinin koltuktaki huzurlu duruşuna odak kilidi.",
            "hands": "Gülşah sessizce, çıt çıkarmadan tüy gibi frezeyle çalışmaya devam eder.",
            "action": "Yorgunluktan gözlerini kapatıp hafifçe uykuya dalan danışanın huzuru 2 saniye, ardından uyanıp tırnaklarını kusursuz görünce yüzüne yayılan tebessümün 6 saniyesi.",
            "trigger": "Tükenmişlikten Kaçış & Tam Güven Sığınağı. Yoğun hayattan yorulmuş kadınlara masanın aynı zamanda bir terapi ve dinlenme köşesi olduğunu hissettirir.",
            "audience_reaction": "'Bir tırnakçıda uyuyabilmek en büyük güven göstergesidir!', 'Bana da böyle bir dinlenme lazım' yorumları.",
            "gulsah_tone": "Fısıltı gibi naif bir sesle: 'Masamıza oturup gözlerini kapatıp dinlenen misafirlerimiz bizim en büyük gururumuz. Burada sadece güzelleşmiyorsunuz, dinleniyorsunuz' de."
        },
        # Day 16: Benden 'Sadece 1 Tırnağa Taş Koyalım' Deyip 10 Tırnağı Taşlattı!
        {
            "tripod": "90° dik açıda, pırıltılı Swarovski taş kutusu ve cımbıza odaklı.",
            "focus": "2x Makro, kristalin ışık kırmasına odak kilidi.",
            "hands": "Gülşah gülerek cımbızla taşları dizerken danışan 'bir tane daha koyalım' der.",
            "action": "Danışanın 'Gülşah sadece yüzük parmağına küçük bir taş yeter' deyişi 2 saniye, ardından 10 parmağın da ışıl ışıl mücevhere döndüğü 6 saniyelik eğlenceli kurgu.",
            "trigger": "Eğlenceli Kadın Dayanışması & Kendini Şımartma. Her kadının kuaförde yaşadığı o tatlı 'biraz daha ışıltı' anını tiye alır.",
            "audience_reaction": "'Hahahah tam olarak ben! Başta sade derim sonunda disko topu olurum', 'Taşlar ne kadar dayanıyor?' yorumları.",
            "gulsah_tone": "Muzip ve neşeli: 'Kadınlar masaya oturunca 'ben çok sadeyimdir' der ama o taş kutusu açılınca her şey değişir :) Çok da yakıştı ama!' gülüşü."
        },
        # Day 17: Kırılan Tırnağı Yüzünden Ağlayarak Kapımızı Çalan Danışan
        {
            "tripod": "45° açıda, tırnağın kırık yarık hattına odaklı.",
            "focus": "2x Makro, hasarlı tırnak plağına odak kilidi.",
            "hands": "Gülşah elinde ılık ıslak mendille danışanın elini sakinleştirir.",
            "action": "Danışanın üzgün yüz ifadesi ve kırık tırnak 2 saniye, ardından 20 dakikada şablon jelle yeniden yapılan ve danışanın gözyaşını silip güldüğü 6 saniyelik rahatlama.",
            "trigger": "Çaresizlikten Kurtarma & Empati. Tırnağı kırılınca günü mahvolan kadınların duygusal kurtarıcısıdır.",
            "audience_reaction": "'Tırnağı kırılınca ağlayan tek ben değilmişim!', 'Hızır gibi yetişmişsiniz ellerinize sağlık' yorumları.",
            "gulsah_tone": "Şefkatli bir dost gibi: 'Kimine göre alt tarafı bir tırnak, bize göre haftalarca verilen bir emek. Üzülmek yok, Gülşah burada' de."
        },
        # Day 18: Fransa'dan Tatile Gelip Bizi Tercih Eden Ziyaretçimiz
        {
            "tripod": "45° açıda, stüdyonun lüks köşesi ve tırnak işlemlerine odaklı.",
            "focus": "1x Lens, -0.2 EV. Doğal gün ışığında parlayan Fransız manikürüne odak kilidi.",
            "hands": "Gülşah zarifçe top coat sürerken danışan Fransızca teşekkür eder.",
            "action": "Paris'ten gelen misafirin 'Paris'te bile böyle Rus manikürü bulamadım' deyişi 2 saniye, ardından tırnakların 6 saniyelik uluslararası standarttaki zarafeti.",
            "trigger": "Küresel Standart & Gurur Duyulan Kalite. Yurt dışından gelenlerin bile Linail'i övmesi yerel kadınlarda 'ben burada en iyisine gidiyorum' hissi uyandırır.",
            "audience_reaction": "'Fransız kadınını bile hayran bıraktınız helal olsun!', 'Ataşehir'in gururu' yorumları.",
            "gulsah_tone": "Gururla ve mütevazılıkla: 'Paris'ten gelen misafirimizden 'Fransa'da böyle temiz kütikül işçiliği yok' sözünü duymak tüm ekibimizi gururlandırdı' de."
        },
        # Day 19: Tırnak Modeli Seçerken 20 Dakika Kararsız Kalan Misafirimiz
        {
            "tripod": "90° dik açıda, masaya serilmiş 50 farklı nude oje paletine odaklı.",
            "focus": "1x Lens, oje paletlerinin ton sür ton geçişlerine odak kilidi.",
            "hands": "Danışanın parmakları 3 farklı nude ton arasında gidip gelir, Gülşah ten rengine göre eline sürer.",
            "action": "Danışanın 'Gülşah hepsi aynı gibi ama hepsi çok farklı!' çaresizliği 2 saniye, ardından ten rengine en kusursuz oturan o tonun sürülüp parladığı 6 saniye.",
            "trigger": "Tatlı Kararsızlık & Renk Seçim Rehberliği. Nude ton seçerken 20 dakika harcayan her kadının birebir kendisini bulduğu mizahi video.",
            "audience_reaction": "'Aynı ben! 50 tane nude ojeye bakıp kararsız kalırım', 'Seçtiğiniz tonun numarası nedir harika olmuş' soruları.",
            "gulsah_tone": "Kahkaha atarak: 'Nude oje deyip geçmeyin; 100 farklı tonu var ve teninizin alt tonuna göre biri ellerinizi soluk gösterirken diğeri pırlanta gibi parlatır' de."
        },
        # Day 20: Hamilelik Döneminde Güvenli Medikal Bakım Arayan Anne Adayı
        {
            "tripod": "45° açıda, anne adayının rahat koltuktaki huzurlu oturuşuna odaklı.",
            "focus": "1x Lens, -0.3 EV. Otoklavdan yeni çıkan cerrahi steril poşete odak kilidi.",
            "hands": "Gülşah cerrahi eldivenleriyle su kullanmadan tamamen medikal kuru bakımı uygular.",
            "action": "Otoklav poşetinin anne adayının gözü önünde açılışı 2 saniye, ardından kimyasal kokusuz, sıfır formaldehitli güvenli manikürün 6 saniyelik huzurlu seansı.",
            "trigger": "Anne Adayı Güvenliği & Toksisite Korkusu. Hamilelikte kuaföre gitmeye korkan kadınlara tıbbi seviyede güven aşılar.",
            "audience_reaction": "'Hamileyim ve maniküre gitmeye çok korkuyordum, aradığım yer tam burası!', 'Randevu alabilir miyim?' yorumları.",
            "gulsah_tone": "Son derece koruyucu bir uzmanlıkla: 'Hamilelik döneminde tırnak etleri daha hassastır ve enfeksiyon riski kabul edilemez. Masamızda cerrahi otoklav güvencesiyle içiniz tamamen rahat' de."
        },
        # Day 21: Ekrandaki Tasarımı Beğenmeyip Masada Sıfırdan Çizdiğimiz An
        {
            "tripod": "45° makro açı, fırçanın tırnak yüzeyindeki serbest dansına odaklı.",
            "focus": "2x Makro, ince fırçanın mikron kontür hareketlerine odak kilidi.",
            "hands": "Sol el tırnağı çevirir, sağ el silgi yerine temiz fırçayla çizgiyi yeniden çeker.",
            "action": "Danışanın 'içime tam sinmedi' dediği o samimi an 2 saniye, ardından Gülşah'ın 'hiç sorun değil baştan yapıyoruz' diyerek danışanın içine sinen tasarımı yarattığı 6 saniye.",
            "trigger": "Koşulsuz Memnuniyet & Kaprissiz Hizmet. Kuaförlerde 'beğenmedim' demeye çekinen kadınlar için en büyük güvence.",
            "audience_reaction": "'İşte müşteri memnuniyeti budur! Bazı yerlerde surat asıyorlar', 'Bu tavrınız için bile gelinir' yorumları.",
            "gulsah_tone": "Gönül rahatlığıyla: 'Masamdan içine %100 sinmeyen hiçbir tırnakla kimse kalkamaz. Gerekirse 5 kere sileriz, o tebessümü görmeden uğurlamayız' de."
        },
        # Day 22: Göz Kapağı Ameliyatı Sonrası Doğal Kirpik Arayan Danışanımız
        {
            "tripod": "Kirpik masasında 45° açıda, doğal kirpik hattına odaklı.",
            "focus": "2x Makro, tüy gibi hafif 0.07 mikron kirpiklerin dizilişine odak kilidi.",
            "hands": "Cımbızlar mikro kirpikleri doğal kıvrımla yerleştirir.",
            "action": "Ameliyat sonrası hassas göz kapağına sıfır ağırlık yapan doğal ipek kirpiklerin takıldığı ve göz açıldığında sıfır batma hissinin yaşandığı 6 saniyelik konfor.",
            "trigger": "Medikal Hassasiyet & Doğallık Arayışı. Ağır, yapay kirpiklerden korkan olgun kadınları hedefler.",
            "audience_reaction": "'O kadar doğal durmuş ki sanki kendi kirpiği!', 'Ameliyat sonrası için çok iyi bir seçenek' yorumları.",
            "gulsah_tone": "Hassasiyetle: 'Göz kapağı ameliyatı geçiren kadınlara kalın kirpik takamazsınız. Tüyden bile hafif 0.07 mikron ipeklerle kendi kirpiğiniz gibi bir doğallık kurduk' de."
        },
        # Day 23: Kendi Kendine Protez Çıkarmaya Çalışıp Pişman Olan Misafir
        {
            "tripod": "45° açıda, tırnak plağındaki soyulma hasarına odaklı.",
            "focus": "2x Makro, hasarlı tırnak plağının onarım protokolüne odak kilidi.",
            "hands": "Gülşah şefkatle danışanın elini tutar, onarıcı baz sürer.",
            "action": "Danışanın mahcup bir şekilde 'Gülşah bir delilik yaptım soydum' deyişi 2 saniye, ardından azarlamadan tırnağı onarıp eski gücüne kavuşturduğumuz 6 saniye.",
            "trigger": "Yargılanmama Rahatlaması (Non-Judgmental Sanctuary). Hata yapmış kadını azarlamayan, şefkatle toparlayan uzman sevgisi.",
            "audience_reaction": "'Beni azarlamayan bir tırnakçı mı? Cennettesiniz resmen!', 'Ben de yaptım hemen geliyorum' yorumları.",
            "gulsah_tone": "Gülümseyerek ve sarılarak: 'Burada azar işitmek yok kızlar :) Olmuşla ölmüşe çare yok, gelin o tırnağı beraber eski haline getirelim' de."
        },
        # Day 24: Doğum Gününde Kendine VIP Bakım Hediye Eden Misafirimiz
        {
            "tripod": "45° açıda, masadaki zarif pasta mumu ve Linaura aromatik mumuyla.",
            "focus": "1x Lens, -0.2 EV. Şampanya kadehi veya porselen kahve fincanına odak kilidi.",
            "hands": "Danışan ellerini ışıkta çevirirken tırnaklar pırlanta gibi parlar.",
            "action": "Masaya gelen küçük doğum günü sürprizi ve danışanın gülümsemesi 2 saniye, ardından kendine hediye ettiği kusursuz Spa bakımının 6 saniyelik zarafeti.",
            "trigger": "Self-Love & Kendini Ödüllendirme. Kadınların doğum günlerinde kendilerine özel bir ritüel arama güdüsünü yakalar.",
            "audience_reaction": "'Doğum günümde ben de kendime bu randevuyu alacağım!', 'Çok zarif düşünmüşsünüz tebrikler' yorumları.",
            "gulsah_tone": "Kutlama coşkusuyla: 'Bir kadının kendine verebileceği en güzel doğum günü hediyesi 2 saatlik kesintisiz huzur ve bakım seansıdır. İyi ki doğdun Elif!' de."
        },
        # Day 25: Aynı Anda 3 İşlem Yaptırıp Zamana Meydan Okuyan Avukat
        {
            "tripod": "Geniş sinematik açıda, VIP odada 3 uzmanın senkronize çalışmasına odaklı.",
            "focus": "1x Lens, -0.3 EV. Sessiz ve ahenkli takım çalışmasına odak kilidi.",
            "hands": "Biri manikür yaparken diğeri pedikür koltuğunda, kirpik uzmanı baş ucunda çalışır.",
            "action": "Danışanın VIP koltukta gözlerini kapatıp dinlenmesi 2 saniye, ardından 1.5 saat sonra baştan aşağı yenilenmiş olarak duruşmaya yetiştiği 6 saniyelik süper lüks.",
            "trigger": "Zaman Zenginliği (Ultimate Time Efficiency). Saatlerce kuaförde çürümek istemeyen elit kadınların tek tercihi.",
            "audience_reaction": "'Aynı anda 3 işlem benim hayalim resmen!', 'Ataşehir'de bunu yapan tek yersiniz fiyatı nedir?' yorumları.",
            "gulsah_tone": "Etkileyici bir güçle: 'Ayrı ayrı randevularla bütün gününüzü öldürmeyin. VIP odamızda 1.5 saatte manikür, pedikür ve kirpiğinizi bitirip sizi gününüze geri veriyoruz' de."
        },
        # Day 26: 10 Yıl Sonra İlk Kez Manikür Yaptıran Misafirimizin Tepkisi
        {
            "tripod": "45° açıda, danışanın tırnaklarına şaşkınlıkla baktığı ana odaklı.",
            "focus": "1x Lens, ellerin dönüşüm sonrası pürüzsüzlüğüne odak kilidi.",
            "hands": "Danışan parmaklarını yavaşça açar, sanki kendi elleri değilmiş gibi inceler.",
            "action": "Danışanın '10 yıldır ellerim böyle görünmüyordu' diyerek gözlerinin dolduğu 2 saniye, ardından o zarif dokunuşun elleri 10 yaş gençleştirdiği 6 saniye.",
            "trigger": "Yeniden Doğuş & Öz Şefkatin Hatırlanması. Kendini uzun süredir ihmal etmiş anneler ve kadınlar için güçlü bir uyanış çağrısı.",
            "audience_reaction": "'Gözlerim doldu resmen kendimi ihmal ettiğimi fark ettim', 'Hemen annemle kendime randevu alıyorum' yorumları.",
            "gulsah_tone": "Duygusal ve dokunaklı: 'Kendinizi ne kadar ihmal etmiş olursanız olun; bir saatlik özenli bir dokunuş ellerinizi ve ruhunuzu yeniden canlandırmaya yeter' de."
        },
        # Day 27: Nail Artı Görünce Masada Dans Eden Enerjik Danışanımız
        {
            "tripod": "45° açıda, danışanın yüzündeki mutluluk ve ellerine odaklı.",
            "focus": "1x Lens, tırnaklardaki eğlenceli krom ve pastel desenlere odak kilidi.",
            "hands": "Danışan parmaklarını ritmik olarak kameraya doğru şaklatır ve dans ettirir.",
            "action": "Tırnağını görüp yerinde duramayan danışanın tatlı neşesi 2 saniye, ardından tırnakların ışık altındaki kusursuz enerjisi 6 saniye.",
            "trigger": "Saf Neşe & Dopamin Patlaması. Manikürün verdiği mutluluğu ve enerjiyi izleyiciye geçirerek anında paylaşım yaptırır.",
            "audience_reaction": "'Enerjiniz harika ben de böyle sevinirdim!', 'Tasarım aşırı tatlı olmuş' yorumları.",
            "gulsah_tone": "Gülerek ve coşkuyla: 'Masadan böyle kalkmayan danışanımız olunca biz işimizi yapmamış sayıyoruz :) O neşe bütün stüdyoya yayıldı!' de."
        },
        # Day 28: Sevgilisi Tarafından Randevusu Alınan Sürpriz Seans
        {
            "tripod": "45° açıda, stüdyoya şaşkınlıkla giren misafirimize odaklı.",
            "focus": "1x Lens, masadaki 'Sana Özel' not kartına odak kilidi.",
            "hands": "Danışan masadaki notu okur, Gülşah kahvesini ikram eder.",
            "action": "Danışanın kapıda yaşadığı şaşkınlık ve mutluluk 2 saniye, ardından ona özel hazırlanan VIP bakım seansının 6 saniyelik lüks detayları.",
            "trigger": "Düşünülmüş Hediye İlhamı. Erkeklere hediye fikri verirken kadınlara da 'keşke bana da yapılsa' dedirterek etiketleme (Tag) patlaması yaratır.",
            "audience_reaction": "'Kocama hemen bu videoyu atıyorum :)', 'Mükemmel bir hediye fikri bayıldım' etiketlemeleri.",
            "gulsah_tone": "Gülümseyerek: 'Beyler not alsın: Bir kadına alınabilecek en ince ve en mutlu edici hediye onun için kapatılmış bir VIP bakım seansıdır' de."
        },
        # Day 29: Kendi Tırnaklarını Uzatmayı Başaran Danışanımızın Sevinç Çığlığı
        {
            "tripod": "45° makro açı, kendi doğal tırnaklarının uzunluğuna odaklı.",
            "focus": "2x Makro, protez olmayan doğal tırnağın alt dokusuna odak kilidi.",
            "hands": "Danışan tırnaklarını masaya 'tıkır tıkır' vurur, doğal tırnak sesini dinletir.",
            "action": "Danışanın tırnaklarını masaya vurup 'Gülşah bunlar benim kendi tırnaklarım!' deyişi 2 saniye, ardından 6 saniyelik doğal tırnak dayanıklılık testi.",
            "trigger": "Başarı Hissi & Kendi Tırnağına Kavuşma Arzusu. Protez olmadan kendi tırnağını uzatmak isteyenlere rehber olur.",
            "audience_reaction": "'Kendi tırnağı olduğuna inanamıyorum harikasınız!', 'Ben de uzatmak istiyorum jel güçlendirme ne kadar?' yorumları.",
            "gulsah_tone": "Gururlu bir antrenör gibi: 'İşte 3 aylık sabrın sonu. Sıfır protez, sadece doğru jel güçlendirme ve kendi doğal tırnakları. İsteyince başaramayacağımız tırnak yok' de."
        },
        # Day 30: Aydan Kalanlar: Masamızda Çözülen 30 Harika Hikaye
        {
            "tripod": "45° sinematik açıda, stüdyonun gün batımındaki sıcak mermer ambiyansına odaklı.",
            "focus": "1x Lens, -0.3 EV. Yanan Linaura mumuna ve masada kahvesini yudumlayan Gülşah'a odak kilidi.",
            "hands": "Gülşah iki elini fincanın etrafında birleştirir, kameraya doğrudan konuşur.",
            "action": "Bu ay masamızda gülünen, dertleşilen ve güzelleştirilen tüm ellerin sinematik supercut montajının 6 saniyelik nostaljisi.",
            "trigger": "Kolektif Samimiyet & Topluluk Ruhu. İzleyiciyi Linail ailesinin bir parçası olmaya davet eden zirve kapanış.",
            "audience_reaction": "'İzlediğim en samimi ve kaliteli güzellik sayfası', 'Gelecek ay ben de o masada olacağım' yorumları.",
            "gulsah_tone": "İçten bir teşekkürle: 'Bu ay masamızı sadece elleriyle değil, hikayeleriyle, kahkahalarıyla şenlendiren tüm harika kadınlara teşekkürler. Önümüzdeki ay siz de yerinizi alın' de."
        }
    ]
    return entries

print("Storytelling cues & psychology generator ready.")
