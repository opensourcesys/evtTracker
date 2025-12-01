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

Ayrıca olayları bir listede görüntülemek için bir hareket atayabilirsiniz (NVDA menüsü/Tercihler/Girdi hareketleri, Olay İzleyici kategorisi). Liste, işlenen en son 100 olayı kaydeder.

Bu eklentiyi yararlı buluyorsanız, lütfen NVDA Eklenti Mağazasında [inceleyin][1].

## Sürüm 25.1.0

* NVDA 2025.1 ile Uyumlu.
* Python 3.11 yükseltmesi nedeniyle NVDA 2024.1 veya üstü gereklidir.
* Windows 8.1 için sınırlı destek geri yüklendi.
* Pyright (bir Python statik tür denetleyicisi) yardımıyla eklenti kodu daha sağlam hale getirildi.
* NVDA, olayları bildirirken tamsayılar yerine gerçek kontrol rolü adını kaydeder.

## Sürüm 24.1.0

* NVDA 2024.1 ile Uyumlu.
* openSourcesys/EVTTRACKER #4: Etkinlik görüntüleyicisini ilk açarken ilk olayın açıklaması artık eksik değil. Katkıda bulunan: Wangfeng Huang (HWF1324)

## Sürüm 23.02

* NVDA 2022.4 veya üstü gereklidir.
* Windows 10 21H2 (Kasım 2021 Güncellemesi/derlemesi 19044) veya üstü gereklidir.
* Uyarı olayı (çoğunlukla IAccessible nesneler için) izlenecektir.

## Sürüm 23.01

* NVDA 2022.3 veya üstü gereklidir.
* Ocak 2023 itibariyle Windows 7, 8 ve 8.1 artık Microsoft tarafından desteklenmediğinden Windows 10 veya sonraki sürümleri gereklidir.

## Sürüm 22.12

* Eklenti (Thiago Seus) tarafından kaydedilen en son 100 olayı listelemek için olaylar listesi iletişim kutusu (komut atanmamış) eklendi.
* UIA bildirim özellikleri gibi ek olay bilgileri, olaylarla aynı anda kaydedilir.

## Sürüm 22.10

* Güvenlik nedeniyle NVDA 2022.2 veya üstü gereklidir.
* Aşağıdaki UIA özellik değişiklikleri izlenir: sürükle bırak efekti, bırakma hedefi etkisi.
* UIA öğe durumu özellik metni günlüğe kaydedilir.
* Bir nesne bir pencere sınıfı adı tanımlamıyorsa, NVDA artık hata sesleri çalmayacak veya hiçbir şey yapmıyormuş gibi görünecektir.

## Sürüm 22.06

* Güvenlik nedeniyle NVDA 2021.3 veya üstü gereklidir.

## Sürüm 21.10

* Bu eklentiyi etkileyen NVDA değişiklikleri nedeniyle NVDA 2021.2 veya üstü gereklidir.
* UIA düzeni geçersiz kılınan olay izlenecektir.
* Nesne rolü ve durum bilgileri, daha yeni NVDA sürümlerinde bulunan geliştirici bilgilerine benzeyecektir.

## Sürüm 21.07

* İlk sürüm.

[1]: https://github.com/nvaccess/addon-datastore/discussions/2717
