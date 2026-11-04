import json

def get_authority_cues_and_psychology():
    # 30 unique entries for authority program
    entries = [
        # Day 1: Tırnak Nefes Alır mı? Keratin Gerçeği
        {
            "tripod": "Telefonu göz hizasında 45° açıyla tırnak plağına 15 cm yaklaştırın.",
            "focus": "2x Makro, tırnak plağının keratin pullarının makro dokusuna odak kilidi.",
            "hands": "Sol el tırnağı tutar, sağ el mikro fırçanın ucuyla tırnak yüzeyini işaret eder.",
            "action": "Kameraya doğrudan 'Tırnağım nefes alsın diye ojeyi sildim diyorsanız...' diyerek başlayın, ardından tırnak plağının mikron yapısını göstererek 6 saniye anlatımı tamamlayın.",
            "trigger": "Mit Çökertme & Entelektüel Aydınlanma. Kadınlar yıllardır inandıkları 'hava alma' efsanesinin bilimsel gerçeğini öğrenince otoriteye anında bağlanır.",
            "audience_reaction": "'Yıllardır yanlış biliyormuşum çok teşekkürler!', 'Peki jel tırnak plağına hiç mi zarar vermez?' soruları.",
            "gulsah_tone": "Ders verir gibi değil, sohbet ederken tatlı bir bilgi paylaşır gibi: 'Bunu bana her gün masada soruyorsunuz, gelin doğrusunu konuşalım' samimiyeti."
        },
        # Day 2: Jel Neden Lambada Yanar? (Ekzotermik Reaksiyon)
        {
            "tripod": "UV lambanın girişini yandan görecek 30° açıda sabitleyin.",
            "focus": "1x Lens, lambanın içindeki mor LED ışık huzmesine odak kilidi.",
            "hands": "Elin lambaya giriş anı ve parmakların lambanın tabanında dinlenişi.",
            "action": "Elin lambaya girdiği anı çekin, hafifçe elin dışarı çıkarılıp ters çevrildiği o profesyonel refleksi 6 saniye gösterin.",
            "trigger": "Fiziksel Korkunun Açıklanması. Lambadaki yanma hissi kadınları korkutur; 'tırnağım mı yandı?' endişesini kimya bilimiyle yatıştırmak güven inşa eder.",
            "audience_reaction": "'Meğer polimerleşme reaksiyonuymuş içim rahatladı!', 'Elinizi hemen dışarı çıkarın taktiği harika' yorumları.",
            "gulsah_tone": "Şefkatli bir uyarıcı: 'O yanma anında elinizi içeride tutup acı çekmeyin; hemen dışarı alıp ters çevirin, 3 saniyede geçer' de."
        },
        # Day 3: Tırnak Etlerini Makasla Kesmek Neden Hatadır?
        {
            "tripod": "Masanın 45° açısında, tırnak etinin makro planına odaklı.",
            "focus": "2x Makro, frezenin kuru deriyi toza çevirdiği hatta odak kilidi.",
            "hands": "Sol el parmağı gergin tutar, sağ el elmas frezeyi kütiküle temas ettirmeden havada gösterir.",
            "action": "Makasın tırnak etine yaklaştığı 'dur' uyarısı karesi 2 saniye, ardından Rus frezesiyle toz gibi süpürülen pürüzsüz kütikül cebi 6 saniye.",
            "trigger": "Hata Yüzleşmesi & Alışkanlık Kırma. Kuaförlerde makasla et kestirip sonra pişman olan kadınların kök sorununu çözer.",
            "audience_reaction": "'Kestikçe daha çok çıkıyordu meğer sebebi buymuş!', 'Rus manikürü için randevu almak istiyorum' yorumları.",
            "gulsah_tone": "Net ve tavizsiz bir zanaatkar otoritesi: 'Vücut akıllıdır; makasla kesersen kendini korumak için kalın deri üretir. Çözüm kesmek değil, cilalamaktır' de."
        },
        # Day 4: Tırnak Plağındaki Çizgiler ve Yaş Alma
        {
            "tripod": "45° makro açı, tırnak üzerindeki dikey çizgileri net gösterecek hizada.",
            "focus": "2x Makro, dikey çizgilerin ışık altındaki çizgisel gölgesine odak kilidi.",
            "hands": "Sol el parmağı ışıkta hafifçe eğer, dikey çizgilerin gölgesi kameraya yansır.",
            "action": "Işık altında dikey çizgili tırnak yüzeyini 2 saniye gösterin, ardından kauçuk bazla doldurulup cam gibi düzleşen yüzeyi 6 saniye kaydırın.",
            "trigger": "Yaşlanma / Kusur Kaygısının Yatıştırılması. Dikey çizgileri hastalık sanan kadınlara doğal olduğunu gösterip estetik çözümü sunar.",
            "audience_reaction": "'Tırnağım yaşlanıyor sanıyordum çok rahatladım', 'Bu baz tırnağa zarar vermeden mi düzleştiriyor?' soruları.",
            "gulsah_tone": "Biyolog sakinliğiyle: 'Yüzümüzde nasıl mimik çizgileri oluşuyorsa tırnakta da dikey çizgiler olur. Bu bir kusur değil, tırnağın karakteridir' de."
        },
        # Day 5: Apeks Mimarisi: Tırnak Neden Kırılmaz?
        {
            "tripod": "0° yan profil açısında, tırnak kavisiyle aynı hizada.",
            "focus": "2x Makro, tırnağın C-kavisi tepe noktasına odak kilidi.",
            "hands": "Sol el parmağı profilden tutar, sağ el fırçanın arkasıyla tepe kavisini işaret eder.",
            "action": "Yandan tırnağın zarif kavisini 2 saniye gösterin, ardından tırnağın masaya tok bir sesle 'tık' diye vurulup esnediğini 6 saniye çekin.",
            "trigger": "Kalite & Sağlamlık Merakı. Neden bazı protezlerin takoz gibi kalın, bazılarınınsa incecik ama kırılmaz olduğunu açıklar.",
            "audience_reaction": "'Bana hep kalın kalıp gibi yapıyorlardı, sizinki ne kadar zarif!', 'Apeks noktasını bu kadar iyi anlatan ilk uzman' yorumları.",
            "gulsah_tone": "Mimari bir özgüvenle: 'Kalınlık sağlamlık demek değildir; doğru mimari tırnağı tüy gibi hafif ama çelik gibi sağlam yapar' de."
        },
        # Day 6: Kalıcı Oje Tırnağı Sarıya Boyar mı?
        {
            "tripod": "45° açıda, tırnak plağından ojenin tek parça çıkarıldığı ana odaklı.",
            "focus": "1x Lens, -0.2 EV. Alttan çıkan doğal pembe tırnak rengine odak kilidi.",
            "hands": "Sol el parmağı tutar, sağ el pamukla tırnak plağını temizler.",
            "action": "Koyu oje çıkarıldıktan sonra alttan çıkan pırıl pırıl pembe tırnağı kameraya 6 saniye boyunca gösterin.",
            "trigger": "Leke & Toksisite Korkusunun Giderilmesi. Kalıcı ojenin tırnağı sararttığı korkusunu kaliteli baz protokolüyle çürütür.",
            "audience_reaction": "'Benim tırnaklarım sararıyordu meğer ucuz baz kullanıyorlarmış!', 'Hangi bazı kullanıyorsunuz?' soruları.",
            "gulsah_tone": "Dürüst ve bilgilendirici: 'Tırnağı sarartan oje değil, araya sürülen kalitesiz bazlardır. Bizim bazımız tırnakla pigment arasına görünmez bir kalkan çeker' de."
        },
        # Day 7: Genosys EZ CO2 Karboksi: Cilt Neden Kızarır?
        {
            "tripod": "Kabin koltuğu yanında 45° yüz hizasında softbox aydınlatmalı.",
            "focus": "1x Lens, yanak bölgesindeki köpüren karboksi jelin mikro kabarcıklarına odak kilidi.",
            "hands": "Gülşah'ın nitril eldivenli elleri karboksi maskesini danışanın yüzüne nazikçe yerleştirir.",
            "action": "Maskenin yüze değdiği an çıkan hafif 'cızz' köpürme sesini ve ardından cildin anında parlayan oksijenlenmiş ışıltısını 6 saniye çekin.",
            "trigger": "Bilimsel Merak & Anti-Aging Arzusu. Karboksi terapisindeki hafif kızarıklığın aslında hücresel oksijen patlaması (Bohr etkisi) olduğunu açıklamak elit güven sağlar.",
            "audience_reaction": "'O köpürme anı harika görünüyor!', 'Cildim çok mat karboksi iyi gelir mi, seans ücreti nedir?' yorumları.",
            "gulsah_tone": "Klinik estetisyen zarafetiyle: 'Cildiniz hafif kızarıyorsa korkmayın; hücreleriniz şu an oksijene boğuluyor. 10 dakika sonra aynada bebek teni göreceksiniz' de."
        },
        # Day 8: İpek Kirpik Doğal Kirpiği Döker mi?
        {
            "tripod": "Kirpik uzanma koltuğunun baş ucunda, makro kirpik ayrımına odaklı.",
            "focus": "2x Makro, tek bir doğal kirpiğe tek bir mikron ipek kirpiğin yapışma noktasına odak kilidi.",
            "hands": "İki eldeki medikal cımbızlar: Sol cımbız tek bir kirpiği izole eder, sağ cımbız ipeği kondurur.",
            "action": "Cımbızın tek bir doğal kirpiği mikron hassasiyetinde izole edip tüy gibi hafif ipeği kondurduğu o cerrahi 6 saniyeyi çekin.",
            "trigger": "Göz Sağlığı & Kirpik Kaybı Korkusu. 'Kendi kirpiğim dökülür mü' endişesi yaşayan kadınların 1 numaralı itirazını anında yok eder.",
            "audience_reaction": "'Bana başka yerde demet yapıştırdılar hepsi döküldü, tek tek takılması şartmış meğer', 'Ataşehir'de randevu alacağım' yorumları.",
            "gulsah_tone": "Cerrahi bir hassasiyetle: 'Kirpiği döken ipek kirpik değildir; birbirine yapıştırılan kaba demetlerdir. Tek tek izole edilen kirpik doğal dökülme döngüsünde uzar ve düşer' de."
        },
        # Day 9: Tırnak Yatağı Neden Asla Törpülenmez?
        {
            "tripod": "45° makro açı, tırnak plağının parmak etiyle buluştuğu hatta odaklı.",
            "focus": "2x Makro, tırnak plağının doğal parlaklığına odak kilidi.",
            "hands": "Sol el tırnağı tutar, sağ el yumuşak parlatıcı buffer'ı nazikçe dokundurur.",
            "action": "Sert törpünün tırnağa yaklaştırılmayıp kenara bırakılışını, yerine kadife buffer ile nazikçe dokunulduğu 6 saniyelik güven anını çekin.",
            "trigger": "Gereksiz Agresif İşlemlerden Korunma. Tırnaklarının üstünün törpüyle oyulmasından korkan kadınlara derin bir nefes aldırır.",
            "audience_reaction": "'Önceki kuaförüm tırnağımı oyup inceltmişti canım çok yandı!', 'Harikasınız gerçekten bilerek yapıyorsunuz bu işi' yorumları.",
            "gulsah_tone": "Koruyucu bir hekim tavrıyla: 'Tırnak plağının üstü zımparalanacak bir tahta değildir. Oraya sadece jelin tutunacağı mikron düzeyde matlık verilir, fazlası cinayettir' de."
        },
        # Day 10: Kış Aylarında Tırnaklar Neden Daha Çok Çatlar?
        {
            "tripod": "45° açıda, Linaura botanik mumunun eriyen ılık yağının tırnağa damlayışına odaklı.",
            "focus": "1x Lens, -0.2 EV. Damlayan ılık botanik yağın kütiküle yayılışına odak kilidi.",
            "hands": "Sol el danışanın elini tutar, sağ el ılık botanik mumuyla tırnak diplerine dairesel masaj yapar.",
            "action": "Ilık Linaura yağının tırnak etine masajla yedirildiği ve kurumuş derinin anında ipeğe dönüştüğü 6 saniyeyi çekin.",
            "trigger": "Mevsimsel Çaresizlik & Lüks Bakım İhtiyacı. Kışın elleri kuruyup çatlayan kadınlara evde yapamayacakları botanik bir çözüm sunar.",
            "audience_reaction": "'Kışın tırnaklarım felaket oluyor o mum nedir acaba?', 'Stüdyoda bu masajı yapıyor musunuz?' soruları.",
            "gulsah_tone": "Sıcak ve samimi: 'Soğuk hava tırnaktaki nemi çeker alır. Kışın sadece krem yetmez; lipid bariyerini mühürleyen sıcak botanik yağlar şarttır' de."
        },
        # Day 11: Neden 3 Haftada Bir Bakıma Gelmelisiniz?
        {
            "tripod": "0° yan profil açısında, 4 hafta uzamış tırnağın ağırlık merkezine odaklı.",
            "focus": "2x Makro, tırnağın serbest ucundaki uzama boşluğu ve apeks kaymasına odak kilidi.",
            "hands": "Sol el parmağı yatay tutar, sağ el fırça sapıyla kayan apeks noktasını gösterir.",
            "action": "Apeksin tırnak uzadıkça öne doğru kaydığı ve kaldıraç etkisiyle kırılmaya hazır hale geldiği 6 saniyelik statik analizi gösterin.",
            "trigger": "Düzenli Randevu Sadakati (Retention Psychology). Müşterinin 'daha uzamadı bekleyeyim' deyip tırnağını kırmasını önleyen mantıksal açıklama.",
            "audience_reaction": "'Aaa meğer tırnak uzadıkça ağırlık merkezi kayıyormuş!', 'Hemen 3. hafta için randevumu sabitleyeyim' tepkileri.",
            "gulsah_tone": "Mantıklı ve ikna edici: 'Biz sizi sık görmek istediğimiz için değil; tırnağınızın ağırlık merkezi öne kayıp kökten kırılmasın diye 3 haftada bir çağırıyoruz' de."
        },
        # Day 12: Tırnağı Evde Zorla Soyarsanız Ne Olur?
        {
            "tripod": "45° makro açı, soyulmuş tırnak plağının katmanlarına odaklı.",
            "focus": "2x Makro, soyulma sonucu matlaşmış mikron katmanlara odak kilidi.",
            "hands": "Sol el tırnağı tutar, sağ el büyütücü lupla tırnak yüzeyini inceler.",
            "action": "Mikroskopik loptan tırnak pullarının nasıl ayrıldığının gösterilmesi ve ardından onarıcı serumun sürülüş anı 6 saniye.",
            "trigger": "Görsel Şok & Kötü Alışkanlığı Durdurma. Tırnağını soymaya yeltenen kadının elini havada durduracak bilimsel yüzleşme.",
            "audience_reaction": "'Şu an tam soymak üzereydim videonuz önüme düştü vazgeçtim!', 'Çok net anlatmışsınız teşekkürler' yorumları.",
            "gulsah_tone": "Tatlı-sert bir uyarı: 'Ojenin ucunu tutup çektiğinizde sadece ojeyi çekmiyorsunuz; tırnağınızın 20 katmanlık keratin zırhını da beraberinde söküyorsunuz. Lütfen yapmayın' de."
        },
        # Day 13: Kauçuk Baz (Rubber Base) ile Normal Baz Farkı
        {
            "tripod": "45° açıda, iki farklı bazın cam yüzey üzerindeki esneme testine odaklı.",
            "focus": "2x Makro, kauçuk bazın esnek kıvamına odak kilidi.",
            "hands": "Sağ el fırçayla kauçuk bazı kaldırır, bal kıvamındaki elastikiyeti gösterir.",
            "action": "Normal bazın sert ve kırılgan yapısı 2 saniye, kauçuk bazın esnek ve darbe emici elastikiyetinin gösterildiği 6 saniyelik deney.",
            "trigger": "Premium Malzeme Bilinci. Neden bazı işlemlerin daha pahalı ve kaliteli olduğunu müşteriye sorgulatmadan kanıtlar.",
            "audience_reaction": "'İşte bu yüzden Linail Beauty'ye geliyorum, her malzemenin bir mantığı var', 'Benim tırnağıma kesin kauçuk lazım' yorumları.",
            "gulsah_tone": "Usta malzeme uzmanı edasıyla: 'Doğal tırnak canlıdır ve esner. Esnek bir dokunun üstüne taş gibi sert baz koyarsanız çatlar. Kauçuk baz tırnakla nefes alır' de."
        },
        # Day 14: Hassas Gözler İçin Medikal Kirpik Yapıştırıcısı
        {
            "tripod": "Kirpik masasında 45° açıda, medikal yapıştırıcı damlasına odaklı.",
            "focus": "2x Makro, yapıştırıcının yeşim taşı üzerindeki parlak damlasına odak kilidi.",
            "hands": "Sağ el cımbızla ipek kirpiği mikro damlaya batırıp çıkarır.",
            "action": "Buhar yapmayan, sıfır formaldehitli medikal yapıştırıcının tüy gibi hafif temasını ve danışanın gözünü açtığında sıfır kızarıklığını gösteren 6 saniye.",
            "trigger": "Göz Alerjisi & Yanma Korkusunun Aşılması. İpek kirpikten gözleri kan çanağına dönmüş kadınlara klinik bir vaha sunar.",
            "audience_reaction": "'Benim gözlerim çok hassas hep sulanır, bu yapıştırıcıyı denemek istiyorum', 'Ataşehir'de neredesiniz?' soruları.",
            "gulsah_tone": "Medikal titizlikle: 'Göz şakaya gelmez. Düşük kaliteli yapıştırıcıların dumanı gözü yakar. Bizim kullandığımız medikal formül sıfır buhar ve sıfır kızarıklıktır' de."
        },
        # Day 15: Tırnaktaki Beyaz Lekeler Kalsiyum Eksikliği midir?
        {
            "tripod": "45° makro açı, tırnak plağındaki beyaz puantiyelere odaklı.",
            "focus": "2x Makro, beyaz lekenin tırnak plağı içindeki derinliğine odak kilidi.",
            "hands": "Sol el tırnağı tutar, sağ el işaret parmağıyla lekeyi gösterir.",
            "action": "Tırnaktaki beyaz lekenin gösterilmesi 2 saniye, ardından tırnak köküne yapılan mikro darbe travmasının anlatıldığı 6 saniyelik görsel analiz.",
            "trigger": "Popüler Sağlık Efsanesini Çökertme. 'Süt içsem geçer mi' diyen kadınlara gerçek mekanik sebebi açıklar.",
            "audience_reaction": "'Annem hep kalsiyum eksik derdi meğer çarpmadanmış!', 'Harika bir bilgilendirme çok teşekkürler' yorumları.",
            "gulsah_tone": "Gülümseyerek: 'Hemen süt içmeye koşmayın :) O beyaz lekeler çoğu zaman kalsiyum eksikliği değil, tırnak kökünüzü kapıya veya masaya hafifçe çarpmanızın mikro hava kabarcığıdır' de."
        },
        # Day 16: Neden Bazı Ojeler 3 Günde Soyulur?
        {
            "tripod": "45° açıda, tırnak plağının dehidratör ile kurutulma anına odaklı.",
            "focus": "2x Makro, tırnak yüzeyindeki doğal yağ tabakasının buharlaşmasına odak kilidi.",
            "hands": "Sol el parmağı tutar, sağ el fırçayla asitsiz primer sürer.",
            "action": "Tırnak yüzeyindeki doğal yağ ve nemin arındırıldığı ve tırnağın jelle moleküler olarak kilitlendiği 6 saniyelik hazırlık süreci.",
            "trigger": "Hayal Kırıklığı Çözümü. 'Benim tırnağımda hiçbir şey durmuyor' diyen kadına problemin kendisinde değil, hazırlık protokolünde olduğunu gösterir.",
            "audience_reaction": "'Bana daha önce hiç primer sürmemişlerdi direkt oje sürdüler meğer o yüzden çıkıyormuş!', 'Ataşehir'deki yerinize gelmek istiyorum' yorumları.",
            "gulsah_tone": "Teknik bir güvenle: 'Tırnağınız problemli değil; tırnağınızın nem dengesi doğru arındırılmamış. Asitsiz primer tırnağın çift taraflı bandıdır; o olmadan oje durmaz' de."
        },
        # Day 17: Medikal Kuru Manikür ile Klasik Islak Manikür Farkı
        {
            "tripod": "Masanın 45° açısında, kuru manikür frezesi ve klasik manikür kabını yan yana kadraja alarak.",
            "focus": "1x Lens, -0.3 EV. Su kabının kadraj dışına itilişine odak kilidi.",
            "hands": "Sol el su kabını masadan kenara iter, sağ el elmas uçlu frezeyi merkeze alır.",
            "action": "Su kabının masadan itilip yerine otoklavdan çıkan elmas frezenin devreye girdiği ve kuru derinin toza dönüştüğü 6 saniyelik devrim.",
            "trigger": "Eski Yöntem vs. Modern Lüks Kıyası. Klasik sulu manikürün demode ve hijyensiz olduğunu, Rus kuru manikürünün üstünlüğünü kanıtlar.",
            "audience_reaction": "'Artık asla suya el sokmam!', 'Kuru manikürün kalıcılığı gerçekten 4 katı' yorumları.",
            "gulsah_tone": "Vizyoner bir salon sahibi olarak: 'Su tırnak plağını sünger gibi şişirir, oje sürülünce kurur ve soyulur. Kuru manikür hem cerrahi hijyendir hem de 4 hafta kalıcılık sağlar' de."
        },
        # Day 18: Alerjik Tırnaklar İçin Hipoalerjenik Jel
        {
            "tripod": "45° açıda, hipoalerjenik şişenin etiketindeki 'HEMA-Free' ibaresine odaklı.",
            "focus": "2x Makro, HEMA-Free amblemine ve jelin şeffaf dokusuna odak kilidi.",
            "hands": "Sağ el şişeyi çevirir, HEMA-free ve 9-free ibaresini kameraya gösterir.",
            "action": "Alerjik tırnaklar için özel formüle edilmiş HEMA-free jelin tırnağa sıfır kaşıntı ve sıfır reaksiyonla uygulanışının 6 saniyelik güven karesi.",
            "trigger": "Alerji Korkusunun Yenilmesi. Daha önce kalıcı ojeden parmakları kaşınmış, su toplamış hassas kadınlara tek güvenli kapıyı açar.",
            "audience_reaction": "'HEMA alerjim vardı protez yaptıramıyordum, sizde HEMA-free var mı çok mutlu oldum!', 'Hemen randevu almak istiyorum' yorumları.",
            "gulsah_tone": "Hassas ve koruyucu: 'Alerjiniz var diye güzel tırnaklardan mahrum kalmak zorunda değilsiniz. Masamızda sadece HEMA-Free, 9-Free tıbbi standartta jeller kullanıyoruz' de."
        },
        # Day 19: Tırnak Altındaki Hiponişyum Derisi Nedir?
        {
            "tripod": "Tırnağın alt cephesini görecek şekilde 60° yukarı eğimli açıda.",
            "focus": "2x Makro, tırnak altındaki canlı pembe hiponişyum dokusuna odak kilidi.",
            "hands": "Sol el tırnağı yukarı kaldırır, sağ el ahşap çubuğun ucuyla o canlı dokuyu işaret eder.",
            "action": "Tırnak altındaki canlı hiponişyum dokusunun gösterilmesi ve 'burayı asla sert cisimle kazımayın' uyarısının 6 saniyelik görseli.",
            "trigger": "Bilinmeyen Anatomi Uyarısı. Kadınların tırnak altını temizlerken yaptıkları büyük hatayı gösterip uzmanlık saygısı kazandırır.",
            "audience_reaction": "'Ben orayı hep kürdanla kazıyordum canım yanıyordu meğer canlı dokuymuş!', 'Çok değerli bir bilgi teşekkürler' yorumları.",
            "gulsah_tone": "Hassas bir doktor gibi: 'Tırnağınızın altındaki o küçük et parçası mikropların tırnak yatağına girmesini engelleyen canlı güvenlik kilididir. Lütfen sivri aletlerle kazımayın' de."
        },
        # Day 20: Tırnak Şekli Seçerken El Anatomisi Analizi
        {
            "tripod": "90° tam tepe açısında, müşterinin elinin mermer masa üzerinde dinlendiği açı.",
            "focus": "1x Lens, -0.2 EV. Parmak boğumlarının uzunluk oranlarına odak kilidi.",
            "hands": "Gülşah'ın elleri müşterinin parmaklarını nazikçe hizalar, parmak yapısına göre badem/kare form analizi yapar.",
            "action": "Elin genel anatomisinin incelenmesi ve parmak yapısına göre en asil formun (badem/oval) çizildiği 6 saniyelik profesyonel danışmanlık anı.",
            "trigger": "Kişiye Özel Hizmet Arzusu (Customization). 'Herkese aynı tırnağı yapmıyorlar, elime özel form seçiyorlar' ayrıcalığı hissettirir.",
            "audience_reaction": "'Bana hangi form yakışır kararsızdım, gelip el analizi yaptırmak istiyorum', 'Ataşehir Uphill Towers'taydınız değil mi?' soruları.",
            "gulsah_tone": "Stil danışmanı zarafetiyle: 'Arkadaşınızda çok güzel duran bir kare form sizin elinizde kaba durabilir. Biz tırnağı elinizin kemik yapısına ve parmak uzunluğunuza göre tasarlarız' de."
        },
        # Day 21: Kirpik Lifting mi İpek Kirpik mi? Karar Rehberi
        {
            "tripod": "Göz hizasında 45° açıda, bir gözde lifting diğer gözde ipek kirpik kıyaslaması.",
            "focus": "1x Lens, göz kapağının kıvrım çizgisine odak kilidi.",
            "hands": "Gülşah iki parmağıyla kirpiklerin kıvrımını gösterir.",
            "action": "Lifting'in doğal 'rimelli' duruşu ile ipek kirpiğin dramatik 'hacimli' duruşunun yan yana 6 saniyelik net görsel kıyası.",
            "trigger": "Kararsızlık Giderme & Rehberlik. İki işlem arasında kalan kadınlara net bir karar matrisi sunarak satış hunisini hızlandırır.",
            "audience_reaction": "'Tam da bu ikisi arasında kalmıştım harika özetlemişsiniz!', 'Benim kirpiklerim düz hangisini önerirsiniz?' yorumları.",
            "gulsah_tone": "Dürüst bir danışman tavrıyla: 'Rimel sürmeyi seven ama kıvrım isteyenler için Lifting; sabah uyandığında sıfır makyajla hazır olmak isteyenler için İpek Kirpik' de."
        },
        # Day 22: Ayak Tırnağı Neden Düz Kesilmelidir? (Batık Tehlikesi)
        {
            "tripod": "Medikal pedikür koltuğunda 45° açıda, ayak başparmağının kesim hattına odaklı.",
            "focus": "1x Lens, tırnak kenarının düz hat çizgisine odak kilidi.",
            "hands": "Eldivenli eller düz uçlu medikal tırnak makasını tutar.",
            "action": "Tırnağın köşelerinin yuvarlatılmayıp dümdüz kesildiğinin ve batık riskinin sıfırlandığının 6 saniyelik klinik karesi.",
            "trigger": "Batık Ağrısı Korkusu & Önleyici Sağlık. Ayak tırnağı batması kabusu yaşayan herkese hayat kurtaran altın kural.",
            "audience_reaction": "'Ben hep köşeleri oyuyordum batık oluyordu meğer bu yüzdenmiş!', 'Medikal pedikür randevusu almak istiyorum' yorumları.",
            "gulsah_tone": "Podoloji uzmanı netliğiyle: 'Ayak tırnağının köşelerini yuvarlarsanız tırnak ete batarak uzar. Ayak tırnağı daima düz kesilir, köşeler sadece hafifçe törpüyle yuvarlatılır' de."
        },
        # Day 23: LED Işık ile UV Işık Arasındaki Cilt Güvenliği
        {
            "tripod": "Masanın 45° açısında, modern LED lambanın dijital ekranına odaklı.",
            "focus": "1x Lens, -0.3 EV. Lambanın mor değil beyaz-soğuk LED ışıltısına odak kilidi.",
            "hands": "Danışanın elleri lambaya girer, lamba sensörüyle otomatik açılır.",
            "action": "Göz ve cilt sağlığı onaylı dar spektrumlu LED teknolojisinin elleri karartmadan 30 saniyede jeli dondurduğu 6 saniyelik güvenlik karesi.",
            "trigger": "Kanser & Yaşlanma Korkusunun Yatıştırılması. 'Lamba ellerimi yaşlandırır mı' diyen elit kitleye en son teknoloji güvencesi verir.",
            "audience_reaction": "'Ellerim kararır diye korkuyordum yeni nesil LED'ler harikaymış', 'Çok profesyonel bir stüdyosunuz tebrikler' yorumları.",
            "gulsah_tone": "Modern teknoloji güvencesiyle: 'Eski tip floresan UV lambaları rafa kalktı. Masamızdaki yeni nesil LED lambalar sadece jelin dalga boyuna odaklanır; ellerinizi karartmaz ve cildi yaşlandırmaz' de."
        },
        # Day 24: Tırnak Sertleştirici Cilalar Neden Tırnağı Kırar?
        {
            "tripod": "45° makro açı, eczane tipi sertleştirici cila sürülüp cam gibi çatlayan tırnağa odaklı.",
            "focus": "2x Makro, tırnak plağındaki mikro çatlaklara odak kilidi.",
            "hands": "Sol el tırnağı tutar, sağ el tırnağı hafifçe büktüğünde sertleştiricinin çıt diye kırılışını gösterir.",
            "action": "Aşırı sertleştiği için esneyemeyen ve kırılan tırnak plağının analizi ve nemlendirici yağla esnetilme anı 6 saniye.",
            "trigger": "Yanlış Ürün Hayal Kırıklığı. Eczaneden sertleştirici alıp tırnağı daha çok kırılan kadınların gizemini çözer.",
            "audience_reaction": "'Ben de sürekli sertleştirici sürüyordum cam gibi kırılıyordu meğer esneklik lazımmış!', 'İnanılmaz aydınlatıcı bir video' yorumları.",
            "gulsah_tone": "Fizik kuralı gibi: 'Bir ağaç fırtınada esnerse kırılmaz; taş gibi sert olursa devrilir. Tırnak sertleştiriciler tırnağın suyunu çeker ve cam gibi kırılgan yapar. Tırnağa sertlik değil esneklik gerekir' de."
        },
        # Day 25: Tırnak Etlerinin Çatlamasını Önleyen 2 Altın Kural
        {
            "tripod": "45° açıda, Linaura el ve kütikül balmının zengin dokusuna odaklı.",
            "focus": "1x Lens, balmın sıcak parmak temasıyla ipeksi eriyişine odak kilidi.",
            "hands": "İki el birbirine nazikçe masaj yapar, tırnak dipleri ışıldar.",
            "action": "Suyla temas sonrası kütikül yağı sürme refleksi ve gece yatmadan botanik balm uygulamasının 6 saniyelik estetik ritüeli.",
            "trigger": "Kolay & Uygulanabilir Güzellik Tüyosu. Evde hemen yapabilecekleri pratik bilgiyle yüksek kaydetme (Save) sayısı alır.",
            "audience_reaction": "'Bu 2 kuralı not aldım hemen başlıyorum!', 'Linaura bakım mumunu nereden alabiliriz?' soruları.",
            "gulsah_tone": "Samimi bir ev ödevi gibi: 'Tırnak etleriniz için pahalı kremlere gerek yok: 1. Asla ıslak bırakmayın, 2. Gece yatarken jojoba veya shea içerikli bir balmı tırnak diplerinize yedirin' de."
        },
        # Day 26: Tırnakta C-Kavisi Neden Estetik Değil Fiziktir?
        {
            "tripod": "Tırnağın ön cephesinden tünel bakış açısında 0° seviyede.",
            "focus": "2x Makro, tırnağın serbest kenarının kusursuz C harfi şeklindeki tüneline odak kilidi.",
            "hands": "Sol el parmakları dik tutarak kameraya tünelleri gösterir.",
            "action": "Kusursuz C-kavisi tünelinin ışık altındaki kusursuz simetrisinin 6 saniyelik hipnotik gösterimi.",
            "trigger": "Statü & Yüksek Ustalık İspatı. Her kuaförün yapamadığı ileri seviye tırnak mimarisini sergileyerek elit müşteri çeker.",
            "audience_reaction": "'Şu kavise bakar mısınız sanat eseri resmen!', 'Ataşehir'de böyle işçilik yapan tek yersiniz' yorumları.",
            "gulsah_tone": "Zanaatkar gururuyla: 'Önden baktığınızda tırnağın ucu düz bir çizgi değil, zarif bir C kavisi çizmelidir. Bu hem tırnağı dar gösterir hem de kırılmalara karşı kalkan görevi görür' de."
        },
        # Day 27: Göz Kapağı Düşüklüğünde Kirpik Kıvrımı Seçimi
        {
            "tripod": "Göz hizasında 30° profilden, göz kapağı katlantısına odaklı.",
            "focus": "1x Lens, kirpiğin L ve M kıvrımının göz kapağını yukarı kaldıran açısına odak kilidi.",
            "hands": "Sağ el cımbızla L-kıvrımlı kirpiği göz kapağının dibine yerleştirir.",
            "action": "Düşük göz kapağını gölgelemeyen, doğrudan öne ve yukarı doğru kıvrılarak gözü 1.5 kat daha açık gösteren 6 saniyelik illüzyon karesi.",
            "trigger": "Göz Kusurunu Ameliyatsız Kaldırma Arzusu. Düşük göz kapağı olan kadınların en büyük makyaj çilesini çözer.",
            "audience_reaction": "'Benim göz kapağım çok düşük kirpikler hep batıyordu, L kıvrım yaptırmak istiyorum!', 'Fiyat nedir?' yorumları.",
            "gulsah_tone": "Makyaj mimarı gibi: 'Düşük göz kapaklarına yuvarlak C kıvrım yaparsanız göz kapağına çarpar ve gözü daha da küçültür. Biz L ve M kıvrımlarla göz kapağını optik olarak yukarı kaldırıyoruz' de."
        },
        # Day 28: Kalıcı Oje Sonrası Doğru Çıkarma Protokolü
        {
            "tripod": "45° makro açıda, seramik karpit frezenin ojeyi tüy gibi sıyırışına odaklı.",
            "focus": "2x Makro, karpit frezenin sadece oje katmanında kaymasına odak kilidi.",
            "hands": "Sol el parmağı sıkıca tutar, sağ el yeşil kuşaklı karpit frezeyi tek yönde kaydırır.",
            "action": "Frezenin tırnak plağına hiç değmeden, sadece oje katmanını kar gibi ufalayarak sıyırdığı ve altta doğal tırnağı pürüzsüz bıraktığı 6 saniye.",
            "trigger": "Tırnak Kazınması Travmasını Silme. Çıkarma işleminde tırnaklarının inceltilmesinden korkan kadınları masaya çeker.",
            "audience_reaction": "'Çıkartırken tırnağım delinecek diye ödüm patlıyordu, ne kadar nazik yapıyorsunuz!', 'Randevu için yazdım' yorumları.",
            "gulsah_tone": "Hassas ve dikkatli: 'Kalıcı oje tırnağa zarar vermez; onu yanlış çıkaran acemi eller zarar verir. Doğru frezeyle doğal tırnağa tek bir milimetrik çizik bile atmadan temizliyoruz' de."
        },
        # Day 29: Somon DNA ve Hyaluronik Asit Cilde Nasıl İşler?
        {
            "tripod": "Kabin baş ucunda 45° açıda, mezoterapi serumunun mikro damlasına odaklı.",
            "focus": "1x Lens, -0.2 EV. Somon DNA damlasının cam ampulden damlayışına odak kilidi.",
            "hands": "Gülşah eldivenli parmaklarıyla serumu cilde mikro masaj hareketleriyle yedirir.",
            "action": "Cildin serumu sünger gibi emdiği ve anında cam gibi parlayan nem bariyerine kavuştuğu 6 saniyelik klinik bakım karesi.",
            "trigger": "Klinik Gençleşme & Cam Cilt Arzusu. Medikal içeriklerin (Somon DNA / Peptit) bilimsel gücünü göstererek yüksek biletli seans satar.",
            "audience_reaction": "'O ışıltı gerçek mi filtre mi inanamıyorum!', 'Somon DNA seansı için Ataşehir stüdyonuza geleceğim' yorumları.",
            "gulsah_tone": "Klinik estetisyen derinliğiyle: 'Yüzeyden sürülen kremler cildin alt katmanlarına ulaşamaz. Somon DNA hücresel yenilenmeyi tetikler, hyaluronik asit nemi kilitler. İşte gerçek cam cilt budur' de."
        },
        # Day 30: 30 Günlük Tırnak Sağlığı Özeti: Sağlıklı Tırnağın 5 Şifresi
        {
            "tripod": "Masanın 45° açısında, stüdyonun sakin mermer ve altın detaylarını arka plana alarak.",
            "focus": "1x Lens, -0.2 EV. Gülşah'ın masadaki duruşuna ve bakımlı ellerine odak kilidi.",
            "hands": "Gülşah iki elini masada birleştirir, kendinden emin ve sıcak bir tebessümle konuşur.",
            "action": "Gülşah'ın doğrudan kameraya bakıp 30 günlük bilimsel yolculuğu özetlediği ve izleyiciyi Linail masasına davet ettiği 6 saniyelik asil duruş.",
            "trigger": "Tam Otorite & Kalıcı Güven Mührü. 30 gün boyunca takip edenleri sadık birer Linail misafirine dönüştüren zirve çağrıdır.",
            "audience_reaction": "'1 aydır tüm videolarınızı izliyorum artık başka yere gidemem!', 'Haftaya Ataşehir'deyim ilk işim size gelmek' yorumları.",
            "gulsah_tone": "Sıcak bir teşekkür ve davet: 'Güzellik kulaktan dolma bilgilerle değil, tırnağınızın anatomisine saygı duyarak başlar. Masamızda siz de yerinizi alın' de."
        }
    ]
    return entries

print("Authority cues & psychology generator ready.")
