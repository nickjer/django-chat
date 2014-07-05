$(function() {
	var Context = getContext();
	var msg_id = 0;

	var chatSendAction = function(event) {
		if ($('#msg').val() != "") {
			var data_to_send = {
				"name": $('#name').val(),
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
			$('#loading').remove();
			var chat_text = getChatText(data);
			$('#messagewindow').prepend(chat_text);
			msg_timer = window.setTimeout(chatGetMessages, 4000);
		});
	};

	var getChatText = function(data) {
		var to_append = [];

		if ( data.length ) {
			msg_id = data[0].id;

			$.each(data, function(i, item) {
				if ($('.msg').length == 10) {
					$('#messagewindow span:last-child').remove();
				}

				to_append.push('<span class="msg">');
				to_append.push('<b>');
				to_append.push(item.author__name);
				to_append.push('</b>: ');
				to_append.push(item.msg_text);
				to_append.push('</span>');
			});
		}

		return to_append.join("");
	};

	$('#chatform').submit(chatSendAction);

	msg_timer = window.setTimeout(chatGetMessages, 0);
});
