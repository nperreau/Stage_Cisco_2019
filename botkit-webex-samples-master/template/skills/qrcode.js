//
// Command: Qr
//
module.exports = function (controller) {

    controller.hears(["QR:"], 'direct_message,direct_mention', function (bot, message) {
        var url = message.text.replace("QR:","");
        url = url.replace(bot.commons["nickname"] + " ", "");
        const fs = require('fs');
        console.log("LOG: text: "+url);
        const qrcode = require('qrcode');

        run().catch(error => console.error(error.stack));

        async function run() {
            const res = await qrcode.toDataURL(url);
            bot.reply(message, res);

        }
    });
}