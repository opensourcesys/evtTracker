# Olayİzleyici

* Yazarlar: Joseph Lee, Thiago Seus

Bu eklenti, olayların tetiklendiği nesneler hakkında bilgi verir. Hata ayıklama günlük modunda kaydedilen özellikler, nesne türü, ad, rol, olay, uygulama modülü ve IAccessible nesnesi için accName ve UIA nesneleri için Otomasyon Kimliği gibi erişilebilirlik API'sine özgü bilgileri içerir.

Notlar:

* Bu eklenti, uygulamalardan ve çeşitli denetimlerden gelen olayları izlemesi gereken geliştiriciler ve uzman kullanıcılar için tasarlanmıştır.
* Eklentiyi kullanmak için, NVDA'nın hata ayıklama modunda oturum açması gerekir (genel ayarlar/kayıt düzeyinden yapılandırılır veya hata ayıklama günlüğü etkinken yeniden başlatılır).
* Olay İzleyicisi'nden önce yüklenen eklentilerin, olayı Olay İzleyicisi de dahil olmak üzere diğer eklentilere aktarmaması mümkün olabilir. Bu durumda, Olay İzleyici olayları günlüğe kaydedemez.
* Olaylar, bu sırayla global eklentiler, uygulama modülleri, ağaç önleyiciler ve NVDA nesnelerinden işlenir.

## Olaylar ve bilgileri

Aşağıdaki olaylar izlenir ve kaydedilir:

* Odak manipülasyonu: odak kazan, odak kaybet, odak girildi, ön plan
* Değişiklikler: ad, değer, durum, açıklama, canlı bölge
* Diğer olaylar: uyarı
* UIA olayları: denetleyici, sürükle bırak ve bırak hedef efektleri, seçilen öğe, öğe durumu, düzen geçersiz kılındı, bildirim, sistem uyarısı, metin değişikliği, araç ipucu açık, pencere açık

Her olay için aşağıdaki bilgiler kaydedilecektir:

* Olay adı
* Nesne
* Nesne adı
* Nesne rolü
* Olaylara bağlı olarak nesne değeri veya durumu
* Uygulama modülü
* IErişilebilir nesneler için: erişim adı, alt kimlik
* UIA nesneleri için: Otomasyon Kimliği, sınıf adı, bildirim olay bilgisi kaydediliyorsa bildirim özellikleri, düzen geçersiz kılınan olay için çocuk sayısı, öğe durumu özellikleri, tanımlıysa sürükle bırak ve bırakma hedefi etkisi

Ayrıca, olayları bir listede görüntülemek için bir hareket de atayabilirsiniz (NVDA menüsü/Tercihler/Girdi hareketleri, Olay İzleyici kategorisi). Liste, iletişim kutusunu açmadan önce işlenen en son 100 olayı kaydeder.

Bu eklentiyi yararlı buluyorsanız, lütfen NVDA Eklenti Mağazasında [inceleyin][1].

[1]: https://github.com/nvaccess/addon-datastore/discussions/2717
