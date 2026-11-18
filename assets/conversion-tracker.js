/**
 * Linail Beauty - Google Ads & GA4 Canlı Dönüşüm Takip Motoru
 * Account CID: 971-981-9437 | Google Tag: AW-18351341167 / G-GSH1K69E49
 *
 * Dönüşüm Kuralları (Görev 006):
 * - WhatsApp tıklaması: wa.me, api.whatsapp.com, whatsapp:// -> BİRİNCİL (300 TL, Sayım: Bir)
 *   Label: AW-18351341167/LxLwCMe9hLUdEO_8zK5E
 * - Telefon tıklaması: tel: -> BİRİNCİL (300 TL, Sayım: Bir)
 *   Label: AW-18351341167/LxLwCMe9hLUdEO_8zK5E
 * - Yol tarifi tıklaması: maps.google, goo.gl/maps, google.com/maps -> İKİNCİL (Teklife etki etmez)
 */

(function () {
  'use strict';

  // Global reportConversion helper
  window.reportConversion = function (category, label, value) {
    if (typeof window.gtag === 'function') {
      window.gtag('event', 'conversion', {
        'send_to': 'AW-18351341167/LxLwCMe9hLUdEO_8zK5E',
        'value': typeof value === 'number' ? value : 300.0,
        'currency': 'TRY'
      });
      window.gtag('event', 'generate_lead', {
        'event_category': category || 'Contact',
        'event_label': label || 'WhatsApp VIP Randevu',
        'value': typeof value === 'number' ? value : 300.0,
        'currency': 'TRY'
      });
    }
  };

  function handleConversionClick(e) {
    var target = e.target;
    var a = target && target.closest ? target.closest('a') : null;
    if (!a) return;

    var rawHref = a.getAttribute('href') || '';
    if (!rawHref) return;
    var href = rawHref.trim().toLowerCase();

    // 1. WhatsApp Tıklaması (wa.me, api.whatsapp.com, whatsapp://)
    if (href.indexOf('wa.me') !== -1 ||
        href.indexOf('api.whatsapp.com') !== -1 ||
        href.indexOf('whatsapp:') !== -1) {
      if (typeof window.gtag === 'function') {
        window.gtag('event', 'conversion', {
          'send_to': 'AW-18351341167/LxLwCMe9hLUdEO_8zK5E',
          'value': 300.0,
          'currency': 'TRY'
        });
        window.gtag('event', 'generate_lead', {
          'event_category': 'Contact',
          'event_label': 'WhatsApp VIP Randevu Tıklaması',
          'value': 300.0,
          'currency': 'TRY'
        });
      }
    }
    // 2. Telefonla Arama Tıklaması (tel:)
    else if (href.indexOf('tel:') === 0) {
      if (typeof window.gtag === 'function') {
        window.gtag('event', 'conversion', {
          'send_to': 'AW-18351341167/LxLwCMe9hLUdEO_8zK5E',
          'value': 300.0,
          'currency': 'TRY'
        });
        window.gtag('event', 'contact', {
          'event_category': 'Contact',
          'event_label': 'Telefonla Arama Tıklaması',
          'value': 300.0,
          'currency': 'TRY'
        });
      }
    }
    // 3. Yol Tarifi Tıklaması (maps.google, goo.gl/maps, google.com/maps) - İKİNCİL
    else if (href.indexOf('maps.google') !== -1 ||
             href.indexOf('goo.gl/maps') !== -1 ||
             href.indexOf('google.com/maps') !== -1) {
      if (typeof window.gtag === 'function') {
        window.gtag('event', 'get_directions', {
          'event_category': 'Location',
          'event_label': 'Google Maps Yol Tarifi Tıklaması'
        });
      }
    }
  }

  // Event listener on window/document with capture to catch all child elements (svg, icons, spans)
  if (typeof document !== 'undefined') {
    document.addEventListener('click', handleConversionClick, true);
  }
})();
