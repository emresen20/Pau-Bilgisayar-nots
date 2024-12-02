const WebSocket = require('ws');

// Sunucuya bağlan
const ws = new WebSocket('ws://localhost:6000');

// İstemci adı
const name = 'Client3';

// Sunucuya bağlanınca yapılan işlemler
ws.on('open', () => {
    console.log('Sunucuya bağlanıldı.');

    // İstemci adıyla kayıt
    ws.send(JSON.stringify({ type: 'register', name }));
    
    // Broadcast mesajı gönder
    setTimeout(() => {
        ws.send(JSON.stringify({ type: 'broadcast', from: name, message: 'Merhaba herkese! ben Client3' }));
    }, 1000);

    // Deneme broadcasti
    setTimeout(() => {
        ws.send(JSON.stringify({ type: 'broadcast', from: name, message: 'Merhaba benim adım Client3 bu bir broadcast yayını' }));
    }, 1000);

    // Unicast mesajı gönder
    setTimeout(() => {
        ws.send(JSON.stringify({ type: 'unicast', from: name, to: 'Client1', message: 'Merhaba Client1! ben Client3' }));
    }, 2000);
});

// Mesaj alındığında yapılacak işlemler
ws.on('message', (data) => {
    const message = JSON.parse(data);
    console.log(`Mesaj alındı: Bu client ismi ${name}, mesajı gönderen: ${message.from}, içerik: "${message.message}"`);
});

// Bağlantı kapanınca yapılacak işlemler
ws.on('close', () => {
    console.log('Bağlantı kapatıldı.');
});