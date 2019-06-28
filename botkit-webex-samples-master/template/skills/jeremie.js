module.exports = function (controller) {

    controller.hears(["Jeremie"], "direct_message,direct_mention", function (bot, message) {

        bot.startConversation(message, function (err, convo) {

            convo.ask("Jeremie est qqn qui travaille à Cisco. et toi, qui est tu ?", [
                    {
                        pattern: "^Jeremie$",
                        callback: function (response, convo) {
                            convo.gotoThread("Jeremie");
                        }
                    },
                    {
                        pattern: "^Naïl$",
                        callback: function (response, convo) {
                            convo.gotoThread("Nail");
                        }
                    },
                    {
                        pattern: "^David$",
                        callback: function (response, convo) {
                            convo.gotoThread("David");
                        }
                    },
                    {
                        pattern: "^Personne$",
                        callback: function (response, convo) {
                            convo.gotoThread("Personne");
                        }
                    },
                    {
                        default: true,
                        callback: function (response, convo) {
                            convo.gotoThread('bad_response');
                        }
                    }
            ], { key: "answer" });

            // Success thread
            convo.addMessage(
                "WAAAW J'ais LE jérémie devant moi !",
                "Jeremie");
            convo.addMessage(
                "je le connait, c'est le stagiaire à qui ont donne des annotations à faire.",
                "Nail");
            convo.addMessage(
                "C'est l'ingénieur qui donne des anotations au stagiaire",
                "David");
            convo.addMessage(
                "C'est bizarre, je suis  né il y même pas une semaine et je parle déjà tout seul !",
                "Personne");

            // Bad response
            convo.addMessage({
                text: "Ce gars la j'le connait pas, mais il as un nom d'BG",
                action: 'default',
            }, 'bad_response');
        });
    });
};