$(function() {
	var Context = getContext();
	var msg_id = 0;

	var chatSendAction = function(event) {
		if ($('#msg').val() != "") {
			var data_to_send = {
				"message": $('#msg').val(),
				"csrfmiddlewaretoken": Context.csrf_token
			};
			$.post(Context.send_url, data_to_send, function() {
				$('#msg').val('');
				clearTimeout(msg_timer);
				chatGetMessages();
			});
		}
		event.preventDefault();
	};

	var chatGetMessages = function() {
		var data_to_send = {
			"csrfmiddlewaretoken": Context.csrf_token,
			"msg_id": msg_id
		};
		$.get(Context.get_url, data_to_send, function(data) {
			var chat_text = getChatText(data);
			$('#messageWindow').prepend(chat_text);
			msg_timer = window.setTimeout(chatGetMessages, 4000);
		});
	};

	var getChatText = function(data) {
		var to_append = [];

		if ( data.length ) {
			msg_id = data[0].id;

			$.each(data, function(i, item) {
				if ($('.chatMessage').length == 10) {
					$('.chatMessage:last-child').remove();
				}

				to_append.push('<div class="chatMessage">');
				to_append.push('<span class="messageAuthor">');
				to_append.push(item.author__username);
				to_append.push('</span>');
				to_append.push('<span class="messageText">: ');
				to_append.push(item.msg_text);
				to_append.push('</span>');
				to_append.push('</div>');
			});
		}

		return to_append.join("");
	};

	$('#chatForm').submit(chatSendAction);

	msg_timer = window.setTimeout(chatGetMessages, 0);
});
