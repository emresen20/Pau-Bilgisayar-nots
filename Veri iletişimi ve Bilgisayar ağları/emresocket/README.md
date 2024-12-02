Emre Şen


Bu kod node js ile Websocket kütüphanesi kullanılarak yapıldı. Belirli bir port üzerinden bu işlemleri yaptık
ilk önce serverımı ayağa kaldırdım.
daha sonra ayağa kalkan server kendine gelecek istekleri dinler hale geldi
if else yapısı ile gelen mesajın broodcast yayını mı unicast yayını mı yoksa yeni bir client in mi bağlanacağını kontrol ettirdim.
Daha sonra eğer broadcastse bütün kullanıcılara kimden mesaj geldiyse o kişinin adından bir mesaj yaydı.
Daha sonra eğer unicastse o kişi adına serverımız mesajı gitmesi gereken yere yolladı
Birde yeni istemci bağlanması var register işlemi bağlanır ve açık oldukça dinler
mesajları aynı yere yollamaması için de bir kod ekledim
işlemler bittiğinde ise tamamala yazılarak olayları bitirdik.
