const phone = '905318696764';
const defaultMessage = 'Merhaba, Ataşehir Uphill Towers stüdyonuzda randevu ve uygun saatler hakkında bilgi almak istiyorum.';
const whatsappUrl = (message) => `https://wa.me/${phone}?text=${encodeURIComponent(message)}`;

for (const link of document.querySelectorAll('[data-booking]')) {
  link.href = whatsappUrl(link.dataset.message || defaultMessage);
}

const menuButton = document.querySelector('.menu-toggle');
const mobileMenu = document.querySelector('#mobile-menu');
menuButton.addEventListener('click', () => {
  const expanded = menuButton.getAttribute('aria-expanded') === 'true';
  menuButton.setAttribute('aria-expanded', String(!expanded));
  menuButton.setAttribute('aria-label', expanded ? 'Menüyü aç' : 'Menüyü kapat');
  mobileMenu.hidden = expanded;
});
for (const link of mobileMenu.querySelectorAll('a')) {
  link.addEventListener('click', () => {
    mobileMenu.hidden = true;
    menuButton.setAttribute('aria-expanded', 'false');
    menuButton.setAttribute('aria-label', 'Menüyü aç');
  });
}
window.addEventListener('keydown', (event) => {
  if (event.key === 'Escape' && !mobileMenu.hidden) {
    mobileMenu.hidden = true;
    menuButton.setAttribute('aria-expanded', 'false');
    menuButton.setAttribute('aria-label', 'Menüyü aç');
    menuButton.focus();
  }
});

const filters = [...document.querySelectorAll('[data-filter]')];
const serviceCards = [...document.querySelectorAll('[data-category]')];
for (const filter of filters) {
  filter.addEventListener('click', () => {
    for (const button of filters) {
      const active = button === filter;
      button.classList.toggle('active', active);
      button.setAttribute('aria-pressed', String(active));
    }
    for (const card of serviceCards) {
      card.hidden = filter.dataset.filter !== 'all' && card.dataset.category !== filter.dataset.filter;
    }
  });
}

const services = {
  nails: {
    title: 'Protez Jel Tırnak & Güçlendirme',
    intro: 'Doğal tırnak yapınıza, tercih ettiğiniz forma ve kişisel tarzınıza göre planlanan jel uygulaması.',
    url: '/atasehir-protez-tirnak/',
    details: [
      ['Protez jel tırnak', 'Şablonla uzatma, Rus manikürü, jel form inşası ve kalıcı oje ile tamamlanan bakım.'],
      ['Jel güçlendirme', 'Kendi tırnak boyunuzu koruyarak jel uygulamasıyla destekleyici bir form oluşturulur.'],
      ['Periyodik bakım', 'Uzayan tırnaklarda form düzenleme, dip tazeleme ve yeni renk seçimi yapılır. Ortalama 3–4 haftalık bakım aralığı, kullanımınıza göre planlanır.']
    ],
    time: 'Uygulama süresi, model ve tırnak yapısına göre planlanır.'
  },
  lashes: {
    title: 'İpek Kirpik & Lifting',
    intro: 'Göz yapınıza ve istediğiniz görünüme göre klasik, soft volüm veya lifting seçenekleri.',
    url: '/atasehir-ipek-kirpik/',
    details: [
      ['Klasik 1:1 ipek kirpik', 'Her doğal kirpiğe tek bir lif eklenerek daha belirgin bir görünüm hedeflenir.'],
      ['Soft volüm', 'Ultra ince liflerle, tercihinize uygun daha dolgun bir tasarım hazırlanır.'],
      ['Kirpik lifting', 'Kendi doğal kirpiklerinize kıvrım ve keratin bakım uygulaması. Hassasiyetiniz varsa işlem öncesinde ekibimize bildirin.']
    ],
    time: 'Klasik: 90–120 dk · Soft volüm: 120–150 dk · Lifting: 60–75 dk'
  },
  skin: {
    title: 'Profesyonel Cilt Bakımı',
    intro: 'Cildinizin o anki ihtiyacına göre belirlenen, kişiye özel arındırma ve nem odaklı bakım.',
    url: '/atasehir-cilt-bakimi/',
    details: [
      ['Kişiye özel yaklaşım', 'Bakım öncesinde cildinizin ihtiyaçları ve tercih ettiğiniz protokol birlikte değerlendirilir.'],
      ['Arındırma ve nem', 'Vakumlu gözenek arındırma, nem uygulaması ve seçilen protokole uygun bakım adımları.'],
      ['Size uygun bakım', 'Hassasiyetlerinizi, kullandığınız ürünleri ve özel durumlarınızı önceden ekibimizle paylaşın. Hizmet bir tıbbi teşhis veya tedavi yerine geçmez.']
    ],
    time: 'Kaynak hizmet bilgisine göre ortalama 60–75 dk.'
  },
  manicure: {
    title: 'Rus Manikürü & Spa Pedikür',
    intro: 'El ve ayaklarınıza özen gösteren, kombi manikür tekniği ve steril kuru pedikür seçenekleri.',
    url: '/rus-manikur-atasehir/',
    details: [
      ['Rus kombi manikürü', 'Elmas freze uçlarıyla tırnak çevresinin düzenlenmesi, ardından nemlendirici bakım.'],
      ['Steril kuru pedikür', 'Seçilen protokole göre ayak ve tırnak çevresi bakımı ile nemlendirme.'],
      ['Spa dokunuşu', 'Aromaterapi, peeling ve masajla bakımınızı tamamlayabilirsiniz. Kalıcı oje ve nail art seçeneklerini ayrıca sorabilirsiniz.']
    ],
    time: 'Manikür: 45–60 dk · Pedikür: 60–75 dk · Spa bakım: yaklaşık 90 dk'
  },
  brows: {
    title: 'Kaş Tasarımı & Laminasyon',
    intro: 'Yüz hatlarınızla uyumlu, doğal görünüm odaklı kaş şekillendirme ve laminasyon.',
    url: '/atasehir-kas-laminasyon/',
    details: [
      ['Kaş şekillendirme', 'Kaş formunuz yüz anatominize göre değerlendirilir, ağda veya cımbız tekniğiyle düzenlenir.'],
      ['Laminasyon', 'Kaş kıllarını yönlendiren ve keratin bakımıyla tamamlanan uygulama.'],
      ['Kombine bakım', 'Şekillendirme ve laminasyon birlikte planlanabilir. İşlem sonrası bakım bilgisi ekibimiz tarafından paylaşılır.']
    ],
    time: 'Şekillendirme: 20–30 dk · Laminasyon: 45–60 dk · Kombine: 60–75 dk'
  },
  art: {
    title: 'Nail Art & Özel Tasarım',
    intro: 'Zamansız bir French veya size ait bir el çizimi: tarzınızı en ince detayda yansıtalım.',
    url: '/atasehir-nail-art/',
    details: [
      ['Zamansız seçenekler', 'French ve baby boomer, krom ve inci tozu, degrade ombre ve cat eye.'],
      ['Kişisel tasarımlar', 'Mikro fırça el çizimi, çiçekler, geometrik desenler ve seçilen süslemeler.'],
      ['Birlikte seçelim', 'Beğendiğiniz referans fotoğrafı WhatsApp’tan paylaşabilirsiniz. Nail art, temel bakım ücretine ek olarak fiyatlandırılır.']
    ],
    time: 'Tasarım süresi, seçtiğiniz modelin detaylarına göre değişir.'
  }
};

const dialog = document.querySelector('#service-dialog');
let lastServiceTrigger;

function openServiceModal(serviceKey, triggerEl) {
  const service = services[serviceKey];
  if (!service || !dialog) return;
  lastServiceTrigger = triggerEl;
  document.querySelector('#dialog-title').textContent = service.title;
  document.querySelector('#dialog-intro').textContent = service.intro;
  document.querySelector('#dialog-time').textContent = service.time;
  document.querySelector('#dialog-book').href = whatsappUrl(`Merhaba, ${service.title} bakımınız için güncel fiyat ve uygun randevu saatleri hakkında bilgi almak istiyorum.`);
  const detailLink = document.querySelector('#dialog-detail-link');
  if (detailLink) {
    detailLink.href = service.url || '#';
  }
  const container = document.querySelector('#dialog-detail');
  container.replaceChildren();
  for (const [title, text] of service.details) {
    const heading = document.createElement('h4');
    const paragraph = document.createElement('p');
    heading.textContent = title;
    paragraph.textContent = text;
    container.append(heading, paragraph);
  }
  dialog.showModal();
  document.body.classList.add('dialog-open');
}

// Global click delegator for any service card, image, title or "Bakımı incele" button
document.addEventListener('click', (event) => {
  const target = event.target.closest('[data-service]');
  if (!target) return;
  const serviceKey = target.dataset.service;
  if (serviceKey && services[serviceKey]) {
    event.preventDefault();
    openServiceModal(serviceKey, target);
  }
});
dialog.querySelector('.dialog-close').addEventListener('click', () => dialog.close());
dialog.addEventListener('click', (event) => {
  if (event.target !== dialog) return;
  const bounds = dialog.getBoundingClientRect();
  if (event.clientX < bounds.left || event.clientX > bounds.right || event.clientY < bounds.top || event.clientY > bounds.bottom) {
    dialog.close();
  }
});
dialog.addEventListener('close', () => {
  document.body.classList.remove('dialog-open');
  lastServiceTrigger?.focus();
});

const selectedRituals = new Set();
const ritualButtons = [...document.querySelectorAll('[data-ritual]')];
const ritualBook = document.querySelector('#ritual-book');
const ritualStatus = document.querySelector('#ritual-status');
function updateRitual() {
  const selected = [...selectedRituals];
  ritualStatus.textContent = selected.length ? `${selected.length}/3 bakım seçtiniz. Kombinasyon stüdyo teyidiyle planlanır.` : 'Sizin ritüeliniz, sizin seçiminiz.';
  ritualBook.href = whatsappUrl(selected.length ? `Merhaba, VIP odanızda ${selected.join(' + ')} bakımlarını birlikte planlamak istiyorum. Bu kombinasyonun uygunluğunu, fiyatını ve randevu müsaitliğini öğrenebilir miyim?` : 'Merhaba, VIP odanızda aynı anda 3 işlem konsepti için kombinasyonlar, fiyat ve uygun randevu saatleri hakkında bilgi almak istiyorum.');
}
for (const button of ritualButtons) {
  button.addEventListener('click', () => {
    const ritual = button.dataset.ritual;
    if (selectedRituals.has(ritual)) {
      selectedRituals.delete(ritual);
    } else if (selectedRituals.size < 3) {
      selectedRituals.add(ritual);
    } else {
      ritualStatus.textContent = 'En fazla 3 bakım seçebilirsiniz. Değiştirmek için önce bir seçimi kaldırın.';
      return;
    }
    button.setAttribute('aria-pressed', String(selectedRituals.has(ritual)));
    updateRitual();
  });
}
updateRitual();

const reviewSlides = [...document.querySelectorAll('.review-slide')];
let reviewIndex = 0;
function showReview(index) {
  reviewIndex = (index + reviewSlides.length) % reviewSlides.length;
  reviewSlides.forEach((slide, position) => { slide.hidden = position !== reviewIndex; });
  document.querySelector('#review-current').textContent = String(reviewIndex + 1).padStart(2, '0');
}
document.querySelector('#review-next').addEventListener('click', () => showReview(reviewIndex + 1));
document.querySelector('#review-prev').addEventListener('click', () => showReview(reviewIndex - 1));

for (const item of document.querySelectorAll('.faq-list details')) {
  item.addEventListener('toggle', () => {
    if (!item.open) return;
    for (const other of document.querySelectorAll('.faq-list details')) {
      if (other !== item) other.open = false;
    }
  });
}
document.querySelector('#year').textContent = new Date().getFullYear();

// Google Ads Conversion Reporting
window.reportConversion = function(action, label) {
  if (typeof gtag === 'function') {
    gtag('event', 'conversion', {
      'send_to': 'AW-18351341167',
      'event_category': 'Engagement',
      'event_label': label || action,
      'value': 2500,
      'currency': 'TRY'
    });
  }
};

document.querySelectorAll('a[href*="wa.me"]').forEach(el => {
  el.addEventListener('click', () => window.reportConversion('WhatsApp_Click', el.textContent.trim().slice(0, 30)));
});

// Cinematic hero story: logo reveal → VIP experience → why Linail.
const storySlides = [...document.querySelectorAll('[data-story-slide]')];
const storyCurrent = document.querySelector('[data-story-current]');
const storyVideos = storySlides.flatMap((slide) => [...slide.querySelectorAll('video')]);
let storyIndex = 0;
let storyTimer;

function showStory(index) {
  if (!storySlides.length) return;
  window.clearTimeout(storyTimer);
  storyIndex = (index + storySlides.length) % storySlides.length;
  storySlides.forEach((slide, position) => slide.classList.toggle('is-active', position === storyIndex));
  storyVideos.forEach((video) => {
    video.pause();
  });
  const activeVideo = storySlides[storyIndex].querySelector('video');
  if (activeVideo) {
    activeVideo.currentTime = 0;
    activeVideo.playbackRate = storyIndex === 1 ? 1.35 : 1;
    activeVideo.play().catch(() => {});
    storyTimer = window.setTimeout(() => showStory(storyIndex + 1), storyIndex === 0 ? 10500 : 20500);
  } else {
    storyTimer = window.setTimeout(() => showStory(storyIndex + 1), 7200);
  }
  if (storyCurrent) storyCurrent.textContent = String(storyIndex + 1).padStart(2, '0');
}

for (const video of storyVideos) video.addEventListener('ended', () => showStory(storyIndex + 1));
document.querySelector('[data-story-next]')?.addEventListener('click', () => showStory(storyIndex + 1));
document.querySelector('[data-story-prev]')?.addEventListener('click', () => showStory(storyIndex - 1));
if (storySlides.length) showStory(0);

// Quick booking dialog
const quickBookingDialog = document.querySelector('#quick-booking-dialog');
const quickBookingBook = document.querySelector('#quick-booking-book');
if (quickBookingDialog) {
  const openQuickBooking = () => {
    if (quickBookingBook) {
      quickBookingBook.href = 'https://wa.me/905318696764?text=' + encodeURIComponent('Merhaba, bakım menünüzden bir hizmet seçtim. Uygunluk, güncel fiyat ve randevu süreci hakkında bilgi alabilir miyim?');
    }
    quickBookingDialog.showModal();
    document.body.classList.add('dialog-open');
  };
  document.querySelectorAll('[data-quick-booking]').forEach((trigger) => trigger.addEventListener('click', openQuickBooking));
  quickBookingDialog.querySelector('[data-quick-booking-close]')?.addEventListener('click', () => quickBookingDialog.close());
  quickBookingDialog.addEventListener('click', (event) => {
    if (event.target !== quickBookingDialog) return;
    const bounds = quickBookingDialog.getBoundingClientRect();
    if (event.clientX < bounds.left || event.clientX > bounds.right || event.clientY < bounds.top || event.clientY > bounds.bottom) {
      quickBookingDialog.close();
    }
  });
  quickBookingDialog.addEventListener('close', () => document.body.classList.remove('dialog-open'));
}

