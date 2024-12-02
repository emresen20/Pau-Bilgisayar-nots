

// const WebSocket = require('ws');

// const wss = new WebSocket.Server({ port: 6000 });
// const clients = new Map();

// wss.on('connection', (ws) => {
//     console.log('Yeni istemci bağlandı');
    
//     ws.on('message', (message) => {
//         const data = JSON.parse(message);

//         if (data.type === 'broadcast') {
//             wss.clients.forEach((client) => {
//                 if (client !== ws && client.readyState === WebSocket.OPEN) {
//                     client.send(JSON.stringify({ from: data.from, message: data.message }));
//                 }
//             });
//         } else if (data.type === 'unicast') {
//             const recipient = Array.from(clients.keys()).find((name) => name === data.to);
//             if (recipient) {
//                 const recipientSocket = clients.get(recipient);
//                 recipientSocket.send(JSON.stringify({ from: data.from, message: data.message }));
//             }
//         } else if (data.type === 'register') {
//             clients.set(data.name, ws);
//             console.log(`İstemci kaydedildi: ${data.name}`);
//         }
//     });

//     ws.on('close', () => {
//         for (let [name, socket] of clients) {
//             if (socket === ws) {
//                 clients.delete(name);
//                 console.log(`İstemci ayrıldı: ${name}`);
//                 break;
//             }
//         }
//     });
// });

// console.log('WebSocket sunucusu 6000 portunda çalışıyor...');

// // Kapatma komutunu dinle  tamamla yazarak kapat
// process.stdin.on('data', (data) => {
//     const input = data.toString().trim();
//     if (input === 'tamamla') {
//         console.log('Sunucu kapatılıyor...');
//         wss.clients.forEach((client) => {
//             client.close();
//         });
//         wss.close(() => {
//             console.log('WebSocket sunucusu kapandı.');
//             process.exit(0);
//         });
//     }
// });

const WebSocket = require('ws');

const wss = new WebSocket.Server({ port: 6000 });
const clients = new Map();

wss.on('connection', (ws) => {
    console.log('Yeni istemci bağlandı');
    
    ws.on('message', (message) => {
        const data = JSON.parse(message);

        if (data.type === 'broadcast') {
            wss.clients.forEach((client) => {
                // kodu kendine yollamasın
                if (client !== ws && client.readyState === WebSocket.OPEN) {
                    client.send(JSON.stringify({ from: data.from, message: data.message }));
                }
            });
        } else if (data.type === 'unicast') {
            const recipient = Array.from(clients.keys()).find((name) => name === data.to);
            if (recipient) {
                const recipientSocket = clients.get(recipient);
                // Check that the sender is not the recipient
                if (recipientSocket !== ws) {
                    recipientSocket.send(JSON.stringify({ from: data.from, message: data.message }));
                }
            }
        } else if (data.type === 'register') {
            clients.set(data.name, ws);
            console.log(`İstemci kaydedildi: ${data.name}`);
        }
    });

    ws.on('close', () => {
        for (let [name, socket] of clients) {
            if (socket === ws) {
                clients.delete(name);
                console.log(`İstemci ayrıldı: ${name}`);
                break;
            }
        }
    });
});

console.log('WebSocket sunucusu 6000 portunda çalışıyor...');

// Kapatma komutunu dinle  tamamla yazarak kapat
process.stdin.on('data', (data) => {
    const input = data.toString().trim();
    if (input === 'tamamla') {
        console.log('Sunucu kapatılıyor...');
        wss.clients.forEach((client) => {
            client.close();
        });
        wss.close(() => {
            console.log('WebSocket sunucusu kapandı.');
            process.exit(0);
        });
    }
});
