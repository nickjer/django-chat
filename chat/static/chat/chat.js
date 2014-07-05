$(function() {
	var Context = getContext();
	var msg_id = 0;

	var chatSendAction = function(event) {
		if ($('#msg').val() != "") {
			var data_to_send = {
				"name": $('#name').val(),
				"message": $('#msg').val(),
				"csrfmiddlewaretoken": Context.csrf_token,
				"msg_id": msg_id,
			};
			$.post(Context.send_url, data_to_send, function(data) {
				$('#msg').attr('value', "");
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
		$.post(Context.get_url, data_to_send, function(data) {
			$('#loading').remove();
			var chatText = getChatText(data);
			$('#messagewindow').prepend(chatText);
			window.setTimeout(chatGetMessages, 1000);
		});
	};

	var getChatText = function(data) {
		var to_append = [];

		msg_id = data.msg_id;

		$.each(data.msgs, function(i, item) {
			if ($('.msg').length == 10) {
				$('messagewindow span:last-child').remove();
			}

			to_append.push('<span class="msg">');
			to_append.push('<b>');
			to_append.push(item.author__name);
			to_append.push('</b>: ');
			to_append.push(item.msg_text);
			to_append.push('</span>');
		});

		return to_append.join("");
	};

	$('#chatform').submit(chatSendAction);

	window.setTimeout(chatGetMessages, 0);
});
