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
        var phoneLabel = window.GOOGLE_ADS_PHONE_CONVERSION_LABEL || 'AW-18351341167/phone_call';
        window.gtag('event', 'conversion', {
          'send_to': phoneLabel,
          'value': 300.0,
          'currency': 'TRY'
        });
        window.gtag('event', 'phone_call_lead', {
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

  // 4. Google Ads (gclid) Dinamik WhatsApp Mesajı (Görev 010)
  function initGoogleAdsWhatsAppRouting() {
    try {
      if (typeof window === 'undefined' || !window.location) return;
      var params = new URLSearchParams(window.location.search);
      if (params.has('gclid')) {
        var path = window.location.pathname.toLowerCase();
        var svcName = "randevu";
        if (path.indexOf('protez-tirnak') !== -1 || path.indexOf('tirnak') !== -1) {
          svcName = "protez tırnak";
        } else if (path.indexOf('kirpik') !== -1) {
          svcName = "ipek kirpik";
        } else if (path.indexOf('manikur') !== -1 || path.indexOf('oje') !== -1) {
          svcName = "kalıcı oje ve manikür";
        } else if (path.indexOf('cilt') !== -1 || path.indexOf('hydrafacial') !== -1) {
          svcName = "cilt bakımı";
        }
        var customMsg = "Merhaba, Google'dan ulaşıyorum. " + (svcName === "randevu" ? "Hizmetleriniz" : svcName.charAt(0).toUpperCase() + svcName.slice(1)) + " için randevu almak istiyorum.";
        var encodedMsg = encodeURIComponent(customMsg);

        var links = document.querySelectorAll('a[href*="wa.me"], a[href*="whatsapp"]');
        for (var i = 0; i < links.length; i++) {
          links[i].href = "https://wa.me/905318696764?text=" + encodedMsg;
        }
      }
    } catch(err) {}
  }

  // Event listener on window/document with capture to catch all child elements (svg, icons, spans)
  if (typeof document !== 'undefined') {
    document.addEventListener('click', handleConversionClick, true);
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', initGoogleAdsWhatsAppRouting);
    } else {
      initGoogleAdsWhatsAppRouting();
    }
  }
})();
