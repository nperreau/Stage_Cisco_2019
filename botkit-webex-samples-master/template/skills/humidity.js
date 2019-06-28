module.exports = function (controller) {

    controller.hears(['humidity'], 'direct_message,direct_mention', function (bot, message) {

        const request = require('request');
        request('http://localhost:8080/humidity', function (error, response, body) {
            //convo.say('error:', error); // Print the error if one occurred
            //convo.say('statusCode:', response && response.statusCode); // Print the response status code if a response was received
            bot.reply(message, body);
        });
    });
        
}